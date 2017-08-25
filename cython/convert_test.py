from functions_cython import *

liste_teilchen = init_particle_list(10)

data = convert_data(liste_teilchen)

for i in data:
    print i
