class Persona:
    def __init__(self, nombre, apellido_nac, sexo):
        self.nombre = nombre
        self.apellido_nac = apellido_nac
        self.apellido = apellido_nac
        self.sexo = sexo

    def __str__(self):
        return f"Hola, yo soy {self.nombre} {self.apellido}."