from rest_framework.viewsets import ModelViewSet
from SlotDeHorario.models import SlotDeHorario
from .serializers import SlotDeHorarioSerializer

class SlotDeHorarioViewSet(ModelViewSet):
    queryset = SlotDeHorario.objects.all()
    serializer_class = SlotDeHorarioSerializer
