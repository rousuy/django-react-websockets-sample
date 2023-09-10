from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.account import models


@admin.register(models.Account)
class UserAdminConfig(UserAdmin):
    class Meta:
        model = models.Account
        verbose_name_plural = "Accounts"
        verbose_name = "Account"

    ordering = ("-date_joined",)
    search_fields = ("username", "first_name", "last_name")
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "role",
                    "groups",
                    "is_staff",
                    "is_active",
                    "user_permissions",
                ),
            },
        ),
        (
            "Personal",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
