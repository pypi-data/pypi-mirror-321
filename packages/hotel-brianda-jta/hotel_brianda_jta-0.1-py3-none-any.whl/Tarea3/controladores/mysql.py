"""
Módulo para gestionar la conexión con la base de datos MySQL
"""
__name__ = "mysql"
__author__ = "Jasmine Trillo Álvarez"

import mysql.connector
from mysql.connector import Error
    
def conectar():
    """
    Establece una conexión con la base de datos MySQL y retorna la conexión y el cursor.

    :return: La conexión a la base de datos y el cursor asociado para ejecutar consultas.
    """
    try:
        conexion = mysql.connector.connect(
                    host = "127.0.0.1",
                    port = 3306,
                    user = "hotel",
                    password = "Brianda23$",
                    database = "reservas"
                )
        cursor = conexion.cursor()
        return conexion, cursor
    
    except Error as e:
        print(f"Error al conectar con la base de datos. Comprueba la conexión. Más información: {e}")
        return None, None 