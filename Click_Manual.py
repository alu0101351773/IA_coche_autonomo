from VentanaPrincipal import*

def Click_Manual(ancho, alto):
    frame=Toplevel()
    frame1=Label(frame)
    alto_frame = 700
    ancho_frame = 700
    frame.geometry(f"{alto_frame}x{ancho_frame}")

    self=[] 
    for x in range(ancho):
        self.append([])
        for y in range(alto):
            Grid.rowconfigure(frame,y,weight=1) 
            Grid.columnconfigure(frame,x,weight=1) 
            self[x].append(Button(frame, command=lambda x1=x, y1=y: color_change(x1, y1), relief="groove"))
            self[x][y].grid(column=x, row=y, sticky="NSEW")

    def color_change(x, y):
        self[x][y].config(bg="black")
