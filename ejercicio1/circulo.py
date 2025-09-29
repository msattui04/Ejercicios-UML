from .figura import Figura
import math

class Circulo(Figura):

    def __init__ (self, color, diametro):
        super().__init__("Circulo")
        self.color = color
        self.diametro = diametro

    def area(self):
        return math.pi * (self.diametro / 2) ** 2
    
    def perimetro(self):
        return math.pi * self.diametro