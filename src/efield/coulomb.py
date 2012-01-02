from itertools import chain, repeat
from numpy import array, isnan, mgrid, pi, sqrt, zeros_like
from enthought.mayavi import mlab


def efield(name, sources, grid):
#~ def efield():
    X, Y, Z = grid
    Ex, Ey, Ez = (zeros_like(X), zeros_like(Y), zeros_like(Z))
    for source in sources:
        (Xp, Yp, Zp), q = source
        if q < 0e0:
            color = (0,0,1)
        else:
            color = (1,0,0)
        mlab.points3d(Xp, Yp, Zp, color=color, scale_factor=q)
        Xs, Ys, Zs = (X - Xp, Y - Yp, Z - Zp)
        rminus3half = (Xs*Xs + Ys*Ys + Zs*Zs)**(-1.5e0)
        #~ rminus3half[isnan(rminus3half)] = 0
        Ex += q * rminus3half * Xs
        Ey += q * rminus3half * Ys
        Ez += q * rminus3half * Zs
        
    #  Run isnan on the data after adding all of the field contributions
    Xs[isnan(Xs)] = 0
    Ys[isnan(Ys)] = 0
    Zs[isnan(Zs)] = 0
    mlab.quiver3d(X, Y, Z, Ex, Ey, Ez, line_width=2, scale_factor=1)
    mlab.show()
    #~ mlab.savefig(name + '.mv2')

def plane(z=0e0, charge=10e0):
    numpts = 9e0
    q = charge / numpts
    sources = (((x, y, z), q) for x in range(-3, 4) for y in range(-3, 4))
    grid = mgrid[-5:5:10j, -5:5:10j, -5:5:10j]
    efield('plane', sources, grid)

def plane(z=0e0, dz=2e0, charge=10e0):
    numpts = 9e0
    q = charge / numpts
    top = (((x, y, z + dz), q) for x in range(-3, 4) for y in range(-3, 4))
    bottom (((x, y, z - dz), -q) for x in range(-3, 4) for y in range(-3, 4))
    sources = chain(top, bottom)
    grid = mgrid[-5:5:10j, -5:5:10j, -5:5:10j]
    efield('capacitor', sources, grid)
    
if __name__ == '__main__':
    #~ sources = (((-2,0,0), -1), ((2,0,0), 1))
    #~ sources = (((-2,0,0), 1), ((-1,0,0), 1), ((0,0,0), 1), ((1,0,0), 1),
               #~ ((2,0,0), 1))
    #~ grid = mgrid[-5:5:10j, -5:5:10j, -5:5:10j]
    #~ efield('dipole', sources, grid)
    #~ plane()
    capacitor()
