from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    #vamos a decir que consultas se van a poder hacer con el viewset
    queryset = Project.objects.all()
    #permisos
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer