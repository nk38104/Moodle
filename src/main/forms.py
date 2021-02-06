from django import forms
from django.contrib.auth import authenticate
from users.models import CustomUsers


# Create your forms here.

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUsers
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')


