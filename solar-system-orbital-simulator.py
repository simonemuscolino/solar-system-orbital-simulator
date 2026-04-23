# Solar System 3D Orbital Simulator (Advanced Keplerian Model)
# Author: Simone Muscolino
#
# Description:
# This simulation models planetary motion in 3D using Keplerian orbital elements.
# Features:
# - Elliptical orbits (Sun at one focus)
# - Orbital inclination (true 3D visualization)
# - Animated motion over time
#
# Note:
# This is not an N-body simulation. Planet interactions are neglected.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('TkAgg')


# -----------------------------
# Planet Data: (a, e, inclination in degrees)
# -----------------------------
planet_data = {
    "Mercury": (0.39, 0.205, 7.0),
    "Venus": (0.72, 0.0067, 3.4),
    "Earth": (1.00, 0.0167, 0.0),
    "Mars": (1.52, 0.093, 1.85),
    "Jupiter": (5.20, 0.048, 1.3),
    "Saturn": (9.58, 0.056, 2.5),
    "Uranus": (19.22, 0.047, 0.77),
    "Neptune": (30.05, 0.009, 1.77)
}

# -----------------------------
# Figure Setup
# -----------------------------
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Sun
ax.scatter(0, 0, 0, color='yellow', s=300, label='Sun')

# Store planet objects
planet_points = []
planet_orbits = []

theta_vals = np.linspace(0, 2*np.pi, 500)

# -----------------------------
# Create Orbits
# -----------------------------
for planet, (a, e, inc_deg) in planet_data.items():
    inc = np.radians(inc_deg)

    # Elliptical orbit (Sun at focus)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta_vals))

    x = r * np.cos(theta_vals)
    y = r * np.sin(theta_vals)
    z = np.zeros_like(x)

    # Inclination rotation (around x-axis)
    y_rot = y * np.cos(inc) - z * np.sin(inc)
    z_rot = y * np.sin(inc) + z * np.cos(inc)

    # Plot orbit
    orbit_line, = ax.plot(x, y_rot, z_rot, linewidth=1)
    planet_orbits.append(orbit_line)

    # Planet marker
    point, = ax.plot([], [], [], 'o', label=planet)
    planet_points.append((point, a, e, inc))

# -----------------------------
# Animation Function
# -----------------------------
def update(frame):
    for point, a, e, inc in planet_points:
        theta = frame * (0.02 / a)

        r = (a * (1 - e**2)) / (1 + e * np.cos(theta))

        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = 0

        # Inclination rotation
        y_rot = y * np.cos(inc) - z * np.sin(inc)
        z_rot = y * np.sin(inc) + z * np.cos(inc)


        point.set_data([x], [y_rot])
        point.set_3d_properties([z_rot])

    return [p[0] for p in planet_points]

# -----------------------------
# Plot Settings
# -----------------------------
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
ax.set_zlabel("Z (AU)")
ax.set_title("3D Solar System Simulation (Keplerian Orbits)")

ax.legend(fontsize=8)

# Scale axes
limit = 35
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit/5, limit/5)

# -----------------------------
# Run Animation
# -----------------------------
ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=False)

plt.show()


