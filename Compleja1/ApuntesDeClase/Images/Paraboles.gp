# Creando las gráficas de la clase 15 en Gnuplot
# Se toman las ecuaciones paramétricas en contradas en el plano v-u
set output "Parabolas.png"
set title "Ejemplo Clase 15"
set xrange [-2:2]
set yrange [-2:2]
set xlabel "v"
set ylabel "y"


## Ploteando las ecuaciones (estan respecto de x pero se sabe que es v)
plot [-2:2] (1-x**2)/2 lc black, (x**2 - 1)/2 lc "red"

show plot
