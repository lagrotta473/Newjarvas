# Estratégia de Deploy e Infraestrutura

## 1. Ambiente de Hospedagem
*   **Provedor:** VPS Hostinger.
*   **Sistema Operacional:** Linux (Ubuntu/Debian).
*   **Gestão de Containers:** Todos os serviços (PostgreSQL, n8n, Django) rodam como daemons via Docker Compose.

## 2. Topologia de Rede e Segurança (Tailscale)
*   A VPS não expõe portas críticas diretamente para a internet pública (exceto as portas web HTTP/HTTPS 80 e 443, se configurado um proxy reverso).
*   O acesso administrativo aos serviços internos (ex: painel do n8n na porta 5678 e banco de dados na 5432) é feito através da rede privada do **Tailscale**.
*   **Comunicação do Agente:** Ao executar scripts de teste (pasta `/tools`), o agente deve assumir que os serviços estão acessíveis via `localhost` (quando rodando dentro da VPS) ou pelo IP do Tailscale, caso esteja rodando remotamente.

## 3. Dispositivo de Operação
*   O acesso e o desenvolvimento principal são realizados via iPad.
*   Quaisquer scripts ou ferramentas de linha de comando criados devem ser compatíveis com terminais SSH padrão e evitar dependências de interfaces gráficas (GUI) de desktop.
