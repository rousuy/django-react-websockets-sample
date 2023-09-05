import server.schema as schema
from django_filters import rest_framework as dj_filter
from rest_framework import viewsets
from rest_framework.response import Response
from server import filters, models
from server.serializers import server


class ServerViewSet(viewsets.ViewSet):
    """
    Api endpoint to allows list create or update servers.
    """

    queryset = models.Server.objects.all()
    serializer_class = server.ServerSerializer
    filter_backends = [dj_filter.DjangoFilterBackend]
    filterset_class = filters.ServerFilter

    def get_serializer_class(self):
        ACTIONS_MAP: dict = {"list": server.ServerListSerializer}
        action = ACTIONS_MAP.get(self.action)
        return action if action else self.serializer_class

    @schema.server_list
    def list(self, request, *args, **kwargs):
        """
        Request object containing query parameters.

        `Returns`:

        A filtered queryset of servers based on specified parameters,
        or the full queryset if no filters are applied.

        `Parameters`:
        - `id(int)`: Filter servers by server ID.
        - `category_name(str)`: Filter servers by category name.
        - `qty(int)`: Limit the number of servers returned.
        - `instructor(int)`: Filter servers by instructor ID.
        - `by_user(bool)`: Filter servers by authenticated user.
        - `with_num_members(bool)`: Annotate each server with the number of members.

        `Example`:

        To retrieve all servers in the "gaming" category with at least 5 members,
        use the following request:

        `[GET]` .../select/?category_name="gaming"&with_num_members=true&qty=5

        To retrieve the first 10 servers that the authenticated user is a member of,
        use the following request:

        `[GET]` .../select/?by_user=true&qty=10
        """

        queryset = self.queryset.prefetch_related("channel_servers")
        get_serializer = self.get_serializer_class()
        serializer = get_serializer(queryset, many=True)
        return Response(serializer.data)
