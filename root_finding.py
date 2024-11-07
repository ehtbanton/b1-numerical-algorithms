import numpy as np
import scipy as sp
from scipy.optimize import newton

def pi_root_estimate():
    # The root of sin(x) near 3 is π
    return newton(np.sin, 3.0)

print("Root finding estimate of π:", pi_root_estimate())