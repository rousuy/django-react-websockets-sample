from typing import Optional

from rest_framework import serializers
from server import models


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Channel
        fields = [
            "id",
            "name",
            "instructor",
            "topic",
            "server",
        ]


class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()

    class Meta:
        model = models.Server
        fields = [
            "id",
            "name",
            "category",
            "instructor",
            "num_members",
            "description",
        ]

    def get_num_members(self, instance) -> Optional[int]:
        print(hasattr(instance, "with_num_members"))
        if hasattr(instance, "with_num_members"):
            return instance.num_members
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        number_members = data.get("num_members")
        if not number_members:
            data.pop("num_members", None)
        return data


class ServerListSerializer(ServerSerializer):
    channel_servers = ChannelSerializer(many=True)

    class Meta(ServerSerializer.Meta):
        fields = ServerSerializer.Meta.fields + ["channel_servers"]
