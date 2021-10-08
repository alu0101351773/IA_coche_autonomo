from VentanaPrincipal import*
from Click_Manual import Click_Manual
from Intro_Coordenadas import Intro_Coordenadas

# --> Variables

Ancho_as_int = IntVar(value=10)
Alto_as_int = IntVar(value=10)
NumOBS = IntVar(value=30)
ValorOpciones = tk.IntVar(value=1)

# --> Funciones

def Start():
    botonEmpezar = Button(base, text="Empezar Simulación")
    botonEmpezar.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'), justify="center")
    botonEmpezar.grid(row=13, column=1, pady=50)

def Opciones(ancho, alto):
        opcion = int(ValorOpciones.get())
        if (opcion == 2):
            Click_Manual(ancho, alto)
        if (opcion == 3):
            Intro_Coordenadas(ancho, alto)

def send_data():
    ancho = int(Ancho_as_int.get())
    alto = int(Alto_as_int.get())
    area = ancho*alto
    num_obs = int(NumOBS.get())
    porcentaje_obs = int(area*num_obs/100)
    Opciones(ancho, alto)
    Start()

# --> Títulos

tituloTam=Label(base, text="DIMENSIÓN MAPA")
tituloTam.grid(row=0, column=0, pady=10, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloES=Label(base, text="ENTRADA/SALIDA")
tituloES.grid(row=3, column=1, pady=10)
tituloES.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloOB=Label(base, text="% OBSTÁCULOS             +")
tituloOB.grid(row=3, column=0, pady=10, padx=40)
tituloOB.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'), justify="center")

# --> Etiquetas

tituloAncho=Label(base, text="Ancho:")
tituloAncho.grid(row=1, column=0)
tituloAncho.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloAlto=Label(base, text="Alto:")
tituloAlto.grid(row=2, column=0)
tituloAlto.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

tituloNum=Label(base, text="Nº Obstáculos:")
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
OpcionOB3 = tk.Radiobutton(base, text='Manual (Coordenadas)', variable=ValorOpciones, value=3)
OpcionOB3.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB1.grid(row=5, column=1, sticky="w")
OpcionOB2.grid(row=6, column=1, sticky="w")
OpcionOB3.grid(row=7, column=1, sticky="w")

# --> Botones

send2 = Button(base, command=send_data, text="Actualizar Datos")
send2.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
send2.grid(column=0, row=13, pady=50)



