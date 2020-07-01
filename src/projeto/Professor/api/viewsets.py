from rest_framework.viewsets import ModelViewSet
from Professor.models import Professor
from .serializers import ProfessorSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
