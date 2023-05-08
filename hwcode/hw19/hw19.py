# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg
# from PIL import Image
# import pandas as pd 
# from tabulate import tabulate
# ################################################################################
# # 11.94
# problem = """
# 11.94 Calculate the thermal conductivities for ceramics at porosities of 1%, 5%, 10%, 
# 20%, and 30% for ko  = 0.7 W/m-K"""
# def ThermalConductivity(ko, p):
#     return ko*(1-p)
# print(problem)
# ko = 0.7
# p = 0.01
# k = ThermalConductivity(ko, p)
# print('Thermal conductivity @ 1% porosity ' + str(round(k,3)))
# p = 0.05
# k = ThermalConductivity(ko, p)
# print('Thermal conductivity @ 5% porosity ' + str(round(k,3)))
# p = 0.10
# k = ThermalConductivity(ko, p)
# print('Thermal conductivity @ 10% porosity ' + str(round(k,3)))
# p = 0.20
# k = ThermalConductivity(ko, p)
# print('Thermal conductivity @ 20% porosity ' + str(round(k,3)))
# p = 0.30
# k = ThermalConductivity(ko, p)
# print('Thermal conductivity @ 30% porosity ' + str(round(k,3)))

################################################################################
# Web Problem W6-1
problem = """
Estimate the elastic modulus of a particle composite with 47% wood particles and 53% 
sodium silicate (ss) matrix. E_ss=45 GPa. and E_wood=10.8 GPa."""
print(problem)
answer = """
"""
E_1=(0.47*(10.8))+(0.53*(45))
print(E_1)

E_m = 45
E_f = 10.8
x_m = 0.53
x_f = 0.47
E_2=(E_m*E_f)/((x_m*E_f)+(x_f*E_m ))
print(E_2)
# print(answer)
################################################################################
