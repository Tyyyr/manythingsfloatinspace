import matplotlib.pyplot as plt
import numpy as np

#  x .. = f(x)
def f(x):
    return -x

def leapfrog(startwertx, startwertv, intervallende, anzahlschritte):
    h = (intervallende - startwertx)/anzahlschritte
    tpoints = np.linspace(0, intervallende, anzahlschritte)
    xpoints = []
    vpoints = []
    x = startwertx
    v = startwertv
    for t in tpoints:
        xpoints.append(x)
        vpoints.append(v)
        x += 0.5 * v * h
        v += f(x) * h
        x += 0.5 * v * h
        #x += h * f(x) + f(x) * h**2/2
    return tpoints, xpoints

def euler(startwertx, startwertv, intervallende, anzahlschritte):
    h = (intervallende - startwertx)/anzahlschritte
    tpoints = np.linspace(0, intervallende, anzahlschritte)
    xpoints = []
    vpoints = []
    x = startwertx
    v = startwertv
    for t in tpoints:
        xpoints.append(x)
        vpoints.append(v)
        v_neu = v + h * f(x)
        x += h * v
        v = v_neu
        #x += h * f(x) + f(x) * h**2/2
    return tpoints, xpoints


t1, x1 = leapfrog(0.,1., 100, 500)
t2, x2 = euler(0.,1., 100, 500)
pointsin = np.sin(t1)
abweichung_1 = []
abweichung_2 = []
for i in range(len(t1)):
    abweichung_1.append(pointsin[i]-x1[i])
    abweichung_2.append(pointsin[i]-x2[i])

fig = plt.figure(figsize = (18, 8.5))
ax = fig.add_subplot(111)

ax.plot(t1, x1, label="Leapfrog")
ax.plot(t2, x2, label="Euler")
ax.plot(t1, np.sin(t1), label="np.Sinus")
ax.plot(t1, abweichung_1, label="Abweichung Leapfrog")
ax.plot(t1, abweichung_2, label="Abweichung Euler")
ax.plot(t1, 0*t1, color="black")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
