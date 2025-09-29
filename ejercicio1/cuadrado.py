from .figura import Figura

class Cuadrado(Figura):
    def __init__(self, color, largo):
        super().__init__("Cuadrado")
        self.color = color
        self.largo = largo
    
    def area(self):
        return self.largo ** 2
    
    def perimetro(self):
        return 4 * self.largo