from django.conf import settings
from django.db import models
from apps.server.utils import upload
from apps.server import managers
from django_cleanup import cleanup


@cleanup.select
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload.icon_path
    )

    def __str__(self):
        return self.name


@cleanup.select
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
    icon = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload.icon_path,
    )
    banner = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload.banner_path,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
