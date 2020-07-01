from rest_framework.viewsets import ModelViewSet
from Disciplina.models import Disciplina
from .serializers import DisciplinaSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
