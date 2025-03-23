from abc import abstractmethod, ABC
class Pieza(ABC):

    @abstractmethod
    def cambiar_name(self, new_name: int) -> None:
        pass
    