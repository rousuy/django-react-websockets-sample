from django.db.models import Count
from django_filters import rest_framework as filters
from server import models


class ServerFilter(filters.FilterSet):
    by_category_name = filters.NumberFilter(field_name="category")
    with_num_members = filters.CharFilter(field_name="members", method="filter_members")

    class Meta:
        models.Server
        fields = ["category", "instructor"]

    def filter_members(self, queryset, name, value):
        print("Entrou no filter")
        if value == "true":
            return queryset.annotate(with_num_members=Count("members"))
        return queryset
