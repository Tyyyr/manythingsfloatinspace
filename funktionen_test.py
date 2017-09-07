import matplotlib.pyplot as plt
import numpy as np

blau = []
gruen = []
rot = []
def berechne(n):
	for i in xrange(n*8+1):
		wert = i/float(n)
		#blau
		if i >= 2*n and i <= 4*n:
			funktion_blau = .25*((wert-2)**3-3*(wert-2)**2)+1
			blau.append(int(funktion_blau*255))
		elif i < 2*n:
			blau.append(255)
		else:
			blau.append(0)
		#gruen
		if i <= 2*n:
			funktion_gruen = .25*(-wert**3+3*wert**2)
			gruen.append(int(funktion_gruen*255))
		elif i >= 6*n:
			funktion_gruen = .25*((wert-6)**3-3*(wert-6)**2)+1
			gruen.append(int(funktion_gruen*255))
		else:
			gruen.append(255)
		#rot
		if i >= 4*n and i <= 6*n:
			funktion_rot = .25*(-(wert-4)**3+3*(wert-4)**2)
			rot.append(int(funktion_rot*255))
		elif i < 4*n:
			rot.append(0)
		else:
			rot.append(255)

berechne(100)

plt.plot(blau,'b')
plt.plot(gruen,'g')
plt.plot(rot,'r')
plt.ylabel('colour value')
plt.xlabel('range from min to max')
plt.axis([0,800,0,270])
plt.show()
