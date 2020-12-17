# Code for solving 2nd order ODEs via Runge-Kutta 4th order method

import numpy as np

def runge_kutta_step(dydt, y, t, h):

    k1 = dydt(y, t)
    
    k2 = dydt(y + h*(k1/2), t + h/2)

    k3 = dydt(y + h*(k2/2), t + h/2)

    k4 = dydt(y + h*k3, t + h)

    return (y + (1/6) * h * (k1 + 2*k2 + 2*k3 + k4), t + h)




