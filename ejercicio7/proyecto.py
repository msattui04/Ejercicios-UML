class Proyecto():
    def __init__(self, nombre_proy, fecha_inicio, fecha_fin, lugar):
        self.nombre_proy = nombre_proy
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.lugar = lugar
    
    def __str__ (self):
        return f"El proyecto {self.nombre_proy} se inició el {self.fecha_inicio} hasta el {self.fecha_fin} en la ciudad {self.lugar.nombre}"