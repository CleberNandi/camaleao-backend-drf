from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import ChameleonUser
from .forms import UserChangeForm, UserCreationForm


@admin.register(ChameleonUser)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = ChameleonUser
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {
            "fields": (

            ),
        }),
    )
