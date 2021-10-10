from VentanaPrincipal import*

def Intro_Coordenadas(num_obstaculos):

    # --> Frames

    frame=Toplevel()
    frame.resizable(0,0)
    frame.iconbitmap("coche.ico")
    alto_frame = 450
    ancho_frame = 530
    frame.geometry(f"{alto_frame}x{ancho_frame}")
    frame.config(bg="#3892CF")

    SectionA=LabelFrame(frame)
    SectionB=LabelFrame(frame)
    
    myCanvas = Canvas(SectionA)
    myCanvas.pack(side=LEFT)
    
    yscrollbar=tk.Scrollbar(SectionA, orient="vertical", command=myCanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    myCanvas.configure(yscrollcommand=yscrollbar.set)
    myCanvas.bind("<Configure>", lambda e: myCanvas.configure(scrollregion = myCanvas.bbox("all")))
    myCanvas.config(width=380, height=400, bg="#3892CF")

    myFrame = Frame(myCanvas) 
    myFrame.pack()
    myFrame.config(bg="#3892CF")

    myCanvas.create_window((0,0), window=myFrame, anchor="nw")

    SectionA.pack(fill="both", expand="yes", padx=20, pady=10)
    SectionB.pack(fill="both", expand="yes", padx=20, pady=10)
    SectionA.config(bg="#3892CF")
    SectionB.config(bg="#3892CF")

    # --> Variables

    entrada_x = IntVar()
    entrada_y = IntVar()
    salida_x = IntVar()
    salida_y = IntVar()

    valor_coord = [*range(1, num_obstaculos*2+1, 1)]

    # --> Funciones
    """    
    def actualizar_info():
        coordenadas_entrada = []
        coordenadas_salida = []
        coordenadas_obstaculos = []

        for x in range(num_obstaculos*2):
            coordenadas_obstaculos[x].append(int(valor_coord[x])) 

        for y in range(num_obstaculos*2):
            print(coordenadas_obstaculos[y])

        coordenadas_entrada[0].append(int(entrada_x.get()))
        coordenadas_entrada[1].append(int(entrada_y.get()))

        coordenadas_salida[0].append(int(salida_x.get()))
        coordenadas_salida[1].append(int(salida_y.get()))
    """
    # --> Botón Actualizar Datos

    send = Button(SectionB, text="Actualizar Datos")
    send.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
    send.grid(column=0, padx=100, pady=15)

    # --> Etiquetas + Título

    Coordenada_titulo = Label(myFrame, text="COORDENADAS", justify="center")
    Coordenada_titulo.grid(row=0, column=1)
    Coordenada_titulo.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, "bold"))

    Coordenada_x = Label(myFrame, text="X", justify="center")
    Coordenada_x.grid(row=1, column=1)
    Coordenada_x.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, "bold"))

    Coordenada_y = Label(myFrame, text="Y", justify="center")
    Coordenada_y.grid(row=1, column=2)
    Coordenada_y.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, "bold"))

    # --> Creación de cuadros de texto y etiquetas (Obstáculos)

    self=[] 
    self_x=[]
    self_y=[]

    for x in range(num_obstaculos):
        self.append(Label(myFrame, text=f"Obstáculo {x+1}:"))
        self[x].grid(row=x+2, column=0, pady=2, padx=10)
        self[x].config(bg="#3092CE", fg="white", font=("Century Gothic", 12, "bold"))
        
        self_x.append(Entry(myFrame, textvariable=valor_coord[x], width=6))
        self_x[x].grid(row=x+2, column=1)
        self_x[x].config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

        self_y.append(Entry(myFrame, textvariable=valor_coord[x + num_obstaculos], width=6))
        self_y[x].grid(row=x+2, column=2)
        self_y[x].config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

    # --> Entry
    
    self_e_x = Entry(myFrame, textvariable=entrada_x, width=6)
    self_e_x.grid(row=num_obstaculos+2, column=1)
    self_e_x.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")
    
    self_e_y = Entry(myFrame, textvariable=entrada_y, width=6)
    self_e_y.grid(row=num_obstaculos+2, column=2)
    self_e_y.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")
    
    self_s_x = Entry(myFrame, textvariable=salida_x, width=6)
    self_s_x.grid(row=num_obstaculos+3, column=1)
    self_s_x.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")
    
    self_s_y = Entry(myFrame, textvariable=salida_y, width=6)
    self_s_y.grid(row=num_obstaculos+3, column=2)
    self_s_y.config(fg="#FF8837", font=("Century Gothic", 12, 'bold'), justify="center")

    # --> Etiquetas

    self_es = Label(myFrame, text="Entrada:")
    self_es.grid(row=num_obstaculos+2, column=0, pady=2, padx=10)
    self_es.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, "bold"))

    self_es = Label(myFrame, text="Salida:")
    self_es.grid(row=num_obstaculos+3, column=0, pady=2, padx=10)
    self_es.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, "bold"))

    
