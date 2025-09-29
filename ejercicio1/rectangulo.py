from .figura import Figura
import math

class Rectangulo(Figura):
    def __init__(self, color, largo, ancho):
        super().__init__("Rectangulo")
        self.color = color
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho
    
    def perimetro(self):
        return 2*self.largo+2*self.ancho