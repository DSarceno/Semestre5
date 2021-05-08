!    2021-05-06
!    simulacion.f95
!    Diego Sarceño (dsarceno68@gmail.com)

!    Gráfico de Incertezas.

!    Codificación del texto: UTF8
!    Compiladores probados: GNU Fortran (Ubuntu 20.04 Linux) 9.3.0
!    Instrucciones de compilación: no requiere nada más
!    gfortran -Wall -pedantic -std=f95 -c -o simulacion.o simulacion.f95
!    gfortran -o simulacion.x simulacion.o

!    Copyright (C) 2021
!    D. R. Sarceño Ramírez
!    dsarceno68@gmail.com
!
!
!    This program is free software: you can redistribute it and/or
!    modify it under the terms of the GNU General Public License as
!    published by the Free Software Foundation, either version 3 of
!    the License, or (at your option) any later version.
!
!    This program is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
!    General Public License for more details.
!
!    You should have received a copy of the GNU General Public License
!    along with this program.  If not, see
!    <http://www.gnu.org/licenses/>.
!
! Inicio
PROGRAM simulacion
IMPLICIT NONE

INTEGER(8) :: n,i,j
INTEGER(4) :: k
INTEGER(8) :: frecuencia
REAL(8),ALLOCATABLE,DIMENSION(:,:) :: num
INTEGER(4) :: base
INTEGER(4), ALLOCATABLE,DIMENSION(:) :: seed
INTEGER(4) :: s
INTEGER(4):: err


OPEN(21,FILE="n.in",STATUS="OLD",IOSTAT=err)
IF (err.EQ.0) THEN
  READ(21,*) n
  CLOSE(21)
ELSE
   STOP 'Archivo no encontrado'
END IF



! Leer la base
OPEN(12,FILE="seed.in",STATUS="OLD",IOSTAT=err)
IF (err.EQ.0) THEN
  READ(12,*) base
  CLOSE(12)
END IF
! Tamaño optimo para el seed
CALL RANDOM_SEED(SIZE = s)
! allocate seed
ALLOCATE(seed(s), STAT=err)
IF (err.NE.0) STOP 'Memoria no reservada'
! Generador de números para el seed
seed = base + 37 * (/ (k-1,k=1,s) /)
CALL RANDOM_SEED(PUT = seed)
DEALLOCATE(seed)



ALLOCATE(num(n,10),STAT=err)
IF (err.NE.0) STOP 'Memoria no reservada'

CALL RANDOM_NUMBER(num)

DO i = 1,n
  frecuencia = 0
  DO j = 1,10
    frecuencia = frecuencia + FLOOR(2*num(i,j))
  END DO
  WRITE(1,*) frecuencia
END DO
 CLOSE(1)



END PROGRAM simulacion

































! END
