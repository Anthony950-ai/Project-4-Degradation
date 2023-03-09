# ODEINT visualization
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import math


xs =np.linspace(0,100,20)

#plot of system representing degradation of data
X1= (-1/50)*xs + (3/100)*xs
X2 = (1/50)*xs + (-3/100)*xs




lam = xs
#plot of degradation found using matrix manipulation for PART1
eigen = -lam**3-((9/50)*lam**2)-(9/1000)*lam-(3/2500)
plt.plot(lam,eigen)
plt.show()

#Part 2 plot of degradation
t =np.linspace(0,1000,1)


xt = -(1/50)*((t-1)/20)*(math.exp(((t-1)/20))-1)*(t-1)+1+(3/100)*((t-1)/20)*(math.exp(((t-1)/20))-1)*(t-1)+1

xT = -(1/50)*((t-1)/20)*(math.exp(((t-1)/20))-1)*(t-1)-1+(3/100)*((t-1)/20)*(math.exp(((t-1)/20))-1)*(t-1)-1

plt.plot(t,xt)
plt.plot(t,xT)
plt.show()
