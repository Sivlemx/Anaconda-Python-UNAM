import matplotlib.pyplot as plt

año = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050]
pop = [2.519, 3.692, 5.263, 6.972, 7.298, 7.678, 8.422, 9.168, 10.521, 11.741, 12.037]

### Linea Plot
plt.plot(año, pop)
plt.show()

### Plot Scatter Plot
plt.scatter(año, pop)
plt.show()

### Plot Histogram
help(plt.hist)

estatura = [1.60, 1.65, 1.50, 1.75]
plt.hist(estatura, bins=3)
plt.show()

### Customizar las gráficas
### Linea Plot
plt.plot(año, pop)
plt.show()

## Etiquetas a los ejes
plt.plot(año, pop)
plt.xlabel('Año')
plt.ylabel('Población')
plt.show()

## Título de la gráfica
plt.plot(año, pop)
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Aumento de la Población Mundial')
plt.show()

## Hacer especifico las etiquetas del eje y
plt.plot(año, pop)
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Aumento de la Población Mundial')
plt.yticks([4, 6, 8, 10, 12],
           ['4B', '6B', '8B', '10B', '12B'])
plt.savefig('gráfica1.png')
plt.show()

## Agregar más datos
año = [1900, 1910, 1920, 1930] + año
pop = [0.489, 0.890, 1.365, 1.831] + pop

plt.plot(año, pop)
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Aumento de la Población Mundial')
plt.yticks([4, 6, 8, 10, 12],
           ['4B', '6B', '8B', '10B', '12B'])
plt.savefig('gráfica2.png')
plt.show()

















