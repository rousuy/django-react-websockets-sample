import server.serializers.server as serializers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

QUERY_LOCATION = OpenApiParameter.QUERY

server_list = extend_schema(
    responses=serializers.ServerListSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category_name",
            type=OpenApiTypes.STR,
            location=QUERY_LOCATION,
            description="Category of servers to retrieve.",
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            location=QUERY_LOCATION,
            description="Number of servers to retrieve.",
        ),
        OpenApiParameter(
            name="instructor_id",
            type=OpenApiTypes.INT,
            location=QUERY_LOCATION,
            description="Filter by instructor ID.",
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            location=QUERY_LOCATION,
            description="Filter by the current authenticated user (true/false)",
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            location=QUERY_LOCATION,
            description="Include the number of members for each server in the response.",
        ),
    ],
)
