import tkinter as tk
from paciente.gui import Frame
def main():
    root = tk.Tk()
    root.title('Registro de Historia Clínica')
    root.resizable(0,0)
    root.iconbitmap('img/registro.ico')
    frame = Frame(root)
    frame.mainloop()

if __name__ == '__main__':
    main()