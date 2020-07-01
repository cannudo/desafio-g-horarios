from rest_framework.serializers import ModelSerializer
from Turma.models import Turma

class TurmaSerializer(ModelSerializer):

    class Meta:
        model = Turma
        fields = '__all__'
