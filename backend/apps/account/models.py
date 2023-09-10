import django.core.validators as dj_validator
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


from apps.account import enums, managers


class Account(AbstractUser, PermissionsMixin):
    DEFAULT_ROLE = enums.AccountRole.ADMIN

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(validators=[dj_validator.EmailValidator], unique=True)
    role = models.CharField(max_length=11, choices=enums.AccountRole.choices)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    objects = managers.AccountManager()

    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.DEFAULT_ROLE
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class AdminAccount(Account):
    DEFAULT_ROLE = enums.AccountRole.ADMIN
    objects = managers.AccountAdminManager()

    class Meta:
        proxy = True


class InstructorAccount(Account):
    DEFAULT_ROLE = enums.AccountRole.INSTRUCTOR
    objects = managers.AccountInstructorManager()

    class Meta:
        proxy = True


class ParticipantAccount(Account):
    DEFAULT_ROLE = enums.AccountRole.PARTICIPANT
    objects = managers.AccountParticipantManager()

    class Meta:
        proxy = True
