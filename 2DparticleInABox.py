"""
2DparticleInABox.py
Ashley Ung 
A two-dimensional "particle in a box" problem describes the behavior of a particle confined to a finite region in a two-dimensional space. The solutions to this problem can be used to model a variety of physical systems, such as electrons in a semiconductor or atoms in a small molecule.
This program solves the "particle in a box" problem for a two-dimensional box. 
This program can be modified accordinly to a problem's requirments. 
"""

import numpy as np

# Define the parameters of the problem
xBoxLength = 1 # length of the box in x-direction in nm
yBoxLength = 2 # length of the box in y-direction in nm
particleMass = 1 # mass of the particle in kg
hbar = 1 # reduced Planck's constant in J*s

# The energy for the nx-th and ny-th energy level
def nthEnergy (nx, ny):
    return (nx**2 * np.pi**2 * hbar**2)/(2 * particleMass * xBoxLength**2) + (ny**2 * np.pi**2 * hbar**2)/(2 * particleMass * yBoxLength**2)

# The wave function for the nx-th and ny-th energy level
def psi (x, y, nx, ny):
    return np.sqrt (2/xBoxLength)*np.sqrt (2/yBoxLength)*np.sin (nx*np.pi*x/xBoxLength)*np.sin (ny*np.pi*y/yBoxLength)


# Find the energy for the first 3 energy levels
for nx in range (1, 4):
    for ny in range (1, 4):
        En = nthEnergy (nx, ny)
        print ("Energy level (",nx,",",ny,"):", nthEnergy, "J")
        
