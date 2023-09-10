from backend.apps.server import exceptions
from PIL import Image

def validate_icon_image_size(image):
    if not image:
        return
    with Image.open(image) as img:
        if not img.width > 70 or img.height > 70:
            return
        raise exceptions.IconMaxSizeExceeded()