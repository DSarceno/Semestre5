file = open('times.csv','r')
data = [line.split(',') for line in file]
file.close()

file = open('tabla_tiempos.tex','w')
file.write('\\hline \n')
file.write('\\hline \n')
file.write('No. & $h_1 (cm)$ & $h_2 (cm)$ & $h_3 (cm)$ & $h_4 (cm)$ & $h_5 (cm)$ \\\\ \n')
file.write(' & $5.7 \pm 0.1$ & $9.7 \pm 0.1$ & $10.3 \pm 0.1$ & $12.9 \pm 0.1$ & $14.6 \pm 0.1$ \\\\ \n')
file.write('\\hline \n')
file.write('\\hline \n')
file.write(' & $t_{h_1} (s)$ & $t_{h_2} (s)$ & $t_{h_3} (s)$ & $t_{h_4} (s)$ & $t_{h_5} (s)$ \\\\ \n')
file.write('\\hline \n')


for i in range(len(data)):
	file.write('$' + data[i][0] + '$ & $' + data[i][1] + '$ & $' + data[i][2] + '$ & $' + data[i][3] + '$ & $' + data[i][4] + '$ & $' + str(float(data[i][5])) + '$ \\\\ \n')
	
file.write('\\hline')
