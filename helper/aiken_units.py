import scipy.constants as u

u.kg = 1
u.m = 1
u.N = 1

u.mm = 1 / 1000 * u.m
u.MPa = u.N / u.mm**2
u.kN = 1000 * u.N
u.J = u.N * u.m
u.kJ = 1000 * u.J

u.ksi = 1000 * u.psi
u.psf = 144 * u.psi
u.ft = 12 * u.inch
