from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoVievSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer
