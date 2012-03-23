from numpy import cos, linspace, pi, sin
from enthought.mayavi.mlab import plot3d, show

def solenoid(N=10, L=5e0, R=1e0, numpts=1000):
    """Generates a solenoid."""
    z = linspace(0, L, numpts)
    theta = 2 * pi * N / L * z
    x = R * cos(theta)
    y = R * sin(theta)
    l = plot3d(x, y, z, tube_radius=0.025, colormap='Spectral')
    return l

if __name__ == '__main__':
    solenoid()
    show()