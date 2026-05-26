import tkinter as tk
from tkinter import messagebox



hambre = 50
felicidad = 50
energia = 50
higiene = 50
edad = 0

viva = True



def alimentar():
    global hambre

    if viva:
        hambre -= 15

        if hambre < 0:
            hambre = 0

        actualizar()


def jugar():
    global felicidad
    global energia

    if viva:
        felicidad += 15
        energia -= 10

        if felicidad > 100:
            felicidad = 100

        if energia < 0:
            energia = 0

        actualizar()


def dormir():
    global energia

    if viva:
        energia += 20

        if energia > 100:
            energia = 100

        actualizar()


def banar():
    global higiene

    if viva:
        higiene += 20

        if higiene > 100:
            higiene = 100

        actualizar()


def actualizar():

    texto.config(
        text=
        f"🍔 Hambre: {hambre}\n"
        f"😄 Felicidad: {felicidad}\n"
        f"⚡ Energía: {energia}\n"
        f"🛁 Higiene: {higiene}\n"
        f"🎂 Edad: {edad}"
    )

    
    if not viva:
        estado.config(text="☠️ La mascota murió")
        return

    if hambre >= 80:
        estado.config(text="😢 Tengo mucha hambre")

    elif felicidad <= 20:
        estado.config(text="😭 Estoy triste")

    elif energia <= 20:
        estado.config(text="😴 Tengo sueño")

    elif higiene <= 20:
        estado.config(text="🤢 Estoy sucio")

    elif felicidad >= 80:
        estado.config(text="😄 Estoy muy feliz")

    else:
        estado.config(text="🙂 Estoy normal")

def tiempo():

    global hambre
    global felicidad
    global energia
    global higiene
    global edad
    global viva

    if viva:

        
        hambre += 2
        felicidad -= 1
        energia -= 1
        higiene -= 1

        edad += 1

        
        if hambre > 100:
            hambre = 100

        if felicidad < 0:
            felicidad = 0

        if energia < 0:
            energia = 0

        if higiene < 0:
            higiene = 0

        
        if hambre >= 100:
            viva = False

            messagebox.showinfo(
                "Mascota",
                "☠️ Tu mascota murió de hambre"
            )

        actualizar()

    ventana.after(2000, tiempo)



def reiniciar():

    global hambre
    global felicidad
    global energia
    global higiene
    global edad
    global viva

    hambre = 50
    felicidad = 50
    energia = 50
    higiene = 50
    edad = 0

    viva = True

    actualizar()



ventana = tk.Tk()

ventana.title("🐾 Mascota Virtual")
ventana.geometry("350x400")

titulo = tk.Label(
    ventana,
    text="🐶 Mascota Virtual",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

texto = tk.Label(
    ventana,
    text="",
    font=("Arial", 14),
    justify="left"
)
texto.pack(pady=10)

estado = tk.Label(
    ventana,
    text="",
    font=("Arial", 12)
)
estado.pack(pady=10)


btn1 = tk.Button(
    ventana,
    text="🍔 Alimentar",
    width=20,
    command=alimentar
)
btn1.pack(pady=5)

btn2 = tk.Button(
    ventana,
    text="🎮 Jugar",
    width=20,
    command=jugar
)
btn2.pack(pady=5)

btn3 = tk.Button(
    ventana,
    text="😴 Dormir",
    width=20,
    command=dormir
)
btn3.pack(pady=5)

btn4 = tk.Button(
    ventana,
    text="🛁 Bañar",
    width=20,
    command=banar
)
btn4.pack(pady=5)

btn5 = tk.Button(
    ventana,
    text="🔄 Reiniciar",
    width=20,
    command=reiniciar
)
btn5.pack(pady=5)


actualizar()
tiempo()

ventana.mainloop()