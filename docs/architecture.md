# Arquitetura do Sistema

## Padrão de Projeto (Design Pattern)
O backend Python (Django) será estruturado utilizando conceitos de **Clean Architecture**. O objetivo é separar as regras de negócio de qualidade (entidades e casos de uso) da infraestrutura (ORM do Django e rotas da web).

## Modelagem Preliminar de Dados (PostgreSQL)

**Tabela: `ocorrencias`**
*   `id` (UUID, Primary Key)
*   `codigo_nc` (String, Unique)
*   `data_relato` (Timestamp)
*   `descricao` (Text)
*   `severidade` (Enum: Baixa, Media, Alta)
*   `status` (Enum: Aberta, Em Analise, Concluida)
*   `link_trello` (String)

**Tabela: `analises_causa_raiz`**
*   `id` (UUID, Primary Key)
*   `ocorrencia_id` (Foreign Key -> ocorrencias.id)
*   `metodo_utilizado` (Enum: 5_Porques, Ishikawa)
*   `detalhes_analise` (JSONB)
*   `plano_acao` (Text)

## Redes Docker
Todos os serviços operam na mesma rede interna provida pelo Docker Compose. O n8n se comunica com o banco usando o hostname `db` na porta `5432`.
