#    2021-04-07
#    incetezas.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráfico de Incertezas.

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: requiere archivo 'diferencias.dat'
#    gnuplot incetezas.gp

#    Copyright (C) 2021
#    D. R. Sarceño Ramírez
#    dsarceno68@gmail.com
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

# PROGRAM
# Idioma
set encoding utf8
# terminal
set terminal pdf
set output "diferencias.pdf"


# Labels
set title "Gráfico de Incertezas"
set xlabel "Altura (m)"
set ylabel "Aceleración (m/s^2)"

# Grid y leyenda
set grid
unset key

# linea punteada remarcando el eje x = 0
set arrow from 0.05,0 to 0.15,0 nohead dt 2 lc -1

# plot de los datos con sus respectivas incertezas
plot 'diferencias.dat' u 1:2:3:4 with xyerrorbars lc "blue"


# Ejemplo archivo 'diferencias.dat'
# dato x	dato y		incerteza x	  incerteza y
