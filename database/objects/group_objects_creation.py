from database.models import Group
from .test_data import groups

group_objects = [Group(name=group) for group in groups]
