from ejercicio1.circulo import Circulo
from ejercicio1.rectangulo import Rectangulo
from ejercicio1.cuadrado import Cuadrado
from ejercicio1.elipse import Elipse

from ejercicio2.persona import Persona
from ejercicio2.casada import Casada
from ejercicio2.hijo import Hijo

from ejercicio3.lugar import Lugar
from ejercicio3.Cuadro import Cuadro

from ejercicio4.lugar import Lugar2
from ejercicio4.etapa_construccion import Etapa_Construccion
from ejercicio4.edificio import Edificio

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

    L13 = Lugar("Museo del Prado", "Madrid", "España")
    L23 = Lugar("Museo de Louvre", "París", "Francia")

    replica_gioconda = Cuadro(L13.institucion, L13.ciudad, L13.pais, "Gioconda de El Prado", "1503-1516", "Óleo", "Pincelada Simple", "Madera de Nogal", "Desconocido", "Bueno")
    gioconda = Cuadro(L23.institucion, L23.ciudad, L23.pais, "La Gioconda", "1503-1516", "Óleo", "Sfumato", "Madera de Álamo", "Leonardo da Vinci", "Regular")

    print(replica_gioconda)
    print("")
    print(gioconda)
    print("")

    print("=====Ejercicio 4=====")

    L14 = Lugar2("Santiago de Compostela","Galicia", "España")
    EC1 = Etapa_Construccion(1075,1122)
    EC2 = Etapa_Construccion(1168,"-")

    catedral_de_santiago = Edificio("Catedral de Santiago de Compostela","Católico", 1128, 3/4/1211, 1896, "Granito", "Románico", L14.ciudad, L14.comunidad, L14.pais, EC1.fecha_inicio, EC1.fecha_fin, EC2.fecha_inicio, EC2.fecha_fin)

    print(catedral_de_santiago)