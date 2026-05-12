# Diretrizes do Sistema de Gestão de Qualidade (SGQ)

## 1. Definição de Não Conformidade (NC)
Qualquer desvio de um Procedimento Operacional Padrão (POP) estabelecido ou falha que impacte a integridade, segurança ou produtividade da operação.

## 2. Classificação de Severidade
*   **Baixa:** Erro documental ou desvio que não impacta o cliente final nem gera retrabalho significativo. Ação corretiva simples.
*   **Média:** Falha que gera gargalo no fluxo ou exige retrabalho interno, mas é contida antes de atingir o cliente.
*   **Alta:** Falha crítica. Exige contenção imediata.

## 3. Obrigatoriedade de Análise de Causa Raiz
*   Para NCs de severidade **Alta**, o sistema DEVE travar o fluxo no Kanban (Trello/Dashboard) até que uma ferramenta de análise de causa raiz seja preenchida.
*   **Ferramentas aceitas:** Diagrama de Ishikawa (Espinha de Peixe) ou os 5 Porquês.

## 4. Single Source of Truth
O banco de dados PostgreSQL é a única fonte da verdade. O Google Sheets e o Trello são apenas interfaces de visualização e entrada.
