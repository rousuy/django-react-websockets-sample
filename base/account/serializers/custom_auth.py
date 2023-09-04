from typing import Any, Dict, Mapping

from django.contrib.auth import get_user_model, user_logged_in
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validate = super().validate(attrs)
        user_logged_in.send(
            sender=self.user.__class__,
            request=self.context["request"],
            user=self.user,
        )
        return validate

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        hydrated_token = cls.add_custom_claims(user, token)

        return hydrated_token

    @classmethod
    def add_custom_claims(
        cls,
        user: User,
        token: Mapping[str, Any],
    ) -> Dict[str, Any]:
        token["email"] = user.email
        token["username"] = user.username
        token["firstName"] = user.first_name
        token["lastName"] = user.last_name
        return token
