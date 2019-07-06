import numpy as np

# Engine Parameters:
engineSpeed = [800, 2000, 3000, 4000, 4750, 5930, 6200]
engineTorque = [115, 150, 170, 175, 189, 179, 170]

# Vehicle Parameters:
dragCoefficient = 0.32
dynamicWheelRadius = 0.3
CrossSection = 1.94
maxEngineTorque = 189
mass = 1515
rollingResistanceCoefficient = 0.005

# Drivetrain Parameters:
#gearRatios = {"1st Gear" : 3.72, "2nd Gear" : 2.04, "3rd Gear" : 1.34, "4th Gear" : 1.0, "5th Gear" : 0.8}

gearRatios = [3.72, 2.04, 1.34, 1.0, 0.8]
efficiency = 0.92
hasGearSplit = "false"
gearRatioFinal = 3.2
gearRatioSplit = 0
gearRatioRange = 0
gearRatioAxle = 0
gearRatioHub = 0

def TractionForce(engineTorque,\
                  dynamicWheelRadius,\
                  efficiency,\
                  gearRatios,\
                  gearRatioFinal):

    n = len(engineTorque)
    m = len(gearRatios)

    result = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            result[j, i] = (engineTorque[j] * gearRatioFinal * gearRatios[i]) /\
                            dynamicWheelRadius * efficiency * 0.001

    return result


def Velocity(engineSpeed,\
             dynamicWheelRadius,\
             gearRatios,\
             gearRatioFinal):

    n = len(engineSpeed)
    m = len(gearRatios)

    result = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            result[j, i] = (3.6 * (np.pi / 30) * engineSpeed[j] * dynamicWheelRadius) /\
                            (gearRatios[i] * gearRatioFinal)  

    return result

def TractionPower(velocityTable, tractionForceTable):

    result = velocityTable * tractionForceTable / 3.6

    return result

tractionForceTable = TractionForce(engineTorque, dynamicWheelRadius, efficiency, gearRatios, gearRatioFinal)
velocityTable = Velocity(engineSpeed, dynamicWheelRadius, gearRatios, gearRatioFinal)
tractionPowerTable = TractionPower(velocityTable, tractionForceTable)

print(tractionForceTable)
print(tractionPowerTable)