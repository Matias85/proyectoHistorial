from .conexion import ConexionDB
from tkinter import messagebox
import traceback

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaMedica, p.apellido || " " || p.nombre AS Paciente, h.fechaHistoria, h.motivoDeConsulta, h.antecedenteDeEnfermedadActual, h.examenFisico, h.tricoscopia, h.indicaciones, h.estudiosSolicitados, h.tratamientoRealizado FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTA HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)    

    return listaHistoria    


def guardarHistoria(idPersona, fechaHistoria, motivoDeConsulta, antecedenteDeEnfermedadActual, examenFisico, tricoscopia, indicaciones, estudiosSolicitados, tratamientoRealizado):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona, fechaHistoria, motivoDeConsulta, antecedenteDeEnfermedadActual, examenFisico, tricoscopia, indicaciones, estudiosSolicitados, tratamientoRealizado) VALUES ({idPersona},'{fechaHistoria}', '{motivoDeConsulta}', '{antecedenteDeEnfermedadActual}', '{examenFisico}', '{tricoscopia}', '{indicaciones}', '{estudiosSolicitados}', '{tratamientoRealizado}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Medica'
        mensaje = 'Historia Registrada Exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Agregar Historia'
        mensaje = 'Error al agregar historia Medica'
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Agregar Historia: {str(e)}\n")
            traceback.print_exc(file=log_file)  
        messagebox.showerror(title, mensaje)    

def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'   

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia Medica'
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Eliminar Historia: {str(e)}\n")
            traceback.print_exc(file=log_file)  
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, motivoDeConsulta, antecedenteDeEnfermedadActual, examenFisico, tricoscopia, indicaciones, estudiosSolicitados, tratamientoRealizado, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = '{fechaHistoria}', motivoDeConsulta = '{motivoDeConsulta}', antecedenteDeEnfermedadActual = '{antecedenteDeEnfermedadActual}', examenFisico = '{examenFisico}', tricoscopia = '{tricoscopia}', indicaciones = '{indicaciones}', estudiosSolicitados = '{estudiosSolicitados}', tratamientoRealizado = '{tratamientoRealizado}' WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia Medica'
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Editar Historia: {str(e)}\n")
            traceback.print_exc(file=log_file)  
        messagebox.showerror(title, mensaje)

class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivoDeConsulta, antecedenteDeEnfermedadActual, examenFisico, tricoscopia, indicaciones, estudiosSolicitados, tratamientoRealizado):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivoDeConsulta = motivoDeConsulta
        self.antecedenteDeEnfermedadActual = antecedenteDeEnfermedadActual
        self.examenFisico = examenFisico
        self.tricoscopia = tricoscopia
        self.indicaciones = indicaciones
        self.estudiosSolicitados = estudiosSolicitados
        self.tratamientoRealizado = tratamientoRealizado

    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivoDeConsulta},{self.antecedenteDeEnfermedadActual},{self.examenFisico},{self.tricoscopia},{self.indicaciones},{self.estudiosSolicitados},{self.tratamientoRealizado}]'

    
