from apps.server import serializers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

QUERY_LOCATION = OpenApiParameter.QUERY

server_list = extend_schema(
    responses=serializers.ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category_name",
            type=OpenApiTypes.STR,
            location=QUERY_LOCATION,
            description="Filter by category name.",
        ),
        OpenApiParameter(
            name="category_id",
            type=OpenApiTypes.INT,
            location=QUERY_LOCATION,
            description="Filter by category ID.",
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
            name="member_id",
            type=OpenApiTypes.INT,
            location=QUERY_LOCATION,
            description="Filter by members IDs (e.g., 1,2,3...)",
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            location=QUERY_LOCATION,
            description="Include the number of members for each server in the response.",
        ),
    ],
)
