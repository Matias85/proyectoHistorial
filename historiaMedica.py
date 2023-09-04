import tkinter as tk
from paciente.gui import Frame

def main():
    root = tk.Tk()
    root.title('Registro de Historia Clínica')
    root.resizable(True, True) # La ventana ahora puede agrandarse o achicarse en ambas direcciones
    root.geometry("800x650")
    root.iconbitmap('img/registro.ico')
    frame = Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)  # Hacer que el Frame se ajuste al tamaño de la ventana
    root.mainloop()


if __name__ == '__main__':
    main()