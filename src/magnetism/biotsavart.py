from enthought.mayavi.mlab import orientation_axes, plot3d, quiver3d, show
from numpy import array, cross, linspace, meshgrid
from scipy.constants.constants import mu_0, pi


def bfield():
    x = linspace(0, 2*np.pi, 15)
    rho = linspace(1, 2.5, 3)
    rhogrid, phigrid = meshgrid(rho, phi)
    x = rhogrid * np.cos(phigrid)
    y = rhogrid * np.sin(phigrid)
    z = np.zeros_like(x)
    #  phihat = -sin(phi)*xhat + cos(phi)*yhat = -y/rho*xhat + x/rho*yhat
    #  Be careful when you divide by zero as the eps graphic will be corrupted
    u = -y / rhogrid; u[np.isnan(u)] = 0
    v =  x / rhogrid; v[np.isnan(v)] = 0
    w = np.zeros_like(z)
    obj = quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=0.3)
#    outline()
    return obj

def biot_savart(source):
    x, y, z = numpy.mgrid[-2:3, -2:3, -2:3]
#    dr = 
    obj = plot3d(x, y, z, color=(0.1, 0.1, 1))#, tube_radius=0.1, opacity=0.5)
    return obj
    
def line(pt1, pt2, tmin, tmax, numpts=30):
    t = linspace(tmin, tmax, numpts)
    x = pt1[0] + (pt2[0] - pt1[0]) * t
    y = pt1[1] + (pt2[1] - pt1[1]) * t
    z = pt1[2] + (pt2[2] - pt1[2]) * t
    obj = plot3d(x, y, z, color=(0.1, 0.1, 1))
    return (x, y, z)

if __name__ == '__main__':
##    bfield()
    pt1 = array([-1, 0, 1], dtype=float)
    pt2 = array([2, 0, 1], dtype=float)
    linecharge = line(pt1, pt2, 0, 1)
    biot_savart(linecharge)
#    axes()

#    title('Free Electron Gas On a Ring')
    orientation_axes()
#    savefig('temp.eps')
    show()