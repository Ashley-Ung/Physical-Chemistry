"""
1DparticleInABox.py
Ashley Ung 
A "particle in a box" is a studied in quantum mechanics and it describes the behavior of a particle confined to a finite region in space (the "box"). The solutions to this problem can be used to model a variety of physical systems, such as electrons in a semiconductor or atoms in a small molecule.
This program solves the "particle in a box" problem for a one-dimensional box. This program defines the wave function and energy for the n-th energy level of the particle in a box. A "for loop" will then find the normalized wave function and energy for the first 3 energy levels. The quad function from scipy.integrate is used to evaluate the integral of the square of the wave function over the length of the box to obtain the normalization constant.
This program can be modified accordinly to a problem's requirments. 
"""

import numpy as np
from scipy.integrate import quad

# Define the parameters of the problem
boxLength = 1 # length of the box in nm
particleMass = 1 # mass of the particle in kg
hbar = 1 # reduced Planck's constant in J*s

# Define the energy for the nth energy level
def nthEnergy (n):
    return (n**2 * np.pi**2 * hbar**2)/(2 * particleMass * boxLength**2)

# Define the wave function for the n-th energy level
def psi (x, n):
    return np.sqrt (2/boxLength)*np.sin (n*np.pi*x/boxLength)

# Find the normalized wave function and energy for the first 3 energy levels
for n in range (1, 4):
    norm_constant, _ = quad (lambda x: psi (x, n)**2, 0, boxLength)
    psi_n = lambda x: psi (x, n)/np.sqrt (norm_constant)
    En = nthEnergy (n)
    print ("Energy level", n, ":", En, "J")
    # specific value of x
    x = 0.5 
    print ("Normalized wave function at x =",x,":", psi_n (x))
