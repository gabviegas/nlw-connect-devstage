from abc import ABC, abstractmethod
from src.model.entities.eventos import Eventos

# Essa é uma classe abstrata. Ela serve como base para a implementação "verdadeira" da classe, obrigando a presença dos métodos passados.
class EventosRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, event_name: str) -> None: pass # isso é a assinatura de um método

    @abstractmethod
    def select_event(self, event_name: str) -> Eventos: pass # isso é a assinatura de um método