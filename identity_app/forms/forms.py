from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),required=True)
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address','class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password1','class':'form-control'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password2','class':'form-control'}),required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        
    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('A user with that email already exists')
      
    #modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
        return user


class AuthenticationForm(forms.Form):     
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}),required=True)
    
    class Meta:
        model = User
        
    def clean(self):
        cleaned_data = super(AuthenticationForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                user = authenticate(username = username,password= password)
                if user is None:
                    raise Exception
            except Exception:
                raise forms.ValidationError('Invalid Credentials')
            else:
                return user
        return None