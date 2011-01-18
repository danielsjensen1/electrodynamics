from math import degrees, pi, sqrt
from scipy.constants.constants import e, epsilon_0, m_e


k = 1 / (4 * pi * epsilon_0)
def prob01(E0=350e0, x0=0.1, r=0.06):
    phiE = E0 * pi * r**2
    print('phiE = {0:.5e}'.format(phiE))
    phiE_tot = 2 * phiE
    print('phiE_tot = {0:.5e}'.format(phiE_tot))
    Qenc = epsilon_0 * phiE_tot
    print('Qenc = {0:.5e}'.format(Qenc))

def prob02(phi=7.9e3):
    Q = epsilon_0 * phi
    print('Q = {0:.5e} nC'.format(Q * 1e9))

def prob03(q=5e-6, r=0.5):
    SA = 4 * pi * r**2
    print('SA = {0:.5e} m^2'.format(SA))
    E0 = q / (4 * pi * epsilon_0 * r**2)
    print('E0 = {0:.5e}'.format(E0))
    phi = q / epsilon_0
    print('phi = {0:.5e}'.format(phi))

def prob04(q=17e-6, l=0.4):
    phi = q / (6 * epsilon_0)
    print('phi = {0:.5e}'.format(phi))

def prob05(r=0.06, sigma=15e-9):
    Q = sigma * 4 * pi * r**2
    print('Q = {0:.5e} nC'.format(Q*1e9))

def prob06(R=0.06, sigma=15e-9):
    def E(r):
        return sigma / epsilon_0 * (R / r)**2
    print('E = {0:.5e}'.format(E(.061)))
    print('E = {0:.5e}'.format(E(.17)))

if __name__ == '__main__':
    prob01()
    prob02()
    prob03()
    prob04()
    prob05()
    prob06()