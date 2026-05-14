from observer import Observavel
from states import State, EstadoPendente, EstadoConfirmada, EstadoCancelada


class Reserva(Observavel):
    def __init__(self, sala, usuario, inicio, fim, state: None):
        super().__init__()
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.tipo_usuario = usuario.tipo_usuario
        self.setReservaState(state or EstadoPendente())

    def setReservaState(self, novo_estado):
        self.state = novo_estado
        self.state.reserva = self
    @property
    def get_status(self):
        return self.state.__class__.__name__.replace("Estado", "").lower()
    
    def cancelar(self):
        self.state.cancelar()
        self.notificar("cancelamento", {"reserva": self, "status": self.get_status})
        
    def confirmar(self):
        self.state.confirmar()
        self.notificar("confirmacao", {"reserva": self, "status": self.get_status})

    def modificar(self, novo_inicio, novo_fim):
        self.inicio = novo_inicio
        self.fim = novo_fim
        self.notificar("modificacao", {"inicio": novo_inicio, "fim": novo_fim, "reserva": self})
    
    def descricao(self):
        return f"Reserva | Sala {self.sala.id} | {self.usuario.nome} | Status: {self.get_status}"

