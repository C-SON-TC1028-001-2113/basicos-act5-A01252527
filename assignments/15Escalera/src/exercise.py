import math
def main():
    #escribe tu código abajo de esta línea
    altura = float(input('Altura de la casa: '))
    angulo = int(input('Angulo en grados: '))
    escalera = altura/(math.sin(math.radians(angulo)))

    print("Largo de la escalera: " +str(round(escalera)))
    



if __name__ == '__main__':
    main()
