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

# Drivetrain Parameters:
#gearRatios = {"1st Gear" : 3.72, "2nd Gear" : 2.04, "3rd Gear" : 1.34, "4th Gear" : 1.0, "5th Gear" : 0.8}
gearRatios = [3.72, 2.04, 1.34, 1.0, 0.8]
gearSplitRatio = 0.0
rangeUnitRatio = 1.0
axleDriveRatio = 3.2
hubDriveRatio = 1.0
transferBoxRatio = 1.0
efficiency = 0.92

# Case Parameters:
roadGradients = [10, 20, 30, 40 , 50]
rollingResistanceCoefficient = 0.0124
rollingResistanceCoefficientList = np.array([0.0124, 0.0124, 0.0124, 0.0124, 0.0124, 0.0124, 0.0125, 0.0127, 0.0128, 0.0130, 0.0131, 0.0134, 0.0136, 0.0139, 0.0142, 0.0145, 0.0155, 0.0165, 0.0176, 0.0188, 0.0200, 0.0221, 0.0244, 0.0270, 0.0299, 0.0325, 0.0352, 0.0379, 0.0406, 0.0434, 0.0461])

# Calculate input variables:
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


def StallTorqueRatio(gradient,
                     mass,
                     dynamicWheelRadius, 
                     rollingResistanceCoefficient, 
                     efficiency, 
                     maxEngineTorque):

    gravity = 9.81
 
    result = (dynamicWheelRadius * mass * gravity * (rollingResistanceCoefficient * np.cos(np.arctan(gradient/100)) + \
              np.sin(np.arctan(gradient/100)) )) / (maxEngineTorque * efficiency)

    return result

    
def DrivingResistance(mass,
                      rollingResistanceCoefficient,
                      roadGradients):

    velocity = np.arange(0, maxVelocity, 10) / 3.6
    
    n = len(velocity)
    m = len(roadGradients)
    gravity = 9.81
    airResistance = np.zeros((n, 1))
    rollinResistance = np.zeros((n, 1))
    drivingResistance = np.zeros((n, m))
 
 
 #accelerationResistance = rotationalInertiaCoefficient * vehicleMass * acceleration #Add function
 
    for i in range(m):
 
        gradientResistance = mass * gravity * np.sin( roadGradients[i] / 100 )
 
        rollinResistance[:, 1] = rollingResistanceCoefficientList[:n] * mass * gravity * np.cos(roadGradients[i]/100)
        airResistance[:, 1] = 0.5 * airDensity * dragCoefficient * crossSection * (velocity^2)
 
        drivingResistance(:, i) = (airResistance + rollinResistance + gradientResistance) .* (1/1000); %+ accelerationResistance;

    return drivingResistance

gradient = 50
stallRatio = StallTorqueRatio(gradient,
                              mass,
                              dynamicWheelRadius, 
                              rollingResistanceCoefficient, 
                              efficiency, 
                              maxEngineTorque)

print(f"Stall torque ratio for: {gradient}% gradient is: {format(stallRatio, '.2f')}")

tractionForceTable = TractionForce(engineTorque,
                                   dynamicWheelRadius,
                                   efficiency,
                                   powertrainRatios)

velocityTable = Velocity(engineSpeed, 
                         dynamicWheelRadius, 
                         powertrainRatios)

tractionPowerTable = TractionPower(velocityTable, tractionForceTable)

np.set_printoptions(precision=2)
print(tractionForceTable)
print(tractionPowerTable)
#print(velocityTable)

gears = ["1st Gear" , "2nd Gear", "3rd Gear", "4th Gear", "5th Gear"]
fig, ax = plt.subplots()
ax.plot(velocityTable, tractionForceTable)

ax.legend(gears, loc='upper right')
ax.set(xlabel='Velocity [km/h]', ylabel='Traction [kN]',
       title='Traction force diagram')

fig.savefig("TractionForceDiagram.png")
plt.show()