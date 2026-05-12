from rest_framework import serializers
from .models import Ocorrencia, AnaliseCausaRaiz


class AnaliseCausaRaizSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseCausaRaiz
        fields = '__all__'


class OcorrenciaSerializer(serializers.ModelSerializer):
    analise_causa_raiz = AnaliseCausaRaizSerializer(read_only=True)

    class Meta:
        model = Ocorrencia
        fields = '__all__'
