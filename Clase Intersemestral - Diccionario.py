### Lista

pop = [30.55, 2.77, 39.21]

paises = ["afganistan", "albania", "algeria"]

ind_alb = paises.index("albania")

pop[ind_alb]

### Diccionario
mundo = { "Afganistan":30.55, "Albania":2.77, "Algeria":39.21 }

mundo['Albania']

## Agregar más cosas
mundo['CDMX'] = 120 

mundo

'CDMX' in mundo

del(mundo['CDMX'])

mundo

## Bucle For
for key, value in mundo:
    print(key + ' -- ' + str(value))
    
for key, value in mundo.items():
    print(key + ' -- ' + str(value))

for k, v in mundo.items():
    print(k + ' -- ' + str(v))