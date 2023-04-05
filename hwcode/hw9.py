import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


def final_height(h0,reduction):
    return h0-(reduction*h0)/100

def final_radius(ri,h0,hf):
    return ri*(h0/hf)**(0.5)

def force(flow_stress, mu, rf, hf):
    return flow_stress*(1+((2*mu*rf)/(3*hf)))*math.pi*rf*rf

# reduction = list(range(9,71))
reduction = [10, 20, 30, 40, 50, 60, 70]
force_list_0 = []
force_list_025 = []
force_list_05 = []
mu =  [0, 0.25, 0.5]
K = 315 #MPa
h0 = 50 #mm
di = 25 #mm
ri = di/2
n = 0.54

for x in reduction:
    true_strain = abs(math.log(h0/final_height(50,x)))
    # print('the true strain is ' + str(round(true_strain,2)))
    flow_stress = K*true_strain**n
    hf = final_height(h0, x)
    rf = final_radius(ri,h0,hf)
    # print('the flow stress is ' + str(round(flow_stress,2)))
    force_0 = force(flow_stress, mu[0], rf, hf)
    force_list_0.append(round(force_0,2))
    force_025 = force(flow_stress, mu[1], rf, hf)
    force_list_025.append(round(force_025,2))
    force_05 = force(flow_stress, mu[2], rf, hf)
    force_list_05.append(round(force_05,2))

print(force_list_0)

GradeList = zip(force_list_0, force_list_025, force_list_05)
df = pd.DataFrame(data = GradeList,
    columns=['force(N) @ mu = 0', 'force(N) @ mu = 0.25', 'force(N) @ mu = 0.5'])
df = df.set_index([pd.Index(reduction)])
df.index.name='% reduction'
# print(df)

# plt.plot(reduction, force_list_0, label = 'mu = ' + str(mu[0]))
# plt.plot(reduction, force_list_025, label = 'mu = ' + str(mu[1]))
# plt.plot(reduction, force_list_05, label = 'mu = ' + str(mu[2]))
# plt.legend()
# plt.title('Force vs. % Reduction in height curve')
# plt.xlabel('% Reduction in height')
# plt.ylabel('Force (N)')
# plt.show()

Area = 175*(1+((2*0.25*5)/(15)))*math.pi*25

print(Area)
