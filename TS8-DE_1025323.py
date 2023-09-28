#Trabajo supervisado, sección 17
#28/09/2023
#Daniel Maldonado 1025323
#Uso ciclos FOR y WHILE
#Entrada: 
#Procesos 
#Salida: Secuencia entre un rango

for i in range(1, 26):
    print(i, end=", ")
print()

i=1
while i <= 25:
    print(i, end=", ")
    i += 1
print()

for i in range(5, 51, 5):
    print(i, end=", ")
print()

i=5
while i <= 50:
    print(i, end=", ")
    i += 5
print()

for i in range(20, -2, -2):
    print(i, end=", ")
print()

i=20
while i >= 0:
    print(i, end=", ")
    i -= 2
print()