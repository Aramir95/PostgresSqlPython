import psycopg2
import logging

class FailConect(Exception):
    """Excepción que se lanza cuando no se puede establecer una conexión con la base de datos."""
    def __init__(self, message):
        """Inicializa la excepción con un mensaje de error."""
        self.message = message

    def __str__(self):
        return self.message

class FunctionExtras():
    @staticmethod
    def add_quotes(object):
        if isinstance(object, str):
            
            return f"'{object}'"
        return object
    
class DataBasePostgres():
    """Clase que representa una base de datos PostgreSQL.

    Atributos:
        host (str): El host de la base de datos.
        port (int): El puerto de la base de datos.
        user (str): El nombre de usuario para conectarse a la base de datos.
        password (str): La contraseña para conectarse a la base de datos.
        database_name (str): El nombre de la base de datos.
        conn (psycopg2.extensions.connection): La conexión a la base de datos.
    """
    def __init__(self , host: str, port: int , user: str, password: str, database_name: str):
        """Inicializa los atributos de la clase.

        Args:
            host (str): El host de la base de datos.
            port (int): El puerto de la base de datos.
            user (str): El nombre de usuario para conectarse a la base de datos.
            password (str): La contraseña para conectarse a la base de datos.
            database_name (str): El nombre de la base de datos existente ya en el servidor postgres.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name
        self.conn = self.connect()

    def connect(self) -> psycopg2.extensions.connection:
        """Intenta establecer una conexión con la base de datos.

        Si la conexión se realiza con éxito, muestra un mensaje de éxito. Si ocurre un error al conectarse, muestra un
        mensaje de error.
        """
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            logging.warning("Conexion exitosa")
            return self.conn

        except Exception as e:
            logging.error(f"Error al conectar a base de datos: {str(e)}")
            raise FailConect("No se pudo establecer una conexión con la base de datos")

