import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate pi using polygon approximation
def calculate_pi_polygon(n_sides):
    # Radius of the circle
    r = 1.0

    # Inscribed polygon side length
    inscribed_side = 2 * r * np.sin(np.pi / n_sides)
    inscribed_perimeter = n_sides * inscribed_side
    pi_inscribed = inscribed_perimeter / (2 * r)

    # Circumscribed polygon side length
    circumscribed_side = 2 * r * np.tan(np.pi / n_sides)
    circumscribed_perimeter = n_sides * circumscribed_side
    pi_circumscribed = circumscribed_perimeter / (2 * r)

    # Average of inscribed and circumscribed polygon pi estimations
    pi_estimate = (pi_inscribed + pi_circumscribed) / 2
    return pi_estimate, pi_inscribed, pi_circumscribed