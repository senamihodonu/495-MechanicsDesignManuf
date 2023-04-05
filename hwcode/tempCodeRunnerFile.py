def spring_back_factor(R, Sy, E, t):
   return 4*((R*Sy)/(E*t))**3 - 3*((R*Sy)/(E*t)) + 1

t = 1 # mm
Ri = 0.25 # mm
Rf = 250 # mm
R = np.arange(Ri,Rf,0.25)

# 1100-O aluminum
Sy_Al = 35 # MPa
E_Al = 70000 #MPa
Ks_Al = spring_back_factor(R, Sy_Al, E_Al, t)
plt.plot(R, Ks_Al, label = '1100-O aluminum')

# Ti-6Al-4V (Annealed)
Sy_Ti = 925 # MPa
E_Ti = 110000 #MPa
Ks_Ti = spring_back_factor(R, Sy_Ti, E_Ti, t)
plt.plot(R, Ks_Ti, label = 'Ti-6Al-4V (Annealed)')
plt.legend()
plt.title('Springback Factor vs. Radius')
plt.xlabel('Radius (mm)')
plt.ylabel('Springback Factor, Ks')
plt.show()