print("""Bienvenidos a su clase de Python.
Hoy es 12 de junio de 2017.
""")

#### Tipos de Variables (en el Shell)
edad = 25
nombre = 'Christian'
numero = 10
estatura = 1.76

type(edad)
type(nombre)
type(numero)
type(estatura)

print(edad)
print(nombre)
print(numero)
print(estatura)

## Entrada de datos  'sentencia "input()"'
nombre = 'Chris'
print('¿Cómo te llamas?')
nombre = input()
print('Yo me llamo', nombre)

## Conversión de datos (en el Shell)
int(1.76)
str(25)
float(10)

# + = suma
# - = resta
# * = multiplicación
# / = división coma flotante
# // = división sin coma flotante
# % = sobrante de una división
# ** = potencia

## Ejercicio con números "int"
print('Teclea un número')
a = input()
print('Teclea otro número')
b = input()
c = int(a) + int(b)
print('La suma es: ', c)

c = int(a) - int(b)
print('La resta es: ',c)

c = int(a) * int(b)
print('La multiplicación es: ', c)
c = int(a) ** int(b)
print('La potencia es: ', c)
c = int(a) / int(b)
print('La división con décimal es: ', c)
c = int(a) // int(b)
print('La división sin décimal es: ', c)
c= int(a) % int(b)
print('El sobrante de la división es: ', c)

## Posición numérica de caracteres
nombre = 'Christian Lopez'
print (nombre [1])

## Colección de tipos de datos
# Las tuplas se identifican encerrándolas en “()” y son inmutables.
# Las listas se identifican encerrándolas en “[]” y pueden ser editadas.

color = ('verde', 'blanco', 'rojo', 'negro')
numeros = [1, 3, 5, 7]
print(color)
print(numeros)
type(color) ## (en el Shell)
type(numeros) ## (en el Shell)

## Pegar listas
enteros = (2, 5, 8)
decimales = [4.12, 6.25, 3.57]
enterosydecimales = [enteros, decimales]
print(enterosydecimales)

#Posición dentro de una lista
print(decimales [2])

## Función "len()" cuenta la cantidad de datos o elementos en una lista o tupla.
print(len(enteros))
print(len(decimales))
print(len(enterosydecimales))

## Ejercicio
nombre = ['Christian', 'Lopez']
print(nombre)
a = len(nombre)
print(a)
completo = ['Christian', 'Lopez']
print(completo)
b = len(completo)
print(b)
c = a + b
print(c)
nombre.insert(0, 'Christian')
print(nombre)
nombre.insert(3, 'Lopez')
print(nombre)
print(len(nombre))
print('Los caracteres que tengo son de: ', c)
print('Tengo %s caracteres en mi nombre completo' % c)

## Función "index" se utiliza para buscar la posición de
## un elemento en una lista o tupla.

nombresapellidos = ('Javier', 'Villanueva', 'Christian', 'López', 'Said', 'Jiménez')
print(nombresapellidos.index('Christian'))
print(nombresapellidos.index('Javier'))
print(nombresapellidos.index('Said'))

## Función "range()" se utiliza para crear una sucesión
## de números enteros que serán inmutables.

print(range(3))
print(list(range(6)))


## Edición de Listas. (Correrlo de 1 x 1)
# Métodos = "append, insert, remove"

# "append()" Se utiliza para agregar un nuevo valor al final de una lista.
nombres = ['Javier', 'Christian', 'Said']
print(nombres)
nombres.append('Francisco')
print(nombres)

# "insert()" Se utiliza para agregar un nuevo valor
# a una lista en una posición indicada.
nombres.insert(2, 'Daniel')
print(nombres)

# "remove()" Se utiliza para eliminar un elemento de la lista.
nombres.remove('Said')
print(nombres)

# editar un elemento de la lista ya sea para reemplazarlo o corregirlo
nombres[0] = 'Said'
print(nombres)

## Operador "+" agregar datos a una lista.
nombres = ['Javier', 'Christian', 'Said']
print(nombres + ['Pedro'])

####################################
#### Operaciones Lógicas
## == "es igual que"
## != "es distinto que"
##  < "es menor que"
## <= "es menor o igual que"
##  > "es mayor que"
## >= "es mayor o igual que"
####################################

print(1 == 1)
print(2 != 3)
print(3 < 2)
print(4 <= 4)
print(5 > 4)
print(6 >= 3)
print(1.80 > 1.78)

## Ejercicio con números "int"
print('Ingrese un número')
a = input()
print('Ingrese otro número')
b = input()
print(a, '==', b, int(a) == int(b))
print(a, '!=', b, int(a) != int(b))
print(a, '<', b, int(a) < int(b))
print(a, '<=', b, int(a) <= int(b))
print(a, '>', b, int(a) > int(b))
print(a, '>=', b, int(a) >= int(b))

## Realiza cadenas de operaciones
a = 1
b = 9
print(5 > a < 3)
print(5 > a > b)

# No compara valores con tipos diferentes.
print('2' == 2)

# Pero si lo convertimos a...
print(int('2') == 2)

## Operador Booleano "is"
# devuelve verdadero si la referencia del objeto que está a su
# izquierda se refiere al mismo objeto que está a su derecha.
a = 1
b = 2
print(1 is a)
print(2 is a)
print(a is 1)
print(a is 2)
print(1 is b)
print(2 is b)
print(b is 1)
print(b is 2)

# verifica contenidos en listas y tuplas.
color = ('verde', 'blanco', 'rojo', 'negro')
numeros = [1, 3, 5, 7]
apellidos = ('Javier', 'Villanueva', 'Christian', 'López', 'Said', 'Jímenez')
a = color
print(a)
print(a is color)
b = numeros
print(b)
print(b is numeros)
print(a is b)
print(a and b is apellidos)

## ¿Y qué pasa cuando son similares los objetos?
a = 1, 2, 3
b = 1, 2, 3
print(a is b)

## La respuesta es... (AYUDENME A ENTENDER ESTE PEDO)
# porque aunque su contenido sea el mismo a y b
# son dos objetos diferentes, por lo tanto hay que
# asignarle los contenidos a una de las dos variables
# para que la operación pueda realizarse correctamente.

## Operador "and" (a y b) ##
############ and #############
######## operandos ########      ## resultados ##
# izquierdo #  # derecho #
# True           True               True
# True           False              False
# False          True               False
# False          False              False

## Operador "or" (a o b) ##
############ or #############
######## operandos ########      ## resultados ##
# izquierdo #  # derecho #
# True           True               True
# True           False              True
# False          True               True
# False          False              False

## Operador "not" (a no b) ##
############ not #############
# operandos # resultados #
# True           False
# False          True

"""
     Operadores booleanos
---------------------------
True and True es True
True and False es False
False and True es False
False and False es False

True or True es True
True or False es True
False or True es True
False or False es False

Not True es False
Not False es True

"""

#### Operadores de Pertenencia
## ayudan a realizar verificaciones de datos dentro de una lista o tupla.

## Operador "in"
# operador booleando que devuelve verdadero si el valor de la izquierda
# está contenido en el valor de la derecha.
nombresapellidos = ('Javier', 'Villanueva', 'Christian', 'López', 'Said', 'Jímenez')
print(nombresapellidos)
print('¿Javier está en la lista?')
print('Javier' in nombresapellidos)
print('¿Gudberto está en la lista?')
print('Gudberto' in nombresapellidos)

## Operador "not in"
# operador booleando que devuelve verdadero
# si el valor de la izquierda no está contenido en el valor de la derecha.
# Es lo contrario de "in".
nombresapellidos = ('Javier', 'Villanueva', 'Christian', 'López', 'Said', 'Jímenez')
print(nombresapellidos)
print('¿Javier está en "nombresapellidos"?')
print('Javier' in nombresapellidos)
print('¿Es verdad que Gudberto no está en "nombresapellidos"?')
print('Gudberto' not in nombresapellidos)

# búsqueda de pertenencia de trozos de palabras en cadenas.
nombre = ('Javier Villanueva')
print(nombre)
print('¿Está "ier" en Javier Villanueva?')
print('ier' in nombre)
print('¿Está "Oh" en Javier Villanueva?')
print('Oh' in nombre)
print('¿Está " " en Javier Villanueva?')
print(' ' in nombre)

## Sentencias Condicionales "if, elif, else, ":".
# Sentencia  # Significado
# if           Si
# elif         De lo contrario si
# else         De lo contrario
# :            Entonces

#Ejercicio 1
def lectura():
    print('¿Qué libros te gusta leer? Escoge entre "Ficción", "Aventura", "Documental" y "Terror".\n')
    libro = input()
    if libro == 'Ficción' or libro == 'ficción' or libro == 'ficcion':
        print('Costo $350.82 pesos. Aplicas para un 15% de descuento.\n')
    elif libro == 'Aventura' or libro == 'aventura':
        print('Costo $186.59 pesos. Aplicas para un 25% de descuento.\n')
    elif libro == 'Documental' or libro == 'documental':
        print('Costo $130.58 pesos. Aplicas para un 35% de descuento.\n')
    elif libro == 'Terror' or libro == 'terror':
        print('Eso $6,478.99 pesos. Aplicas para un 2% de descuento. Son los más cotizados.\n')
    else:
        print('No aplicas para descuento.\n')

lectura()
lectura()
lectura()


#######################################################
#Ejercicio 2
def pago():
    print('Ingrese el costo con todo y centavos de la laptop que tienes en uso')
    compra = float(input())
    print('Mira güero, este pedo está condicionado.\nLa laptop tiene que costar más de $8000 para aplicar descuento.\n\nAplicado el descuento de 75%, más bajo que en Julio Regalado por que somos fien fergas')
    descuento = 0.75
    if compra >= float(8000.00):
        descuento = (compra * descuento)
        total_a_pagar = compra - descuento
        print('Su total a pagar es: ', total_a_pagar)
    else:
        print('No aplica descuento\n\n')
pago()
pago()

######################################################
#Ejercicio 3
def lectura():
    libfic = 350.82
    descfic = 0.15
    libaven = 186.59
    descaven = 0.25
    libdoc = 130.58
    desdoc = 0.35
    libsex = 6478.99
    descsex = 0.12
    print("""¿Qué libros te gusta leer?\n
Escoge entre "Ficción", "Aventura", "Documental" y "Terror".\n
También teclea de otro tema que no sean de los que están escritos arriba.\n
Diviertete, entiendelo, sugiere y aporta.\n
Escribe Ficción, Aventura, documental o Sexoso.""")
    libro = input()
    if libro == 'Ficción' or libro == 'ficción' or libro == 'ficcion':
        print('Costo $350.82 pesos. Aplicas para un 15% de descuento.\n')
        print('¿Quieres el libro de Ficción con descuento?')
        print('Teclea "S" si lo quieres, teclea "N" si no lo quieres')
        ficcion = input()
        if ficcion == 'S' or ficcion == 's':
            compra = libfic * descfic
            total_ficcion = libfic - compra
            print('Tu libro de Ficción te costará: ', total_ficcion)
        else:
            print('Tu libro tiene un costo de: ', libfic)
    elif libro == 'Aventura' or libro == 'aventura':
        print('Costo $186.59 pesos. Aplicas para un 25% de descuento.\n')
        print('¿Quieres el libro de Aventuras con descuento?')
        print('Teclea "S" si lo quieres, teclea "N" si no lo quieres')
        aventura = input()
        if aventura == 'S' or aventura == 's':
            compra = libaven * descaven
            total_aventura = libaven - compra
            print('Tu libro de aventura te costará: ', total_aventura)
        else:
            print('Tu libro de Aventura te costará: ', libaven)
    elif libro == 'Documental' or libro == 'documental':
        print('Costo $130.58 pesos. Aplicas para un 35% de descuento.\n')
        print('¿Quieres el libro Documental con descuento?')
        print('Teclea "S" si lo quieres, teclea "N" si no lo quieres')
        documental = input()
        if documental == 'S' or documental == 's':
            compra = libdoc * desdoc
            total_documental = libdoc - compra
            print('Tu libro te costará: ', total_documental)
        else:
            print('Tu libro Documental te costará: ', libdoc)
    elif libro == 'Sexoso' or libro == 'sexoso':
        print('Kamasutra edición "Jayden James" con todo y vieja $6,478.99 pesos. Aplicas para un 12% de descuento. Son los más cotizados. Ni te quejes.\n')
        print('¿Quieres el Kamasutra con todo y vieja con descuento?')
        print('Teclea "S" si lo quieres, teclea "N" si no lo quieres')
        sexoso = input()
        if sexoso == 'S' or sexoso == 's':
            compra = libsex * descsex
            total_sexoso = libsex - compra
            print('Hasta la vieja te vas a llevar por unos %s pesitos' % total_sexoso)
        else:
            print('Aprovecha el descuento, no seas güey. Sí no lo quieres te saldrá en %s' % libsex)
    else:
         print('No tenemos nada de ese tema y no insista, escoja otro')
   
lectura()
lectura()
lectura()

## NO MOSTRAR LA SOLUCIÓN QUE ESTÁ MÁS ABAJO ##

## Problema: Desarrollar una aplicación que indique si
#            un niño, adolescente o adulto pertenece a uno de los siguientes grupos.

## Grupo ##   ## Edad ##
#    A        De 0 a 5 años
#    B        De 6 a 12 años
#    C        De 13 a 18 años
#    D        De 19 a 24 años



print('Ingresa la edad del niño, adolescente o adulto')
edad = int(input())
if edad >= 0 and edad <= 5:
    print('Pertenece al Grupo A')
elif edad >= 6 and edad <= 12:
    print('Pertenece al Grupo B')
elif edad >= 13 or edad <= 18:    ## De acuerdo a lo que se buscar
    print('Pertenece al Grupo C') ## Esto es un ERROR. ¿Por qué?
elif edad >= 19 and edad <= 24:
    print('Pertenece al Grupo D')
else:
    print('No pertenece a ningún Grupo')


## NO MOSTRAR LA SOLUCIÓN QUE ESTÁ MÁS ABAJO ##

# Nos complicaremos la vida.
## Problema:

# Los Trastornos Mentales en este ejercicio se hicieron un problema.
# Con solo introducir el nombre del trastorno, se busca:

# 1.- Que trastorno está en que institución.
# 2.- Su porcentaje entre hombres y mujeres con relación al total del trastorno.
# 3.- El porcentaje de trastorno por institución donde se atiende.
# 4.- El total de Pacientes entre las 2 instituciones.
# 5.- El porcentanje del trastorno entre las 2 instituciones.

### INPRFM
## Trastorno ##         ## Número de Pacientes ##     ## Proporción ##
#  TLP                            767               78% Mujeres - ¿?% Hombres
#  Esquizofrenia                  54                45% Mujeres - ¿?% Hombres
#  Obsesión-Compulsiva            150               69% Mujeres - ¿?% Hombres
#  Fobia Social                   152               32% Mujeres - ¿?% Hombres 

### Fray Bernardino

# Narcisismo                      843               85% Hombres - ¿?% Mujeres
# Depresión                       157               58% Hombres - ¿?% Mujeres
# Trastornos Disociativos         493               36% Hombres - ¿?% Mujeres
# Bipolaridad                     349               49% Hombres - ¿?% Mujeres

TLP = 767
porcmuTLP = 0.78 
esqui = 54
porcmuesqui = 0.45
TOC = 150
porcmuTOC = 0.69
fobsoc = 152
porcmufobsoc = 0.32
narc = 843
porchonarc = 0.85
depr = 157
porchodepr = 0.58
disoc = 493
porchodisoc = 0.36
bipol = 349
porchobipol = 0.49
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from pylab import *
print('TLP, Esquizofrenia, TOC, Fobia Social,\nNarcisismo, Depresión, Disociación, Bipolar')
print('Escribe el Trastorno y te diré que show')
trastorno = str(input())
if trastorno == 'TLP' or trastorno == 'Trastorno Límite de la Personalidad' or trastorno == 'Trastorno Limite de la Personalidad' or trastorno == 'trastorno limite de la personalidad' or trastorno == 'Trastorno Limítrofe de la Personalidad' or trastorno == 'Límites':
    print('\nSe atienden en el INPRFM.')
    pobmuTLP = (TLP * porcmuTLP) / 1
    pobhoTLP = (TLP - pobmuTLP)
    porchoTLP = (pobhoTLP * porcmuTLP) / pobmuTLP
    print('Hay %s pacientes con TLP en el INPRFM.\nHay %s mujeres y %s hombres con TLP.' % (TLP, pobmuTLP, pobhoTLP))
    print('Las mujeres representan el %s y los hombres representan el %s de la población.' % (porcmuTLP, porchoTLP))
    pobinprfm = TLP + esqui + TOC + fobsoc
    porcTLPinprfm = (TLP * 1) / pobinprfm
    print('El TLP representa el %s de la población en el INPRFM.' % porcTLPinprfm)
    pobinprfmfray = pobinprfm + narc + depr + disoc + bipol
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcTLPinprfmfray = (TLP * 1) / pobinprfmfray
    print('El TLP es el %s de la población entre el INPRFM y el Fray.\n' % porcTLPinprfmfray)    
elif trastorno == 'Esquizofrenia' or trastorno == 'esquizofrenia':
    print('\nSe atienden en el INPRFM.')
    pobmuesqui = (esqui * porcmuesqui) / 1
    pobhoesqui = (esqui - pobmuesqui)
    porchoesqui = (pobhoesqui * porcmuesqui) / pobmuesqui
    print('Hay %s pacientes con Esquizofrenia en el INPRFM.\nHay %s mujeres y %s hombres con Esquizofrenia.' % (esqui, pobmuesqui, pobhoesqui))
    print('Las mujeres representan el %s y los hombres representan el %s de la población.' % (porcmuesqui, porchoesqui))
    pobinprfm = esqui + TLP + TOC + fobsoc
    porcesquiinprfm = (esqui * 1) / pobinprfm
    print('La Esquizofrenia representa el %s de la población en el INPRFM.' % porcesquiinprfm)
    pobinprfmfray = pobinprfm + narc + depr + disoc + bipol
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcesquiinprfmfray = (esqui * 1) / pobinprfmfray
    print('La Esquizofrenia es el %s de la población entre el INPRFM y el Fray.\n' % porcesquiinprfmfray)
elif trastorno == 'TOC' or trastorno == 'Trastorno Obsesivo-Compulsivo' or trastorno == 'Obsesión Compulsiva':
    print('\nSe atienden en el INPRFM.')
    pobmuTOC = (TOC * porcmuTOC) / 1
    pobhoTOC = (TOC - pobmuTOC)
    porchoTOC = (pobhoTOC * porcmuTOC) / pobmuTOC
    print('Hay %s pacientes con Trastorno Obsesivo-Compulsivo en el INPRFM.\nHay %s mujeres y %s hombres con Trastorno Obseivo-Compulsivo.' % (TOC, pobmuTOC, pobhoTOC))
    print('Las mujeres representan el %s y los hombres representan el %s de la población.' % (porcmuTOC, porchoTOC))
    pobinprfm = TOC + TLP + esqui + fobsoc
    porcTOCinprfm = (TOC * 1) / pobinprfm
    print('El Trastorno Obsesivo-Compulsivo representa el %s de la población en el INPRFM.' % porcTOCinprfm)
    pobinprfmfray = pobinprfm + narc + depr + disoc + bipol
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcTOCinprfmfray = (TOC * 1) / pobinprfmfray
    print('El Trastorno Obsesivo-Compulsivo es el %s de la población entre el INPRFM y el Fray.\n' % porcTOCinprfmfray)
elif trastorno == 'Fobia Social' or trastorno == 'fobia social':
    print('\nSe atienden en el INPRFM.')
    pobmufobsoc = (fobsoc * porcmufobsoc) / 1
    pobhofobsoc = (fobsoc - pobmufobsoc)
    porchofobsoc = (pobhofobsoc * porcmufobsoc) / pobmufobsoc
    print('Hay %s pacientes con Fobia Social en el INPRFM.\nHay %s mujeres y %s hombres con Fobia Social.' % (fobsoc, pobmufobsoc, pobhofobsoc))
    print('Las mujeres representan el %s y los hombres representan el %s de la población.' % (porcmufobsoc, porchofobsoc))
    pobinprfm = fobsoc + TLP + esqui + TOC
    porcfobsocinprfm = (fobsoc * 1) / pobinprfm
    print('La Fobia Social representa el %s de la población en el INPRFM.' % porcfobsocinprfm)
    pobinprfmfray = pobinprfm + narc + depr + disoc + bipol
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcfobsocinprfmfray = (fobsoc * 1) / pobinprfmfray
    print('La Fobia Social es el %s de la población entre el INPRFM y el Fray.\n' % porcfobsocinprfmfray)
elif trastorno == 'Narcisismo' or trastorno == 'Narsicismo' or trastorno == 'narcisismo':
    print('\nSe atienden en el Fray Bernardino.')
    pobhonarc = (narc * porchonarc) / 1
    pobmunarc = (narc - pobhonarc)
    porcmunarc = (pobmunarc * porchonarc) / pobhonarc
    print('Hay %s pacientes con Trastorno Narcisista de la Personalidad en el Fray.\nHay %s hombres y %s mujeres con Trastorno Narcisista de la Personalidad.' % (narc, pobhonarc, pobmunarc))
    print('Los hombres representan el %s y las mujeres representan el %s de la población.' % (porchonarc, porcmunarc))
    pobfray = narc + depr + disoc + bipol
    porcnarcfray = (narc * 1) / pobfray
    print('El Trastorno Narcisista de la Personalidad representa el %s de la población en el Fray Bernardino.' % porcnarcfray)
    pobinprfmfray = pobfray + TLP + esqui + TOC + fobsoc
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcnarcinprfmfray = (narc * 1) / pobinprfmfray
    print('El Trastorno Narcisista de la Personalidad es el %s de la población entre el INPRFM y el Fray.\n' % porcnarcinprfmfray)
elif trastorno == 'Depresión' or trastorno == 'depresión':
    print('\nSe atienden en el Fray Bernardino.')
    pobhodepr = (depr * porchodepr) / 1
    pobmudepr = (depr - pobhodepr)
    porcmudepr = (pobmudepr * porchodepr) / pobhodepr
    print('Hay %s pacientes con Trastorno Depresivo en el Fray.\nHay %s hombres y %s mujeres con Trastorno Depresivo.' % (depr, pobhodepr, pobmudepr))
    print('Los hombres representan el %s y las mujeres representan el %s de la población.' % (porchodepr, porcmudepr))
    pobfray = depr + narc + disoc + bipol
    porcdeprfray = (depr * 1) / pobfray
    print('El Trastorno Depresivo representa el %s de la población en el Fray Bernardino.' % porcdeprfray)
    pobinprfmfray = pobfray + TLP + esqui + TOC + fobsoc
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcdeprinprfmfray = (depr * 1) / pobinprfmfray
    print('El Trastorno Depresivo es el %s de la población entre el INPRFM y el Fray.\n' % porcdeprinprfmfray)
elif trastorno == 'Disociación' or trastorno == 'disociativo' or trastorno == 'disociación':
    print('\nSe atienden en el Fray Bernardino.')
    pobhodisoc = (disoc * porchodisoc) / 1
    pobmudisoc = (disoc - pobhodisoc)
    porcmudisoc = (pobmudisoc * porchodisoc) / pobhodisoc
    print('Hay %s pacientes con Trastorno por Disociación en el Fray.\nHay %s hombres y %s mujeres con Trastorno de Disociación.' % (disoc, pobhodisoc, pobmudisoc))
    print('Los hombres representan el %s y las mujeres representan el %s de la población.' % (porchodisoc, porcmudisoc))
    pobfray = depr + narc + disoc + bipol
    porcdisocfray = (disoc * 1) / pobfray
    print('El Trastorno por Disociación representa el %s de la población en el Fray Bernardino.' % porcdisocfray)
    pobinprfmfray = pobfray + TLP + esqui + TOC + fobsoc
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcdisocinprfmfray = (disoc * 1) / pobinprfmfray
    print('El Trastorno por Disociación es el %s de la población entre el INPRFM y el Fray.\n' % porcdisocinprfmfray)
elif trastorno == 'Bipolar' or trastorno == 'bipolar':
    print('\nSe atienden en el Fray Bernardino.')
    pobhobipol = (bipol * porchobipol) / 1
    pobmubipol = (bipol - pobhobipol)
    porcmubipol = (pobmubipol * porchobipol) / pobhobipol
    print('Hay %s pacientes con Trastorno Bipolar en el Fray.\nHay %s hombres y %s mujeres con Trastorno Bipolar.' % (bipol, pobhobipol, pobmubipol))
    print('Los hombres representan el %s y las mujeres representan el %s de la población.' % (porchobipol, porcmubipol))
    pobfray = depr + narc + disoc + bipol
    porcbipolfray = (bipol * 1) / pobfray
    print('El Trastorno Bipolar representa el %s de la población en el Fray Bernardino.' % porcbipolfray)
    pobinprfmfray = pobfray + TLP + esqui + TOC + fobsoc
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcbipolinprfmfray = (bipol * 1) / pobinprfmfray
    print('El Trastorno Bipolar es el %s de la población entre el INPRFM y el Fray.\n' % porcbipolinprfmfray)
else:
    print('No existe ese trastorno')



### De Regalo (POR QUE ME CAEN DE HUEVOS) ###
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from pylab import *
print('Escribe "TLP"')
trastorno = str(input())
if trastorno == 'TLP' or trastorno == 'Trastorno Límite de la Personalidad' or trastorno == 'Trastorno Limite de la Personalidad' or trastorno == 'trastorno limite de la personalidad' or trastorno == 'Trastorno Limítrofe de la Personalidad' or trastorno == 'Límites':
    print('\nSe atienden en el INPRFM.')
    pobmuTLP = (TLP * porcmuTLP) / 1
    pobhoTLP = (TLP - pobmuTLP)
    porchoTLP = (pobhoTLP * porcmuTLP) / pobmuTLP
    print('Hay %s pacientes con TLP en el INPRFM.\nHay %s mujeres y %s hombres con TLP.' % (TLP, pobmuTLP, pobhoTLP))
    print('Las mujeres representan el %s y los hombres representan el %s de la población.' % (porcmuTLP, porchoTLP))
    pobinprfm = TLP + esqui + TOC + fobsoc
    porcTLPinprfm = (TLP * 1) / pobinprfm
    print('El TLP representa el %s de la población en el INPRFM.' % porcTLPinprfm)
    pobinprfmfray = pobinprfm + narc + depr + disoc + bipol
    print('Entre el Fray y el INPRFM hay %s de pacientes con Dx de trastorno mental.' % pobinprfmfray)
    porcTLPinprfmfray = (TLP * 1) / pobinprfmfray
    print('El TLP es el %s de la población entre el INPRFM y el Fray.\n' % porcTLPinprfmfray)
    print('¿Quieres gráficar? "S" o "N"')
    TLPgraf = str(input())
    if TLPgraf == 'S' or TLPgraf == 's':
        grafhoTLP = np.random.normal(pobhoTLP, 1000)
        grafmuTLP = np.random.normal(pobmuTLP, 1000)
        datos = [grafhoTLP, grafmuTLP]
        boxplot(datos)
        show()
    else:
        print('Entonces sin gráfica')
else:
    print('Teclea bien')
    
    
    

