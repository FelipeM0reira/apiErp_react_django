from companies.views.base import Base
from companies.utils.exceptions import RequiredFields
from companies.utils.permissions import GroupsPermission
from companies.serializers import GroupsSerializer

from accounts.models import Group, Group_Permissions

from rest_framework.views import Response
from rest_framework.exceptions import APIException

from django.contrib.auth.models import Permission

class Groups(Base):
    permission_classes = [GroupsPermission]

    def get(self, request):
        enterprise_id = self.get_enterprise_id(request.user.id)
        groups = Group.objects.filter(enterprise_id=enterprise_id).all()
        
        serializer = GroupsSerializer(groups, many=True)
        
        return Response({"groups": serializer.data})