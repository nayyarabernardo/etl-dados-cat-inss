Projeto ETL para dados do sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB)

Este projeto tem como objetivo consolidar as informações disponíveis no sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB), referentes ao ano de 2022. Os dados serão processados utilizando técnicas de extração, transformação e carregamento (ETL), utilizando ferramentas como Colab e Google Cloud.

## Escopo do Projeto Project

O objetivo do projeto é consolidar os dados disponíveis no sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB), referentes ao ano de 2022, e realizar a sua limpeza e organização. Os dados serão salvos em coleções diferentes no MongoDB Atlas e em um bucket do CloudStorage, e o dataset final será disponibilizado em um mysql. O projeto será desenvolvido em três níveis: infraestrutura, pandas e PySpark.

## Ingestão

A extração dos dados será realizada diretamente do sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB), utilizando técnicas de web scraping. Os dados serão baixados em formato CSV e posteriormente carregados no ambiente de processamento.
Processing
### Nível Infra

No nível de infraestrutura, o arquivo original e tratado será salvo em MongoDB Atlas em coleções diferentes, com a identificação do final tratado ou original. Os datasets serão obrigatoriamente salvos em um bucket do CloudStorage, tanto na versão original quanto na tratada. O dataset final será disponibilizado em um mysql.
### Nível Pandas

No nível Pandas, será realizada a extração dos dados para um dataframe, com a verificação da existência de dados inconsistentes e a realização da limpeza para NaN/NA ou algum valor atribuído pelo analista, com a explicação da decisão tomada. Será realizada a exclusão de colunas do dataframe, caso necessário, com a realização do comentário explicando a exclusão. Serão agregados todos os dataframes originais em um único dataframe tratado. 

### Nível PySpark

No nível PySpark, será montada a estrutura do dataframe utilizando o StructType, com a verificação da existência de dados inconsistentes, nulos e a realização da limpeza. Será verificada a necessidade de drop em colunas ou linhas, caso necessário, com a realização do comentário explicando a exclusão. Será realizada a mudança de nome de pelo menos 2 colunas. Serão criadas pelo menos duas novas colunas contendo alguma informação relevante sobre as outras colunas já existentes, utilizando funções de agrupamento, agregação ou joins. Serão utilizados filtros, ordenação e agrupamento, trazendo dados relevantes para o negócio em questão. Serão utilizadas pelo menos duas Window Functions.

### Storing

Os dados serão salvos em MongoDB Atlas em coleções diferentes, com a identificação do final tratado ou original. Os datasets serão obrigatoriamente salvos em um bucket do CloudStorage, tanto na versão original quanto na tratada. O dataset final será disponibilizado em um mysql.

## Considerações

O processo de ETL pode ser uma tarefa complexa, mas é fundamental para garantir a qualidade e consistência dos dados. Ao utilizar ferramentas como o Colab e o Google Cloud, podemos simplificar e automatizar muitas das etapas envolvidas. A limpeza e transformação dos dados foram etapas críticas para obter insights significativos. Durante este projeto, foram identificados e tratados vários problemas, como valores nulos, dados inconsistentes e colunas desnecessárias. 
As três insights identificadas neste projeto 
> as profissões com maior incidência de acidentes, 
> as causas mais comuns de acidentes 
> e os estados com mais registros de acidentes

podem ser úteis para diferentes públicos, como profissionais de segurança do trabalho, empresas e instituições governamentais.

## Contribuição

Este projeto é aberto a contribuições. Se você deseja melhorar ou adicionar recursos, sinta-se à vontade para criar uma solicitação pull ou entrar em [contato](https://www.linkedin.com/in/nayyarabernardo).

## Links

- [Documentation Apache Airflow](https://airflow.apache.org/docs/stable/)
- [Documentation Timeline Weather API ](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)

