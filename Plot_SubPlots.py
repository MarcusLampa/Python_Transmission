import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def CreatePlots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)

    return xs, ys

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax3 = fig.add_subplot(211)

x, y = CreatePlots()
ax1.plot(x, y)

x, y = CreatePlots()
ax2.plot(x, y)



x, y = CreatePlots()
ax3.plot(x, y)

plt.show()