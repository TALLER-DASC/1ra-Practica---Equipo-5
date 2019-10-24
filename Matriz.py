rows = 0
cols = 0
teclado = []

ejeX=0
ejeY=0
almacenX=0
almacenY=0
posantX=0
posantY=0
movimientos=0
ocupado=0

# LEER EL ARCHIVO
fil = open("C:/Users/ELG/PycharmProjects/Practica1-Avanzada/notas.txt", "r")
if fil.mode == 'r':
    # obtener el contenido
    lines = fil.readlines()
    c = 1
    l = 0
    #Recorrer los renglones
    for line in lines:

        #Encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ', row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])

        #Encontrar las letras del teclado
        if c > 1 and c <= (rows + 1):
            letters = list(line)
            letters.pop()
            teclado.append(letters)

        #Encontrar la palabra
        if c == (rows + 2):
            palabra = list(line)
            palabra.append("*")
        c += 1

    for tamPalabra in range(len(palabra)):
        #print("Repetición: ",tamPalabra)
        ocupado=0
        for ejeX in range(rows):
            #print("fila: ", ejeX)
            for ejeY in range(cols):
                #print("columna: ",ejeY)
                if teclado[ejeX][ejeY] == palabra[tamPalabra]:
                    print("Se encontro la letra ",teclado[ejeX][ejeY]," en la posición: ",ejeX,ejeY)

                    if ocupado==0:
                        #movimientos+=1
                        almacenX=ejeX
                        almacenY=ejeY

                        #POSICIONES EN X
                        if almacenX > posantX:
                            movimientos = (movimientos) + (posantX+almacenX)
                            posantX=almacenX
                        if almacenX < posantX:
                            movimientos = (movimientos) + (almacenX-posantX)
                            posantX = almacenX

                        #POSICIONES EN Y
                        if almacenY > posantY:
                            movimientos = (movimientos) + (posantY + almacenY)
                            posantY = almacenY
                        if almacenX < posantX:
                            movimientos = (movimientos) + (almacenY - posantY)
                            posantY = almacenY

                        #PRESIONAR BOTON
                        if almacenX == posantX and almacenY == posantY:
                            movimientos += 1
                        '''if almacenY == posantY:
                            movimientos += 1'''
                        #print("Movimientos actuales: ", movimientos)
                        ocupado+=1

movimientos+=len(palabra)

movimientos+=1
print(teclado)

print(palabra)

print("El número de movimientos es: ",movimientos)