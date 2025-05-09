import numpy as np
import math
import time

#constants and variables

chamberDiameter=0.085725 #m
chamberPressure  = 3895540 #Pa
throatArea = 0.0006575790181 #m^2
throatRadiusofCurvature = .00635 #m
gravtiy = 9.81 #m/s^2
universalGasConstant = 8.314 #j/molK

localMachNumber = 0 #unitless
hotSideHeatFlux = 2000000 #W/m^2

#chamber values from CEA
specificHeatRatio = 1.2409 #unitless
chamberTemperature = 3048.54 #K
molecularWeight = .019615 #kg/mol
specificHeatCapacity = 2183.2 #J/kgK
viscosity = 0.000092148 #Pa*s
gasThermalConductivity = 0.35289 #W/mk

gravtiy = 9.81 #m/s^2
universalGasConstant = 8.314 #j/molK

hotSideHeatFlux = 2000000 #W/m^2

#Calulated chamber values
chamberArea = math.pi*(chamberDiameter/2)**2 #m^2
prandtlNumber = (specificHeatCapacity*viscosity)/gasThermalConductivity #unitless
specificGasConstant = universalGasConstant/molecularWeight #J/kgK
characteristicVelocity =math.sqrt(((specificGasConstant*chamberTemperature)/(specificHeatRatio))* ((specificHeatRatio + 1)/2)**((specificHeatRatio+1)/(specificHeatRatio-1))) #m/s
throatDiameter = 2*math.sqrt(throatArea/math.pi)  #m

localRecoveryFactor = prandtlNumber**.33 #unitless
adiabaticWallTemperature =  chamberTemperature*((1+(localRecoveryFactor*((specificHeatRatio-1)/2)*localMachNumber))/(1+(((specificHeatRatio-1)/2)*localMachNumber)))

