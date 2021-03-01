"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import Iterable
import config as cf
import sys
from DISClib.ADT import list as lt
import csv
from DISClib.Algorithms.Sorting import mergesort as me
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Imprimir lista original")
    print("2- Ordenar según average rating")
    print("3- Ordenar según title")
    print("4- Ordenar según average title")


    print("0- Salir")


def loadBooks():
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    catalog = {'books': None}
    booksfile = cf.data_dir + "/GoodReads/books-small.csv"
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    catalog['books'] = lt.newList()
    for book in input_file:
        lt.addLast(catalog['books'], book)
    return catalog


def sortFunction(sorted_list, cmpfunction):
    me.sort(sorted_list['books'], cmpfunction)
    return sorted_list


def compareratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))


def comparetitle(book1, book2):
    if(book1['title'] != book2['title']):
        return (book1['title'] < book2['title'])
    else:
        return (book1['average_rating']<book2['average_rating'])

def compare_average_title(book1, book2):
    if(float(book1['average_rating']) != float(book2['average_rating'])):
        return (float(book1['average_rating'] < book2['average_rating']))
    else:
        return (book1['title']>book2['title'])

"""
Menu principal
"""
while True:
    printMenu()
    catalogo = loadBooks()
    copy_list= lt.subList(catalogo['books'], 0, len(catalogo['books']))
    sorted_list = copy_list.copy()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        for book in lt.iterator(catalogo['books']):
            print(book['title']+"/"+ book['average_rating'])

    elif int(inputs[0]) == 2:
        sortFunction(catalogo, compareratings)
        for book in lt.iterator(catalogo['books']):
            print(book['title']+"/"+ book['average_rating'])
    elif int(inputs[0]) == 3:
        sortFunction(catalogo,comparetitle)
        for book in lt.iterator(catalogo['books']):
            print(book['title']+"/"+ book['average_rating'])
    elif int(inputs[0]) == 4:
        sortFunction(catalogo,compare_average_title)
        for book in lt.iterator(catalogo['books']):
            print(book['title']+"/"+ book['average_rating'])
    else:
        sys.exit(0)
