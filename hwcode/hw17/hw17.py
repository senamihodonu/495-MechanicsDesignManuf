from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import pandas as pd 
from tabulate import tabulate
################################################################################
# # 10.20
# problem = """
# 10.20 What products have you personally seen that are made of reinforced plastics? 
# How can you tell that they are reinforced?"""
# print(problem)
# answer = """
# """
# print(answer)
# ################################################################################
# # 10.34
# problem = """
# Explain how you would go about determining the hardness of the reinforced plastics 
# and composite materials described in this chapter. Are hardness measurements for 
# these types of materials meaningful? Does the size of the indentation make a 
# difference in your answer? Explain."""
# print(problem)
# answer = """
# The hardness of reinforce plastics and composite materials can be determined by measuring the 
# materials resistance to indentation or scratching. Because of the sometimes isotropic, anisotropic or orthotropic
# nature of reinforced plastics, hardness could vary depending on the material orientation. The size of indentation
# should not matter since the material hardness is being determined for the whole material and not just a layer of 
# the material.
# """
# print(answer)

# ################################################################################
# Prob 10.110
problem = """
10.110 Calculate the elastic modulus and load supported by fibers in a composite 
with an epoxy matrix (E = 100 GPa), made up of 25% fibers made of (a) high-modulus 
carbon fiber and (b) Kevlar 29 fibers."""
print(problem)

answer = """
area fraction of fibers, x = 0.25
area fraction of matrix, Af = 1 - 0.25 = 0.75
Elastic modulus of matrix, Em = 100 GPa
Elastic modulus of high-modulus carbon fiber, Ef = 415 GPa
Elastic modulus of high-modulus Kevlar 29 fibers, Ef = 70.5 GPa
Elastic modulus of composite, Ec = x*Ef + (1-x)*Em
"""

def ElasticModulusComposite(x, Ef, Em):
    Ec = x*Ef + (1-x)*Em
    return Ec

def LoadFraction(Af, Am, Ef, Em):
    """
    Ff/Fm = (Af*Ef)/(Am*Em)
    """
    res = (Af*Ef)/(Am*Em)
    return res

def Solution(xf,Ef,Em): #Ff/Fc
    ret_val = 1/(((1-xf)*Em)/(xf*Ef) + 1)
    return ret_val

x = 0.25
Em = 100 #GPa
Ef_carbon = 415 #GPa
Ef_kevlar = 70.5 #GPa

Ec_kevlar = ElasticModulusComposite(x, Ef_kevlar, Em)
print(answer)

print('for high-modulus carbon fiber')
print('Ec = x*Ef + (1-x)*Em')
Ec_carbon = ElasticModulusComposite(x, Ef_carbon, Em)
print('Ec = ' + str(Ec_carbon) + ' GPa')
print('Load Fraction, Ff/Fm = (Af*Ef)/(Am*Em)')
# load_fraction = LoadFraction(x, 1-x,Ef_carbon,Em)
# print('Ff/Fm = ' + str(round(load_fraction, 3)))
load_fraction_solution = Solution(x, Ef_carbon,Em)
print('Ff/Fc = ' + str(round(load_fraction_solution, 3)))

print('\nfor Kevlar 29 fibers')
Ec_kevlar = ElasticModulusComposite(x, Ef_kevlar, Em)
print('Ec = ' + str(Ec_kevlar) + ' GPa')
# load_fraction = LoadFraction(x, 1-x,Ef_kevlar,Em)
# print('Ff/Fm = ' + str(round(load_fraction, 3)))
load_fraction_solution = Solution(x, Ef_kevlar,Em)
print('Ff/Fc = ' + str(round(load_fraction_solution, 3)))





# ################################################################################

# # Prob 10.111
# problem = """
# 10.111 Calculate the stress in the fibers and in the matrix for Problem 10.110 . 
# Assume that the cross-sectional area is 50 mm^2  and Fc = 2000 N"""
# print(problem)

# answer = """
# from eqn(10.12),

# Fc = Ff + Fm

# also, Ff/Fm = ratio

# so, Fc = Ff + Ff/ratio
# """
# print(answer)
################################################################################
# Composites Web Problem (W5-1)
# problem = """
# Your defense firm is working on a stealth plane. Hematite can be added to polymers to 
# absorb radar and you are considering this approach for a landing gear component. You 
# need to determine the coefficient of thermal expansion of an acetal-based composite 
# filled to 45% volume with hematite particles."""
# print(problem)

# answer = """
# Ehematite=298GPa
# Eacetal= 2.9GPa
# CTEhematite= 9.9 x 10-6/°C
# CTEacetal=96.3 x 10-6/°C

# """
# Eb = 2.9
# Ep = 289
# alpha_p = 9.9*(10**-6)
# alpha_b = 96.3*(10**-6)
# Vf = .45

# def Epc(Vf, Eb, Ep):
#     A = (Vf**0.67)*Eb
#     D = 1-(Eb/Ep)
#     B = 1-((Vf**0.33)*D)
#     C = 1 - (Vf**0.67)*Eb

#     return (A/B) + C

# def Ep_bar(Eb, Vf, Ep):
#     B = 1-(Eb/Ep)
#     A = 1-((Vf**0.33)*B)
#     return  Eb/A

# def alpha_bar(alpha_b, Vf, alpha_p):
#     return alpha_b - (Vf**0.33)*(alpha_b-alpha_p)

# def alpha_pc(alpha_bar, Vf, Ep_bar, Epc, alpha_b, Eb):
#     A = alpha_bar*(Vf**0.67)*(Ep_bar/Epc)
#     B = alpha_b*(Eb/Epc)
#     C = alpha_b*(Vf**0.67)*(Eb/Epc)
#     return A + B - C

# print(answer)

# Epc = Epc(Vf, Eb, Ep)
# print('Epc = '+ str(round(Epc,3)) + ' GPa')

# Ep_bar = Ep_bar(Eb, Vf, Ep)
# print('Ep_bar = '+ str(round(Ep_bar,3)))

# alpha_bar = alpha_bar(alpha_b, Vf, alpha_p)
# print('alpha_bar = '+ str(alpha_bar))

# alpha_pc = alpha_pc(alpha_bar, Vf, Ep_bar, Epc, alpha_b, Eb)
# print('alpha_pc = '+ str(alpha_pc))

