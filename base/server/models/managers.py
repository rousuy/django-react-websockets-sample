from django.contrib.auth.models import BaseUserManager
from django.db import models


class ServerManager(BaseUserManager, models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username=username)
