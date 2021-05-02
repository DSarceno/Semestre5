from math import sqrt, ceil, floor
import matplotlib.pyplot as plt
import numpy as np




file = open('datos.csv','r')
data = [line.split() for line in file]

datos = [float(data[i][0]) for i in range(len(data))]

def mean(data):
    sum = 0
    for dat in data:
        sum += dat
    return sum/len(data)

print(mean(datos))
m = mean(datos)

def desvest(data):
    m = mean(data)
    sqsum = 0
    for dat in data:
        sqsum += (dat - m)**2
    desv = sqrt(sqsum/(len(data) - 1))
    return desv


print(desvest(datos))
desv = desvest(datos)

print(min(datos),max(datos))

num = (max(datos) - min(datos))*10
a = min(datos)
b = max(datos)
h = round((b - a)/num,1)
print(h)
frecuencias = []
for i in range(int(num) + 1):
    delta = round(a + h*i,1)
    cuantity = datos.count(delta)
    frecuencias.append((delta,cuantity))

print(frecuencias)
suma = 0
for tuple in frecuencias:
    suma += tuple[1]

print(suma)



suma_1 = 0
suma_2 = 0
suma_3 = 0
suma_4 = 0
suma_5 = 0
suma_6 = 0
for frec in frecuencias:
    if frec[0] <= m - 2*desv:
        suma_1 += frec[1]
    elif m -2*desv < frec[0] <= m - desv:
        suma_2 += frec[1]
    elif m - desv < frec[0] <= m:
        suma_3 += frec[1]
    elif m < frec[0] <= m + desv:
        suma_4 += frec[1]
    elif m + desv < frec[0] <= m + 2*desv:
        suma_5 += frec[1]
    else:
        suma_6 += frec[1]

print(suma_1, suma_2, suma_3, suma_4, suma_5, suma_6)


sumas = [suma_1, suma_2, suma_3, suma_4, suma_5, suma_6]


frec, extremos = np.histogram(datos, bins = (0,2.288,2.902,3.516,4.13,4.744,6))


print(frec, extremos)


plt.hist(datos, bins = (0,2.288,2.902,3.516,4.13,4.744,6))
plt.xticks((0,2.288,2.902,3.516,4.13,4.744,6))
plt.savefig('histo.pdf')
plt.show()









# END
