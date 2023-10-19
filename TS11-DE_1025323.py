#Trabajo supervisado de pensamiento computacional, sección 17
#19/10/2023
#Daniel Maldonado 1025323
#Variables tipo cadena
#Entrada: Solicitar al usuario una palabra
#Procesos: Realizar una cadena y una sub-cadena por las primeras letras del texto ingresado por el usuario
#Salida:Sustituir las vocales "o" que encuentre, por la letra "x"

#Solicitar al usuario una palabra
palabra=input("Ingrese una palabra: ")

#Mostrar las primeras tres letras de la palabra una a una
nueva_subcadena = ""
for i in range(3):
    letra = palabra[i]
    print(letra)
    nueva_subcadena += letra

#Mostrar la nueva subcadena
print("Nueva subcadena:", nueva_subcadena)

#Solicitar al usuario un nuevo texto
nuevo_texto=input("Ingrese un nuevo texto: ")

#Sustituir las vocales "O" por la letra "x" en el nuevo texto
nuevo_texto_modificado = ""
for letra in nuevo_texto:
    if letra == "O" or letra == "o":
        nuevo_texto_modificado += "x"
    else:
        nuevo_texto_modificado += letra

#Mostrar el nuevo texto modificado
print("Nuevo texto modificado", nuevo_texto_modificado)

#Investigación
#Funcion 1: len(), sirve para obtener el tamaño de una cadena, es decir, obtiene el numero de caracteres de una cadena (tamaño)
#Funcion 2: count(), sirve para contar el número de veces que una subcadena aparece en una cadena