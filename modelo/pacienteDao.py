from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
        conexion = ConexionDB()
        sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellido = '{persona.apellido}', dni = '{persona.dni}', fechaNacimiento = '{persona.fechaNacimiento}', edad = '{persona.edad}', telefono = '{persona.telefono}', profesion = '{persona.profesion}', app = '{persona.app}', apq = '{persona.apq}', toxicos = '{persona.toxicos}', alergias = '{persona.alergias}', medicamentos = '{persona.medicamentos}', dieta = '{persona.dieta}', activo = 1 WHERE idPersona = {idPersona}"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrarConexion()
            title = 'Editar Paciente'
            mensaje = 'Paciente Editado Exitosamente'
            messagebox.showinfo(title, mensaje)
        except Exception as e:
            title = 'Editar Paciente - Error'
            mensaje = f'Error al editar paciente: {e}'
            messagebox.showerror(title, mensaje)
            print(f"Error: {e}")
            print("SQL:", sql)
            print("Datos:", datos)

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = """INSERT INTO Persona (nombre, apellido, dni, fechaNacimiento, edad, telefono, profesion, app, apq, toxicos, alergias,
             medicamentos, dieta, activo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)"""
    datos = (persona.nombre, persona.apellido, persona.dni, persona.fechaNacimiento, persona.edad, persona.telefono,
             persona.profesion, persona.app, persona.apq, persona.toxicos, persona.alergias, persona.medicamentos,
             persona.dieta)
    try:
        conexion.cursor.execute(sql, datos)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title, mensaje)
        print(f"Error: {e}")
        print("SQL:", sql)
        print("Datos:", datos)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona    

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)  
    return listaPersona       

def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)




class Persona:
    def __init__(self, nombre, apellido, dni, fechaNacimiento, edad, telefono, profesion, app, apq, toxicos, alergias, medicamentos, dieta):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.telefono = telefono
        self.profesion = profesion
        self.app = app
        self.apq = apq
        self.toxicos = toxicos
        self.alergias = alergias
        self.medicamentos = medicamentos
        self.dieta = dieta

    def __str__(self):
        return f'Persona[{self.nombre}, {self.apellido}, {self.dni}, {self.fechaNacimiento}, {self.edad}, {self.telefono}, {self.profesion}, {self.app}, {self.apq}, {self.toxicos}, {self.alergias}, {self.medicamentos}, {self.dieta}]'