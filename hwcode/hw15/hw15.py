from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import pandas as pd 
from tabulate import tabulate
################################################################################
# 10.3
problem = """
10.3 What properties are influenced by the degree of polymerization?"""
print(problem)
answer = """
i. Tensile and impact stregth
i1. Vicousity 
"""
print(answer)

# 10.11
problem = """
10.11 Discuss the significance of the glass-transition temperature, Tg , in 
engineering applications."""
print(problem)
answer = """
The glass transition temperature, Tg, is the temperature at which amorphous 
polymers transition from being hard, brittle and glassy to being softer, more 
flexible and rubbery, and the mechanical propertiesare change significantly.

Because the mechanical properties are changed significantly as this temperature,
engineering applicationscan be developed to exploit this property. For example, 
at below the Tg, amorphous polymers, are more hard,rigid and brittle, this
property can be used to develop polymer parts that require these properties and 
are only exposed to low temperatures.

This temperature also affects properties like the workability of the polymer, 
dimensional stability the material and a few other. These are properties that 
can be exploited for different suitable engineering applications
"""
print(answer)

################################################################################
# Prob 10.27
# image = mpimg.imread("figure10.8.png")
# plt.imshow(image)
# plt.show()
image = Image.open('figure10.8.png')
image.show()

problem = """
10.27 Review the three curves in Fig. 10.8, and name applications for each type
of behavior. Explain your choices."""
print(problem)

answer = """
Rigid and brittle (Melamine)
Melamine are rigid and brittle and can be applied in the area of funiture making. 
Melamine is hard, and highly durable and can tolerate heat better than other 
plastics. This makes it a great material in furniture making.

Tough and ductile (ABS)
ABS can be applied in the making of steering wheel covers and dashboards. The 
toughness and ductility are great qualities that can absorb and redistribute 
energy on impact and as a consequence keep passangers safe.

Soft and flexible (Polyethylene)
Polyethylene can be applied in the making of insulation for wires and cables. 
Polyethylene is soft and flexible which is a desirable characteristic for 
insulations for wires and cables as wires and cables usually have to turn over 
tight corners and are not usually load bearing. 
"""
print(answer)
################################################################################

# Prob 10.58
problem = """
10.58 What characteristics make polymers attractive for applications such as 
gears? What characteristics are drawbacks for such applications?"""
print(problem)

answer = """
Characteristics make polymers attractive for applications
Corrosion resistance - Compared to metals, polymers are very corrosion 
resistant. This is a favorable property for a gear, especially in an 
application that is exposed to harsh chemicals.

Light weight - Polymers gear are considerably lighter than metal gears of 
similar size.

Good shock absorption - Polymer gears can deflect to absorb impact loads 
more than metal gears.

Noise reduction - The dampening properties of polymers result in more quiet 
gears compared to metals gears.

Drawbacks
Temperature sensitivity - High tempeartures may alter the material properties and
hence reduce the effectiveness of the gear.

Strength - The strength of polymers are considerably less than the strength of 
metals. 

Wear resistance - Compared to metals, polymer gears may need to be replaced more
often.
"""
print(answer)
################################################################################

# Prob 10.87
image = Image.open('figure10.9.png')
image.show()
problem = """
10.87 Calculate the areas under the stress–strain curve (toughness) for the 
material in Fig. 10.9 , plot them as a function of temperature, and describe 
your observations."""
print(problem)

curve_neg_25 = 0.5*3*10
curve_0 = (0.5*4*9.5) + ((13-4)*9.5)
curve_25 = (0.5*3*6) + ((20-3)*6)
curve_50 = (0.5*3*3) + ((30-3)*3)
curve_65 = (0.5*2.5*2) + ((30.5-2)*2.5)
curve_80 = (0.5*1.5*2) + ((31-2)*2)

dict = {'temperature': [-25, 0, 25, 50, 65, 80],
'area': [curve_neg_25, curve_0, curve_25, curve_50, curve_65, curve_80]
}

df = pd.DataFrame(dict)
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
plt.plot(dict['temperature'], dict['area'])
plt.xlabel('Temperature (degrees C)')
plt.ylabel('Area under curve (psi x 10^3)')
plt.show()

observation = """
The area under the curve, toughness, increases as the temperature increases until
around 50 degree celsius and where the area, toughness, starts to degrees.
"""
print(observation)
################################################################################

# Prob 10.88
image = Image.open('figure10.9.png')
image.show()
problem = """
10.88 Note in Fig. 10.9  that, as expected, the elastic modulus of the polymer 
decreases as temperature increases. Using the stress-strain curves in the figure, 
make a plot of the modulus of elasticity versus temperature.
"""
print(problem)

curve_neg_25 = 5.2/1
curve_0 = 4/1
curve_25 = 3/1
curve_50 = 2.3/1
curve_65 = 2/1
curve_80 = 1.75/1

dict = {'temperature': [-25, 0, 25, 50, 65, 80],
'E': [curve_neg_25, curve_0, curve_25, curve_50, curve_65, curve_80]
}

df = pd.DataFrame(dict)
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
plt.plot(dict['temperature'], dict['E'])
plt.xlabel('Temperature (degrees C)')
plt.ylabel('Modulus of Elasticity (psi x 10^3)')
plt.show()
