from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext as _


class IconMaxSizeExceeded(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = _("The maximum allowed dimensions for the image are 70x70.")
    default_code = 'icon_size_exceeded'

