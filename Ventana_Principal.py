from tkinter import*
import tkinter as tk

from Simulacion import Crear_Aleatorio, Click_Manual

base= tk.Tk()

# --> Diseño ventana principal

base.title("Entorno Simulación Coche Autónomo")
base.resizable(0,0)
base.iconbitmap("coche.ico")
base.geometry("650x450")
base.config(bg="#3092CE", bd="20")

# --> Variables

Ancho_as_int = IntVar(value=10)
Alto_as_int = IntVar(value=10)
NumOBS = IntVar(value=30)
ValorOpciones = tk.IntVar(value=1)

# --> Funciones

def Opciones(ancho, alto):
    opcion = int(ValorOpciones.get())
    num_obstaculos = int(NumOBS.get())
    area = ancho*alto
    porcentaje_obs = int(area*num_obstaculos/100)
    if (opcion == 1):
        Crear_Aleatorio(TRUE, ancho, alto, porcentaje_obs)
    if (opcion == 2):
        Click_Manual(TRUE, ancho, alto)

def send_data():
    ancho = int(Ancho_as_int.get())
    alto = int(Alto_as_int.get())
    Opciones(ancho, alto)

# --> Títulos

tituloTam=Label(base, text="DIMENSIÓN MAPA")
tituloTam.grid(row=0, column=0, pady=10, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloES=Label(base, text="ENTRADA/SALIDA")
tituloES.grid(row=3, column=1, pady=10)
tituloES.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloOB=Label(base, text="% OBSTÁCULOS             &")
tituloOB.grid(row=3, column=0, pady=10, padx=40)
tituloOB.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'), justify="center")

# --> Etiquetas

tituloAncho=Label(base, text="Ancho:")
tituloAncho.grid(row=1, column=0)
tituloAncho.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloAlto=Label(base, text="Alto:")
tituloAlto.grid(row=2, column=0)
tituloAlto.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloNum=Label(base, text="Nº Obstáculos (%):")
tituloNum.grid(row=4, column=0, padx=20)
tituloNum.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloComo=Label(base, text="¿Cómo?:")
tituloComo.grid(row=5, column=0, padx=20)
tituloComo.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

# --> Cuadro Texto

cuadroAncho=Entry(base, textvariable=Ancho_as_int)
cuadroAncho.grid(row=1, column=1, sticky="w")
cuadroAncho.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

cuadroAlto=Entry(base, textvariable=Alto_as_int)
cuadroAlto.grid(row=2, column=1, sticky="w")
cuadroAlto.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

cuadroNum=Entry(base, textvariable=NumOBS)
cuadroNum.grid(row=4, column=1, sticky="w", pady=5)
cuadroNum.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

# --> Botón Opciones

OpcionOB1 = tk.Radiobutton(base, text='Aleatorio', variable=ValorOpciones, value=1) 
OpcionOB1.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")
OpcionOB2 = tk.Radiobutton(base, text='Manual (Click)', variable=ValorOpciones, value=2) 
OpcionOB2.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB1.grid(row=5, column=1, sticky="w")
OpcionOB2.grid(row=6, column=1, sticky="w")

# --> Botones

send2 = Button(base, command=send_data, text="Actualizar Datos")
send2.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
send2.grid(column=0, row=13, pady=50)


base.mainloop()

