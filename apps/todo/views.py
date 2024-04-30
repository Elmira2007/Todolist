from django.urls import path
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializers

class TodoViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['title']
    permission_classes = (IsAuthenticated, )