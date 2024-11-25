import numpy as np 
import skfuzzy as fuzz 
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

fan_ctrl_simulation = ctrl.ControlSystemSimulation(fan_ctrl)

temperature_input = float(input("Enter temperature (0-100°C): "))
humidity_input = float(input("Enter humidity (0-100%): "))
if 0 <= temperature_input <= 100 and 0 <= humidity_input <= 100:
    fan_ctrl_simulation.input['temperature'] = temperature_input
    fan_ctrl_simulation.input['humidity'] = humidity_input
    fan_ctrl_simulation.compute()
    result = fan_ctrl_simulation.output['fan_speed']
    print(f"Fan Speed: {result:.2f}%")
else:
    print("Invalid input. Temperature and humidity values must be in the range 0-100.")