import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from matplotlib import style

#https://matplotlib.org/users/annotations.htmlmatplt

slices = [7,2,3,4]
labelList = ["label1", "label2", "label3", "label4"]
colorLists = ['c', 'm', 'r', 'b']

x = [800, 2000, 3000, 4000, 4750, 5930, 6200]
y1 = [115, 150, 170, 175, 189, 179, 170]
y2 = [95, 140, 180, 185, 169, 175, 160]

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

ax1.plot(x, y1, '-', label='myline1')
ax1.plot(x, y2, '-', label='myline2')

### Annotations with text and arrow
myFont = {'family' : 'serif', 'color' : 'darkred', 'size' : 15}
ax1.text(3000, 100, 'Text example', fontdict=myFont)

ax1.annotate('myPoint', (x[4], y1[4]),                                  # Coordinates to point to, NOTE the "(x, y)" 
             xytext=(0.6, 0.6), textcoords='axes fraction',             # Coordinated to text
             arrowprops = dict(facecolor='green', color='gray'))

### Annotation on axis 

bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)

ax1.annotate(str(y2[-1]), (x[-1], y2[-1]), 
                 xytext = (x[-1] + 500, y2[-1]),       # Troligen bättre att hämta x-axelns värde än att bara dra till men sista punkten +500
                 bbox=bbox_props)

plt.xlabel('Speed')
plt.ylabel('Torque')
plt.title('Torque vs Speed')
plt.legend()
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2, wspace=0.2, hspace=0.2) # % left to right och % bottom to top


plt.show()