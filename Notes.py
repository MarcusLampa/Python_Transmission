import matplotlib.pyplot as plt 
import matplotlib.image as mpimg



slices = [7,2,3,4]
labelList = ["label1", "label2", "label3", "label4"]
colorLists = ['c', 'm', 'r', 'b']

# -------------------------------------------Methode 1-------------------------------------------
'''
plt.pie(slices, startangle=45,
                labels=labelList, 
                colors=colorLists, 
                shadow=True, 
                explode=(0,0,0.1,0),
                autopct='%1.1f%%')

plt.show()
'''
# -------------------------------------------Methode 2-------------------------------------------
x = [800, 2000, 3000, 4000, 4750, 5930, 6200]

y1 = [115, 150, 170, 175, 189, 179, 170]
y2 = [95, 140, 180, 185, 169, 175, 160]



fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

ax1.plot(x, y1, '-', label='myline1')
ax1.plot(x, y2, '-', label='myline2')

ax1.fill_between(x, y1, y2, where=(y2 > y1), facecolor='r', interpolate=True,  alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y2 < y1), facecolor='g', interpolate=True,  alpha=0.3)

ax1.axhline(y1[3], color='red', linewidth=3)

ax1.spines['left'].set_color('blue')
ax1.spines['left'].set_linewidth(5)

ax1.spines['top'].set_visible(False)




for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.grid(True, color='g', linestyle='--', linewidth=0.3)    
ax1.xaxis.label.set_color('c')
ax1.title.set_color('r')
ax1.set_yticks([50, 100, 150, 200])


plt.xlabel('Speed')
plt.ylabel('Torque')
plt.title('Torque vs Speed')
plt.legend()
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2, wspace=0.2, hspace=0.2) # % left to right och % bottom to top
'''
# ------------------------------------------- add image -------------------------------------------
#https://stackoverflow.com/questions/3003108/adding-a-small-photo-image-to-a-large-graph-in-matplotlib-python

img = mpimg.imread('D:\VSCode\Transmission\scania.png')
#lum_img = img[:, :, 0]

plt.imshow(img, extent=[0, 0.2, 0.8, 0], aspect=3,  cmap='hot')
plt.colorbar()

# ------------------------------------------- add image -------------------------------------------
'''


plt.show()