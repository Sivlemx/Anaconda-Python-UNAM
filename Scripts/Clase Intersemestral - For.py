### "for" loop
estatura = [1.60, 1.65, 1.50, 1.75]
print(estatura[0])
print(estatura[1])
print(estatura[2])
print(estatura[3])

for elemento in estatura:
    print(elemento)
    
for indice, elemento in enumerate(estatura):
    print('Índice ' + str(indice) + ': ' + str(elemento))

for letra in 'Javier Villanueva':
    print(letra.capitalize())
