#    2021-05-06
#    analisis.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráfico de Incertezas.

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de compilación: requere un archivo con una sola columna con los datos
#    python3 analisis.py <inputfile.ext> <outputfile.ext>

#    Copyright (C) 2021
#    D. R. Sarceño Ramírez
#    dsarceno68@gmail.com
#
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.
# PROGRAM analisis
import numpy as np
from math import sqrt
import sys

name_input = sys.argv[1]
name_output = sys.argv[2]

file = open(name_input,'r')
data = [line.split() for line in file]
file.close()
frec = []
for line in data:
    frec.append(int(line[0]))
print(frec, len(frec))

bins = [i for i in range(0,11)]
frecuencias = [frec.count(i) for i in range(0,11)]
print(frecuencias, bins)

file = open(name_output,'w')
for num in frecuencias:
    file.write(str(num) + '\n')
file.close()


sum_fn = 0
for i in range(len(bins)):
    sum_fn += bins[i]*frecuencias[i]

prom = sum_fn/len(frec)

sum_des = 0
for i in range(len(bins)):
    sum_des += frecuencias[i]*(bins[i] - prom)**2
desvest = sqrt(sum_des/len(frec))
print(prom, desvest)

































# END PROGRAM analisis
