# ETL-CAT-INSS
Processo de Extração,Transformação e carregamento de dados cadastradas no sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB)

O projeto foi desenvolvido consolidando as bases disponibilizadas em uma única por meio do processo de ETL, utilizando como ferramentas o Colab bem como o Google Cloud e observando os seguintes parâmetros:

Da base de dados:
Os dados disponibilizados são da base dos dados de CAT do ano de 2022 contendo os dados cadastrados no sistema informatizado de Comunicação de Acidentes do Trabalho do INSS (CATWEB) ou quando da concessão de benefício por incapacidade acidentário. Por tais dados serem efetuados por sistema, telefone e ou presencial podem existir dados divergentes ou ausentes(faltantes).
1. Nível Infra:
O arquivo original e tratado deve ser salvo em MongoDB Atlas em coleções diferentes (enumerar com o final tratado ou original). Os Datasets devem ser obrigatoriamente salvos em uma bucket do CloudStorage(original e tratado). Disponibilizar o dataset final em um mysql. COMENTÁRIOS
2. Nível Pandas
Realizar a extração correta para um dataframe.
Verificar a existência de dados inconsistentes e realizar a limpeza para NaN/NA ou algum valor atribuído por você explicando o porque da decisão.
Realizar o drop(se necessário) de colunas do dataframe realizando o comentário do porque da exclusão
Todos os passos devem ser comentados(exclusivos)
Agregar todos os DF's originais em um unico DF tratado
Criar no mínimo 3 insights dos dados apresentados podendo ser construído com auxilio de plots.
3. Nivel PySpark
Deverá ser montada a estrutura do DataFrame utilizando o StructType.
Verificar a existência de dados inconsistentes, nulos e realizar a limpeza.
Verificar a necessidade de drop em colunas ou linhas. Caso seja necessário, fazer comentário do porque.
Realizar a mudança de nome de pelo menos 2 colunas
Deverá criar pelo menos duas novas colunas contendo alguma informação relevante sobre as outras colunas já existentes (Funções de Agrupamento, Agregação ou Joins). (Use a sua capacidade analítica)
Deverá utilizar filtros, ordenação e agrupamento, trazendo dados relevantes para o negócio em questão. (Use a sua capacidade analítica)
Utilizar pelo menos duas Window Functions
