import numpy as np
import matplotlib.pyplot as plt
# Note: mpl_toolkits.mplot3d is required for projection='3d'
# It's typically included with matplotlib installations.
from mpl_toolkits.mplot3d import Axes3D

# --- Lorenz System Definition ---
def lorenz(x, y, z, s=10, r=28, b=8/3):
    """
    Calculate the time derivatives of the Lorenz system.

    Args:
        x, y, z: Current state variables.
        s, r, b: System parameters (sigma, rho, beta). Default values
                 are the classic ones known to produce chaotic behavior.

    Returns:
        Tuple containing (dx/dt, dy/dt, dz/dt).
    """
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot

# --- Simulation Parameters ---
dt = 0.01  # Time step for numerical integration
num_steps = 10000  # Number of steps to simulate

# --- Initial Conditions ---
# Small changes in initial conditions lead to vastly different trajectories (Butterfly Effect)
x0, y0, z0 = (0., 1., 1.05)

# --- Simulation ---
# Initialize arrays to store the trajectory
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set the initial state
xs[0], ys[0], zs[0] = (x0, y0, z0)

# Perform numerical integration using the simple Euler method
print(f"Simulating Lorenz system for {num_steps} steps with dt={dt}...")
for i in range(num_steps):
    # Get derivatives at the current state
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    # Update state using Euler method: state_new = state_old + derivative * dt
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
print("Simulation complete.")

# --- Visualization ---
print("Generating 3D plot...")
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the trajectory
ax.plot(xs, ys, zs, lw=0.7, color='magenta') # Use a thinner line for clarity

# Add starting point marker
ax.scatter(xs[0], ys[0], zs[0], color='green', marker='o', s=60, label='Start Point')

# Improve plot aesthetics
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor: Visualizing Deterministic Chaos")
ax.legend()
ax.grid(True)

# Provide context
print("\n--- Lorenz Attractor Simulation ---")
print("This simulation demonstrates the Lorenz system, a classic example of deterministic chaos.")
print("Observe the intricate 'butterfly' pattern traced by the system's state over time.")
print("Key takeaway: Simple, deterministic rules (the Lorenz equations) can lead to complex,")
print("non-repeating, and highly sensitive behavior (chaos). A tiny change in the starting")
print("point would result in a completely different trajectory over time - the 'Butterfly Effect'.")
print("This discovery fundamentally changed our understanding of predictability in fields like")
print("weather forecasting, physics, biology, and economics.")

plt.show()

print("\nPlot displayed. Close the plot window to exit.")
