from rest_framework.generics import RetrieveAPIView

from users.models import User
from users.serializers import UserProfileSerializer


class UserProfileViewSet(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "pk"
