from django_filters import rest_framework as dj_filter
from rest_framework import viewsets

import apps.server.utils.schema as schema
from apps.server import filters, models, serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Api endpoint to allows list create or update categories.
    """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [dj_filter.DjangoFilterBackend]
    filterset_class = filters.CategoryFilter


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Api endpoint to allows list create or update channels.
    """

    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    filter_backends = [dj_filter.DjangoFilterBackend]
    filterset_class = filters.ChannelFilter


class ServerViewSet(viewsets.ModelViewSet):
    """
    Api endpoint to allows list create or update servers.
    """

    queryset = models.Server.objects.all()
    serializer_class = serializers.ServerSerializer
    filter_backends = [dj_filter.DjangoFilterBackend]
    filterset_class = filters.ServerFilter

    @schema.server_list
    def list(self, request, *args, **kwargs):
        return super(ServerViewSet, self).list(request, *args, **kwargs)
