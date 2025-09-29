from .persona import Persona

class Hijo(Persona):
    def __init__ (self, nombre, apellido_nac, sexo, papa=None):
        super().__init__(nombre,apellido_nac,sexo)
        self.papa = papa

        if papa != None:
            self.apellido = self.papa.apellido

        else:
            self.apellido = apellido_nac
    
    def __str__(self):
        return f"Hola, yo soy {self.nombre} {self.apellido} y soy hijo de {self.papa.nombre} {self.papa.apellido}."
        