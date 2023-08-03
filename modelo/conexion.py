import sqlite3

class ConexionDB:
    def __init__(self):
        self.conexion = sqlite3.connect('database/database.db')
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()
