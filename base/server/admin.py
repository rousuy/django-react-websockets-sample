from django.contrib import admin
from server.models import Category, Channel, Server

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Server)
