import reservas
from abc import ABC, abstractmethod
class State(ABC):
    def __init__(self):
        self.reserva = None
    
    @abstractmethod
    def cancelar(self):
        pass
    @abstractmethod
    def confirmar(self):
        pass
    

class EstadoPendente(State):
    def cancelar(self):
        self.reserva.setReservaState(EstadoCancelada())
    def confirmar(self):
        self.reserva.setReservaState(EstadoConfirmada())

class EstadoConfirmada(State):
    def cancelar(self):
        self.reserva.setReservaState(EstadoCancelada())
    def confirmar(self):
        print("Reserva já confirmada.")

class EstadoCancelada(State):
    def cancelar(self):
        print("Reserva já cancelada.")
    def confirmar(self):
        print("Não é possível confirmar uma reserva cancelada.")

