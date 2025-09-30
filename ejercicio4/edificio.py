from .lugar import Lugar
from .etapa_construccion import Etapa_Construccion

class Edificio (Lugar, Etapa_Construccion):
    def __init__ (self, nombre, culto, primera_consagracion, segunda_consagracion, fecha_declaracion_BIC, material, estilo, ciudad, comunidad, pais, primera_construccion, segunda_construccion):
        super().__init__(ciudad, comunidad, pais)
        