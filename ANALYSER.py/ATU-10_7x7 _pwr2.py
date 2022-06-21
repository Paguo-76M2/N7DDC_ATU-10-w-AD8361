#!/usr/bin/env python3

# Aleksander Alekseev (c)
# David Fainitski (c)
# some tweaks by Paguo-76M2

import numpy as np
from math import pi
from matplotlib import pyplot as pp
from smithplot import SmithAxes

# High-pass T
#  ┌──ZC1──┬──ZC2──>
# Za      ZL1       <─┐
#  └───────┴───────> ZhpT
# to be implemented
def ZhpT(freq, Za, L1, C1, C2):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    C2 = C2/1000/1000/1000/1000
    L1 = L1/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZC2 = 1/(1j*omega*C2)
    ZL1 = 1j*omega*L1

    Z1 = Za + ZC1
    return ZC2+(Z1*ZL1/(Z1+ZL1))

# Low-pass T
#  ┌──ZL1──┬──ZL2──>
# Za      ZC1       <─┐
#  └───────┴───────> ZlpT
# to be implemented
def ZlpT(freq, Za, L1, L2, C1):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    L1 = L1/1000/1000
    L2 = L2/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZL1 = 1j*omega*L1
    ZL2 = 1j*omega*L2

    Z1 = Za + ZL1
    return ZL2+(Z1*ZC1/(Z1+ZC1))

# High-pass L Step down
#  ┌──ZC1──┬───>
# Za      ZL1   <─┐
#  └───────┴───> ZhpLsd
# Green on the graph
def ZhpLsd(freq, Za, L1, C1):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    L1 = L1/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZL1 = 1j*omega*L1

    Z1 = Za + ZC1
    return Z1*ZL1/(Z1+ZL1)

# High-pass L Step up
#  ┌───┬──ZC1──>
# Za  ZL1       <─┐
#  └───┴───────> ZhpLsu
# Magenta on the graph
def ZhpLsu(freq, Za, L1, C1):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    L1 = L1/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZL1 = 1j*omega*L1

    Z1 = Za*ZL1/(Za+ZL1)
    return Z1 + ZC1

# Low-pass L Step down
#  ┌──ZL1──┬───>
# Za      ZC1   <─┐
#  └───────┴───> ZlpLsd
# Blue on the graph
def ZlpLsd(freq, Za, L1, C1):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    L1 = L1/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZL1 = 1j*omega*L1

    Z1 = Za + ZL1
    return Z1*ZC1/(Z1+ZC1)

# Low-pass L Step up
#  ┌───┬──ZL1──>
# Za  ZC1       <─┐
#  └───┴───────> ZlpLsu
# Red on the graph
def ZlpLsu(freq, Za, L1, C1):
    omega = 2*pi*freq
    C1 = C1/1000/1000/1000/1000
    L1 = L1/1000/1000
    ZC1 = 1/(1j*omega*C1)
    ZL1 = 1j*omega*L1

    Z1 = Za*ZC1/(Za+ZC1)
    return Z1 + ZL1

# permit apparent SWRs up to 1.25
za_min = 40
za_max = 61
za_step = 1

# Elecraft QRP
#c = [10, 20, 39, 82, 160, 330, 660] # C array, pF
#l = [0.05, 0.11, 0.22, 0.45, 0.95, 1.9, 3.8] # L array, uH
# ATU-10
#c = [22, 47, 100, 220, 470, 1000, 2220] # C array, pF
#l = [0.1, 0.22, 0.45, 1.0, 2.2, 4.5, 10.0] # L array, uH
# ATU-100
#c = [10, 22, 47, 100, 220, 470, 1000] # C array, pF
#l = [0.05, 0.1, 0.22, 0.45, 1.0, 2.2, 4.4] # L array, uH
# Perfect "powers of two" for L-types
c = [10, 20, 40, 80, 160, 320, 640] # C array, pF
l = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2] # L array, uH
# Perfect "powers of two" for T-type
#c = [10, 20, 40, 80, 160, 320, 640] # C array, pF; C2 = (1270.02-C1)
#c = [5, 10, 20, 40, 80, 160, 320] # C array, pF; C2 = (635.02-C1)
#l = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4] # L array, uH; L2 = (12.72-L1)


c_list = [0.01]
l_list = [0.01]
for i in range(0, len(c)):
    for x in range(0, len(c_list)):
        c_list += [c[i] + c_list[x]]

for i in range(0, len(l)):
    for x in range(0, len(l_list)):
        l_list += [l[i] + l_list[x]]

f_list = [1.820, 3.540, 7.020, 14.1, 18.1, 21.4, 24.9, 28.3]

for f in f_list:
    freq = int(f*1000000)
    print("freq = {}".format(freq))
    pp.figure(figsize=(6, 6))
    ax = pp.subplot(1, 1, 1, projection = 'smith')
    ax.update_scParams(axes_impedance = 50)
    imp_list1 = []  # Low pass L Step down impedances
    imp_list2 = []  # Low pass L Step up impedances
    imp_list3 = []  # High pass L Step down impedances
    imp_list4 = []  # High pass L Step up impedances
    imp_list5 = []  # Low pass T
    imp_list6 = []  # High pass T
    for C1 in c_list:      
        for L1 in l_list:
            for Za in np.arange(za_min, za_max, za_step):
#                imp = ZlpLsd(freq, Za, L1, C1)
#                imp_list1 += [imp]
#                imp = ZlpLsu(freq, Za, L1, C1)
#                imp_list2 += [imp]
                imp = ZhpLsd(freq, Za, L1, C1)
                imp_list3 += [imp]
                imp = ZhpLsu(freq, Za, L1, C1)
                imp_list4 += [imp]
#                imp = ZlpT(freq, Za, L1, (12.72-L1), C1)
#                imp_list5 += [imp]
# select a better capacitance range for T-types
#                imp = ZhpT(freq, Za, L1, C1, (1270.02-C1))
#                imp = ZhpT(freq, Za, L1, C1, (635.02-C1))
#                imp_list6 += [imp]
#    pp.plot(np.array(imp_list1), color='blue', linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')
#    pp.plot(np.array(imp_list2), color='red',  linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')
    pp.plot(np.array(imp_list3), color='blue', linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')
    pp.plot(np.array(imp_list4), color='red',  linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')
#    pp.plot(np.array(imp_list5), color='blue',  linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')
#    pp.plot(np.array(imp_list6), color='red',  linestyle='', marker='o', markersize=2, alpha=0.2, datatype='Z')

#    pp.savefig('./Test_result/Low_pass-L-pwr2-{}.png'.format(freq))
    pp.savefig('./Test_result/High_pass-L-pwr2-{}.png'.format(freq))
#    pp.savefig('./Test_result/Low_pass-T-pwr2-{}.png'.format(freq))
#    pp.savefig('./Test_result/High_pass-custom_T-pwr2-{}.png'.format(freq))
