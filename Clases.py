from functools import reduce
#Creación de clases
class Persona:
    def __init__ (self,nombre, apellido, correo, direccion, telefono, dni, idpersona):
        self.__nombre=nombre
        self.__apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion
        self.idpersona=idpersona

    def obtenerNombre(self):
        return self.__nombre

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def obtenerApellido(self):
        return self.__apellido

    def establecerApellido(self, apellido):
        self.__apellido = apellido

    #metodo

    def actualizarDatos(self, correo, telefono):
        self.correo = correo
        self.telefono = telefono
        print("Datos actualizados correctamente")

    def obtenerNombreCompleto(self):
        return self.__nombre + " " + self.__apellido
    
    def mostrar_informe(self):
        print("Nombre completo:",self.obtenerNombreCompleto())
        print("Dni:", self.dni)
        print("Teléfono:",self.telefono)
        print("Correo:",self.correo)
        print("Dirección:",self.direccion)

#Herencias: hijos

class Paciente(Persona):
    def __init__(self, nombre, apellido, correo, direccion, telefono, dni, idpersona,fechanacimiento):
        super().__init__(nombre, apellido, correo, direccion, telefono, dni, idpersona)
        self.fechanacimiento=fechanacimiento
        self.historial = []

    #metodo

    def registrar(self):
        print("Paciente registrado:",self.obtenerNombreCompleto())

    def consultarhistorial(self):
        return self.historial
    def agregarAtencion(self, atencion):
        self.historial.append(atencion)
        print("Atención agregada al historial")

class PersonalSalud(Persona):
    def __init__(self, nombre, apellido, correo, direccion, telefono, dni, idpersona,cargo):
        super().__init__(nombre, apellido, correo, direccion, telefono, dni, idpersona)
        self.cargo=cargo
        self.agenda = []

    #metodo

    def consultarAgenda(self):
        return self.agenda

    def verificarDisponibilidad(self):
        return len(self.agenda) < 5
    def agregarCita(self, cita):
        if self.verificarDisponibilidad():
            self.agenda.append(cita)
            return True
        return False
    
class Medico(PersonalSalud):
    def __init__(self, nombre, apellido, correo, direccion, telefono, dni, idpersona, colegiatura, especialidad):
        super().__init__(nombre, apellido, correo, direccion, telefono, dni, idpersona, "Medico")

        self.colegiatura=colegiatura
        self.especialidad=especialidad

    #metodo

    def atenderPaciente(self):
        print("Atendiendo al paciente")

    def registrarDiagnostico(self, diagnostico):
        print("Diagnostico registrado:", diagnostico)

class Citamedica:
    def __init__(self, idcita, fecha, hora, motivo, estado, medico, paciente):
        self.idcita=idcita
        self.fecha=fecha
        self.hora=hora
        self.motivo=motivo
        self.estado= estado
        self.medico= medico
        self.paciente= paciente

    def programar(self):
        self.estado = "Programada"
        print("Cita programada")

    def reprogramar(self,fecha,hora):
        self.fecha=fecha
        self.hora=hora
        print("Cita reprogramada")

    def cancelar(self):
        self.estado = "Cancelada"

    def confirmar(self):
        self.estado = "Confirmada"

class Atencionmmedica:
    def __init__(self, Idatencion, Fechaatencion, sintomas, diagnostico, indicaciones, medico, paciente):
        self.Idatencion = Idatencion
        self.Fechaatencion = Fechaatencion
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.indicaciones = indicaciones
        self.medico= medico
        self.paciente= paciente

    def registraratencion (self):
        print("Atención medica registrada")

    def actualizardiagnostico (self, diagnostico):
        self.diagnostico = diagnostico

    def emitirindicaciones(self):
        print("Indicaciones", self.indicaciones)

class Medicamentos:
    def __init__(self, Idmedicamentos, nombre, presentacion, Fechavencimiento, stock):
        self.Idmedicamentos = Idmedicamentos
        self.nombre = nombre
        self.presentacion = presentacion
        self.Fechavencimiento = Fechavencimiento
        self.stock = stock

    def consultarstock (self):
        return self.stock

    def verificarvencimiento(self, fechaactual):
        return fechaactual <= self.Fechavencimiento

class Inventario:
    def __init__(self, idInventario, stockMinimo):
        self.idInventario = idInventario
        self.stockMinimo = stockMinimo
        self.medicamentos = []

    def agregarMedicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def registrarIngreso(self, medicamento, cantidad):
        if cantidad > 0:
            medicamento.stock += cantidad
            print("Ingreso registrado")
        else:
            print("Cantidad inválida")

    def registrarSalida(self, medicamento, cantidad):
        if 0 < cantidad <= medicamento.stock:
            medicamento.stock -= cantidad
            print("Salida registrada")
        else:
            print("Cantidad no disponible")

    def verificarStockMinimo(self):
        return list(filter(
            lambda medicamento: medicamento.stock <= self.stockMinimo,
            self.medicamentos
        ))
class reporte: 
    def __init__(self, Idreporte, fechageneracion, tiporeporte):
        self.Idreporte = Idreporte
        self.fechageneracion = fechageneracion
        self.tiporeporte = tiporeporte

    def generarreportecitas(self,citas):
        print("Total de citas", len(citas))

    def generarreporteatencion(self,atenciones):
        print("Total de atenciones", len(atenciones))

    def generarreportepacientes(self,pacientes):
        print("Total de pacientes", len(pacientes))

class Centrosalud:
    def __init__(self, idCentro, nombre, direccion, distrito):
        self.idCentro = idCentro
        self.nombre = nombre
        self.direccion = direccion
        self.distrito = distrito
        self.pacientes = []
        self.citas = []
        self.atenciones = []

    def registrarAtencion(self, atencion):
        self.atenciones.append(atencion)
        atencion.paciente.agregarAtencion(atencion)
        atencion.registraratencion()

    def registrarPaciente(self, paciente):
        self.pacientes.append(paciente)
        paciente.registrar()

    def gestionarCitas(self, cita):
        if cita.medico.agregarCita(cita):
            self.citas.append(cita)
            cita.programar()
        else:
            print("No hay disponibilidad para el médico")

    def consultarAtenciones(self):
        return self.atenciones

def obtenerNombresPacientes(pacientes):
    nombres = list(map(
        lambda paciente: paciente.obtenerNombreCompleto(),
        pacientes
    ))
    return nombres

def filtrarCitasConfirmadas(citas):
    citasConfirmadas = list(filter(
        lambda cita: cita.estado == "Confirmada",
        citas
    ))
    return citasConfirmadas

def calcularStockTotal(medicamentos):
    total = reduce(
        lambda acumulador, medicamento: acumulador + medicamento.stock,
        medicamentos,
        0
    )
    return total