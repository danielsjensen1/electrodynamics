from math import degrees, pi, sqrt
from scipy.constants.constants import e, epsilon_0, m_e


k = 1 / (4 * pi * epsilon_0)
def prob03(q1=-4e-6, x1=(4e0, -2e0), q2=12e-6, x2=(1e0, 2e0), x3=(-1e0, 0e0)):
    pass

def prob05(E=10e4, d=.06):
    v = sqrt(2 * e * E / m_e * d)
    print('v = {0:.5e}'.format(v))

def prob07(r=.028, sigma=3.5e-6, d2=5e0):
    E = sigma / (2e0 * epsilon_0)
    print('(E near) = {0:.5e}'.format(E))
    E = sigma * r**2 / (4 * epsilon_0 * d2**2)
    print('(E far) = {0:.5e}'.format(E))

def prob08(sigma=3.4e-6):
    E = sigma / epsilon_0
    print('E = {0:.5e}'.format(E))

def prob09(x0=.027, lam=6e-9):
    Q = 2 * lam * x0
    print('Q = {0:.5e} nC'.format(Q*1e9))
    def Ey(y0):
        return k * lam * 2 * x0 / (y0 * sqrt(x0**2 + y0**2))
    print('Ey(4 cm) = {0:.5e} N/C'.format(Ey(0.04)))
    print('Ey(12 cm) = {0:.5e} N/C'.format(Ey(0.12)))

if __name__ == '__main__':
    prob05()
    prob07()
    prob08()
    prob09()