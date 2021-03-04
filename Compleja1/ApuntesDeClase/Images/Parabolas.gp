# Creando las gráficas de la clase 15 en Gnuplot
# Se toman las ecuaciones paramétricas en contradas en el plano v-u
set terminal pdf
set output "Parabolas.pdf"
set title "Ejemplo Clase 16"
set grid
set autoscale
set xrange [-4:4]
set yrange [-2:2]
set xlabel "v"
set ylabel "u"


## Ploteando las ecuaciones (estan respecto de x pero se sabe que es v)
plot [-4:4] (1-x**2)/2 lc black, (x**2 - 1)/2 lc "red"

show plot
