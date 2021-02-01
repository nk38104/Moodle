from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers


# Create your forms here.

class CreateUserForm(UserCreationForm):
    class Meta:
        model   = CustomUsers
        fields  = ['email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'status']


