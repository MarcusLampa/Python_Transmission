import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure(facecolor='#f5f5f1')

def CreatePlots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)

    return xs, ys

ax1 = plt.subplot2grid((6,2), (0,0), rowspan=2, colspan=2)
ax2 = plt.subplot2grid((6,2), (2,0), rowspan=4, colspan=1, sharex=ax1)
ax3 = plt.subplot2grid((6,2), (2,1), rowspan=2, colspan=1, sharex=ax1)
ax2v = ax2.twinx()

x, y = CreatePlots()
ax1.plot(x, y)

x, y = CreatePlots()
ax2.plot(x, y)



x, y = CreatePlots()
ax3.plot(x, y, label='Kalle')

ax2v.fill_between(x, y, 0, facecolor='r', alpha=0.3)
ax2v.grid(False)
ax2v.set_ylim(0, 4*max(y))
ax3.legend()
leg = ax3.legend(loc='best', ncol=1, prop={'size' : 8})   # ncol anger hur många kolumner som labels ska "fördelas" på 
leg.get_frame().set_alpha(0.5)

plt.show()