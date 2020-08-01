import mysql.connector
import db_credentials as cred

cnx = mysql.connector.connect(user=cred.user(), password=cred.password(),host=cred.host(),database=cred.db())
cursor = cnx.cursor()

query = ("SHOW TABLES")

print(query)
cursor.execute(query)

cnx.close()    

output = []
for c in cursor:
    output.append(c[0])
for a in output:
    print(a[0])