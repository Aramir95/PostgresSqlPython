from Postgress.ClassPostgress import DataBasePostgres

user="postgres"
name_db="postgres"
pythonname_db="postgres"
password="12345678"
host="localhost"
port="5432"


database=DataBasePostgres(host=host, port=port,user=user, password=password, database_name=name_db)
database.connect()

print("probando establecer conexion")