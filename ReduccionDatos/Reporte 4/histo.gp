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


set xlabel "Número de Caras por Lanzamiento"
set ylabel "Frecuencia"
set title "Histograma de Frecuencias 10 Lanzamientos"

plot "10exp.dat" with boxes lc "red" t "Medido", "10sim.dat" with boxes lc "blue" t "Simulado"







set xlabel "Número de Caras por Lanzamiento"
set ylabel "Frecuencia"
set title "Histograma de Frecuencias 50 Lanzamientos"

plot "50exp.dat" with boxes lc "red" t "Medido", "50sim.dat" with boxes lc "blue" t "Simulado"










set xlabel "Número de Caras por Lanzamiento"
set ylabel "Frecuencia"
set title "Histograma de Frecuencias 100 Lanzamientos"

plot "100exp.dat" with boxes lc "red" t "Medido", "100sim.dat" with boxes lc "blue" t "Simulado"








set xlabel "Número de Caras por Lanzamiento"
set ylabel "Frecuencia"
set title "Histograma de Frecuencias 300 Lanzamientos"

plot "300exp.dat" with boxes lc "red" t "Medido", "300sim.dat" with boxes lc "blue" t "Simulado"











# END PROGRAM histo
