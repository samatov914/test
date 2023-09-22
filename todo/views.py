from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class ToDoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer