# Case livup
## prototipo de solucao de agendamento

O prototipo tem como ideia utilizar o HTML como uma interface onde pode ser simulada a acao do cliente e visualisar informacoes do banco de dados.

Vale notar que nao se utiliza nenhuma forma de encriptacao de senhas uma vez que o ambiente e de testes, e os usuarios sao ficticios.

# Instrucoes para uso:

## Funcao main:

livup_prototype.py

## Notas de uso:

#### Edit

Conforme avisado abaixo, tanto os serviços em já núvem foram fechados. 

#### Informações (antigo)

Uma vez que o banco de dados utilizado foi o do Google Cloud, para criterios de avaliacao, o banco de dados esta aberto para todos. Uma vez que o banco e pago, ele sera mantido por um curto perio de tempo.

Se o acesso ao banco de dados estiver fechado, e possivel realizar o teste localmente.

Sao fornecidos os codigos de criacao das tabelas necessarias para o funcionamento do prototipo no arquivo sql_createtable_query.sql

Devem ser modificadas as credencias para o acesso do banco de dados encontradas em db_credentials.py

Infelizmente, a comunicação com a API de cálculo do tempo estimado de entrega foi encerrado e não é substituível, apenas em caso de criar uma própria e adicioná-lá na aplicação.

### Linguagem:

Python

HTML 

mySQL

### Pacotes (python):

Flask 

datetime

mysql.connector

request

json

