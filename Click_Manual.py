from VentanaPrincipal import*

def Click_Manual(ancho, alto):

    # --> Frames 

    frame_intro=Toplevel()
    frame_intro.iconbitmap("coche.ico")
    alto_frame = 700
    ancho_frame = 700
    frame_intro.geometry(f"{ancho_frame}x{alto_frame}")
    
    frame_actualiza=Toplevel()
    frame_actualiza.resizable(0,0)
    frame_actualiza.iconbitmap("coche.ico")
    frame_actualiza.geometry("400x200")
    frame_actualiza.config(bg="#3892CF")

    # --> Funciones

    def color_change(x, y):
        self[x][y].config(bg="black")

    def color_change_2(x, y):
        self[x][y].config(bg="green")

    def color_change_3(x, y):
        self[x][y].config(bg="red")

    def boton_entrada():
        def boton_salida():
            send_e.destroy()
            selec_e.destroy()

            for x in range(ancho):
                for y in range(alto):
                    self[x][y].config(command=lambda x1=x, y1=y: color_change_3(x1, y1))

            send_s = Button(frame_actualiza, text="Actualizar Salida")
            send_s.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
            send_s.grid(row=1, column=0, pady=15, padx=90)
            
            selec_s = Label(frame_actualiza, text="Seleccione la salida", justify="center")
            selec_s.grid(row=0, column=0, padx=50, pady=20)
            selec_s.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, "bold"))
            
        send_obs.destroy()
        selec_obs.destroy()

        for x in range(ancho):
            for y in range(alto):
                self[x][y].config(command=lambda x1=x, y1=y: color_change_2(x1, y1))

        send_e = Button(frame_actualiza, command=boton_salida, text="Actualizar Entrada")
        send_e.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
        send_e.grid(row=1, column=0, pady=15, padx=80)

        selec_e = Label(frame_actualiza, text="Seleccione la entrada", justify="center")
        selec_e.grid(row=0, column=0, padx=40, pady=20)
        selec_e.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, "bold"))


    # --> Botones (frame_intro)

    self=[] 
    for x in range(ancho):
        self.append([])
        for y in range(alto):
            Grid.rowconfigure(frame_intro,y,weight=1) 
            Grid.columnconfigure(frame_intro,x,weight=1) 
            
            self[x].append(Button(frame_intro, command=lambda x1=x, y1=y: color_change(x1, y1), relief="groove"))
            self[x][y].grid(column=x, row=y, sticky="NSEW")

    # --> Botón Actualizar Obstáculos (frame_actualiza)

    send_obs = Button(frame_actualiza, command=boton_entrada, text="Actualizar Obstáculos")
    send_obs.config(fg="#FF8837", font=("Century Gothic", 18, 'bold'))
    send_obs.grid(row=1, column=0, padx=60, pady=15)

    # --> Etiqueta Seleccionar Obstáculos (frame_actualiza)

    selec_obs = Label(frame_actualiza, text="Seleccione los obstáculos", justify="center")
    selec_obs.grid(row=0, column=0, padx=20, pady=20)
    selec_obs.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, "bold"))
    