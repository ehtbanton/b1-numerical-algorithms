import numpy as np

def monte_carlo_pi(n_points):
    points_inside_circle = 0
    for _ in range(n_points):
        x, y = np.random.rand(), np.random.rand() # Generate random points
        if x**2 + y**2 <= 1: # Check if the point is inside the circle
            points_inside_circle += 1
    pi_estimate = 4 * points_inside_circle / n_points
    return pi_estimate

print (monte_carlo_pi(1000000))