from companies.views.base import Base
from companies.utils.permissions import GroupsPermission
from companies.serializers import PermissionsSerializer

from rest_framework.response import Response

from django.contrib.auth.models import Permission

class PermissionsDetail(Base):
    permission_classes = [GroupsPermission]

    def get(self, request):
       ...