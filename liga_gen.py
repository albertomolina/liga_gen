# -*- coding: utf-8 -*-
from random import randint

def liga_gen(lista_orig):
    """
    Función que recibe una lista de enteros que representa
    los equipos o jugadores de una liga. Ordena la lista de
    forma aleatoria (sorteo) y devuelve dos listas (local y
    visitante) que representan todos los enfrentamientos
    entre los elementos de la lista, alternándolos como local
    y visitante.
    Esta función es válida para cualquier número de elementos
    y en el caso de ser un número impar, añade el elemento
    "-1", que puede interpretarse como un partido de descanso.
    """

    # Sorteamos el orden de los equipos
    lista = []    
    while len(lista_orig) != 0:
        num = randint(0,len(lista_orig)-1)
        lista.append(lista_orig[num])
        lista_orig.remove(lista_orig[num])
    # Si en número de elementos de la lista es impar, se añade
    # el elemento "-1"
    if len(lista) % 2 != 0:
        lista.append(-1)
    num_jornadas = len(lista) - 1
    jornada = 0
    comodin = lista[-1]

    for i in xrange(num_jornadas):
        aux = []
        # Primera jornada
        if i == 0:
            local = []
            visitante = []

            for j in xrange(len(lista) / 2):
                visitante.append([lista[-(j+2)]])
                if j != len(lista) / 2 - 1:
                    local.append([lista[j]])
                else:
                    local.append([comodin])
        # Jornada par
        elif (i % 2 != 0):
            for j in xrange(len(local)):
                aux.append(local[j][i-1])
                local[j].append(visitante[j][i-1])
                if j != 0:
                    visitante[j].append(aux[j-1])
                else:
                    visitante[j].append(comodin)
        # Jornada impar
        else:
            for j in xrange(len(local)):
                aux.append(local[j][i-2])
                if j == 0:
                    local[j].append(visitante[j][i-2])
                    visitante[j].append(visitante[j+1][i-2])
                elif j == (len(local) - 1):
                    local[j].append(comodin)
                    visitante[j].append(visitante[j][i-1])
                else:
                    local[j].append(aux[j-1])
                    visitante[j].append(visitante[j+1][i-2])
    # Devolvemos las dos listas
    return local,visitante