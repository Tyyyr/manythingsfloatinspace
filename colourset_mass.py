def colour_list(liste_temp):
	"""Calculates 'dynamic' or constant limits of mass for a system
	with multiple particles.
	"""
	#Dynamic relies on lightest and haviest particle of all particles.
	#Enable with hmass = max(l)
	#Constant sums all masses of particles and sets it as upper limit,
	#the lower limit is equal to the lightest particle at the start.
	#Enable with hmass = sum(l)
	l = []
	liste_active = [i for i in liste_temp if i.active == True]
	for i in liste_active:
		l.append(i.mass)
	hmass = max(l)
	mmass = min(l)
	return hmass, mmass

def fcolourset(i,hmass,mmass):
	"""Evaluates the colour values for each particle
	based on it's mass in relation to the limits.
	"""
	#Blue = lightest object
	#Green = medium weight object
	#Red = haviest object
	#Default colour scale goes from blue to green, then red.
	#For Reference of default colour curves see files dcc_rgb.png, 
	#dcc_r.png, dcc_g.png, dcc_b.png.
	wert = float(i.mass)/hmass *8
	#green
	if wert <= 2:
		gwert = int(.25*(-wert**3+3*wert**2)*255)
	elif wert >= 6:
		gwert = int(.25*((wert-6)**3-3*(wert-6)**2+4)*255)
	else:
		gwert = 255
	#red
	if wert < 4:
		rwert = 0
	elif wert >= 4 and wert <= 6:
		rwert = int(.25*(-(wert-4)**3+3*(wert-4)**2)*255)
	else:
		rwert = 255
	#blue
	if wert >= 2 and wert <= 4:
		bwert = int(.25*((wert-2)**3-3*(wert-2)**2+4)*255)
	elif wert < 2:
		bwert = 255
	else:
		bwert = 0
	#print rwert, gwert, bwert
	return (rwert,gwert,bwert)
