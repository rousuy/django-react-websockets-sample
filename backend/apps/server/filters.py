from django.db.models import Count
from django_filters import rest_framework as filters

from apps.server import models


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = models.Category
        fields = ["name"]

class ChannelFilter(filters.FilterSet):

    class Meta:
        model = models.Channel
        fields = ["instructor_id", "name"]


class ServerFilter(filters.FilterSet):
    category_name = filters.CharFilter(field_name="category__name")
    with_num_members = filters.BooleanFilter(method="filter_has_num_members")
    qty = filters.NumberFilter(method="filter_by_qty")
    member_id = filters.BaseCSVFilter(
        field_name="members",
        method="filter_by_members",
        distinct=True,
    )

    class Meta:
        model = models.Server
        fields = ["category_id", "instructor_id"]
    
    
    def filter_by_qty(self, queryset, _, value):
        return queryset[: int(value)]

    def filter_has_num_members(self, queryset, _, value):
        if value is True:
            return queryset.annotate(with_num_members=Count("members"))
        return queryset
    
    def filter_by_members(self, queryset, _, value):
        member_ids = value.split(",")
        return queryset.filter(members__id__in=member_ids)




    
