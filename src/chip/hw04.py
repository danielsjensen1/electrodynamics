from math import degrees, pi, sqrt
from scipy.constants.constants import e, epsilon_0, m_e


k = 1 / (4 * pi * epsilon_0)
def prob01(R=0.11, rho=445e-9):
    Q = rho * 4 / 3e0 * pi * R**3
    print('Q = {0:.5e} nC'.format(Q*1e9))
    r = 0.02
    E = rho * r / (3 * epsilon_0)
    print('E(r=2cm) = {0:.5e}'.format(E))
    r = 0.15
    E = Q / (4 * pi * epsilon_0 * r**2)
    print('E(r=15cm) = {0:.5e}'.format(E))



if __name__ == '__main__':
    prob01()
#    prob02()
#    prob03()
#    prob04()
#    prob05()
#    prob06()