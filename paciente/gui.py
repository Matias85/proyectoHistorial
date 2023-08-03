import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import date, datetime

class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def camposPaciente(self):
         #LABELS

        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5) 

        self.lblApellido = tk.Label(self, text='Apellido: ')
        self.lblApellido.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApellido.grid(column=0, row=1, padx=10, pady=5)

        self.lblDni = tk.Label(self, text='DNI: ')
        self.lblDni.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechaDeNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechaDeNacimiento.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblFechaDeNacimiento.grid(column=0, row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Teléfono: ')
        self.lblTelefono.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=5, padx=10, pady=5)

        self.lblProfesion = tk.Label(self, text='Profesión: ')
        self.lblProfesion.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblProfesion.grid(column=0, row=6, padx=10, pady=5)

        self.lblApp = tk.Label(self, text='APP: ')
        self.lblApp.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApp.grid(column=0, row=7, padx=10, pady=5)

        self.lblApq = tk.Label(self, text='APQ: ')
        self.lblApq.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApq.grid(column=0, row=8, padx=10, pady=5)

        self.lblToxicos = tk.Label(self, text='Tóxicos: ')
        self.lblToxicos.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblToxicos.grid(column=0, row=9, padx=10, pady=5)

        self.lblAlergias = tk.Label(self, text='Alergias: ')
        self.lblAlergias.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblAlergias.grid(column=0, row=10, padx=10, pady=5)

        self.lblMedicamentos = tk.Label(self, text='Medicamentos: ')
        self.lblMedicamentos.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblMedicamentos.grid(column=0, row=11, padx=10, pady=5)

        self.lblDieta = tk.Label(self, text='Dieta: ')
        self.lblDieta.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblDieta.grid(column=0, row=12, padx=10, pady=5)

        #ENTRIES

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self, textvariable=self.svApellido)
        self.entryApellido.config(width=50, font=('ARIAL', 15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL', 15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechaDeNacimiento = tk.StringVar()
        self.entryFechaDeNacimiento = tk.Entry(self, textvariable=self.svFechaDeNacimiento)
        self.entryFechaDeNacimiento.config(width=50, font=('ARIAL', 15))
        self.entryFechaDeNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)
        
        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL', 15))
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svProfesion = tk.StringVar()
        self.entryProfesion = tk.Entry(self, textvariable=self.svProfesion)
        self.entryProfesion.config(width=50, font=('ARIAL', 15))
        self.entryProfesion.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svApp = tk.StringVar()
        self.entryApp = tk.Entry(self, textvariable=self.svApp)
        self.entryApp.config(width=50, font=('ARIAL', 15))
        self.entryApp.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svApq = tk.StringVar()
        self.entryApq = tk.Entry(self, textvariable=self.svApq)
        self.entryApq.config(width=50, font=('ARIAL', 15))
        self.entryApq.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svToxicos = tk.StringVar()
        self.entryToxicos = tk.Entry(self, textvariable=self.svToxicos)
        self.entryToxicos.config(width=50, font=('ARIAL', 15))
        self.entryToxicos.grid(column=1, row=9, padx=10, pady=5, columnspan=2)

        self.svAlergias = tk.StringVar()
        self.entryAlergias = tk.Entry(self, textvariable=self.svAlergias)
        self.entryAlergias.config(width=50, font=('ARIAL', 15))
        self.entryAlergias.grid(column=1, row=10, padx=10, pady=5, columnspan=2)

        self.svMedicamentos = tk.StringVar()
        self.entryMedicamentos = tk.Entry(self, textvariable=self.svMedicamentos)
        self.entryMedicamentos.config(width=50, font=('ARIAL', 15))
        self.entryMedicamentos.grid(column=1, row=11, padx=10, pady=5, columnspan=2)

        self.svDieta = tk.StringVar()
        self.entryDieta = tk.Entry(self, textvariable=self.svDieta)
        self.entryDieta.config(width=50, font=('ARIAL', 15))
        self.entryDieta.grid(column=1, row=12, padx=10, pady=5, columnspan=2)

        #BUTTONS

        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=14, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=14, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=14, padx=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self, text='Buscar DNI: ')
        self.lblBuscarDni.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblBuscarDni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS 
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=('ARIAL', 15))
        self.entryBuscarDni.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=('ARIAL', 15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#00396F', cursor='hand2', activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#120061', cursor='hand2', activebackground='#7C6DC1')
        self.btnLimpiarBuscador.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

        self.entryBuscarDni.bind("<Return>", lambda event: self.buscarCondicion())
        self.entryBuscarApellido.bind("<Return>", lambda event: self.buscarCondicion())

        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command=self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#53005B', cursor='hand2', activebackground='#C774CF')
        self.btnCalendario.grid(column=3, row=3, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA DE NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#CDD8FF')

        default_date = date(1990, 1, 1).strftime('%d/%m/%Y')
        self.svCalendario = StringVar(value=default_date)
             
        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1990, month=1, day=1, locale='es_US', bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', textvariable=self.svCalendario, cursor='hand2', date_pattern='dd/mm/yyyy')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column=0)

        #TRACE ENVIAR FECHA
        self.svCalendario.trace('w',self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFechaDeNacimiento.set(self.svCalendario.get())  # Sin el prefijo ' ' para la fecha de nacimiento
        self.calcularEdad()  # Llamada directa a la función calcularEdad() sin args
        
            
    def calcularEdad(self):
        fecha_actual = date.today()
        fecha_nacimiento_str = self.svFechaDeNacimiento.get()

    # Formatear la fecha de nacimiento al formato "%d-%m-%Y"
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()

        edad = fecha_actual.year - fecha_nacimiento.year
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1

        self.svEdad.set(edad)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE dni = " + self.svBuscarDni.get() + "" #WHERE dni = 87878787
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellido LIKE '" + self.svBuscarApellido.get() + "%' AND activo = 1" 

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()               

        
    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellido.get(), self.svDni.get(), self.svFechaDeNacimiento.get(), self.svEdad.get(),
            self.svTelefono.get(), self.svProfesion.get(), self.svApp.get(), self.svApq.get(), self.svToxicos.get(),
            self.svAlergias.get(), self.svMedicamentos.get(), self.svDieta.get()
        )  

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        self.deshabilitar()
        self.tablaPaciente() 

    def habilitar(self):
        # self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaDeNacimiento.set('')
        self.svEdad.set('')
        self.svTelefono.set('')
        self.svProfesion.set('')
        self.svApp.set('')
        self.svApq.set('')
        self.svToxicos.set('')
        self.svAlergias.set('')
        self.svMedicamentos.set('')
        self.svDieta.set('')

        self.entryNombre.config(state='normal')
        self.entryApellido.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFechaDeNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryProfesion.config(state='normal')
        self.entryApp.config(state='normal')
        self.entryApq.config(state='normal')
        self.entryToxicos.config(state='normal')
        self.entryAlergias.config(state='normal')
        self.entryMedicamentos.config(state='normal')
        self.entryDieta.config(state='normal')    

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaDeNacimiento.set('')
        self.svEdad.set('')
        self.svTelefono.set('')
        self.svProfesion.set('')
        self.svApp.set('')
        self.svApq.set('')
        self.svToxicos.set('')
        self.svAlergias.set('')
        self.svMedicamentos.set('')
        self.svDieta.set('')

        self.entryNombre.config(state='disabled')
        self.entryApellido.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFechaDeNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryProfesion.config(state='disabled')
        self.entryApp.config(state='disabled')
        self.entryApq.config(state='disabled')
        self.entryToxicos.config(state='disabled')
        self.entryAlergias.config(state='disabled')
        self.entryMedicamentos.config(state='disabled')
        self.entryDieta.config(state='disabled')    

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)    
        else:
            self.listaPersona = listar()
            self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellido', 'Dni', 'FechaDeNacimiento', 'Edad', 'Telefono', 'Profesion', 'App', 'Apq', 'Toxicos', 'Alergias', 'Medicamentos', 'Dieta'))
        self.tabla.grid(column=0, row=15, columnspan=14, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=15, column=15, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Dni')
        self.tabla.heading('#4',text='Fecha de Nacimiento')
        self.tabla.heading('#5',text='Edad')
        self.tabla.heading('#6',text='Telefono')
        self.tabla.heading('#7',text='Profesion')
        self.tabla.heading('#8',text='App')
        self.tabla.heading('#9',text='Apq')
        self.tabla.heading('#10',text='Toxicos')
        self.tabla.heading('#11',text='Alergia')
        self.tabla.heading('#12',text='Medicamentos')
        self.tabla.heading('#13',text='Dieta')

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=150)
        self.tabla.column('#2', anchor=W, width=120)
        self.tabla.column('#3', anchor=W, width=80)
        self.tabla.column('#4', anchor=W, width=120)
        self.tabla.column('#5', anchor=W, width=50)
        self.tabla.column('#6', anchor=W, width=85)
        self.tabla.column('#7', anchor=W, width=150)
        self.tabla.column('#8', anchor=W, width=150)
        self.tabla.column('#9', anchor=W, width=150)
        self.tabla.column('#10', anchor=W, width=150)
        self.tabla.column('#11', anchor=W, width=150)
        self.tabla.column('#12', anchor=W, width=150)
        self.tabla.column('#13', anchor=W, width=150)

        for p in self.listaPersona:

            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13]), tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=16, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=16, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=16, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=16, column=5, padx=10, pady=5)

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.fechaDeNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.profesionPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.appPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.apqPaciente = self.tabla.item(self.tabla.selection())['values'][8]
            self.toxicosPaciente = self.tabla.item(self.tabla.selection())['values'][9]
            self.alergiasPaciente = self.tabla.item(self.tabla.selection())['values'][10]
            self.medicamentosPaciente = self.tabla.item(self.tabla.selection())['values'][11]
            self.dietaPaciente = self.tabla.item(self.tabla.selection())['values'][12]
            
            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApellido.insert(0,self.apellidoPaciente)
            self.entryDni.insert(0,self.dniPaciente)
            self.entryFechaDeNacimiento.insert(0,self.fechaDeNacimientoPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)
            self.entryProfesion.insert(0, self.profesionPaciente)
            self.entryApp.insert(0, self.appPaciente)
            self.entryApq.insert(0,self.apqPaciente)
            self.entryToxicos.insert(0,self.toxicosPaciente)
            self.entryAlergias.insert(0, self.alergiasPaciente)
            self.entryMedicamentos.insert(0, self.medicamentosPaciente)
            self.entryDieta.insert(0, self.dietaPaciente)
         
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)   




        


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Registro de Historia Clínica')
    root.resizable(0,0)
    app = Frame(root)
    root.mainloop()

