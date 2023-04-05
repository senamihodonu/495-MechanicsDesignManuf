import numpy as np
import matplotlib.pyplot as plt

"""
7.70 Estimate the maximum bending force required for a 2-mm-thick and 
250-mm-long Ti-6Al-4V titanium alloy, annealed and quenched at 25°C, in 
a V-die with a width of 150 mm.
"""
# t = 2 # mm
# L = 250 # mm
# W = 150 # mm
# k = 1.33
# S_ut = 1000 # mm
# F_max = k*S_ut*L*(t**2)/W

# print(str(F_max) + ' N')


"""
7.79 Calculate and plot the springback in bending 1-mm thick sheet metal 
around radii from 0.25 to 250 mm for (a) 303 stainless steel; (b) 1100-O 
aluminum; (c) HK31A magnesium; (d) Ti-6Al-4V.
"""

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
# plt.plot(R, Ks_Al, label = '1100-O aluminum')

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

