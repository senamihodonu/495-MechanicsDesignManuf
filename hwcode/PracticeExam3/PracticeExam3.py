def FractionOfLoad(xf, Em,Ef):
    return 1/((((1-xf)*Em)/(xf*Ef))+1)

def CriticalLength(sigma_f, D, tau):
    return ((sigma_f*D)/(2*tau))

xf = 0.75
Ef = 22*(10**6)
Em = 0.5*(10**6)

print(FractionOfLoad(xf, Em, Ef))
sigma_f = 400*(10**3)
D = 0.46*(10**-3)
tau = 2352
print(CriticalLength(sigma_f, D, tau))

res = (240 + ((240*240)/4) - ((100*100)/4))/50
res = 3.142*138.6*190*(2.1-0.7)
res = (400*(10**3))*(3.142*(0.46*(10**-3))**2)/4
res = 0.067/.99
print(res)