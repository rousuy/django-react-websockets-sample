from django.db import models


class AccountRole(models.TextChoices):
    ADMIN = "Admin"
    INSTRUCTOR = "instructor"
    PARTICIPANT = "Participant"
