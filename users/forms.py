from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
  """Create from for the custom user create"""


  class Meta:
    model = get_user_model()
    fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
  """Create from for the custom user change"""
  
  class Meta:
    model = get_user_model()
    fields = ('email', 'username',)