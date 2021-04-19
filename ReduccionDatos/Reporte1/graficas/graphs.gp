set terminal pdf
set output "angulos.pdf"

set xlabel 'Angulo (Grados)'
set ylabel 'Periodo'
set title 'Periodo al Variar el Ángulo'
set size ratio 1

set yrange [1.5:2.5]
set xrange [4:21.5]

plot "angulos.dat" t 'Periodos'
