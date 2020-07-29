import mysql.connector
import db_credentials as cred

cnx = mysql.connector.connect(user=cred.user(), password=cred.password(),host=cred.host(),database=cred.db())
cursor = cnx.cursor()

query = ("SELECT endereco FROM cliente WHERE id_cliente = 1")

print(query)
cursor.execute(query)

cnx.close()    

output = []
for c in cursor:
    output.append(c)
print(output[0][0])