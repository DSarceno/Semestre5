datos_10 <- scan('10exp.dat')


mu_10 <- 5.3
N <- 10

chi_c_10 <- 0
for (i in 0:10){
  E_k <- 10*dpois(i, lambda = mu_10, log = FALSE)
  chi_c_10 <- chi_c_10 + (E_k - datos_10[i+ 1])**2 / (E_k)
}

datos_300 <- scan('300exp.dat')

mu_300 <- 4.95
chi_c_300 <- 0
for (i in 0:10){
  E_k <-300*dpois(i, lambda = mu_300, log = FALSE)
  chi_c_300 <- chi_c_300 + (E_k - datos_300[i + 1])**2 / (E_k)
}

chis <- c(chi_c_10, chi_c_300)
write(chis, 'chis_cuadrados_10300_poisson.chis')
