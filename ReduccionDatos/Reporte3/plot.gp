set terminal pdf
set output "puta.pdf"

binwidth=5
bin(x,width)=width*floor(x/width)




plot 'dat.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes
