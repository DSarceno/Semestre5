set terminal pdf
set output "normal.pdf"

binwidth = 0.8
set boxwidth binwidth
set xrange [-1:6]
set yrange [-0.001:0.4]
set xtics ("0" -0.5, "2.288" 0.5, "2.9" 1.5, "3.516" 2.5, "4.13" 3.5, "4.744" 4.5, "5.5" 5.5)


set xlabel "Intervalos"
set ylabel "Frecuencia Relativa"
set title "Histograma de Frecuencias"

#X = 3.516
#sigma = 0.614

#phi(x) = (1/(sigma*sqrt(2*pi)))*exp(-(x - X)**2/2*sigma**2)

plot "dat.dat" with boxes lc "red" t "Medidos", "dat2.dat" with boxes lc "blue" t "Esperados"
