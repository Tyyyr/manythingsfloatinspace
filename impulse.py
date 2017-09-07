# -*- coding: utf8 -*-
import numpy as np

"""
def actualize(self, other):
		schwerv = (self.mass * self.velocity + other.mass * other.velocity) / (self.mass + other.mass)
		
		e_kin_s = 1/2 * self.mass * (self.velocity - schwerv)**2				#kin energie auf einander (auf schwerpunkt)
		e_kin_o = 1/2 * other.mass * (other.velocity - schwerv)**2
		
		e_kin_self = np.sqrt (e_kin_s[0]**2 + e_kin_s[1]**2)					#betraege
		e_kin_other = np.sqrt (e_kin_o[0]**2 + e_kin_o[1]**2)					
		
		e_preres_self = 1/3 * self.preres * np.pi * (self.radius **3)			#min energie zur zerstorung
		e_preres_other = 1/3 * other.preres * np.pi * (other.radius **3)

		if e_kin_self < e_preres_other and e_kin_other < e_preres_self:
			fusion(self, other)

		elif e_kin_self < e_preres_other and e_kin_other > e_preres_self:
			bruch(other, self)
		
		else:
			bruch(self, other)


"""



def fusion(self, other):
	#inelastischer Stoss
		print"fusion"
		self.momentum = (self.mass * self.velocity + other.mass * other.velocity)/(self.mass + other.mass)
		self.mass += other.mass
		self.volume += other.volume
		self.radius = np.cbrt((3*self.volume)/(4*np.pi))
		self.velocity = self.momentum/self.mass
		
		newpoint_x = (self.mass * self.x + other.mass * other.x) / (self.mass + other.mass)
		newpoint_y = (self.mass * self.y + other.mass * other.y) / (self.mass + other.mass)
		self.x = newpoint_x
		self.y = newpoint_y
		
		other.active = False
		other.color = (10,10,10)
		
		
		

def bruch(self, other):
	#elastischer Stoss
		print "bruch"
		addv = self.velocity - other.velocity #dadurch other unbewegt --> vereinfachung
		aenderung = other.velocity
		
		x_1 = np.array([self.x, self.y])
		x_2 = np.array([other.x, other.y])

		hvek = x_2 - x_1 	#2ter vektor aus positionen vor kollosion
		
		gamma = np.arccos (((hvek[0]*addv[0])+(hvek[1]*addv[1])) / ((np.sqrt((hvek[0])**2 + (hvek[1])**2)) * (np.sqrt((addv[0])**2 + (addv[1])**2))))
		
		alpha = np.arcsin (((np.sqrt((hvek[0])**2 + (hvek[1])**2)) / (self.radius + other.radius)) * np.sin(gamma))
		
		#aenderungsvektor
		dvek = 2* (self.velocity[0] -other.velocity[0] + alpha*(self.velocity[1] - other.velocity[1])) / ((1+ (alpha **2)) * (1+(other.mass/self.mass))) 
		
		neuselfv_x = self.velocity[0] - (other.mass / self.mass) * dvek
		neuselfv_y = self.velocity[1] - alpha * (other.mass / self.mass) * dvek
		neuotherv_x = other.velocity[0] + dvek
		neuotherv_y = other.velocity[1] + alpha *dvek
		
		self.velocity = np.array([neuselfv_x, neuselfv_y])
		other.velocity = np.array([neuotherv_x, neuotherv_y])
		
		#other wird zerstört werden
