import os
from uuid import uuid4
from apps.server import models


class PathGenerator:
    NAME_LENGTH: int = 15
    SERVER: str = "server"
    PREFIX_ICONS: str = "icons"
    PREFIX_BANNER: str = "banner"
    CATEGORY: str = "server/category"

    @classmethod
    def __generate_path(cls, instance, filename: str, prefix: str) -> str:
        filename = filename[-cls.NAME_LENGTH:]
        field: str = None

        if isinstance(instance, models.Server):
            field = cls.SERVER
        elif isinstance(instance, models.Category):
            field = cls.CATEGORY

        result: str = os.path.join(f"{field}/{prefix}/{str(uuid4())}-{filename}")
        return cls.__clean_path(result)
    
    @staticmethod
    def __clean_path(path: str) -> str:
        return path.lower().replace(" ", "-")

    @classmethod
    def icon_path(cls, instance, filename: str) -> str:
        prefix: str = cls.PREFIX_ICONS
        return cls.__generate_path(instance, filename, prefix)

    @classmethod
    def banner_path(cls, instance, filename: str) -> str:
        prefix: str = cls.PREFIX_BANNER
        return cls.__generate_path(instance, filename, prefix)


icon_path = PathGenerator.icon_path
banner_path = PathGenerator.banner_path
