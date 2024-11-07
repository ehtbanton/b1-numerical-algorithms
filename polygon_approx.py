import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def calculate_pi_polygon(n_sides):
    """Calculate pi approximation using inscribed and circumscribed polygons."""
    r = 1.0
    
    # Inscribed polygon calculation
    inscribed_side = 2 * r * np.sin(np.pi / n_sides)
    inscribed_perimeter = n_sides * inscribed_side
    pi_inscribed = inscribed_perimeter / (2 * r)
    
    # Circumscribed polygon calculation
    circumscribed_side = 2 * r * np.tan(np.pi / n_sides)
    circumscribed_perimeter = n_sides * circumscribed_side
    pi_circumscribed = circumscribed_perimeter / (2 * r)
    
    return (pi_inscribed + pi_circumscribed) / 2, pi_inscribed, pi_circumscribed

# Set style for better-looking output
# plt.style.use('seaborn')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Create static elements
circle = plt.Circle((0, 0), 1, color='lightblue', alpha=0.3, zorder=1)
ax.add_patch(circle)
text_pi = ax.text(-1.4, 1.3, '', fontsize=10)
text_sides = ax.text(-1.4, 1.1, '', fontsize=10)
ax.grid(True, alpha=0.3)

# Create line objects for polygons
theta = np.linspace(0, 2*np.pi, 1000, endpoint=False)
inscribed_line, = ax.plot([], [], 'b-', label='Inscribed', lw=1.5, zorder=2)
circumscribed_line, = ax.plot([], [], 'r-', label='Circumscribed', lw=1.5, zorder=2)
ax.legend(loc='upper right')

def init():
    """Initialize animation."""
    inscribed_line.set_data([], [])
    circumscribed_line.set_data([], [])
    text_pi.set_text('')
    text_sides.set_text('')
    return inscribed_line, circumscribed_line, text_pi, text_sides

def update(frame):
    """Update animation frame."""
    n_sides = frame
    
    # Calculate pi approximation
    pi_estimate, pi_inscribed, pi_circumscribed = calculate_pi_polygon(n_sides)
    
    # Generate polygon vertices
    theta = np.linspace(0, 2*np.pi, n_sides + 1)
    
    # Update inscribed polygon
    inscribed_x = np.cos(theta)
    inscribed_y = np.sin(theta)
    inscribed_line.set_data(inscribed_x, inscribed_y)
    
    # Update circumscribed polygon
    scale = 1 / np.cos(np.pi / n_sides)  # Scale factor for circumscribed polygon
    circumscribed_x = np.cos(theta) * scale
    circumscribed_y = np.sin(theta) * scale
    circumscribed_line.set_data(circumscribed_x, circumscribed_y)
    
    # Update text
    text_pi.set_text(f'π ≈ {pi_estimate:.8f}\nTrue π ≈ {np.pi:.8f}\nError: {abs(pi_estimate - np.pi):.8f}')
    text_sides.set_text(f'Number of sides: {n_sides}')
    
    # Add progress indicator during saving
    if hasattr(update, 'pct'):
        update.pct = frame / (n_frames + 1) * 100
        print(f'Saving animation: {update.pct:.1f}%', end='\r')
    
    return inscribed_line, circumscribed_line, text_pi, text_sides

# Create animation
n_frames = 100
ani = FuncAnimation(
    fig, 
    update,
    frames=range(3, n_frames + 1),
    init_func=init,
    blit=True,
    interval=100,
    repeat=False
)

plt.title('Estimating π using Inscribed and Circumscribed Polygons')

# Save animation as GIF
print("Saving animation as GIF...")
update.pct = 0
writer = PillowWriter(fps=5)
ani.save('pi_approximation.gif', writer=writer)
print("\nAnimation saved as 'pi_approximation.gif'")

# Display the animation in the notebook/window
plt.show()