class Figura:
    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("El método área debe ser implementado por las subclases")
    
    def perimetro(self):
        raise NotImplementedError("El método perímetro debe ser implementado por las subclases")
    
    def __str__ (self):
        return f"Figura: {self.nombre}"