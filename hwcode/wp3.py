import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prettytable import PrettyTable

def average_height(initial_height, final_height):
    return (initial_height+final_height)/2

def length_of_contact(diameter, h0, hf):
    return ((diameter/2)*(h0-hf))**0.5

def rolling_force(diameter, initial_height, final_height, mu, width, flow_stress):
    L = length_of_contact(diameter, initial_height, final_height)
    hav = average_height(initial_height,final_height)
    return L*width*flow_stress*(1+((mu*L)/(2*hav)))

def force_plots(x_values, y_values,type):
    x_title = " "
    if type == 'diameter'.lower():
        x_title = 'Diameter (in)'
    elif type == 'hf'.lower():
        x_title = 'Final height (in)'
    elif type == 'mu'.lower():
        x_title = 'Coefficient of friction'

    t = PrettyTable([x_title, 'Force (N)'])
    for (i,j) in zip(x_values, y_values):
        t.add_row([round(i,2),round(j,2)])
    print(t)

    plt.plot(x_values, y_values)
    plt.title('Force vs. ' + x_title)
    plt.xlabel(x_title)
    plt.ylabel('Force (N)')
    plt.show()
    

def main():
    #web problem
    h0 = 0.5 
    hf_i = 0.4 #vary
    D_i = 20 #vary
    mu_i = 0.1 #vary
    width = 1
    flow_stress = 1

    force_list_D = []
    force_list_hf = []
    force_list_mu = []
    D = list(range(10,D_i+1))
    hf = np.arange(0.05, hf_i+0.05, 0.05)
    mu = np.arange(mu_i, 0.5, 0.05)

    for x in D:
        force = rolling_force(x,h0,hf_i,mu_i, width, flow_stress)
        force_list_D.append(force)
    
    for x in hf:
        force = rolling_force(D_i,h0,x,mu_i, width, flow_stress)
        force_list_hf.append(force)

    for x in mu:
        force = rolling_force(D_i,h0,hf_i,x, width, flow_stress)
        force_list_mu.append(force)

    # force_plots(D,force_list_D, 'diameter')
    # force_plots(hf,force_list_hf, 'hf')
    force_plots(mu,force_list_mu, 'mu')

    # # 6.114
    # h0 = 5 #mm
    # hf = 3.75 #mm
    # w0 = 250 #mm
    # R = 200 #mm
    # mu = 0.25
    # ave_flow_stress = 275 #MPa
    # hav = average_height(h0, hf)
    # print("The average height is " + str(round(hav,2)) + " mm")
    # length = length_of_contact(R*2, h0, hf)
    # print("The length of contact is " + str(round(length, 2)) + " mm")
    # force = rolling_force(R*2,h0,hf,mu,w0,ave_flow_stress)
    # print("The roll force is " + str(round(force, 2)) + " N")



main()