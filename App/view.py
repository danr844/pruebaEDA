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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x libros por promedio")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5 - Ordenar los libros por rating")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    print('se inició la carga de archivos1')
    controller.loadData(catalog)


def printAuthorData(author):
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBestBooks(books):
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print('No se encontraron libros')

def printResults(ord_books, sample=10):
    size = lt.size(ord_books)
    if(size > sample):
        print("Los primeros ", sample, "libros ordenandos son:")
        i = 0
        while i <= sample:
            book = lt.getElement(ord_books, i)
            print('Titulo: ' + book['title'] + ' ISBN: ' + 
                book['isbn'] + ' Rating: ' + book['average_rating'])
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Libros cargados: ' + str(lt.size(catalog['books'])))
        print('Autores cargados: ' + str(lt.size(catalog['authors'])))
        print('Géneros cargados: ' + str(lt.size(catalog['tags'])))
        print('Asociación de Géneros a Libros cargados: ' +
              str(lt.size(catalog['book_tags'])))

    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        books = controller.getBestBooks(catalog, int(number))
        printBestBooks(books)

    elif int(inputs[0]) == 3:
        authorname = input("Nombre del autor a buscar: ")
        author = controller.getBooksByAuthor(catalog, authorname)
        printAuthorData(author)

    elif int(inputs[0]) == 4:
        label = input("Etiqueta a buscar: ")
        book_count = controller.countBooksByTag(catalog, label)
        print('Se encontraron: ', book_count, ' Libros')

    elif int(inputs[0]) == 5:
        size = input("Indique tamaño de la muestra: ")
        result = controller.sortBooks(catalog, int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printResults(result[1])

    else:
        sys.exit(0)
sys.exit(0)
