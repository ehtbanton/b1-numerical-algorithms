import numpy as np
import scipy as sp
from scipy.optimize import newton
import matplotlib.pyplot as plt

def pi_root_estimate():
    # The root of sin(x) near 3 is π
    return newton(np.sin, 3.0)



def theoretical_error():
    pi_estimate = newton(np.sin, 3.0)
    # Machine epsilon gives us a fundamental limitation
    machine_eps = np.finfo(float).eps
    # For Newton's method, error is related to machine precision
    theoretical_bound = machine_eps * abs(pi_estimate)
    return theoretical_bound

print(theoretical_error())