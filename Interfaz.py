import tkinter as tk 
from tkinter import messagebox

#ventana.resizable(False,False) #Para que no modificquen el tamaño de la ventana

usuario_correcto = "Personal01"
contrasena_correcta = "S4lud"

def iniciar_sesion():
    usuario = txt_usuario.get()
    contrasena = txt_contrasena.get()

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        messagebox.showinfo("Acceso permitido", "¡Bienvenido al SistemaRural-PE!")
        ventana.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

def abrir_menu():
    menu = tk.Tk()
    menu.title("SistemaRural-PE")
    menu.geometry("600x400")

    def registro():
        menu.destroy()
        registrar_paciente()
    tk.Label(menu, text="SISTEMARURAL-PE",
             font=("Arial", 20, "bold")).pack(pady=30)

    tk.Label(menu, text="Bienvenido al sistema de gestión de salud").pack()

    btn_cerrar=tk.Button(menu, text="Cerrar sesión", width=25,
              command=menu.destroy)
    btn_cerrar.pack(pady=7)
    
    btn_registrar=tk.Button(menu, text="Registrar paciente", width=25,
              command=registro)
    btn_registrar.pack(pady=7)



def registrar_paciente():
    ventana_registro = tk.Tk()
    ventana_registro.title("SistemaRural-PE")
    ventana_registro.geometry("650x450")

    tk.Label(ventana_registro, text="Registro de pacientes - SistemaRural-PE",
             font=("Arial", 20, "bold")).pack(pady=30)

    tk.Label(ventana_registro, text="Ingrese los nombres del paciente").pack()
    txt_nombres = tk.Entry(ventana_registro, width=25)
    txt_nombres.pack(pady=5)

    tk.Label(ventana_registro, text="Ingrese los apellidos del paciente").pack()
    txt_apellidos = tk.Entry(ventana_registro, width=25)
    txt_apellidos.pack(pady=5)

    tk.Label(ventana_registro, text="Ingrese el número de DNI del paciente").pack()
    txt_dni = tk.Entry(ventana_registro, width=25)
    txt_dni.pack(pady=5)

    tk.Label(ventana_registro, text="Ingrese el telefono del paciente").pack()
    txt_telefono = tk.Entry(ventana_registro, width=25)
    txt_telefono.pack(pady=5)

    tk.Button(ventana_registro, text="Salir",
              command=ventana_registro.destroy).pack(pady=30)

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