from .lugar import Lugar

class Cuadro(Lugar):
    def __init__ (self, institucion, ciudad, pais, titulo, AC, tecnica, subtecnica, soporte, autor, estado):
        super().__innit__(institucion, ciudad, pais)
        self.titulo = titulo
        self.AC = AC
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado = estado
    
    def __str__ (self):
        return f"El cuadro '{self.titulo}' de {self.autor}, realizado en los años {self.AC} con la técnica {self.tecnica} ({self.subtecnica}) sobre {self.soporte}, se encuentra en {self.institucion}, {self.ciudad}, {self.pais}. Estado: {self.estado}."