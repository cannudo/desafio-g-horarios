from rest_framework.viewsets import ModelViewSet
from Turma.models import Turma
from .serializers import TurmaSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


@csrf_exempt
def post(self, request, format=None):
    return Response({'received data': request.data})
