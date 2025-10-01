from enum import Enum

class Tecnica(Enum):
    ACUARELA = "acuarela"
    OLEO = "óleo"
    PASTEL = "pastel"
    FRESCO = "fresco"

class SubTecnica(Enum):
    SFUMATO = "sfumato"
    PINCELADA_SIMPLE = "pincelada simple"
    COLLAGE = "collage"
    VELADURA = "veladura"

class Material(Enum):
    MADERA = "madera"
    ALAMO = "álamo"
    NOGAL = "nogal"
    LIENZO = "lienzo"
    OBRA = "obra"

class EstadoConservacion(Enum):
    EXCELENTE = "excelente"
    BUENO = "bueno"
    REGULAR = "regular"
    MALO = "malo"
    RESTAURADO = "restaurado"

class Cuadro2:
    def __init__(self, titulo, cronologia, tecnica, subtecnica, 
                 material_soporte, autor, estado_conservacion):
        self.titulo = titulo
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material_soporte = material_soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
    
    def __str__(self):
        return f"'{self.titulo}' ({self.cronologia}) de {self.autor}, técnica: {self.tecnica.value} ({self.subtecnica.value}), soporte: {self.material_soporte.value}, estado: {self.estado_conservacion.value}."