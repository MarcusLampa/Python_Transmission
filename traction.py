import numpy as np


def wheelResistance(rollingResistance, vehicleMass, gradient):
    gravity = 9.82
    wheelResistance = rollingResistance * vehicleMass * gravity * np.cos(np.deg2rad(gradient))
    print(f"The wheel resistance is:{wheelResistance}N")
    return wheelResistance

def airResistance(airDensity, dragCoefficient, crossSectionArea, velocity):
    """
    airDensity [kg/m^3], dragCoefficient [-], crossSectionArea [m^2], velocity [km/h]
    """
    airResistance = 0.5 * airDensity * dragCoefficient * crossSectionArea * (velocity / 3.6) ** 2.0
    print(f"The air resistance at {velocity}km/h are: {airResistance}N")
    return airResistance


wheelResistance(0.005, 1515, 10.0)
airResistance(1.199, 0.32, 1.94, 36.0)