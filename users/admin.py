from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomAdmin(UserAdmin):

  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = ['emai', 'username',]


admin.site.register(CustomUser, CustomAdmin)