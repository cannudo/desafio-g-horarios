from rest_framework.serializers import ModelSerializer
from SlotDeHorario.models import SlotDeHorario

class SlotDeHorarioSerializer(ModelSerializer):

    class Meta:
        model = SlotDeHorario
        fields = '__all__'
