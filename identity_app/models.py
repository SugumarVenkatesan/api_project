from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from datetime import timedelta
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    password_token = models.CharField(max_length=40, blank=True,null=True)
    key_expires = models.DateTimeField(default=timezone.now()+timedelta(days=settings.USER_ACTIVATION_MAIL_EXPIRY_PERIOD))
      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
        
    @property
    def key_expired(self):
        return self.key_expires < timezone.now()
    
    @property
    def password_key_expired(self):
        return False if self.password_token else True