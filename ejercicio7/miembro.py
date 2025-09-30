class Miembro:
    def __init__ (self, nombre, apellido, rol, proyecto):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.proyecto = proyecto
    
    def __str__ (self):
        return f"El miembro {self.nombre} {self.apellido} tiene el rol de {self.rol} en el proyecto {self.proyecto.nombre_proy} que tiene lugar en {self.proyecto.lugar.nombre}"