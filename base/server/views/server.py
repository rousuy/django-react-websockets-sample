
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from server import filters, models
from server.serializers import server
from django_filters import rest_framework as dj_filter

class ServerViewSet(viewsets.ViewSet):
    queryset = models.Server.objects.all()
    serializer_class = server.ServerSerializer
    filter_backends = (dj_filter.DjangoFilterBackend,)
    filter_set_class = filters.ServerFilter

    def get_serializer_class(self):
        SERIALIZERS_ACTIONS = {"list": server.ServerListSerializer}
        action = SERIALIZERS_ACTIONS.get(self.action)
        return action if action else self.serializer_class

    def list(self, request, *args, **kwargs):
        print(dir(request))
        print(request.query_params)
        queryset = self.queryset.prefetch_related("channel_servers")
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)
