from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

x = np.array([0,1120,1523,2102,2230,2600,3200,3409,3689,4460])
y = np.array([0,112,345,198,305,372,550,302,420,578])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

# To get coefficient of determination (r_squared)

plt.scatter(x,y)
plt.plot(x,x*slope+intercept,'r')
plt.show()