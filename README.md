# Projeto ETL CATWEB — Versão Avançada 2025 🚀

Este é um redesenho completo do projeto original de ETL dos dados do sistema CATWEB (Comunicação de Acidentes do Trabalho do INSS), utilizando ferramentas modernas de engenharia de dados.

📌 **Objetivo:** Ingerir, transformar e disponibilizar dados de acidentes do trabalho no Brasil, com foco em automação, governança e escalabilidade.

---

## 🔄 Arquitetura Atualizada

**Pipeline Moderno com foco em Cloud & SQL-First:**

```mermaid
flowchart TD
  API[API CATWEB ou Fonte Dados Abertos]
  API -->|Ingestão Automatizada| GCS[Google Cloud Storage]
  GCS -->|Raw Layer| BigQuery[BigQuery ou PostgreSQL]
  BigQuery -->|Transformações SQL| dbt[dbt]
  dbt --> Airflow[Airflow]
  dbt --> Looker[Looker Studio / Power BI]
````

---

## 🧰 Stack Tecnológica

* Python
* Ingestão via API REST
* Google Cloud Storage (GCS)
* BigQuery ou PostgreSQL
* dbt (Transformações SQL com versionamento)
* Airflow (Orquestração)
* Looker Studio / Power BI

---

## 📁 Organização do Repositório

```
.
├── ingestion/           # Scripts Python para ingestão via API
├── transformation/      # Projetos dbt
├── airflow/             # DAGs de orquestração
├── data/                # Esquemas / Samples
├── docs/                # Diagramas e documentação
└── README.md
```

---

## 📊 Novos Insights Gerados

* Profissões com maior risco de acidentes
* Causas mais recorrentes por setor
* Análise geográfica por estado e cidade
* Evolução temporal por tipo de acidente

---

## 🕰 Histórico

Esta versão foi criada a partir do projeto original desenvolvido em 2022.
Você pode visualizar a versão original na [branch `main`](https://github.com/nayyarabernardo/etl-dados-cat-inss/tree/main).

---

## 💬 Contribuições

Pull requests são bem-vindos! Caso queira sugerir melhorias, fique à vontade para abrir uma issue ou entrar em contato.

```
