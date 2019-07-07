import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Engine Parameters:
engineSpeed = [800, 2000, 3000, 4000, 4750, 5930, 6200]
engineTorque = [115, 150, 170, 175, 189, 179, 170]
maxEngineTorque = 189

# Vehicle Parameters:
dragCoefficient = 0.32
dynamicWheelRadius = 0.3
CrossSection = 1.94
mass = 1515
rollingResistanceCoefficient = 0.005

# Drivetrain Parameters:
#gearRatios = {"1st Gear" : 3.72, "2nd Gear" : 2.04, "3rd Gear" : 1.34, "4th Gear" : 1.0, "5th Gear" : 0.8}
gearRatios = [3.72, 2.04, 1.34, 1.0, 0.8]
gearSplitRatio = 0.0
rangeUnitRatio = 1.0
axleDriveRatio = 3.2
hubDriveRatio = 1.0
transferBoxRatio = 1.0
efficiency = 0.92

finalRatio = transferBoxRatio * axleDriveRatio * hubDriveRatio
transmissionRatios = np.array(gearRatios) * rangeUnitRatio
powertrainRatios = transmissionRatios * finalRatio

def TractionForce(engineTorque,
                  dynamicWheelRadius,
                  efficiency,
                  powertrainRatios):

    n = len(engineTorque)       # Calculate the number of rows
    m = len(powertrainRatios)  # Calculate the number of columns
    result = np.zeros((n, m))

    
    for i in range(m):
        for j in range(n):
            result[j, i] = (engineTorque[j] * powertrainRatios[i]) /\
                            dynamicWheelRadius * efficiency * 0.001
    return result


def Velocity(engineSpeed,
             dynamicWheelRadius,
             powertrainRatios):

    n = len(engineSpeed)        # Calculate the number of rows
    m = len(powertrainRatios)  # Calculate the number of columns
    result = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            result[j, i] = (3.6 * (np.pi / 30) * engineSpeed[j] * dynamicWheelRadius) /\
                           (powertrainRatios[i])  
    return result

def TractionPower(velocityTable, tractionForceTable):

    result = velocityTable * tractionForceTable / 3.6
    return result

tractionForceTable = TractionForce(engineTorque,
                                   dynamicWheelRadius,
                                   efficiency,
                                   powertrainRatios)

velocityTable = Velocity(engineSpeed, 
                         dynamicWheelRadius, 
                         powertrainRatios) 

tractionPowerTable = TractionPower(velocityTable, tractionForceTable)

print(tractionForceTable)
print(tractionPowerTable)
print(velocityTable)

gears = ["1st Gear" , "2nd Gear", "3rd Gear", "4th Gear", "5th Gear"]
fig, ax = plt.subplots()
ax.plot(velocityTable, tractionForceTable)

ax.legend(gears, loc='upper right')
ax.set(xlabel='Velocity [km/h]', ylabel='Traction [kN]',
       title='Traction force diagram')

fig.savefig("TractionForceDiagram.png")
plt.show()