# DISCLAIMER: This code was written by John Wilkinson, and should not be copied or used without citation.
# Please adhere to university policy 

import matplotlib.pyplot as plt
import numpy as np

# This function calculates the vapor pressure of water at a given temperature, using the Clausius-Clapeyron equation.
# The equation is as follows: e = 0.611 ** ((17.502 * T) / (240.97 + T))
# Where e is the vapor pressure in kPa, and T is the temperature in degrees Celsius.
def clausius_clapeyron(T): 
    return 0.611 ** ((17.502 * T) / (240.97 + T))

# This function plots a the vapor pressure along a range of temperatures
# Temperatures should be in degrees Celcius
def plot_range(start, end):
    temperatures = np.arange(start, end, 1)
    vapor_pressures = [clausius_clapeyron(t) for t in temperatures]

    plt.plot(temperatures, vapor_pressures)
    plt.xlabel("Temperature (C)")
    plt.ylabel("Vapor Pressure (kPa)")
    plt.savefig('homework1/generated/clausius-clapeyron.png')
    plt.show()

plot_range(0, 40)