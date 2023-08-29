from scipy.stats import ttest_ind

import numpy as np

a=np.array([14,15,33,21,65])
b=np.array([11,15,35,23,15])

t_stat , p_value = ttest_ind(a,b)

print(p_value)

if p_value < 0.05:
  print("Its a null Hypothesis")
 
else:
   print("Fail to reject the null hypothesis")