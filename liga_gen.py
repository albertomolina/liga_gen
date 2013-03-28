# -*- coding: utf-8 -*-
from random import randint

def liga_gen(lista_orig):
    """
    Función que recibe una lista de enteros que representa
    los equipos o jugadores de una liga. Ordena la lista de
    forma aleatoria (sorteo) y devuelve una lista de jornadas,
    cada una de ellas contiene dos listas (local y
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
    partidos = len(lista)/2
    comodin = lista[-1]
    emp = []
    
    for jornada in xrange(num_jornadas):
        emp.append([])
        emp[jornada].append([])
        emp[jornada].append([])

        # Primera jornada
        if jornada == 0:
            for i in xrange(partidos):
                emp[jornada][1].append(lista[-(i+2)])
                if i != partidos - 1:
                    emp[jornada][0].append(lista[i])
                else:
                    emp[jornada][0].append(comodin)
        # Jornada par
        elif (jornada % 2 != 0):
            for i in xrange(partidos):
                emp[jornada][0].append(emp[jornada-1][1][i])
                if i == 0:
                    emp[jornada][1].append(comodin)
                else:
                    emp[jornada][1].append(emp[jornada-1][0][i-1])
        # Jornada impar
        else:
            for i in xrange(partidos):
                if i == 0:
                    emp[jornada][0].append(emp[jornada-2][1][0])
                    emp[jornada][1].append(emp[jornada-2][1][i+1])
                elif i != partidos -1:
                    emp[jornada][0].append(emp[jornada-2][0][i-1])
                    emp[jornada][1].append(emp[jornada-2][1][i+1])
                else:
                    emp[jornada][0].append(comodin)
                    emp[jornada][1].append(emp[jornada-2][0][-2])
                    
    # Devolvemos las dos listas
    return emp
    