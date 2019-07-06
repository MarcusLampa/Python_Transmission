import numpy as np

engineSpeed = [800, 2000, 3000, 4000, 4750, 5930, 6200]
engineTorque = [115, 150, 170, 175, 189, 179, 170]

vehicle = {'dragCoefficient' : 0.32,
           'dynamicWheelRadius' : 0.3,
           'CrossSection' : 1.94,
           'maxEngineTorque' : 189,
           'mass' : 1515,
           'rollingResistanceCoefficient' : 0.005}

powertrain = {'gearRatios' : [3.72, 2.04, 1.34, 1.0, 0.8],
              'efficiency' : 0.92,
              'nGearSteps' : 0, # Not needed, use len(gearRatios)...
              'hasGearSplit' :  "false",
              'gearRatioFinal' : 3.2,
              'gearRatioSplit' : 0,
              'gearRatioRange' : 0,
              'gearRatioAxle' : 0,
              'gearRatioHub' : 0}

def TractionForce(engineTorque, vehicle, powertrain):

    n = len(engineTorque)
    m = len(powertrain["gearRatios"])

    result = np.zeros((n, m))
    jResult = np.zeros((n, 1))

    for i in range(m):
        for j in range(n):
            jResult[j] = (engineTorque[j] * powertrain["gearRatioFinal"] * powertrain["gearRatios"][i]) / \
            vehicle["dynamicWheelRadius"] * powertrain["efficiency"] * 0.001
        result[:, i] = jResult[:,0]
    return result


def Velocity(engineSpeed, vehicle, powertrain):

    n = len(engineSpeed)
    m = len(powertrain["gearRatios"])

    result = np.zeros((n, m))
    jResult = np.zeros((n, 1))

    for i in range(m):
        for j in range(n):
            jResult[j] = (3.6 * (np.pi / 30) * engineSpeed[j] * vehicle["dynamicWheelRadius"]) / (powertrain["gearRatios"][i] * powertrain["gearRatioFinal"])  
        result[:, i] = jResult[:,0]
    return result

def TractionPower(velocityTable, tractionForceTable):

    result = velocityTable * tractionForceTable / 3.6

    return result

tractionForceTable = TractionForce(engineTorque, vehicle, powertrain)
velocityTable = Velocity(engineSpeed, vehicle, powertrain)
tractionPowerTable = TractionPower(velocityTable, tractionForceTable)

print(tractionForceTable)
print(tractionPowerTable)