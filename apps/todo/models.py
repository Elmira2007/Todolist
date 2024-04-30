from django.db import models

from apps.users.models import Users

# Create your models here.
class Todo(models.Model):
    performing = models.ForeignKey(
        Users, on_delete=models.CASCADE,
        verbose_name = 'Выполняющий таск'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название задание",
        unique = True 
    )
    description = models.CharField(
        max_length = 600,
        verbose_name = "Описание"
    )
    image = models.ImageField(
        upload_to = 'image_todo/',
        verbose_name = 'Фотография'
    )
    is_completed = models.BooleanField(
        default = False,
        verbose_name = 'Статус выполнения'
    )
    creater_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата задание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списоки задач'
