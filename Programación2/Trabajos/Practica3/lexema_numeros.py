#    2021-04-28
#    lexema_numeros.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    Implementación de expresión regular.

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de compilación: no requere nada mas
#    python3 lexema_numeros.py

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

class Analizador:

    def __init__(self):
        self.letra_actual=''
        self.estado_actual=0
        self.valor_lexema=''
        self.aceptacion = False

    def switch(self, estado):
        self.estados = {
        0: self.estado_cero,
        1: self.estado_uno,
        2: self.estado_dos,
        }
        func = self.estados.get(estado, lambda: 'No es un caracter válido' )
        return func()

    def estado_cero(self):
        if int(self.letra_actual) > 0:
            self.estado_actual = 2
            self.valor_lexema = self.valor_lexema + self.letra_actual
        elif int(self.letra_actual) == 0:
            self.estado_actual = 1
            self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print('No hay transición disponible de estado 0 con ', self.letra_actual)
            self.valor_lexema = ''

    def estado_uno(self):
        print("He aceptado el lexema ", self.valor_lexema)
        self.estado_actual = 0
        self.aceptacion = True

    def estado_dos(self):
        if self.letra_actual.isdigit():
            self.estado_actual = 2
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True
        else:
            self.estado_actual = 0
            print("He aceptado el lexema ", self.valor_lexema)

    def analizar(self, cadena):
        cadena = str(cadena)
        for x in cadena:
            self.letra_actual = x
            self.switch(self.estado_actual)
        print("He aceptado el lexema ", self.valor_lexema)

Analizador().analizar('1224aq555')
