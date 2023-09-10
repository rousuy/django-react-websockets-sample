from django.contrib import admin

from apps.server import models

admin.site.register(models.Channel)
admin.site.register(models.Category)
admin.site.register(models.Server)
