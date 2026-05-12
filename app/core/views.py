from rest_framework import viewsets
from .models import Ocorrencia, AnaliseCausaRaiz
from .serializers import OcorrenciaSerializer, AnaliseCausaRaizSerializer


class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


class AnaliseCausaRaizViewSet(viewsets.ModelViewSet):
    queryset = AnaliseCausaRaiz.objects.all()
    serializer_class = AnaliseCausaRaizSerializer
