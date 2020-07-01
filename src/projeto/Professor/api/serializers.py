from rest_framework.serializers import ModelSerializer
from Professor.models import Professor

class ProfessorSerializer(ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'
