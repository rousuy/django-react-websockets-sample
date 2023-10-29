from backend.apps.server import exceptions
from PIL import Image


def validate_icon_image_size(image):
    if image is None:
        return
    with Image.open(image) as img:
        if img.width < 70 or img.height < 70:
            return
        raise exceptions.IconMaxSizeExceeded()
