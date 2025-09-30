from ejercicio1.circulo import Circulo
from ejercicio1.rectangulo import Rectangulo
from ejercicio1.cuadrado import Cuadrado
from ejercicio1.elipse import Elipse

from ejercicio2.persona import Persona
from ejercicio2.casada import Casada
from ejercicio2.hijo import Hijo

from ejercicio3.lugar import Lugar
from ejercicio3.Cuadro import Cuadro

if __name__ == "__main__":

    print("=====Ejercicio 1=====")

    circulo1 = Circulo("Negro", 1)

    print(circulo1)
    print(f"Área: {circulo1.area()}")
    print(f"Perímetro: {circulo1.perimetro()}")
    print("")

    rectangulo1 = Rectangulo("Naranja", 3, 1)

    print(rectangulo1)
    print(f"Área: {rectangulo1.area()}")
    print(f"Perímetro: {rectangulo1.perimetro()}")
    print("")

    cudrado1 = Cuadrado("Azul", 1.5)

    print(cudrado1)
    print(f"Área: {cudrado1.area()}")
    print(f"Perímetro: {cudrado1.perimetro()}")
    print("")

    elipse1 = Elipse("Rojo", 3, 1)

    print(elipse1)
    print(f"Área: {elipse1.area()}")
    print(f"Perímetro: {elipse1.perimetro()}")
    print("")

    print("=====Ejercicio 2=====")
    Carlos = Persona("Carlos", "Windsor", "Hombre")
    Diana = Casada("Diana", "Spencer", "Mujer", Carlos)
    Guillermo = Hijo("Guillermo", "Windsor", "Hombre", Carlos)
    Kate = Casada("Kate", "Middleton", "Mujer", Guillermo)

    print(Carlos)
    print(Diana)
    print(Guillermo)
    print(Kate)
    print("")

    print("=====Ejercicio 3=====")

    L1 = Lugar("Museo del Prado", "Madrid", "España")
    L2 = Lugar("Museo de Louvre", "París", "Francia")

    replica_gioconda = Cuadro(L1.institucion, L1.ciudad, L1.pais, "Gioconda de El Prado", "1503-1516", "Óleo", "Pincelada Simple", "Madera de Nogal", "Desconocido", "Bueno")
    gioconda = Cuadro(L2.institucion, L2.ciudad, L2.pais, "La Gioconda", "1503-1516", "Óleo", "Sfumato", "Madera de Álamo", "Leonardo da Vinci", "Regular")

    print(replica_gioconda)
    print("")
    print(gioconda)
    print("")