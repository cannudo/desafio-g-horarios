from rest_framework.viewsets import ModelViewSet
from SalaDeAula.models import SalaDeAula
from .serializers import SalaDeAulaSerializer

class SalaDeAulaViewSet(ModelViewSet):
    queryset = SalaDeAula.objects.all()
    serializer_class = SalaDeAulaSerializer
