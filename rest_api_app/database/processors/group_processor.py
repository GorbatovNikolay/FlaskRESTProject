from rest_api_app.database.models import Group
from .test_data import groups


class FillGroupProcessor:
    @classmethod
    def get_group_objects(cls) -> list:
        return [Group(name=group) for group in groups]
