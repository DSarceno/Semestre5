#    2021-05-09
#    binomial.R
#    Diego Sarceño (dsarceno68@gmail.com)

#    Análisis bajo la distribución binomial.

#    Codificación del texto: UTF8
#    Compiladores probados: R (Ubuntu 20.04 Linux) 4.0.3
#    Instrucciones de compilación: no requiere nada más
#    Rscript binomial.R

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
# PROGRAM binomial
datos_10 <- scan('10exp.dat')


p_10 <- 5.3/10
N <- 10

chi_c_10 <- 0
for (i in 0:10){
  E_k <- 10*dbinom(i, size = N, prob = p_10)
  chi_c_10 <- chi_c_10 + (E_k - datos_10[i+ 1])**2 / (E_k)
}

datos_300 <- scan('300exp.dat')

p_300 <- 4.95/10
chi_c_300 <- 0
for (i in 0:10){
  E_k <-300*dbinom(i, size = N, prob = p_300)
  chi_c_300 <- chi_c_300 + (E_k - datos_300[i + 1])**2 / (E_k)
}

chis <- c(chi_c_10, chi_c_300)
write(chis, 'chis_cuadrados_10300.chis')
