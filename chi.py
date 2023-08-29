from scipy.stats import chi2_contingency
import numpy as np
a=np.array([[14,15],[21,65]])
chi2_stat,p_value,dof,expected=chi2_contingency(a)
print(p_value)
if p_value < 0.05:
  print("reject the null hypothesis: There is a significant association between variables")
else:
   print("Fail to reject the null hypothesis")