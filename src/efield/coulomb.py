from numpy import isnan, mgrid, pi, sqrt
from enthought.mayavi import mlab


def efield(sources, grid):
#~ def efield():
    X, Y, Z = mgrid[-5:5:10j, -5:5:10j, -5:5:10j]
    for source in sources:
        position, charge = source
        mlab.points3d([0e0], [0e0], [0e0], colormap="Reds", scale_factor=.25)
        rminus3half = (X*X + Y*Y + Z*Z)**(-1.5)
        rminus3half[isnan(rminus3half)] = 0
        Ex, Ey, Ez = rminus3half * (X, Y, Z)
    #  Run isnan on the data after adding all of the field contributions
    mlab.quiver3d(X, Y, Z, Ex, Ey, Ez, line_width=2, scale_factor=2)
    mlab.show()
    
if __name__ == '__main__':
    sources = ((array([0,0,0]), 1),)
    efield()
