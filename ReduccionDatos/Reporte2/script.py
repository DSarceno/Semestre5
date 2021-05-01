from math import sqrt

t = [2.248,1.541,1.469,1.137,1.015]
delta_t = [0.177,0.170,0.173,0.167,0.174] # con tiempo de reacción añadido
# t_r=0.16

d = 0.765
delta_d = 0.001

# a_exp
a_e = []
def a_exp(d,t):
    for i in range(len(t)):
        a_e.append(2*d/(t[i])**2)
    return a_e

delta_a_e = []
def delta_a(t,delta_t,a_exp,d,delta_d):
    for i in range(len(a_exp)):
        delta_a_e.append( a_exp[i]*sqrt( (delta_d/d)**2 + (2*delta_t[i]/t[i])**2 ) )
    return delta_a_e

a_exp(d,t)
delta_a(t,delta_t,a_e,d,delta_d)

print(a_e)
print(delta_a_e)




h = [0.057,0.097,0.103,0.129,0.146]
delta_h = 0.001

a_t = []
delta_a_t = []


def a_teo(h,d):
    for i in range(len(h)):
        a_t.append(5*9.8*h[i]/(7*d))
    return a_t
    
a_teo(h,d)


def delta_a_teo(h,delta_h,a_teo,d,delta_d):
    for i in range(len(a_teo)):
        delta_a_t.append( a_teo[i]*sqrt( (delta_d/d)**2 + (delta_h/h[i])**2 ) )
    return delta_a_t
    
delta_a_teo(h,delta_h,a_t,d,delta_d)

print()
print(a_t)
print(delta_a_t)


diff = []
delta_diff = []
for i in range(len(t)):
	diff.append(abs(a_e[i] - a_t[i]))
	delta_diff.append( sqrt(delta_a_e[i]**2 + delta_a_t[i]**2) )	
print()
print(diff)
print(delta_diff)



file = open("diferencias.dat","w")
for i in range(len(t)):
	file.write(str(h[i]) + '\t' + str(diff[i]) + '\t' + str(delta_h) + '\t' + str(delta_diff[i]) + '\n')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
