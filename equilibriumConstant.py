"""
equilibriumConstant.py
Ashley Ung
This program solves an equilibrium constant problem.
The value of equilibrium constant is fixed for a particular reaction at standard condition which is usually at 25 degree celsius and 1 atm pressure. The equilibrium constant is only dependent on the reaction stoichiometry and not on the temperature or pressure.
"""

from chempy import Equilibrium

# The equilibrium constant expression
equilibrium = Equilibrium ({'NH3': 1, 'H2O': 1}, {'NH4+': 1, 'OH-': 1}, {'H+': 1, 'e-': 1})

# Equilibrium constant calculation 
K = equilibrium.K()

# Print the equilibrium constant
print ("Equilibrium constant at standard conditions:", K)
