from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import pandas as pd 
from tabulate import tabulate
################################################################################
# 10.35
problem = """
10.35 Describe the advantages of applying traditional metalworking techniques to the formation of plastics."""
print(problem)
answer = """
Traditional metalworking techniques can be applied to the formation of plastics with few, or no 
additional operations required. Compared to metals, plastics melt or cure at relatively lower 
temperatures, this makes plastics easier to handle and require less energy to process.
"""
print(answer)
################################################################################
# 10.38
problem = """
10.38 Would you use thermosetting plastics for injection molding? Explain."""
print(problem)
answer = """
Due to the irreversible polymerization and crosslinking during the molding of thermosets, conventions injection molding methods are not 
suitable. Instead, thermosets are molded in heated molds, where polymerization and cross-linking take place. 
After the part is sufficiently cured, the molds are opened, and the part is ejected. Essentially in 
thermoset injection molding, cold material is injected into an extremely hot mold to create a part.
"""
print(answer)

################################################################################
# Prob 10.39
problem = """
10.39 By inspecting plastic containers, such as for baby powder, you can see that the lettering on them 
is raised rather than sunk. Can you offer an explanation as to why they are molded in that way?"""
print(problem)

answer = """
Raising the lettering on an injection molded part may be preferred to sinking the lettering due firstly, the 
ease of manufacturability of the part. Raised lettering can be easily stamped into the mold, whereas a 
sunk lettering may require a more complex mold design which may increase the manufacturing cost. 
Secondly, the sunk lettering may fade faster over time compared to the raised lettering. And finally, the 
raised lettering can have a more pleasing tactile quality, which may enhance the overall aesthetic of the 
part.  """
print(answer)
################################################################################

# Prob 10.40
problem = """
10.40 Give examples of several parts that are suitable for insert molding. How would you
manufacture these parts if insert molding were not available?"""
print(problem)

answer = """
Parts that are suitable for insert molding include threaded inserts, screw drivers, electrical and computer 
components (i.e., USB drives, wall plug-ins). Without insert molding, these parts may be manufactured 
using drilling and tapping the molded part, fasteners, adhesive.
"""
print(answer)
###############################################################################

# Prob 10.90
problem = """
10.90 A rectangular cantilever beam 100 mm high, 50 mm wide, and 1 m long is subjected to a 
concentrated force of 100 N at its end. Select two different unreinforced and reinforced materials from 
Table 10.1 , and calculate the maximum deflection of the beam. Then select aluminum and steel, and 
for the same beam dimensions, calculate the maximum deflection. Compare the results."""
print(problem)
answer = """
width, b = 50 mm
height, d = 100 mm
length, L =  1 m
point load, P = 100 N

Acetal 
Elastic modulus (GPa) = 1.4-3.5
Acetal, reinforced
Elastic modulus (GPa) = 10
Polycarbonate
Elastic modulus (GPa) = 2.5-3
Polycarbonate, reinforced
Elastic modulus (GPa) = 6
Aluminum
Elastic modulus (GPa) = 62
Steel, low alloy
Elastic modulus (GPa) = 196
"""

print(answer)

image = Image.open('Figure1.png')
image.show()

b = 50 # wdith in mm
# b = 0.050 # in m
d = 100 # height in mm
# d = 0.100 # in m
I = (b*(d**3))/12 # Moment_of_inertia
L =  1 # length of beam in meters (m)
P = 100 # point load in Newtons (N)

elastic_modulus = [3.5, 10, 3, 6, 62, 200]
max_deflection = []

print('Moment of inertia, I_xx=(bd^3)/12')
print('I_xx = ((50mm)(100mm)^3/12')
print("The moment of inertia is "+ str(I) + " m^4\n")

print("Max deflection, d_max = (PL^3)/3EI")

L = 1000 # in mm

for E in elastic_modulus:
    deflection = (P*(L**3))/(3*(E*1000)*I)
    max_deflection.append(deflection)

elastic_modulus = []
dict = {'Material': ['Acetal', 'Acetal, reinforced', 'Polycarbonate', 'Polucarbonate, reinforced', 'Aluminum', 'Steel'],
'Modulus of Elasticity (GPa)': [3.5, 10, 3, 6, 62, 196],
'Max deflection (mm)': [max_deflection[0], max_deflection[1], max_deflection[2], max_deflection[3], max_deflection[4], max_deflection[5]]
}

df = pd.DataFrame(dict)
print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex=False, numalign='right'))

##############################################################################

# W3-1
problem = """
W3-1
Find a complex injection molded component (or two). Power tools, toys, electronics, packaging/containers, 
consumer products, kitchen appliances, and automotive parts are great places to look. You may have to 
disassemble a little bit.

Take photographs of the component and label all of the design features you observe such as, constant wall 
thickness, strengthening ribs of appropriate thickness, fastening features (screw boss, snap-fit, etc), 
fillets on all corners, appropriate draft all surfaces, gating location, ejector pin locations, textured 
surfaces, fastening features, and creative designs that avoid the use of cross-slides. Compare these features 
with the design rules from the GE design guide. Comment on where you see any deviations from the rules (if any).

Powerpoint is a great tool for labeling your photographs."""
print(problem)
answer = """
"""
print(answer)
##############################################################################

