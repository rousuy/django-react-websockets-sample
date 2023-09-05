from django.conf import settings
from django.db import models
from server.models import managers


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="server_categories",
    )
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="server_instructors",
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="server_members",
    )
    description = models.TextField(null=True, blank=True)
    objects = managers.ServerManager()

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="channel_instructors",
    )
    topic = models.TextField(null=True, blank=True)
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="channel_servers",
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
