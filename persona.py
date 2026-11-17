# SistemaRural-PE - Clase Persona
# Prototipo academico: usar solamente datos ficticios.

class Persona:
    # Constructor
    def __init__(self, idpersona, nombre, apellido, dni, telefono, correo, direccion):
        self.idpersona = idpersona
        self.establecerNombre(nombre)
        self.establecerApellido(apellido)
        if len(dni) != 8 or not dni.isdigit():
            raise ValueError("El DNI debe tener 8 digitos.")
        self.__dni = dni
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Getters y setters
    def obtenerNombre(self):
        return self.__nombre

    def establecerNombre(self, nombre):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")
        self.__nombre = nombre

    def obtenerApellido(self):
        return self.__apellido

    def establecerApellido(self, apellido):
        if apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacio.")
        self.__apellido = apellido

    def obtenerNombreCompleto(self):
        return self.obtenerNombre() + " " + self.obtenerApellido()

    def actualizarDatos(self, telefono, correo, direccion):
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def mostrar_informe(self):
        print("ID:", self.idpersona)
        print("Nombre completo:", self.obtenerNombreCompleto())
        print("DNI:", "******" + self.__dni[-2:])
        print("Telefono:", self.telefono)
        print("Correo:", self.correo)
        print("Direccion:", self.direccion)


# Menu de prueba (fuera de la clase)
def main():
    persona = None
    print("Ingrese solamente datos ficticios.")

    while True:
        print("\n===== SISTEMARURAL-PE =====")
        print("1. Registrar persona")
        print("2. Mostrar datos")
        print("3. Actualizar datos de contacto")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                idpersona = int(input("ID: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = input("DNI ficticio: ")
                telefono = input("Telefono: ")
                correo = input("Correo: ")
                direccion = input("Direccion: ")
                persona = Persona(idpersona, nombre, apellido, dni,
                                  telefono, correo, direccion)
                print("Persona registrada correctamente.")
            except ValueError as error:
                print("Error:", error)

        elif opcion == "2":
            if persona is None:
                print("Primero debe registrar una persona.")
            else:
                persona.mostrar_informe()

        elif opcion == "3":
            if persona is None:
                print("Primero debe registrar una persona.")
            else:
                telefono = input("Nuevo telefono: ")
                correo = input("Nuevo correo: ")
                direccion = input("Nueva direccion: ")
                persona.actualizarDatos(telefono, correo, direccion)
                print("Datos actualizados correctamente.")

        elif opcion == "4":
            print("Fin del programa.")
            break
        else:
            print("Opcion incorrecta.")


# Permite importar Persona desde otro archivo sin ejecutar el menu.
if __name__ == "__main__":
    main()
