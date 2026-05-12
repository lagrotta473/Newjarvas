from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OcorrenciaViewSet, AnaliseCausaRaizViewSet

router = DefaultRouter()
router.register(r'ocorrencias', OcorrenciaViewSet)
router.register(r'analises', AnaliseCausaRaizViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
