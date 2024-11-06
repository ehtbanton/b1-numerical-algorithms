import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(n_points):
    points_inside_circle = 0
    for _ in range(n_points):
        x, y = np.random.rand(), np.random.rand() # Generate random points
        if x**2 + y**2 <= 1: # Check if the point is inside the circle
            points_inside_circle += 1
    pi_estimate = 4 * points_inside_circle / n_points
    return pi_estimate

def visualize_monte_carlo_pi(n_points=1000):
    # Generate random points in the unit square
    x_points = np.random.rand(n_points)
    y_points = np.random.rand(n_points)

    # Determine if points are inside the quarter circle
    inside_circle = x_points**2 + y_points**2 <= 1
    outside_circle = ~inside_circle

    # Estimate π based on points inside the circle
    pi_estimate = 4 * np.sum(inside_circle) / n_points

    # Plot the points
    plt.figure(figsize=(8, 8))
    plt.scatter(x_points[inside_circle], y_points[inside_circle], color='blue', s=1, label='Inside Circle')
    plt.scatter(x_points[outside_circle], y_points[outside_circle], color='red', s=1, label='Outside Circle')
    
    # Plot the quarter circle boundary
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2, linestyle='--', label='Quarter Circle')
    plt.gca().add_patch(circle)

    # Plot configuration
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Monte Carlo Estimation of π with {n_points} Points\nEstimated π ≈ {pi_estimate:.5f}")
    plt.legend()
    plt.show()

def plot_convergence(max_points=1000000, step=10000):
    n_points_list = range(step, max_points + 1, step)
    pi_estimates = [monte_carlo_pi(n) for n in n_points_list]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_points_list, pi_estimates, label='Estimated π')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='True π')
    plt.xlabel('Number of Random Points')
    plt.ylabel('Estimated π')
    plt.title('Convergence of Monte Carlo π Estimate')
    plt.legend()
    plt.show()

# Example usage
# visualize_monte_carlo_pi(1000)

plot_convergence()