# Solar System 3D Orbital Simulator

This project is a Python-based simulation of planetary motion using **Keplerian orbital mechanics**.

It visualizes the Solar System in **3D**, including:
- Elliptical orbits (Sun at one focus)
- Orbital inclinations
- Animated planetary motion

---

## Features

- 3D visualization using `matplotlib`
- Realistic orbital shapes (Kepler's First Law)
- Inclined orbital planes
- Time-based animation
- Scaled astronomical units (AU)

---

## Physics Model

The simulation uses the orbital equation:


r = a(1 - e²) / (1 + e cosθ)


Where:
- `a` = semi-major axis  
- `e` = eccentricity  
- `θ` = true anomaly  

Note: This is a **simplified model** (no gravitational interactions between planets).

---

## Preview

![Simulation](solar_system.gif)

---

## Future Improvements

- N-body simulation
- Real orbital speed (Kepler's Second Law)
- Interactive controls
- Export to video/GIF


## Author

Simone Muscolino
