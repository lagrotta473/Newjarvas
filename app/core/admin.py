from django.contrib import admin
from .models import Ocorrencia, AnaliseCausaRaiz


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo_nc', 'severidade', 'status', 'data_relato')
    list_filter = ('severidade', 'status')
    search_fields = ('codigo_nc', 'descricao')
    ordering = ('-data_relato',)


@admin.register(AnaliseCausaRaiz)
class AnaliseCausaRaizAdmin(admin.ModelAdmin):
    list_display = ('ocorrencia', 'metodo_utilizado', 'data_analise')
    list_filter = ('metodo_utilizado',)
    search_fields = ('ocorrencia__codigo_nc',)
