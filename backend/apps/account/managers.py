from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet

from apps.account import enums


class AccountManager(BaseUserManager):
    def create_user(
        self,
        username,
        first_name,
        last_name,
        email,
        password,
        **other_fields,
    ):
        email = self.normalize_email(email)
        account = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            **other_fields,
        )
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(
        self,
        username,
        first_name,
        last_name,
        email,
        password,
        **other_fields,
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        return self.create_user(
            username,
            first_name,
            last_name,
            email,
            password,
            **other_fields,
        )

    def get_by_natural_key(self, username):
        return self.get(username=username)


class AccountAdminManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=enums.AccountRole.ADMIN)


class AccountInstructorManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=enums.AccountRole.INSTRUCTOR)


class AccountParticipantManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=enums.AccountRole.PARTICIPANT)
