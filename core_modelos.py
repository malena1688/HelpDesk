
class EstadoInvalidoError(Exception):
    """Excepción para estados no permitidos."""
    pass


class TicketTecnico:
    def __init__(self, id, titulo, prioridad):
        self._id = id
        self._titulo = titulo
        self._estado = "Abierto"
        self._prioridad = prioridad

    def cambiar_estado(self, nuevo_estado):
        transiciones = {
            "Abierto": ["En Proceso"],
            "En Proceso": ["Abierto", "Cerrado"],
            "Cerrado": []
        }

        if nuevo_estado not in transiciones:
            raise EstadoInvalidoError("Estado no válido")

        if nuevo_estado not in transiciones[self._estado]:
            raise EstadoInvalidoError(
                f"No se puede pasar de {self._estado} a {nuevo_estado}"
            )

        self._estado = nuevo_estado

    def calcular_sla(self):
        return 48


class TicketHardware(TicketTecnico):
    def __init__(self, id, titulo, prioridad, componente):
        super().__init__(id, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        sla = {
            "Alta": 4,
            "Media": 24,
            "Baja": 48
        }
        return sla.get(self._prioridad, 48)


class TicketSoftware(TicketTecnico):
    def __init__(self, id, titulo, prioridad, sistema_operativo):
        super().__init__(id, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        sla = {
            "Alta": 2,
            "Media": 12,
            "Baja": 36
        }
        return sla.get(self._prioridad, 36)


if __name__ == "__main__":

    ticket1 = TicketHardware(
        1, "Ordenador no enciende", "Alta", "Placa base"
    )

    ticket2 = TicketSoftware(
        2, "Error al abrir programa", "Media", "Windows 11"
    )

    print("Ticket Hardware:", ticket1._titulo)
    print("SLA Hardware:", ticket1.calcular_sla(), "horas")

    print("Ticket Software:", ticket2._titulo)
    print("SLA Software:", ticket2.calcular_sla(), "horas")

    try:
        ticket1.cambiar_estado("En Proceso")
        print("Estado:", ticket1._estado)

        ticket1.cambiar_estado("Cerrado")
        print("Estado:", ticket1._estado)

        ticket1.cambiar_estado("En Proceso")

    except EstadoInvalidoError as error:
        print("Error:", error)
