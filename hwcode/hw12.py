import math
"""
6.121 	Estimate the force required in extruding 70–30 brass at 700°C, if the billet diameter is 125 mm and the extrusion ratio is 20.

"""

Re = 20 #extrusion ratio
d = 125 #billet diameter
Ke = 250

# F = (p)(Ao) 
# p = sigma(1.7 ln Re + 2L/Do)
# p = 8.27 MN

p = Ke*math.log(Re)

# print(p)

A = math.pi*125*125*(1/4)

F = p*A

# print(F)

F= 35*math.log(150/100)*math.pi*150*150*(1/4)
print(F)
R = .3*F
print(R)
res = (F+R)/0.75
print(res)