from .lugar import Lugar2
from .etapa_construccion import Etapa_Construccion

class Edificio:
    def __init__ (self, nombre, culto, primera_consagracion, segunda_consagracion, fecha_declaracion_BIC, material, estilo, ciudad, comunidad, pais, fecha_inicio1, fecha_fin1, fecha_inicio2, fecha_fin2):
        self.nombre = nombre
        self.culto = culto
        self.primera_consagracion = primera_consagracion
        self.segunda_consagracion = segunda_consagracion
        self.fecha_declaracion_BIC = fecha_declaracion_BIC
        self.material = material
        self.estilo = estilo
        self.lugar = Lugar2(ciudad,comunidad,pais)
        self.primera_construccion = Etapa_Construccion(fecha_inicio1, fecha_fin1)
        self.segunda_construccion = Etapa_Construccion(fecha_inicio2, fecha_fin2)

    def __str__(self):
        return f"El edificio {self.nombre} de culto {self.culto} fue primeramente construido durante los años {self.primera_construccion.fecha_inicio} - {self.primera_construccion.fecha_fin} en la ciudad de {self.lugar.comunidad}, {self.lugar.pais}"