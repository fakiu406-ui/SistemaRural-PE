import tkinter as tk 
from tkinter import messagebox

#ventana.resizable(False,False) #Para que no modificquen el tamaño de la ventana

usuario = "Personal01" 
contrasena = "S4lud"

def iniciar_sesion():
    usuario = txt_usuario.get()
    contrasena = txt_contrasena.get()

    if usuario == usuario and contrasena == contrasena:
        messagebox.showinfo("Acceso permitido", "¡Bienvenido al SistemaRural-PE!")
        ventana.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

def abrir_menu():
    menu = tk.Tk()
    menu.title("SistemaRural-PE")
    menu.geometry("600x400")

    tk.Label(menu, text="SISTEMARURAL-PE",
             font=("Arial", 20, "bold")).pack(pady=30)

    tk.Label(menu, text="Bienvenido al sistema de gestión de salud").pack()

    tk.Button(menu, text="Cerrar sesión",
              command=menu.destroy).pack(pady=30)

    menu.mainloop()


# Ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de sesión - SistemaRural-PE")
ventana.geometry("400x300")
ventana.config(bg="#E8F0F8")

tk.Label(ventana, text="SISTEMARURAL-PE",
         font=("Arial", 18, "bold"),
         bg="#E8F0F8").pack(pady=20)

tk.Label(ventana, text="Usuario",
         bg="#E8F0F8").pack()

txt_usuario = tk.Entry(ventana, width=25)
txt_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña",
         bg="#E8F0F8").pack()

txt_contrasena = tk.Entry(ventana, width=25, show="*")
txt_contrasena.pack(pady=5)

tk.Button(ventana, text="Iniciar sesión",
          width=20, command=iniciar_sesion).pack(pady=20)

ventana.mainloop()

