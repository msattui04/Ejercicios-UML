class Arquelogica:

    

    def __init__ (self, fecha_inicio, fecha_fin, tipo):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

        tipos_validos = ["sondeo", "excavación", "seguimiento"]

        if self.tipo.lower() not in tipos_validos:
            raise ValueError ("Tipo de excavación no está en las opciones")
        else:
            pass

    def __str__ (self):
        return f"Actuación arqueológica de tipo {self.tipo}, realizada desde {self.fecha_inicio} hasta {self.fecha_fin}"