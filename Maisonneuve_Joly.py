"""
TD5
Gabriel Maisonneuve
Samuel Joly   
"""

# packages calcul numérique 
import scipy as sp
import numpy as np

#package graphique
from matplotlib import pyplot as plt
import math

# constante physique
h = 6.626E-34;
k = 1.38E-23;
e = 1.602E-19; # charge electron
mo = 9.11E-31; # masse electron Kg

L = 10; # longueur barreaux cm
A = 0.25; # section transversale barreaux en cm^2

# Resistance des semi 
# 300K
R1_300 = 9E6;
R2_300 = 1.31E3;
R3_300 = 283.7E6;
# 400K
R1_400 = 20.8E3;
R2_400 = 22.54;
R3_400 = 6.92E6;

Nd = 1E8; # 1/cm^3
Na = 1E14; # 1/cm^3
# masse effective
# electron
me_ge = 0.57;
me_si = 1.08;
me_gaas = 0.063;
#trou
me_ge_trou = 0.37;
me_si_trou = 0.59;
me_gaas_trou = 0.43;
# Mobilite
# electron
mo_ge = 3900;
mo_si = 1400;
mo_gaas = 8800;
#trou
mo_ge_trou = 1900;
mo_si_trou = 450;
mo_gaas_trou = 400;

# print("{:.4e}".format(x))
#"{:.3f}".format(semi1)
# ********** Question 1 **********
# ***** 1a) *****
print("")
print("1a)")
print("400K est la température la plus propice à la domination des porteurs intrinsèques car le graphique démontre qu'il y ait de meilleurs chances que le semi-conducteur soit dans une zone intrinsèque si la température est plus élevée.")

# ***** 1b) *****
print("")
print("1b)")
semi1 = L/(e*A*R1_400);
semi2 = L/(e*A*R2_400);
semi3 = L/(e*A*R3_400);
print("Semi I ‐ ni x mu   = ","{:.4e}".format(semi1), "(cmVsec)^-1")  
print("Semi II ‐ ni x mu  = ","{:.4e}".format(semi2), "(cmVsec)^-1")
print("Semi III ‐ ni x mu = ","{:.4e}".format(semi3), "(cmVsec)^-1")

# ***** 1c) *****
print("")
print("1c)")
mu_ge = mo_ge + mo_ge_trou;
mu_si = mo_si + mo_si_trou;
mu_ga = mo_gaas + mo_gaas_trou;

# semi 1
semi1_test1 = semi1/mu_ge;
semi1_test2 = semi1/mu_si; # cette valeur correspond au graphique donc semi1 = Silicium
semi1_test3 = semi1/mu_ga;


# semi 2
semi2_test1 = semi2/mu_ge; # cette valeur correspond au graphique donc semi2 = Germanium
semi2_test2 = semi2/mu_si;
semi2_test3 = semi2/mu_ga;


# semi 3
semi3_test1 = semi3/mu_ge;
semi3_test2 = semi3/mu_si;
semi3_test3 = semi3/mu_ga; # cette valeur correspond au graphique donc semi3 = Gallium


print("Semi I   = Si")
print("Semi II  = Ge")
print("Semi III = GaAs")
print("Nous avons estimé les ordres de grandeurs des ni des différents semiconducteur afin de trouver un ordre de grandeur approximatif.")
print("Nous avons ensuite identifié la nature des semi conducteur avec ces résultats.")

# ********** Question 2 **********
# ***** 2a) *****
print("")
print("2a)")

semi1_300 = L/(e*A*R1_300);
semi2_300 = L/(e*A*R2_300);
semi3_300 = L/(e*A*R3_300);

# test pour determiner quel materiau est non dopé
# si le ni est pareil a la valeur sur le graphique, le materiau est non dope
# valeurs sur le graphique sont les valeur non dopé car T = 300K
test_ge = semi2_300/mu_ge;
test_si = semi1_300/mu_si;
test_ga = semi3_300/mu_ga;
print("test dopage")
print("si","{:.4e}".format(test_si)) # pas dope car égal a la valeur théorique
print("Ge","{:.4e}".format(test_ge)) # dope car ne correspond pas a la valeur theorique
print("Ga","{:.4e}".format(test_ga)) # dope car ne correspond pas a la valeur theorique
print("La valeur de ni du silicium est la meme dans nos calculs et dans le graphique donc il n'est pas dopé")

# Calculs avec hyphotèse que les semi-conducteurs sont dopés N
R2N = L/(e*Nd*A*mo_ge)         
R3N = L/(e*Nd*A*mo_gaas)    
print("test dopage N")
print("R Ge","{:.4e}".format(R2N),"ohms")
print("R Ga","{:.4e}".format(R3N),"ohms") 
print("La valeur de la résistance du gallium calculé ci-dessus concorde avec la valeur de la résistance du semi-conducteur 3 dans l'énoncé")
print("Cela prouve que le gallium est dopé N")

# Calcul pour le dernier semiconducteur qui sera dopé P
R2P =  L/(e*Na*A*mo_ge_trou)
print("test dopage P")
print("R Ge","{:.4e}".format(R2P),"ohms")
print("La valeur de la résistance du germanium calculé ci-dessus concorde avec la valeur de la résistance du semi-conducteur 2 dans l'énoncé")
print("Cela prouve que le germanium est dopé P")
print("Le calcul de la résistance confirme que le gallium (2e semi-conducteur) est dopé P")

# ***** 2b) *****
print("")
print("2b)")
# calcul Nc
Nc_semi1 = (2*(mo*2*math.pi*me_si*k*300)**(3/2))/(h**3)
Nc_semi2 = (2*(mo*2*math.pi*me_ge*k*300)**(3/2))/(h**3)
Nc_semi3 = (2*(mo*2*math.pi*me_gaas*k*300)**(3/2))/(h**3)

# calcul Nv
Nv_semi1 = (2*(mo*2*math.pi*me_si_trou*k*300)**(3/2))/(h**3)
Nv_semi2 = (2*(mo*2*math.pi*me_ge_trou*k*300)**(3/2))/(h**3)
Nv_semi3 = (2*(mo*2*math.pi*me_gaas_trou*k*300)**(3/2))/(h**3)

print("Semi 1 ‐ Nc = ",Nc_semi1, "cm‐3 / Nv = ",Nv_semi1, "cm‐3")
print("Semi 2 ‐ Nc = ",Nc_semi2, "cm‐3 / Nv = ",Nv_semi2, "cm‐3")
print("Semi 3 ‐ Nc = ",Nc_semi3, "cm‐3 / Nv = ",Nv_semi3, "cm‐3")

# ***** 2c) *****
print("")
print("2c)")
print("À l'aide de la table 23.1, il est possible de trouver la valeur de la bande interdite en eV des trois semi-conducteurs à 300K")
eg_semi1 = 1.14
eg_semi2 = 0.67
eg_semi3 = 1.43
print("Semi 1 ‐ Eg = ",eg_semi1, "eV")
print("Semi 2 ‐ Eg = ",eg_semi2, "eV")
print("Semi 3 ‐ Eg = ",eg_semi3, "eV")
print("")




