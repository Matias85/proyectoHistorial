import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame, font
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from modelo.historiaMedicaDao import historiaMedica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria, ScrolledFrame
import tkcalendar as tc
import traceback
from tkcalendar import *
from tkcalendar import Calendar
from datetime import date, datetime
from PIL import Image, ImageTk


class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None
        self.idHistoriaMedicaEditar = None
        #self.camposPaciente()
        #self.deshabilitar()
        self.tablaPaciente()
        self.buscadorPaciente()

        # CARGAR Y MOSTRAR LA IMAGEN DE VENTANA "AGREGAR PACIENTE"
        imagen1 = Image.open('img/aPaciente.png')
        imagen1 = imagen1.resize((80, 80))
        self.img1 = ImageTk.PhotoImage(imagen1)

        self.frame2 = tk.LabelFrame(self, text="Agregar Paciente", font=('ARIAL', 12, 'bold'), fg='#f74780', bg='#f7bfd8', border=5)
        self.frame2.place(relx=0.015, rely=0.01, relwidth=0.250, relheight=0.250)

        self.lbl_img = tk.Label(self.frame2, image=self.img1, bg='#f7bfd8' )
        self.lbl_img.place(relx=0.20, rely=0.01, relwidth=0.60, relheight=0.60)

        self.btnEnvia = tk.Button(self.frame2, text='Agregar Paciente', command=self.camposPaciente)
        self.btnEnvia.config(width=15, font=('ARIAL', 12, 'bold'), fg='#DAD5D6',
                             bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnEnvia.place(relx=0.07, rely=0.70, relwidth=0.85, relheight=0.25)

      

        # CARGAR Y MOSTRAR LA IMAGEN DE VENTANA "BUSCAR PACIENTE"
        imagen2 = Image.open('img/buscarPaciente.png')
        imagen2 = imagen2.resize((100, 100))
        self.img2 = ImageTk.PhotoImage(imagen2)

        self.lbl_img_buscar = tk.Label(self.frame1, image=self.img2, bg='#f7bfd8' )
        self.lbl_img_buscar.place(relx=0.007, rely=0.1)


    def camposPaciente(self):
        self.topAPaciente = Toplevel()
        self.topAPaciente.title('AGREGAR PACIENTE')
        self.topAPaciente.resizable(0,0)
        self.topAPaciente.geometry('815x570')
        self.topAPaciente.config(bg='#f7bfd8')

        
        #FRAME 1
        self.frameAgregarPaciente = tk.LabelFrame(self.topAPaciente)
        self.frameAgregarPaciente.config(bg='#f7bfd8', border=2)
        self.frameAgregarPaciente.pack(fill="both", expand="yes", pady=10, padx=20)
        
        #LABELS

        self.lblNombre = tk.Label(self.frameAgregarPaciente, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5) 
        
        self.lblApellido = tk.Label(self.frameAgregarPaciente, text='Apellido: ')
        self.lblApellido.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblApellido.grid(column=0, row=1, padx=10, pady=5)

        self.lblDni = tk.Label(self.frameAgregarPaciente, text='DNI: ')
        self.lblDni.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblDni.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechaDeNacimiento = tk.Label(self.frameAgregarPaciente, text='Fecha de Nacimiento: ')
        self.lblFechaDeNacimiento.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblFechaDeNacimiento.grid(column=0, row=3, padx=10, pady=5)
        
        self.lblEdad = tk.Label(self.frameAgregarPaciente, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblTelefono = tk.Label(self.frameAgregarPaciente, text='Teléfono: ')
        self.lblTelefono.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblTelefono.grid(column=0, row=5, padx=10, pady=5)

        self.lblProfesion = tk.Label(self.frameAgregarPaciente, text='Profesión: ')
        self.lblProfesion.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblProfesion.grid(column=0, row=6, padx=10, pady=5)

        self.lblApp = tk.Label(self.frameAgregarPaciente, text='APP: ')
        self.lblApp.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblApp.grid(column=0, row=7, padx=10, pady=5)

        self.lblApq = tk.Label(self.frameAgregarPaciente, text='APQ: ')
        self.lblApq.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblApq.grid(column=0, row=8, padx=10, pady=5)

        self.lblToxicos = tk.Label(self.frameAgregarPaciente, text='Tóxicos: ')
        self.lblToxicos.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblToxicos.grid(column=0, row=9, padx=10, pady=5)

        self.lblAlergias = tk.Label(self.frameAgregarPaciente, text='Alergias: ')
        self.lblAlergias.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblAlergias.grid(column=0, row=10, padx=10, pady=5)

        self.lblMedicamentos = tk.Label(self.frameAgregarPaciente, text='Medicamentos: ')
        self.lblMedicamentos.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblMedicamentos.grid(column=0, row=11, padx=10, pady=5)

        self.lblDieta = tk.Label(self.frameAgregarPaciente, text='Dieta: ')
        self.lblDieta.config(font=('ARIAL',14, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblDieta.grid(column=0, row=12, padx=10, pady=5)

        
        #ENTRIES

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self.frameAgregarPaciente, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self.frameAgregarPaciente, textvariable=self.svApellido)
        self.entryApellido.config(width=50, font=('ARIAL', 15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self.frameAgregarPaciente, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL', 15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechaDeNacimiento = tk.StringVar()
        self.entryFechaDeNacimiento = tk.Entry(self.frameAgregarPaciente, textvariable=self.svFechaDeNacimiento)
        self.entryFechaDeNacimiento.config(width=50, font=('ARIAL', 15))
        self.entryFechaDeNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)
        
        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self.frameAgregarPaciente, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self.frameAgregarPaciente, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL', 15))
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svProfesion = tk.StringVar()
        self.entryProfesion = tk.Entry(self.frameAgregarPaciente, textvariable=self.svProfesion)
        self.entryProfesion.config(width=50, font=('ARIAL', 15))
        self.entryProfesion.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svApp = tk.StringVar()
        self.entryApp = tk.Entry(self.frameAgregarPaciente, textvariable=self.svApp)
        self.entryApp.config(width=50, font=('ARIAL', 15))
        self.entryApp.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svApq = tk.StringVar()
        self.entryApq = tk.Entry(self.frameAgregarPaciente, textvariable=self.svApq)
        self.entryApq.config(width=50, font=('ARIAL', 15))
        self.entryApq.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svToxicos = tk.StringVar()
        self.entryToxicos = tk.Entry(self.frameAgregarPaciente, textvariable=self.svToxicos)
        self.entryToxicos.config(width=50, font=('ARIAL', 15))
        self.entryToxicos.grid(column=1, row=9, padx=10, pady=5, columnspan=2)

        self.svAlergias = tk.StringVar()
        self.entryAlergias = tk.Entry(self.frameAgregarPaciente, textvariable=self.svAlergias)
        self.entryAlergias.config(width=50, font=('ARIAL', 15))
        self.entryAlergias.grid(column=1, row=10, padx=10, pady=5, columnspan=2)

        self.svMedicamentos = tk.StringVar()
        self.entryMedicamentos = tk.Entry(self.frameAgregarPaciente, textvariable=self.svMedicamentos)
        self.entryMedicamentos.config(width=50, font=('ARIAL', 15))
        self.entryMedicamentos.grid(column=1, row=11, padx=10, pady=5, columnspan=2)

        self.svDieta = tk.StringVar()
        self.entryDieta = tk.Entry(self.frameAgregarPaciente, textvariable=self.svDieta)
        self.entryDieta.config(width=50, font=('ARIAL', 15))
        self.entryDieta.grid(column=1, row=12, padx=10, pady=5, columnspan=2)    

        #BUTTONS
        self.lblFechaDeNacimiento.bind('<Double-1>', self.vistaCalendario) 

        self.btnNuevo = tk.Button(self.frameAgregarPaciente, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=14, padx=10, pady=5)

        self.btnGuardar = tk.Button(self.frameAgregarPaciente, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=14, padx=10, pady=5)

        self.btnCancelar = tk.Button(self.frameAgregarPaciente, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=14, padx=10, pady=5)
 
    
           
    def buscadorPaciente(self):
              
        self.frame1 = LabelFrame(self, text="Buscar Pacientes",font=('ARIAL',12,'bold'),fg='#f74780', bg='#f7bfd8', border=5)
        self.frame1.place(relx=0.2749, rely=0.01, relwidth=0.69, relheight=0.25)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self.frame1, text='Buscar DNI: ')
        self.lblBuscarDni.config(font=('ARIAL',12, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblBuscarDni.place(relx=0.20, rely=0.05)

        self.lblBuscarApellido = tk.Label(self.frame1, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAL',12, 'bold'), bg='#f7bfd8', fg='#f74780')
        self.lblBuscarApellido.place(relx=0.20, rely=0.38)

        

        #ENTRYS 
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self.frame1, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=15, font=('ARIAL', 15))
        self.entryBuscarDni.place(relx=0.48, rely=0.03, relwidth=0.40, relheight=0.20)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self.frame1, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=15, font=('ARIAL', 15))
        self.entryBuscarApellido.place(relx=0.48, rely=0.38, relwidth=0.40, relheight=0.20)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self.frame1, text='Buscar', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=16, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#00396F', cursor='hand2', activebackground='#5B8DBD')
        self.btnBuscarCondicion.place(relx=0.20, rely=0.70, relwidth=0.35, relheight=0.25)

        self.btnLimpiarBuscador = tk.Button(self.frame1, text='Limpiar', command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=16, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#120061', cursor='hand2', activebackground='#7C6DC1')
        self.btnLimpiarBuscador.place(relx=0.60, rely=0.70, relwidth=0.35, relheight=0.25)

        self.entryBuscarDni.bind("<Return>", lambda event: self.buscarCondicion())
        self.entryBuscarApellido.bind("<Return>", lambda event: self.buscarCondicion())
        

    def vistaCalendario(self, event):
        self.topCalendario = Toplevel()
        self.topCalendario.title("FECHA DE NACIMIENTO")
        self.topCalendario.resizable(0,0) #Para que la ventana no pueda ampliarse
        self.topCalendario.iconbitmap('img/registro.ico')
        self.topCalendario.config(bg='#CDD8FF')

        default_date = date(1990, 1, 1).strftime('%d/%m/%Y')
        self.svCalendario = StringVar(value=default_date)
             
        self.calendar = tc.Calendar(self.topCalendario, selectmode='day', year=1990, month=1, day=1, locale='es_US', bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', textvariable=self.svCalendario, cursor='hand2', date_pattern='dd/mm/yyyy')
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
        self.topCalendario.destroy()
        

    def habilitar(self):
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
        
        self.topAPaciente.destroy()

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)    
        else:
            self.listaPersona = listar()
            self.listaPersona.reverse()
        
        self.scrollbarx = Scrollbar(self, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self, orient=VERTICAL)
        
        
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellido', 'Dni', 'FechaDeNacimiento', 'Edad', 'Telefono', 'Profesion', 'App', 'Apq', 'Toxicos', 'Alergias', 'Medicamentos', 'Dieta'))
        self.tabla.place(relx=0.015, rely=0.30, relwidth=0.940, relheight=0.55)   #****Posicionado relativo
     
        

        self.tabla.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.tabla.configure(selectmode='extended')

        self.scrollbary.configure(command=self.tabla.yview)
        self.scrollbarx.configure(command=self.tabla.xview)
        
        self.scrollbarx.place(relx=0.015793, rely=0.85, relwidth=0.940)    #***Posicionado relativo

        self.scrollbary.place(relx=0.955, rely=0.33, relheight=0.50)  #***Posicionado relativo
        
        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.bind('<Double-1>', self.mostrar_detalles_tabla)

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
        self.btnEditarPaciente.place(relx=0.015, rely=0.92,relwidth=0.206972, relheight=0.050)
        

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.place(relx=0.24, rely=0.92,relwidth=0.206972, relheight=0.050)
     

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.place(relx=0.464972, rely=0.92,relwidth=0.206972, relheight=0.050)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.place(relx=0.75, rely=0.92,relwidth=0.206972, relheight=0.050)
           
  
 
    def historiaMedica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            if (self.idPersona > 0):
                idPersona = self.idPersona

            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')                
            self.topHistoriaMedica.iconbitmap('img/registro.ico')
            self.topHistoriaMedica.config(bg='#CDD8FF')
            self.topHistoriaMedica.geometry('800x570')

            self.scrollbarx = Scrollbar(self.topHistoriaMedica, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.topHistoriaMedica, orient=VERTICAL)

            self.listaHistoria = listarHistoria(idPersona)  
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Paciente', 'Fecha Historia', 'Motivo De Consulta', 'Antecedente De Enfermedad Actual', 'Examen Fisico', 'Tricoscopia', 'Indicaciones', 'Estudios Solicitados', 'Tratamiento Realizado'), height=30)
            self.tablaHistoria.place(relx=0.015, rely=0.03, relwidth=0.940, relheight=0.80)

            self.tablaHistoria.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.tablaHistoria.configure(selectmode='extended')	
            self.scrollbary.configure(command=self.tablaHistoria.yview)
            self.scrollbarx.configure(command=self.tablaHistoria.xview)	
            
            self.scrollbarx.place(relx=0.015793, rely=0.83, relwidth=0.940)

            self.scrollbary.place(relx=0.955, rely=0.06, relheight=0.75)
            
            self.tablaHistoria.bind('<Double-1>', self.mostrar_detalles)  
            
            
            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Paciente')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo de Consulta')
            self.tablaHistoria.heading('#4', text='Antecedente De Enfermedad Actual')
            self.tablaHistoria.heading('#5', text='Examen Fisico')
            self.tablaHistoria.heading('#6', text='Tricoscopia')
            self.tablaHistoria.heading('#7', text='Indicaciones')
            self.tablaHistoria.heading('#8', text='Estudios Solicitados')
            self.tablaHistoria.heading('#9', text='Tratamiento Realizado')

            self.tablaHistoria.column('#0', anchor=CENTER, width=50)
            self.tablaHistoria.column('#1', anchor=CENTER, width=100)
            self.tablaHistoria.column('#2', anchor=CENTER, width=200)
            self.tablaHistoria.column('#3', anchor=CENTER, width=300)
            self.tablaHistoria.column('#4', anchor=CENTER, width=350)
            self.tablaHistoria.column('#5', anchor=CENTER, width=300)
            self.tablaHistoria.column('#6', anchor=CENTER, width=300)
            self.tablaHistoria.column('#7', anchor=CENTER, width=400)
            self.tablaHistoria.column('#8', anchor=CENTER, width=350)
            self.tablaHistoria.column('#9', anchor=CENTER, width=500)
           

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]))       
                                               
                  
            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771',cursor='hand2', activebackground='#7198E0')    
            self.btnGuardarHistoria.place(relx=0.015, rely=0.90,relwidth=0.206972, relheight=0.060)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#3A005D',cursor='hand2', activebackground='#B47CD6')  
            self.btnEditarHistoria.place(relx=0.24, rely=0.90,relwidth=0.206972, relheight=0.060)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#890011',cursor='hand2', activebackground='#DB939C')    
            self.btnEliminarHistoria.place(relx=0.464972, rely=0.90,relwidth=0.206972, relheight=0.060)

            self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000',cursor='hand2', activebackground='#6F6F6F')    
            self.btnSalirHistoria.place(relx=0.75, rely=0.90, relwidth=0.206972, relheight=0.060)

            self.idPersona = None   

        except Exception as e:
                title = 'Historia Medica'
                mensaje = 'Error al mostrar historial'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Historia Medica: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
                messagebox.showerror(title, mensaje)     
        
    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.iconbitmap('img/registro.ico')
        self.topAHistoria.config(bg='#f7bfd8')
        #FRAME 1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#f7bfd8', border=2)
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        #LABELS AGREGAR HISTORIA MEDICA
        self.lblMotivoDeConsultaHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de Consulta', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblMotivoDeConsultaHistoria.grid(row=0, column=0, padx=5, pady=3)
        
        self.lblAntecedenteDeEnfermedadActualHistoria = tk.Label(self.frameDatosHistoria, text='Antecedente De Enfermedad Actual', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblAntecedenteDeEnfermedadActualHistoria.grid(row=2, column=0, padx=5, pady=3)

        self.lblExamenFisicoHistoria = tk.Label(self.frameDatosHistoria, text='Examen Fisico', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblExamenFisicoHistoria.grid(row=4, column=0, padx=5, pady=3)

        self.lblTricoscopiaHistoria = tk.Label(self.frameDatosHistoria, text='Tricoscopia', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblTricoscopiaHistoria.grid(row=6, column=0, padx=5, pady=3)

        self.lblIndicacionesHistoria = tk.Label(self.frameDatosHistoria, text='Indicaciones', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblIndicacionesHistoria.grid(row=8, column=0, padx=5, pady=3)

        self.lblEstudiosSolicitadosHistoria = tk.Label(self.frameDatosHistoria, text='Estudios Solicitados', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblEstudiosSolicitadosHistoria.grid(row=10, column=0, padx=5, pady=3)

        self.lblTratamientoRealizadoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento Realizado', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblTratamientoRealizadoHistoria.grid(row=12, column=0, padx=5, pady=3)

        #ENTRY AGREGA HISTORIA MEDICA
        
        self.svMotivoDeConsultaHistoria = tk.StringVar()
        self.motivoDeConsultaHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoDeConsultaHistoria)
        self.motivoDeConsultaHistoria.config(width=60, font=('ARIAL', 15))
        self.motivoDeConsultaHistoria.grid(row=1, column=0, padx=5, pady=3, columnspan=2)

        self.svAntecedenteDeEnfermedadActualHistoria = tk.StringVar()
        self.antecedenteDeEnfermedadActualHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svAntecedenteDeEnfermedadActualHistoria)
        self.antecedenteDeEnfermedadActualHistoria.config(width=60, font=('ARIAL', 15))
        self.antecedenteDeEnfermedadActualHistoria.grid(row=3, column=0, padx=5, pady=3, columnspan=2)

        self.svExamenFisicoHistoria = tk.StringVar()
        self.examenFisicoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svExamenFisicoHistoria)
        self.examenFisicoHistoria.config(width=60, font=('ARIAL', 15))
        self.examenFisicoHistoria.grid(row=5, column=0, padx=5, pady=3, columnspan=2)

        self.svTricoscopiaHistoria = tk.StringVar()
        self.tricoscopiaHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTricoscopiaHistoria)
        self.tricoscopiaHistoria.config(width=60, font=('ARIAL', 15))
        self.tricoscopiaHistoria.grid(row=7, column=0, padx=5, pady=3, columnspan=2)

        self.svIndicacionesHistoria = tk.StringVar()
        self.indicacionesHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svIndicacionesHistoria)
        self.indicacionesHistoria.config(width=60, font=('ARIAL', 15))
        self.indicacionesHistoria.grid(row=9, column=0, padx=5, pady=3, columnspan=2)

        self.svEstudiosSolicitadosHistoria = tk.StringVar()
        self.estudiosSolicitadosHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svEstudiosSolicitadosHistoria)
        self.estudiosSolicitadosHistoria.config(width=60, font=('ARIAL', 15))
        self.estudiosSolicitadosHistoria.grid(row=11, column=0, padx=5, pady=3, columnspan=2)

        self.svTratamientoRealizadoHistoria = tk.StringVar()
        self.tratamientoRealizadoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoRealizadoHistoria)
        self.tratamientoRealizadoHistoria.config(width=60, font=('ARIAL', 15))
        self.tratamientoRealizadoHistoria.grid(row=13, column=0, padx=5, pady=3, columnspan=2)
        #FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#f7bfd8', border=2)
        self.frameFechaHistoria.pack(fill='both', expand='yes', padx=20, pady=10)

        #LABEL FECHA AGREGAR HISTORIA

        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)

        #ENTRY FECHA AGREGAR HISTORIA

        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria, takefocus=False)
        self.entryFechaHistoria.config(width=13, font=('ARIAL', 15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)

        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d/%m/%y %H:%M'))

        # Vincular función al evento de clic con el mouse
        self.entryFechaHistoria.bind("<Button-1>", self.editar_fecha)

    
        #BUTTONS AGREGA HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Agregar Historia', command=self.agregarHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir', command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')
        self.btnSalirAgregarHistoria.grid(row=2, column=2, padx=10, pady=5)

        self.idPersona = None   

    def editar_fecha(self, event):
        # Habilitar la edición del campo al hacer clic con el mouse
        self.entryFechaHistoria.config(state=tk.NORMAL)    

    def eliminarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)

            self.idHistoriaMedica = None
            self.topHistoriaMedica.destroy()
        except Exception as e:
                title = 'Eliminar Historia'
                mensaje = 'Error al eliminar historia Medica'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Eliminar Historia: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
                messagebox.showerror(title, mensaje)    

              

    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1] 
            self.motivoDeConsultaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2] 
            self.antecedenteDeEnfermedadActualEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3] 
            self.examenFisicoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4] 
            self.tricoscopiaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5] 
            self.indicacionesEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][6] 
            self.estudiosSolicitadosEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][7] 
            self.tratamientoRealizadoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][8]   

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.iconbitmap('img/registro.ico')
            self.topEditarHistoria.config(bg='#f7bfd8')

            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#f7bfd8', border=2)
            self.frameEditarHistoria.pack(fill='both', expand='yes', padx=20, pady=10)
                      

            #LABEL EDITAR HISTORIA
            self.lblMotivoDeConsultaEditar = tk.Label(self.frameEditarHistoria, text='Motivo de consulta', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblMotivoDeConsultaEditar.grid(row=0, column=0, padx=5, pady=3)

            self.lblAntecdenteDeEnfermedadActualEditar = tk.Label(self.frameEditarHistoria, text='Antecedente de Enfermedad Actual', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblAntecdenteDeEnfermedadActualEditar.grid(row=2, column=0, padx=5, pady=3)

            self.lblExamenFisicoEditar = tk.Label(self.frameEditarHistoria, text='Examen Fisico', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblExamenFisicoEditar.grid(row=4, column=0, padx=5, pady=3)

            self.lblTricoscopiaEditar = tk.Label(self.frameEditarHistoria, text='Tricoscopia', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblTricoscopiaEditar.grid(row=6, column=0, padx=5, pady=3)

            self.lblIndicacionesEditar = tk.Label(self.frameEditarHistoria, text='Indicaciones', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblIndicacionesEditar.grid(row=8, column=0, padx=5, pady=3)

            self.lblEstudiosSolicitadosEditar = tk.Label(self.frameEditarHistoria, text='Estudios Solicitados', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblEstudiosSolicitadosEditar.grid(row=10, column=0, padx=5, pady=3)

            self.lblTratamientoRealizadoEditar = tk.Label(self.frameEditarHistoria, text='Tratamiento Realizado', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblTratamientoRealizadoEditar.grid(row=12, column=0, padx=5, pady=3)

            
            #ENTRY EDITAR HISTORIA      
                               
            self.svMotivoDeConsultaEditar = tk.StringVar()
            self.entryMotivoDeConsultaEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoDeConsultaEditar)
            self.entryMotivoDeConsultaEditar.config(width=60, font=('ARIAL', 15))
            self.entryMotivoDeConsultaEditar.grid(row=1, column=0, padx=5, pady=3, columnspan=2)

            self.svAntecdenteDeEnfermedadActualEditar = tk.StringVar()
            self.entryAntecedenteDeEnfermedadActualEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svAntecdenteDeEnfermedadActualEditar)
            self.entryAntecedenteDeEnfermedadActualEditar.config(width=60, font=('ARIAL', 15))
            self.entryAntecedenteDeEnfermedadActualEditar.grid(row=3, column=0, padx=5, pady=3, columnspan=2)

            self.svExamenFisicoEditar = tk.StringVar()
            self.entryExamenFisicoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svExamenFisicoEditar)
            self.entryExamenFisicoEditar.config(width=60, font=('ARIAL', 15))
            self.entryExamenFisicoEditar.grid(row=5, column=0, padx=5, pady=3, columnspan=2)

            self.svTricoscopiaEditar = tk.StringVar()
            self.entryTricoscopiaEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTricoscopiaEditar)
            self.entryTricoscopiaEditar.config(width=60, font=('ARIAL', 15))
            self.entryTricoscopiaEditar.grid(row=7, column=0, padx=5, pady=3, columnspan=2)

            self.svIndicacionesEditar = tk.StringVar()
            self.entryIndicacionesEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svIndicacionesEditar)
            self.entryIndicacionesEditar.config(width=60, font=('ARIAL', 15))
            self.entryIndicacionesEditar.grid(row=9, column=0, padx=5, pady=3, columnspan=2)

            self.svEstudiosSolicitadosEditar = tk.StringVar()
            self.entryEstudiosSolicitadosEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svEstudiosSolicitadosEditar)
            self.entryEstudiosSolicitadosEditar.config(width=60, font=('ARIAL', 15))
            self.entryEstudiosSolicitadosEditar.grid(row=11, column=0, padx=5, pady=3, columnspan=2)

            self.svTratamientoRealizadoEditar = tk.StringVar()
            self.entryTratamientoRealizadoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoRealizadoEditar)
            self.entryTratamientoRealizadoEditar.config(width=60, font=('ARIAL', 15))
            self.entryTratamientoRealizadoEditar.grid(row=13, column=0, padx=5, pady=3, columnspan=2)
            
            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#f7bfd8', border=2)
            self.frameFechaEditar.pack(fill='both', expand='yes', padx=20, pady=10)
            
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL',14, 'bold'),bg='#f7bfd8', fg='#f74780')
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5, pady=3, columnspan=2)

            #ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=13, font=('ARIAL', 15))
            self.entryFechaHistoriaEditar.grid(row=1, column=2, pady=3, padx=5)
                             
              
            # #INSERTAR LOS VALORES A LOS ENTRYS*********************Estos eran los originales********************
             # Insertar texto en el widget ScrolledText
            self.entryMotivoDeConsultaEditar.insert(tk.END, self.motivoDeConsultaHistoriaEditar)
            self.entryAntecedenteDeEnfermedadActualEditar.insert(0, self.antecedenteDeEnfermedadActualEditar)
            self.entryExamenFisicoEditar.insert(0, self.examenFisicoEditar)
            self.entryTricoscopiaEditar.insert(0, self.tricoscopiaEditar)
            self.entryIndicacionesEditar.insert(0, self.indicacionesEditar)
            self.entryEstudiosSolicitadosEditar.insert(0, self.estudiosSolicitadosEditar)
            self.entryTratamientoRealizadoEditar.insert(0, self.tratamientoRealizadoEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)
            
            #BUTTON EDITAR HISTORIA

            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Editar Historia', command=self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#030058', cursor='hand2', activebackground='#8986DA')
            self.btnEditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirHistoriaMedica = tk.Button(self.frameFechaEditar, text='Salir', command=self.topEditarHistoria.destroy)
            self.btnSalirHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#676767')
            self.btnSalirHistoriaMedica.grid(row=2, column=2, padx=10, pady=5)

            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica

            self.idHistoriaMedica = None

        except Exception as e:
                title = 'Editar Historia'
                mensaje = 'No ha seleccionado ninguna historia'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Editar Historia: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
                messagebox.showerror(title, mensaje) 
    

    def agregarHistorialMedico(self):
         try:
             if self.idHistoriaMedica == None:
                 guardarHistoria(
                     self.idPersonaHistoria,
                     self.svFechaHistoria.get(),
                     self.svMotivoDeConsultaHistoria.get(),
                     self.svAntecedenteDeEnfermedadActualHistoria.get(),
                     self.svExamenFisicoHistoria.get(),
                     self.svTricoscopiaHistoria.get(),
                     self.svIndicacionesHistoria.get(),
                     self.svEstudiosSolicitadosHistoria.get(),
                     self.svTratamientoRealizadoHistoria.get()
                 )
             self.topAHistoria.destroy()
             self.topHistoriaMedica.destroy()
             self.idPersona = None   
         except Exception as e:
                title = 'Agregar Historia'
                mensaje = 'Error al agregar historia Medica'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Agregar Historia: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
                messagebox.showerror(title, mensaje)

    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoDeConsultaEditar.get(), self.svAntecdenteDeEnfermedadActualEditar.get(), self.svExamenFisicoEditar.get(), self.svTricoscopiaEditar.get(), self.svIndicacionesEditar.get(), self.svEstudiosSolicitadosEditar.get(), self.svTratamientoRealizadoEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except Exception as e:
                title = 'Editar Historia'
                mensaje = 'Error al editar historia Medica'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Editar Historia: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
                messagebox.showerror(title, mensaje)  
                self.topEditarHistoria.destroy() 

    
    def mostrar_detalles(self, event):
     selected_item = self.tablaHistoria.selection()
     if selected_item:
        item_id = selected_item[0]
        detalles = ""

        col_id = self.tablaHistoria.identify_column(event.x)  # Obtiene la columna en la que se hizo clic

        if col_id == '#1':  # Columna 'Paciente'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[0]
        elif col_id == '#2':  # Columna 'Fecha y Hora'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[1]
        elif col_id == '#3':  # Columna 'Motivo de Consulta'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[2]
        elif col_id == '#4':  # Columna 'Antecedente de Enfermedad Actual
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[3]    
        elif col_id == '#5':  # Columna 'Examen Fisico'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[4]  
        elif col_id == '#6':  # Columna 'Tricoscopia'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[5]   
        elif col_id == '#7':  # Columna 'Indicaciones'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[6]         
        elif col_id == '#8':  # Columna 'Estudios Solicitados'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[7]      
        elif col_id == '#9':  # Columna 'Tratamiento Realizado'
            col_title = self.tablaHistoria.heading(col_id)['text']
            detalles = self.tablaHistoria.item(item_id, 'values')[8]     
          
        # Obtener el nombre del paciente
        nombre_paciente = self.tablaHistoria.item(item_id, 'values')[0]  
      
        detalles_window = tk.Toplevel(self.root)
        detalles_window.title(f"Detalles de {nombre_paciente}")
        detalles_window.config(bg='#f7bfd8')  # Establecer el color de fondo de la ventana

        # Establecer el tamaño mínimo y máximo de la ventana al mismo tamaño
        width = 800  # Tamaño deseado en píxeles
        height = 600
        detalles_window.minsize(width, height)
        detalles_window.maxsize(width, height)

        detalles_frame = tk.LabelFrame(detalles_window, text=(col_title),font=('Helvetica', 15), bg='#f7bfd8',fg='#f74780', padx=20, pady=10, border=2)
        detalles_frame.pack(fill='both', expand='yes', padx=20, pady=10)
               
        detalles_text = scrolledtext.ScrolledText(detalles_frame, wrap=tk.WORD, height=20, width=70, font=('Arial', 15), bg='white')
        detalles_text.insert("1.0", detalles)
        detalles_text.config(state=tk.DISABLED)
        detalles_text.pack(padx=5, pady=5)

        cerrar_button = tk.Button(detalles_window, text="Cerrar", command=detalles_window.destroy)
        cerrar_button.config(width=20,height=10, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#2E64FE', cursor='hand2', activebackground='#81BEF7')
        cerrar_button.pack(pady=10)

    def mostrar_detalles_tabla(self, event):
     selected_item = self.tabla.selection()
     if selected_item:
        item_id = selected_item[0]
        detalles = ""

        col_id = self.tabla.identify_column(event.x)  # Obtiene la columna en la que se hizo clic

        if col_id == '#1':  # Columna 'Nombre'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[0]
        elif col_id == '#2':  # Columna 'Apellido'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[1]
        elif col_id == '#3':  # Columna 'Dni'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[2]
        elif col_id == '#4':  # Columna 'Fecha de Nacimiento'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[3]    
        elif col_id == '#5':  # Columna 'Edad'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[4]  
        elif col_id == '#6':  # Columna 'Teléfono'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[5]   
        elif col_id == '#7':  # Columna 'Profesión'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[6]         
        elif col_id == '#8':  # Columna 'App'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[7]      
        elif col_id == '#9':  # Columna 'Apq'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[8]     
	    
        elif col_id == '#10':  # Tóxicos'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[9] 
	    
        elif col_id == '#11':  # Columna 'Alergias'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[10] 
	    
        elif col_id == '#12':  # Columna 'Medicamentos'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[11] 
	    
        elif col_id == '#13':  # Columna 'Dieta'
            col_title = self.tabla.heading(col_id)['text']
            detalles = self.tabla.item(item_id, 'values')[12] 

	    
        nombre_tabla_paciente = self.tabla.item(item_id, 'values')[0]  # Nombre del paciente
        apellido_tabla_paciente = self.tabla.item(item_id, 'values')[1] # Apellido del paciente

        detalles_window_paciente = tk.Toplevel(self.root)
        detalles_window_paciente.title(f"Detalles de {apellido_tabla_paciente} {nombre_tabla_paciente}")
        detalles_window_paciente.config(bg='#f7bfd8')  # Establecer el color de fondo de la ventana

	# Establecer el tamaño mínimo y máximo de la ventana al mismo tamaño
        width = 800  # Tamaño deseado en píxeles
        height = 600
        detalles_window_paciente.minsize(width, height)
        detalles_window_paciente.maxsize(width, height)

	    
        detalles_frame_paciente = tk.LabelFrame(detalles_window_paciente, text=(col_title),font=('Helvetica', 15), bg='#f7bfd8',fg='#f74780', padx=20, pady=10, 	 border=2)
        detalles_frame_paciente.pack(fill='both', expand='yes', padx=20, pady=10)

	    
        detalles_text_paciente = scrolledtext.ScrolledText(detalles_frame_paciente, wrap=tk.WORD, height=20, width=70, font=('Arial', 15), bg='white')
        detalles_text_paciente.insert("1.0", detalles)
        detalles_text_paciente.config(state=tk.DISABLED)
        detalles_text_paciente.pack(padx=5, pady=5)

        cerrar_button_paciente = tk.Button(detalles_window_paciente, text="Cerrar", command=detalles_window_paciente.destroy)
        cerrar_button_paciente.config(width=20,height=10, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#2E64FE', cursor='hand2', activebackground='#81BEF7')
        cerrar_button_paciente.pack(pady=10)         


    def salirTop(self):
        self.topHistoriaMedica.destroy()
        #self.topAHistoria.destroy()     
        #self.topEditarHistoria.destroy()         
        self.idPersona = None  

    def editarPaciente(self):
        self.camposPaciente()
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
           
                
        except Exception as e:
                title = 'Editar Paciente'
                mensaje = 'Error al editar Paciente'
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Editar Paciente: {str(e)}\n")
                    traceback.print_exc(file=log_file)  
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



