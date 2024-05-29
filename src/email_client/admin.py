from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from admin_extra_buttons.api import ExtraButtonsMixin, button


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "last_login",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    @button(
        html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'Reloaded Page')

    def grant_superuser_and_staff(self, request, queryset):
        for user in queryset:
            user.is_superuser = True
            user.is_staff = True
            user.save()
            
    grant_superuser_and_staff.short_description = "Grant Superuser and Staff Status"

    actions = [grant_superuser_and_staff]
