from rest_framework.serializers import ModelSerializer
from SalaDeAula.models import SalaDeAula

class SalaDeAulaSerializer(ModelSerializer):

    class Meta:
        model = SalaDeAula
        fields = '__all__'
