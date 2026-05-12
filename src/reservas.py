from observer import Observavel
from states import State, ReservaPendente, ReservaConfirmada, ReservaCancelada

class Reserva(Observavel):
    def __init__(self, sala, usuario, inicio, fim, state: State):
        super().__init__()
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.tipo_usuario = usuario.tipo_usuario  

    def setReservaState(self, novo_estado):
        self.state = novo_estado
        self.state.reserva = self

    def present_state(self):
        return self.state.__class__.__name__
    
    def estado(self):
        print(f"Estado atual da reserva: {self.state.__class__.__name__}")
    
    def cancelar(self):
        self.state.cancelar()
        self.notificar("cancelamento", {"reserva": self})
        
    def confirmar(self):
        self.state.confirmar()
        self.notificar("confirmacao", {"reserva": self})

    def modificar(self, novo_inicio, novo_fim):
        self.inicio = novo_inicio
        self.fim = novo_fim
        self.notificar("modificacao", {"inicio": novo_inicio, "fim": novo_fim, "reserva": self})
    
    def descricao(self):
        return f"Reserva | Sala {self.sala.id} | {self.usuario.nome}"

