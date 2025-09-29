class Lugar:
    def __innit__ (self, institucion, ciudad, pais):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais

    def __str__ (self):
        return f"La institución {self.institucion} está en {self.ciudad}, {self.pais}."