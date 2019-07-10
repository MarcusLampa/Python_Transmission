import matplotlib.pyplot as plt 

engineSpeed = [800, 2000, 3000, 4000, 4750, 5930, 6200]
engineTorque = [115, 150, 170, 175, 189, 179, 170]

x = [3, 7]
y = [2, 8]

print(x[0])

def LabelPlotCurv(fig, x, y, string, ratio = 0.5):

    myFont = {'family' : 'serif', 'color' : 'darkred', 'size' : 15}
    curveLength = []
    totalLength = 0

    for i in range(len(x)-1):
        print(f"i={i}")
        distancePt2Pt = ((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)**0.5
        totalLength += distancePt2Pt
        curveLength.append(totalLength)
        print(f"{curveLength}")

    t = curveLength[-1] * ratio
    print(f"t = {t}")
    closestPt = min(curveLength, key=lambda x:abs(x-t))
    print(f"index = {closestPt}")
    i = curveLength.index(closestPt)

    xCord = t
    yCord = y[i]
    
    
    plt.text(xCord, yCord, string, fontdict=myFont)

'''
    axis = ax.annotate(string, (x[4], y1[4]),                                  # Coordinates to point to, NOTE the "(x, y)" 
                xytext=(0.6, 0.6), textcoords='axes fraction',             # Coordinated to text
                arrowprops = dict(facecolor='green', color='gray'))
'''


    #return 0 # xCord , yCord
             
fig = plt.figure()
ax = plt.plot(engineSpeed, engineTorque)
LabelPlotCurv(fig, engineSpeed, engineTorque, "10% grad", 0.4)

plt.show()