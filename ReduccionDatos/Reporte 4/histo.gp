#    2021-05-06
#    histo.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráfico de Incertezas.

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.3
#    Instrucciones de compilación: no requiere nada más
#    gnuplot histo.gp

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
# PROGRAM histo
set terminal pdf
set output "normal.pdf"

binwidth = 0.8
set boxwidth binwidth
#set xrange [-1:6]
#set yrange [-0.001:0.4]
#set xtics ("0" -0.5, "2.288" 0.5, "2.9" 1.5, "3.516" 2.5, "4.13" 3.5, "4.744" 4.5, "5.5" 5.5)


#set xlabel "Intervalos"
#set ylabel "Frecuencia Relativa"
#set title "Histograma de Frecuencias"

#X = 3.516
#sigma = 0.614

#phi(x) = (1/(sigma*sqrt(2*pi)))*exp(-(x - X)**2/2*sigma**2)

#plot "dat.dat" with boxes lc "red" t "Medidos", "dat2.dat" with boxes lc "blue" t "Esperados"

plot "300frec.dat" with boxes lc "red"
plot sin(x)











! END PROGRAM histo
