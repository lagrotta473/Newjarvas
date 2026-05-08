# Workflow: Relato e Tratamento de Não Conformidades

## Fatores Desencadeantes (Triggers)
1.  **Entrada:** O colaborador preenche um formulário (Google Forms).
2.  **Captura:** O n8n recebe o Webhook contendo os dados brutos (Data, Setor, Descrição, Severidade Estimada).

## Processamento (Core Logic)
1.  **Sanitização de Dados:** O n8n formata as datas e valida se os campos obrigatórios estão preenchidos.
2.  **Persistência no Banco de Dados:** O n8n realiza um `INSERT` no PostgreSQL na tabela `ocorrencias`. O banco de dados gera um ID único (ex: NC-2026-001).
3.  **Avaliação de Severidade:** Se a severidade for "Alta", o sistema sinaliza a flag `requires_root_cause = True`.

## Saída (Output e Notificação)
1.  **Criação de Card no Trello:** O n8n envia um payload para a API do Trello criando um card na lista "Caixa de Entrada".
    *   O Título do card DEVE conter o ID gerado pelo banco (ex: "[NC-2026-001] Falha de Calibração").
2.  **Atualização de Status:** Quando o card for movido no Trello para "Concluído", um webhook do Trello deve avisar o n8n para atualizar o status correspondente no PostgreSQL.
