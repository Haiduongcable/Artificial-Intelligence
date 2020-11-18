import numpy as np
import skfuzzy as fz
from skfuzzy import control as ctrl

def readData():
    pass

def fuzzification():
    pass


humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')
temp = ctrl.Antecedent(np.arange(-7, 47, 0.2), 'temp')
wind_speed = ctrl.Antecedent(np.arange(0, 100, 1), 'wind_speed')
cloud = ctrl.Antecedent(np.arange(0, 9, 1), 'cloud')
pressure = ctrl.Antecedent(np.arange(980, 1040, 0.2), 'pressure')
rainfall = ctrl.Consequent(np.arange(0, 150, 0.2), 'rainfall')

humidity.automf(3)
temp.automf(3)
wind_speed.automf(3)
cloud.automf(3)
pressure.automf(3)
rainfall.automf(3)


rules = [
    ctrl.Rule(humidity['poor'], rainfall['poor']),
    ctrl.Rule(humidity['average'], rainfall['average']),
    ctrl.Rule(humidity['good'], rainfall['good']),
    ctrl.Rule(temp['poor'], rainfall['poor']),
    ctrl.Rule(temp['average'], rainfall['average']),
    ctrl.Rule(temp['good'], rainfall['average']),
    ctrl.Rule(wind_speed['poor'], rainfall['poor']),
    ctrl.Rule(wind_speed['average'], rainfall['average']),
    ctrl.Rule(wind_speed['good'], rainfall['good']),
    ctrl.Rule(cloud['poor'], rainfall['poor']),
    ctrl.Rule(cloud['average'], rainfall['average']),
    ctrl.Rule(cloud['good'], rainfall['good']),
    ctrl.Rule(pressure['poor'], rainfall['average']),
    ctrl.Rule(pressure['average'], rainfall['average']),
    ctrl.Rule(pressure['good'], rainfall['poor'])
]

CT = ctrl.ControlSystem(rules)
Defz = ctrl.ControlSystemSimulation( CT )
Defz.input['humidity'] = 47
Defz.input['temp'] = 15.5
Defz.input['wind_speed'] = 6
Defz.input['cloud'] = 8
Defz.input['pressure'] = 1005.8
Defz.compute()

print(Defz.output['rainfall'])
