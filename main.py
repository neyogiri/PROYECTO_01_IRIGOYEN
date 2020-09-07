from lifestore_file import *
import usuario
import passw
from heapq import nlargest
from heapq import nsmallest
from collections import Counter
from collections import OrderedDict
import operator

#Generamos un login seguro para el usuario
nombre= input("Ingrese su nombre \n")
contra= input("Ingrese su contraseña \n")
if passw.clave(contra)==True:
  print("Bienvenido\n"+ nombre)



#Creamos un menú con opciones
#CHECAR PORQUE NOD EJA INGRESAR AL MENU
while True:
  print (
  """
    1. Ver los 50 productos más vendidos
    2. Ver los 50 productos menos vendidos
    3. Ver los 100 productos más buscados
    4. Ver los 100 productos menos buscados
    5. Salir
   """
  )
  opcion = input("Digite una opción\n")
    
  if opcion == "1":
    #print("Ver los 50 productos mas vendidos")
    print("USTED ELIGIO VER=\nLOS 50 MAS VENDIDOS\n")
    productos=[]
    cantidad=[]
    
    #Accedemos a la lista lifestore_sales con un bucle for para iterar sobre el id?producto que en este caso se encuentra ubicado en la posicion 1 mientras recibimos los elementos en una nueva lista llamada productos
    for i in lifestore_sales:
        productos.append(i[1])

   #SE UTILIZA LA FUNCI[ON COUNTER PARA ACCEDER A LA CANTIDAD DE VECES QUE SE REPITEN LOS ELEMENTOS EN LA LISTA PRODUCTOS. 
    cantidad=Counter(productos)
   #SE CONCATENA EL MENSAJE QUE EXPLICA LA POSICION DE LOS VALORES LANZADOS
    print("Los 50 productos mas vendidos son=\n {clave=id_product:valor=Cantidad de Ventas}")
    print(cantidad)

  elif opcion == "2":
    #print("Ver los 50 productos MENOS vendidos")
    print("USTED ELIGIO VER=\nLOS 50 MENOS VENDIDOS\n")
    productos=[]
    cantidad=[]
    small=[]
    #Accedemos a la lista lifestore_sales con un bucle for para iterar sobre el id?producto que en este caso se encuentra ubicado en la posicion 1 mientras recibimos los elementos en una nueva lista llamada productos
    for i in lifestore_sales:
        productos.append(i[1])

   #SE UTILIZA LA FUNCION COUNTER PARA ACCEDER A LA CANTIDAD DE VECES QUE SE REPITEN LOS ELEMENTOS EN LA LISTA PRODUCTOS. 
    
    cantidad=Counter(productos)
   #SE ORDENA EL DICCIONARIO POR EL VALOR
    small = dict(sorted(cantidad.items(), key=operator.itemgetter(1)))
    print("Los 50 productos MENOS vendidos son=\n {clave=id_product:valor=Cantidad de Ventas}\n ")
    print(small)
    
  
  elif opcion == "3":
    print("USTED ELIGIO VER=\nLOS 100 PRODUCTOS MAS BUSCADOS\n")

    productos=[]
    cantidad=[]

    for i in lifestore_searches:
        productos.append(i[1])
    #print("productos",productos)

   #SE UTILIZA LA FUNCI[ON COUNTER PARA ACCEDER A LA CANTIDAD DE VECES QUE SE REPITEN LOS ELEMENTOS EN LA LISTA PRODUCTOS. SE CONCATENA EL MENSAJE QUE EXPLICA LA POSICION DE LOS VALORES LANZADOS
    
    cantidad=Counter(productos)
    print("Los 100 productos MAS BUSCADOS son=\n {clave=id_product:valor=Cantidad de Ventas}")
    print(cantidad)

  elif opcion == "4":
    print("USTED ELIGIO VER=\nLOS 100 PRODUCTOS MENOS BUSCADOS\n")

    productos=[]
    cantidad=[]
    small=[]
    
    for i in lifestore_searches:
        productos.append(i[1])

   #SE UTILIZA LA FUNCI[ON COUNTER PARA ACCEDER A LA CANTIDAD DE VECES QUE SE REPITEN LOS ELEMENTOS EN LA LISTA PRODUCTOS. SE CONCATENA EL MENSAJE QUE EXPLICA LA POSICION DE LOS VALORES LANZADOS
    cantidad=Counter(productos)
    #print(cantidad)
    #SE ORDENA EL DICCIONARIO POR EL VALOR
    small = dict(sorted(cantidad.items(), key=operator.itemgetter(1)))
    #print("Los 100 productos MENOS BUSCADOS son=\n {clave=id_product:valor=Cantidad de Ventas}")
    print(small)
  

  elif opcion == "5":
    salir = True
    print ("Que la fuerza te acompane")
  else:
    print ("Introduce un numero entre 1 y 3")
