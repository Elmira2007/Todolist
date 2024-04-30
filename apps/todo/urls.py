from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.todo.views import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet, basename='api_todo')

urlpatterns = router.urls
