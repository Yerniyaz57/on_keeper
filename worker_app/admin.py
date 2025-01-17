from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile
# Register your models here.

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = UserProfile
  list_display = ['email', 'username',]

admin.site.register(UserProfile, CustomUserAdmin)