from functions import *

n = 20
liste_teilchen = init_particle_list(n)

plots = []
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_axis_bgcolor("black")
plt.ion()

for i in liste_teilchen:
	plots.append(plt.plot(i.x,i.y,"co",markersize = i.radius/100))

fig.canvas.draw()
plt.axis([-100000,100000,-100000,100000])
plt.pause(0.002)

#for _ in xrange(100):
while True:
	force_matrix = get_force_matrix(liste_teilchen)
	for a,i in enumerate(liste_teilchen):
		i.force = total_force_per_part(force_matrix,a)
	get_velocity(liste_teilchen)
	move(liste_teilchen)
	for i,p in zip(liste_teilchen,plots):
		if i.active == False:
			p[0].set_c("k")
		else:
			p[0].set_data(i.x,i.y)
	fig.canvas.draw()
	plt.pause(0.002)
