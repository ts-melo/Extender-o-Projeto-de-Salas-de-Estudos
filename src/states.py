import reservas
from abc import ABC, abstractmethod
class State:

    def reserva(self) -> reservas:
        return self.reserva
    
    def reserva(self, nova_reserva):
        self.reserva = nova_reserva
    
    @abstractmethod
    def cancelar(self):
        pass
    @abstractmethod
    def confirmar(self):
        pass
    

class EstadoPendente(State):
    def cancelar(self):
        self.reserva.setReserva(EstadoCancelada())
    def confirmar(self):
        self.reserva.setReserva(EstadoConfirmada())

class EstadoConfirmada(State):
    def cancelar(self):
        self.reserva.setReserva(EstadoCancelada())
    def confirmar(self):
        print("Reserva já confirmada.")

class EstadoCancelada(State):
    def cancelar(self):
        print("Reserva já cancelada.")
    def confirmar(self):
        print("Não é possível confirmar uma reserva cancelada.")

