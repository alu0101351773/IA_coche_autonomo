from VentanaPrincipal import*
from Simulador import Simulator

Ancho_as_int = IntVar(value=0)
Alto_as_int = IntVar(value=0)
NumOBS = IntVar(value=0)

# --> Botón Empezar

def Start():
    botonEmpezar = Button(base, text="Empezar Simulación")
    botonEmpezar.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
    botonEmpezar.grid(row=13, column=1, pady=70)

def send_data():
    ancho = int(Ancho_as_int.get())
    alto = int(Alto_as_int.get())
    area = ancho*alto
    num_obs = int(NumOBS.get())
    porcentaje_obs = int(area*num_obs/100)
    Simulator(ancho, alto)
    Start()


# --> Dimensión Mapa 

tituloTam=Label(base, text="DIMENSIÓN MAPA")
tituloTam.grid(row=0, column=0, pady=10, padx=40)
tituloTam.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloAncho=Label(base, text="Ancho:")
tituloAncho.grid(row=1, column=0)
tituloAncho.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

cuadroAncho=Entry(base, textvariable=Ancho_as_int)
cuadroAncho.grid(row=1, column=1, sticky="w")
cuadroAncho.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

tituloAlto=Label(base, text="Alto:")
tituloAlto.grid(row=2, column=0)
tituloAlto.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

cuadroAlto=Entry(base, textvariable=Alto_as_int)
cuadroAlto.grid(row=2, column=1, sticky="w")
cuadroAlto.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

send2 = Button(base, command=send_data, text="Actualizar Datos")
send2.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
send2.grid(column=0, row=13, pady=70)

# --> Obstáculos

tituloOB=Label(base, text="OBSTÁCULOS")
tituloOB.grid(row=3, column=0, pady=10, padx=40)
tituloOB.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloNum=Label(base, text="Nº Obstáculos:")
tituloNum.grid(row=4, column=0, padx=20)
tituloNum.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

cuadroNum=Entry(base, textvariable=NumOBS)
cuadroNum.grid(row=4, column=1, sticky="w", pady=5)
cuadroNum.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

tituloComo=Label(base, text="¿Cómo?:")
tituloComo.grid(row=5, column=0, padx=20)
tituloComo.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

ValorOpcionOB = tk.IntVar() 

OpcionOB1 = tk.Radiobutton(base, text='Aleatorio', variable=ValorOpcionOB, value=1) 
OpcionOB1.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")
OpcionOB2 = tk.Radiobutton(base, text='Manual (Click)', variable=ValorOpcionOB, value=2) 
OpcionOB2.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")
OpcionOB3 = tk.Radiobutton(base, text='Manual (Coordenadas)', variable=ValorOpcionOB, value=3)
OpcionOB3.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionOB1.grid(row=5, column=1, sticky="w")
OpcionOB2.grid(row=6, column=1, sticky="w")
OpcionOB3.grid(row=7, column=1, sticky="w")

