#from functions import *

#n = 100
#background_colour = (10, 10, 10)
#(width, height) = (800, 480)
#liste_teilchen = init_particle_list(n,width,height)

def fcolorset(liste_temp):
	l = []
	liste_active = [i for i in liste_temp if i.active == True]
	for i in liste_active:
		l.append(i.mass)
	hmass = sum(l)
	mmass = min(l)
	print hmass, mmass, l
	for i in liste_active:
	#gruen
		if i.mass < (hmass/4):
			gwert = int((255/(hmass))*i.mass) 
		elif i.mass >= (hmass/4) and i.mass <= (3*hmass/4):
			gwert = 255
		elif i.mass > (3*hmass/4):
			gwert = int(-(255/hmass)*i.mass + 255)
	#rot
		if i.mass < (hmass/2):
			rwert = 0
		elif i.mass >= (hmass/2) and i.mass <= (3*hmass/4):
			rwert = int((255/(3*hmass/4))*i.mass)
		elif i.mass > (3*hmass/4):
			rwert = 255		
	#blau
		if i.mass <(hmass/4):
			bwert = 255
		elif i.mass >= (hmass/4) and i.mass <= (hmass/2):
			bwert = int(-(255/(hmass/2))*i.mass + 255)
		elif i.mass > (hmass/2):
			bwert = 0
		print i.mass,'   ', gwert, rwert, bwert
	#return liste_temp

#colorset(liste_teilchen)
