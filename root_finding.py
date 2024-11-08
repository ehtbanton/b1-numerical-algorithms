import numpy as np
import scipy as sp
from scipy.optimize import newton
import matplotlib.pyplot as plt

import scipy.optimize as opt
import numpy as np

# Define the function whose root we're trying to find
def func(x):
    return np.sin(x)

# Define the derivative of the function
def fprime(x):
    return np.cos(x)

# Initialize the counter for iterations
iterations = 0

# Define a wrapper to count the number of iterations
def count_calls(x):
    global iterations
    iterations += 1
    print ("Iteration", iterations, "x =", x)
    return func(x)

# Initial guess close to pi
initial_guess = 3.0

# Run the Newton-Raphson method
pi_estimate = opt.newton(count_calls, x0=initial_guess, fprime=fprime, tol=1e-10)

print("Estimated π:", pi_estimate)
print("Actual π:   ", np.pi)
print("Iterations:", iterations)
print("Error:", abs(pi_estimate - np.pi))


def theoretical_error():
    pi_estimate = newton(np.sin, 3.0)
    # Machine epsilon gives us a fundamental limitation
    machine_eps = np.finfo(float).eps
    # For Newton's method, error is related to machine precision
    theoretical_bound = machine_eps * abs(pi_estimate)
    return theoretical_bound

#print(theoretical_error())