import numpy as np
from matplotlib import pyplot as plt

xdata=[]
ydata=[]

print("Enter your x,y values for adding to dataset")

while True:
    
    xinp=int(input("enter your x value"))
    xdata.append(xinp)
    
    yinp=int(input("enter your y value"))
    ydata.append(yinp)
    
    testing = input("Type exit to see the output ")
    if testing == 'exit':
        break
  
plt.plot(xdata,ydata,'ro')
plt.axis([-50,50,-50,50])

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Python Programming Final Take Home')

plt.savefig("xydatas.png")

plt.show()
