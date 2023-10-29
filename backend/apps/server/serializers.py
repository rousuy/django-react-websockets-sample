from typing import Optional

from rest_framework import serializers

from apps.server import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            "id",
            "name",
            "description",
            "icon",
        ]


class ChannelSerializer(serializers.ModelSerializer):
    instructor_id = serializers.IntegerField()
    server_id = serializers.IntegerField()
    class Meta:
        model = models.Channel
        fields = [
            "id",
            "server_id",
            "instructor_id",
            "name",
            "topic",
            "banner",
        ]


class ServerSerializer(serializers.ModelSerializer):
    instructor_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    category_name = serializers.StringRelatedField(source='category')
    num_members = serializers.SerializerMethodField()
   
    class Meta:
        model = models.Server
        fields = [
            "id",
            "category_id",
            "category_name",
            "instructor_id",
            "members",
            "name",
            "icon",
            "banner",
            "num_members",
            "description",
        ]
        extra_kwargs = {"members": {"write_only": True}}
    
    def get_num_members(self, instance) -> Optional[int]:
        if hasattr(instance, "with_num_members"):
            return instance.with_num_members
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        number_members = data.get("num_members")
        if number_members is None:
            data.pop("num_members")
        return data
