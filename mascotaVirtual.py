import tkinter as tk

hambre = 50
felicidad = 50

def alimentar():
    global hambre
    hambre -= 10
    
    if hambre < 0:
        hambre = 0
        
    actualizar()

def jugar():
    global felicidad
    felicidad += 10
    
    if felicidad > 100:
        felicidad = 100
        
    actualizar()

def actualizar():
    texto.config(
        text=f"Hambre: {hambre}\nFelicidad: {felicidad}"
    )

ventana = tk.Tk()
ventana.title("Mascota Virtual")

texto = tk.Label(ventana, text="")
texto.pack()

btn1 = tk.Button(
    ventana,
    text="Alimentar",
    command=alimentar
)
btn1.pack()

btn2 = tk.Button(
    ventana,
    text="Jugar",
    command=jugar
)
btn2.pack()

actualizar()

ventana.mainloop()