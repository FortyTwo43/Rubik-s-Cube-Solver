from Pieza import Pieza

class Arista(Pieza):
    def __init__(self, color1: str, color2: str):
        self.color1: str = color1
        self.color2:str = color2
        
        self.name: int = 0

    def cambiar_name(self, new_name: int) -> None:
        self.name = new_name
        print(f"Nombre cambiado a {new_name}")