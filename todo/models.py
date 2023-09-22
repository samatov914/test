from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        verbose_name="описание"
    )
    completed = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Список дел"
        verbose_name_plural = "Список дел"