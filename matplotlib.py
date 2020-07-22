import matplotlib.pyplot as plt
import numpy as np

x=[3.92,3.94,3.98,4.01,4.04,4.13]
y=[400,350,300,273,250,200]

for i in range(1,len(x)+1):
    katsayi=np.polyfit(x,y,i)
    polinom=np.poly1d(katsayi)
    yy=[polinom(z) for z in x]
    
plt.figure(figsize=(5,6))
plt.plot(x,y,marker="o",linestyle=" ")
plt.plot(x,yy,marker="")
plt.savefig("Grafik-1")
plt.show()
