from tkinter import*
import tkinter as tk

from Simulacion import *

base= tk.Tk()

# --> Diseño ventana principal

base.title("Entorno Simulación Coche Autónomo")
base.resizable(0,0)
base.iconbitmap("coche.ico")
base.geometry("630x750")
base.config(bg="#3092CE", bd="20")

# --> Variables

Ancho_as_int = IntVar(value=20)
Alto_as_int = IntVar(value=20)
NumOBS = IntVar(value=30)
ValorOpciones = tk.IntVar(value=1)
Nombre_Fichero = StringVar(value="mapa.txt")
Num_Dir = IntVar(value=4)
Algoritmo = IntVar(value=1)

# --> Funciones

def Opciones(ancho, alto):
    aleatorio = FALSE
    fichero = FALSE
    algoritmo = int(Algoritmo.get())
    direcciones = int(Num_Dir.get())
    opcion = int(ValorOpciones.get())
    num_obstaculos = int(NumOBS.get())
    area = ancho*alto
    nom_fich = str(Nombre_Fichero.get())
    porcentaje_obs = int(area*num_obstaculos/100)
    matriz_a.resize(alto, ancho)
    if (opcion == 1):
        aleatorio = TRUE
    if (opcion == 3):
        fichero = TRUE
    Click_Manual(TRUE, aleatorio, fichero, porcentaje_obs, direcciones, nom_fich, algoritmo)

def send_data():
    ancho = int(Ancho_as_int.get())
    alto = int(Alto_as_int.get())
    Opciones(ancho, alto)

def Intro_Fichero():
    cuadroAncho=Entry(base, textvariable=Nombre_Fichero)
    cuadroAncho.grid(row=9, column=0)
    cuadroAncho.config(fg="#213B69", font=("Century Gothic", 12, 'bold'), justify="center")

# --> Títulos

tituloTam=Label(base, text="DIMENSIÓN MAPA")
tituloTam.grid(row=0, column=0, pady=10, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloTam=Label(base, text="FUNCIÓN HEURÍSTICA")
tituloTam.grid(row=10, column=0, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloTam=Label(base, text="NÚMERO DIRECCIONES")
tituloTam.grid(row=3, column=0, pady=10, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloES=Label(base, text="ENTRADA/SALIDA")
tituloES.grid(row=5, column=1, pady=10)
tituloES.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloOB=Label(base, text="% OBSTÁCULOS             &")
tituloOB.grid(row=5, column=0, pady=10, padx=40)
tituloOB.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'), justify="center")

# --> Etiquetas

tituloAncho=Label(base, text="Ancho:")
tituloAncho.grid(row=1, column=0)
tituloAncho.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloAlto=Label(base, text="Alto:")
tituloAlto.grid(row=2, column=0)
tituloAlto.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloNum=Label(base, text="Nº Obstáculos (%):")
tituloNum.grid(row=6, column=0, padx=20)
tituloNum.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloComo=Label(base, text="¿Cómo?:")
tituloComo.grid(row=7, column=0, padx=20)
tituloComo.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloComo=Label(base, text="SPACE - Empezar\nClick Der. - Crear\nClick Izq. - Borrar")
tituloComo.grid(row=15, column=1, padx=20, pady=30)
tituloComo.config(bg="#3092CE", fg="#213B69", font=("Century Gothic", 14, 'bold'))

# --> Cuadro Texto

cuadroAncho=Entry(base, textvariable=Ancho_as_int)
cuadroAncho.grid(row=1, column=1, sticky="w")
cuadroAncho.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

cuadroAlto=Entry(base, textvariable=Alto_as_int)
cuadroAlto.grid(row=2, column=1, sticky="w")
cuadroAlto.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

cuadroNum=Entry(base, textvariable=NumOBS)
cuadroNum.grid(row=6, column=1, sticky="w", pady=5)
cuadroNum.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

# --> Botón Opciones

OpcionOB1 = tk.Radiobutton(base, text='Aleatorio', variable=ValorOpciones, value=1) 
OpcionOB1.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB2 = tk.Radiobutton(base, text='Manual (Click)', variable=ValorOpciones, value=2) 
OpcionOB2.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB3 = tk.Radiobutton(base, text='Fichero', variable=ValorOpciones, value=3, command=Intro_Fichero) 
OpcionOB3.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB1.grid(row=7, column=1, sticky="w")
OpcionOB2.grid(row=8, column=1, sticky="w")
OpcionOB3.grid(row=9, column=1, sticky="w")

Dir_4 = tk.Radiobutton(base, text=' >>>> 4 <<<< ', variable=Num_Dir, value=4) 
Dir_4.config(bg="#3092CE", fg="#213B69", font=("Century Gothic", 14, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

Dir_8 = tk.Radiobutton(base, text=' >>>> 8 <<<< ', variable=Num_Dir, value=8) 
Dir_8.config(bg="#3092CE", fg="#213B69", font=("Century Gothic", 14, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

Dir_4.grid(row=4, column=0)
Dir_8.grid(row=4, column=1)

Algoritmo1 = tk.Radiobutton(base, text='Manhattan', variable=Algoritmo, value=1) 
Algoritmo1.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

Algoritmo2 = tk.Radiobutton(base, text='Euclidean', variable=Algoritmo, value=2) 
Algoritmo2.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

Algoritmo3 = tk.Radiobutton(base, text='Chebyshev', variable=Algoritmo, value=3) 
Algoritmo3.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

Algoritmo1.grid(row=11, column=1, sticky="w")
Algoritmo2.grid(row=12, column=1, sticky="w")
Algoritmo3.grid(row=13, column=1, sticky="w")

# --> Botones

send2 = Button(base, command=send_data, text="Actualizar Datos")
send2.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
send2.grid(column=0, row=15, pady=30)


base.mainloop()

