from .figura import Figura

class Elipse(Figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__("Elipse")
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def area(self):
        return 3.1416 * (self.eje_mayor / 2) * (self.eje_menor / 2)
    
    def perimetro(self):
        # Aproximación de Ramanujan para el perímetro de una elipse
        a = self.eje_mayor / 2
        b = self.eje_menor / 2
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return 3.1416 * (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))