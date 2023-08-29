from scipy.stats import f_oneway

import numpy as np

a=np.array([14,15,33,21,65])
b=np.array([11,15,35,23,15])
c=np.array([21,5,15,43,15])

f_stat , p_value = f_oneway(a,b,c)

print(p_value)

if p_value < 0.05:
  print("Its a null Hypothesis")
 
else:
   print("Fail to reject the null hypothesis")