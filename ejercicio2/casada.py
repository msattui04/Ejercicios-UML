from .persona import Persona

class Casada(Persona):
    def __init__(self, nombre, apellido_nac, sexo, esposo=None):
        super().__init__(nombre, apellido_nac, sexo)
        self.esposo = esposo

        if self.esposo != None and self.sexo == "Mujer":
            self.apellido = esposo.apellido
        else:
            self.apellido = apellido_nac

    def __str__(self):
        return f"Hola, yo soy {self.nombre} {self.apellido} y estoy casada con {self.esposo.nombre} {self.esposo.apellido}."