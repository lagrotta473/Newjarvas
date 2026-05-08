import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ocorrencia(models.Model):
    """
    Entidade central do Sistema de Gestão de Qualidade.
    Registra todas as Não Conformidades (NCs) relatadas.
    """

    class SeveridadeChoices(models.TextChoices):
        BAIXA = 'BX', _('Baixa')
        MEDIA = 'MD', _('Média')
        ALTA = 'AL', _('Alta')

    class StatusChoices(models.TextChoices):
        ABERTA = 'AB', _('Aberta')
        EM_ANALISE = 'AN', _('Em Análise')
        CONCLUIDA = 'CO', _('Concluída')

    # UUID garante segurança e evita expor a volumetria de dados do sistema
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Código legível para o usuário final (ex: NC-2026-0001)
    codigo_nc = models.CharField(max_length=20, unique=True, verbose_name="Código da NC")

    data_relato = models.DateTimeField(auto_now_add=True, verbose_name="Data do Relato")

    descricao = models.TextField(verbose_name="Descrição da Não Conformidade")

    severidade = models.CharField(
        max_length=2,
        choices=SeveridadeChoices.choices,
        default=SeveridadeChoices.BAIXA,
        verbose_name="Nível de Severidade"
    )

    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.ABERTA,
        verbose_name="Status Operacional"
    )

    # Link gerado pelo n8n após criação do card no Trello
    link_trello = models.URLField(max_length=255, blank=True, null=True, verbose_name="Link do Card no Trello")

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        ordering = ['-data_relato']

    def __str__(self):
        return f"{self.codigo_nc} - {self.get_severidade_display()}"


class AnaliseCausaRaiz(models.Model):
    """
    Armazena os estudos de causa raiz.
    Exigida por regra de negócio para ocorrências de severidade ALTA.
    """

    class MetodoChoices(models.TextChoices):
        CINCO_PORQUES = '5P', _('5 Porquês')
        ISHIKAWA = 'IS', _('Diagrama de Ishikawa')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # OneToOne garante uma única análise definitiva por ocorrência
    ocorrencia = models.OneToOneField(
        Ocorrencia,
        on_delete=models.CASCADE,
        related_name='analise_causa_raiz',
        verbose_name="Ocorrência Vinculada"
    )

    metodo_utilizado = models.CharField(
        max_length=2,
        choices=MetodoChoices.choices,
        verbose_name="Método de Análise"
    )

    # JSONField permite estruturas distintas: 5 perguntas (5 Porquês) ou categorias (Ishikawa)
    detalhes_analise = models.JSONField(
        verbose_name="Detalhes Técnicos da Análise",
        help_text="Estrutura da análise em formato JSON (Ishikawa ou 5 Porquês)."
    )

    plano_acao = models.TextField(verbose_name="Plano de Ação Corretiva (5W2H)")

    data_analise = models.DateTimeField(auto_now_add=True, verbose_name="Data da Análise")

    class Meta:
        verbose_name = "Análise de Causa Raiz"
        verbose_name_plural = "Análises de Causa Raiz"

    def __str__(self):
        return f"Análise para {self.ocorrencia.codigo_nc} via {self.get_metodo_utilizado_display()}"
