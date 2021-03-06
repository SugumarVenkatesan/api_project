import hashlib,random

from django.db.models.signals import post_save
from .models import UserProfile
from django.dispatch import receiver, Signal
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

def generate_activation_key(value):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
    activation_key = hashlib.sha1(salt+value).hexdigest()
    return activation_key            
        
post_key_expired = Signal(providing_args=['key_expired'])
    
@receiver(post_save, sender=User)
def save_userprofile(sender, created, **kwargs):
        obj = kwargs['instance']
        key_expires = timezone.now() + timedelta(days=settings.USER_ACTIVATION_MAIL_EXPIRY_PERIOD)    
        if created and not obj.is_superuser:
            activation_key = generate_activation_key(obj.email)
            new_profile = UserProfile(user=obj, activation_key=activation_key, 
                                          key_expires=key_expires)
            new_profile.save()


                    
@receiver(post_save, sender=UserProfile)                
def send_activation_mail(sender, created, **kwargs):
        obj = kwargs['instance']
        if created:
            email_subject = 'Account confirmation'
            activation_url = settings.DOMAIN_URL + reverse_lazy('register_confirm',kwargs={'activation_key':obj.activation_key}).lower()
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours %s" % (obj.user.username, activation_url)
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [obj.user.email], fail_silently=False)
            


@receiver(post_key_expired)
def handle_key_expired(sender, **kwargs):
    key_expired = kwargs.get("key_expired")
    obj = sender
    if key_expired:
        obj.activation_key = generate_activation_key(obj.user.email)
        obj.key_expires = timezone.now() + timedelta(days=settings.USER_ACTIVATION_MAIL_EXPIRY_PERIOD)
        obj.save()
        email_subject = 'Account reconfirmation'
        email_body = "Hey %s, as per your request, the activation link was again sent to you. To activate your account, click this link within 48hours http://127.0.0.1:8000/confirm/%s" % (obj.user.username, obj.activation_key)
        send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [obj.user.email], fail_silently=False)