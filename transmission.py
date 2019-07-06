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
#transmissionRatio = {"1st Gear" : 3.72, "2nd Gear" : 2.04, "3rd Gear" : 1.34, "4th Gear" : 1.0, "5th Gear" : 0.8}
gearRatios = [3.72, 2.04, 1.34, 1.0, 0.8]
gearRatioSplit = 0
rangeUnitRatio = 1
axleDriveRatio = 3.2
hubDriveRatio = 1
transferBoxRatio = 1
efficiency = 0.92

finalRatio = transferBoxRatio * axleDriveRatio * hubDriveRatio
transmissionRatio = gearRatios * rangeUnitRatio

def TractionForce(engineTorque,
                  dynamicWheelRadius,
                  efficiency,
                  transmissionRatio,
                  finalRatio):

    n = len(engineTorque)
    m = len(transmissionRatio)
    result = np.zeros((n, m))

    
    for i in range(m):
        for j in range(n):
            result[j, i] = (engineTorque[j] * finalRatio * transmissionRatio[i]) /\
                            dynamicWheelRadius * efficiency * 0.001
    return result


def Velocity(engineSpeed,
             dynamicWheelRadius,
             transmissionRatio,
             finalRatio):

    n = len(engineSpeed)
    m = len(transmissionRatio)

    result = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            result[j, i] = (3.6 * (np.pi / 30) * engineSpeed[j] * dynamicWheelRadius) /\
                           (transmissionRatio[i] * finalRatio)  
    return result

def TractionPower(velocityTable, tractionForceTable):
    
    result = velocityTable * tractionForceTable / 3.6
    return result

tractionForceTable = TractionForce(engineTorque,
                                   dynamicWheelRadius,
                                   efficiency,
                                   transmissionRatio,
                                   finalRatio)

velocityTable = Velocity(engineSpeed, 
                         dynamicWheelRadius, 
                         transmissionRatio, 
                         finalRatio)

tractionPowerTable = TractionPower(velocityTable, tractionForceTable)

print(tractionForceTable)
print(tractionPowerTable)