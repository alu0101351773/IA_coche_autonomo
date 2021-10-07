from VentanaPrincipal import*

# --> Entrada/Salida

tituloES=Label(base, text="ENTRADA/SALIDA")
tituloES.grid(row=8, column=0, pady=10, padx=40)
tituloES.config(bg="#3092CE", fg="white", font=("Bungee Inline", 14, 'bold'))

tituloComo=Label(base, text="¿Cómo?:")
tituloComo.grid(row=9, column=0, padx=20)
tituloComo.config(bg="#3092CE", fg="white", font=("Century Gothic", 12))

ValorOpcionES = tk.IntVar() 

OpcionES1 = tk.Radiobutton(base, text='Aleatorio', variable=ValorOpcionES, value=1) 
OpcionES1.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")
OpcionES2 = tk.Radiobutton(base, text='Manual (Click)', variable=ValorOpcionES, value=2) 
OpcionES2.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")
OpcionES3 = tk.Radiobutton(base, text='Manual (Coordenadas)', variable=ValorOpcionES, value=3)
OpcionES3.config(bg="#3092CE", fg="white", font=("Century Gothic", 12, 'bold'), selectcolor = "#82C4FA", activebackground="#3092CE")

OpcionES1.grid(row=9, column=1, sticky="w")
OpcionES2.grid(row=10, column=1, sticky="w")
OpcionES3.grid(row=11, column=1, sticky="w")