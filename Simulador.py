from VentanaPrincipal import*

def Simulator(ancho, alto):
    frame=Tk()
    frame1=Label(frame)
    frame1.grid(row=0,column=5)

    self=[] 
    for x in range(ancho):
        self.append([])
        for y in range(alto):
            self[x].append(Button(frame,command=lambda x1=x, y1=y: color_change(x1, y1), height=1, width=3))
            self[x][y].grid(column=x, row=y)

    def color_change(x, y):
        self[x][y].config(bg="black")
