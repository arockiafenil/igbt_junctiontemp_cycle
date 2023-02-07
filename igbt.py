# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:40:14 2022

@author: ICER
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m


dti=0
Q_on=500
Q_off=0
T_cas=50
Tn=np.array([0.0005,0.0049,0.0351,0.0566],dtype=float)
Rn=np.array([0.0059,0.0468,0.0695,0.0965],dtype=float)
t_0=np.arange(0.001,.121,0.001)
t_on=np.arange(0.001,0.011,0.001)
t_off=np.arange(0.001,0.031,0.001)

dt1_on=[0]*len(t_on)

"DeltaT value for Cycle1"
dt1_on = [[0 for x in range(len(t_on))]for y in range(4)]
dt1_off = [[0 for x in range(len(t_off))]for y in range(4)]

for n in range(4):
    for i in range(len(t_on)):
        dti=dt1_off[n][len(t_off)-1]
        dt1_on[n][i]=(dti*m.exp((-t_on[i])/Tn[n]))+(Q_on*Rn[n]*(1-m.exp(-t_on[i]/Tn[n])))
        for j in range(len(t_off)):
            dti=dt1_on[n][len(t_on)-1]
            dt1_off[n][j]=(dti*m.exp((-t_off[j])/Tn[n]))+(Q_off*Rn[n]*(1-m.exp(-t_off[j]/Tn[n])))
            
"DeltaT value for Cycle2"   
dt2_on = [[0 for x in range(len(t_on))]for y in range(4)]
dt2_off = [[0 for x in range(len(t_off))]for y in range(4)] 

for n in range(4):
    dti=dt1_off[n][len(t_off)-1]
    for i in range(len(t_on)):
        dti=dt1_off[n][len(t_off)-1]
        dt2_on[n][i]=(dti*m.exp((-t_on[i])/Tn[n]))+(Q_on*Rn[n]*(1-m.exp(-t_on[i]/Tn[n])))
        for j in range(len(t_off)):
            dti=dt2_on[n][len(t_on)-1]
            dt2_off[n][j]=(dti*m.exp((-t_off[j])/Tn[n]))+(Q_off*Rn[n]*(1-m.exp(-t_off[j]/Tn[n])))       

"DeltaT value for Cycle3"   
dt3_on = [[0 for x in range(len(t_on))]for y in range(4)]
dt3_off = [[0 for x in range(len(t_off))]for y in range(4)] 

for n in range(4):
    dti=dt2_off[n][len(t_off)-1]
    for i in range(len(t_on)):
        dti=dt2_off[n][len(t_off)-1]
        dt3_on[n][i]=(dti*m.exp((-t_on[i])/Tn[n]))+(Q_on*Rn[n]*(1-m.exp(-t_on[i]/Tn[n])))
        for j in range(len(t_off)):
            dti=dt3_on[n][len(t_on)-1]
            dt3_off[n][j]=(dti*m.exp((-t_off[j])/Tn[n]))+(Q_off*Rn[n]*(1-m.exp(-t_off[j]/Tn[n])))  

"Addition of different junction deltaT's at on condition"
dtc1=[0]*len(t_on)
dtc2=[0]*len(t_on)
dtc3=[0]*len(t_on)
for i in range(len(t_on)):
    dtc1[i]=[x[i] for x in dt1_on]
    dtc2[i]=[x[i] for x in dt2_on]
    dtc3[i]=[x[i] for x in dt3_on]
    dtc1=np.asarray(dtc1)
    dtc2=np.asarray(dtc2)
    dtc3=np.asarray(dtc3)
    dtc1[i]=sum(dtc1[i])+T_cas
    dtc2[i]=sum(dtc2[i])+T_cas
    dtc3[i]=sum(dtc3[i])+T_cas
    
"Addition of different junction deltaT's at off condition"
dtcc1=[0]*len(t_off)
dtcc2=[0]*len(t_off)
dtcc3=[0]*len(t_off)
for i in range(len(t_off)):
    dtcc1[i]=[x[i] for x in dt1_off]
    dtcc2[i]=[x[i] for x in dt2_off]
    dtcc3[i]=[x[i] for x in dt3_off]
    dtcc1=np.asarray(dtcc1)
    dtcc2=np.asarray(dtcc2)
    dtcc3=np.asarray(dtcc3)
    dtcc1[i]=sum(dtcc1[i])+T_cas
    dtcc2[i]=sum(dtcc2[i])+T_cas
    dtcc3[i]=sum(dtcc3[i])+T_cas    

"Appending Junction Temperatures"
Tjunc=[0]*len(t_0)
Tjunc=np.append(dtc1,dtcc1)
Tjunc=np.append(Tjunc,dtc2)
Tjunc=np.append(Tjunc,dtcc2)
Tjunc=np.append(Tjunc,dtc3)
Tjunc=np.append(Tjunc,dtcc3)


plt.scatter(t_0, Tjunc, c ="blue")
plt.xlabel('time (sec)')
plt.ylabel("Junction Temperature (C)")
plt.show()
