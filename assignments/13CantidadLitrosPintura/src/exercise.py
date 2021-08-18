import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input('Area a pintar en metros: '))
    Rendimiento = int(input('Rendimiento (m2/l): '))
    comprar = area/Rendimiento
    print("Litros a comprar: " +str(math.ceil(comprar)))



if __name__ == '__main__':
    main()