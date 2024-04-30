from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.models import Users
from apps.users.serializers import UsersSerializers

class UsersViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers