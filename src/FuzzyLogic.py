from matplotlib.pyplot import draw
import numpy as np
import pandas as pd
import skfuzzy as fz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class FIS:
    def __init__(self):
        evoparation = ctrl.Antecedent(np.arange(0, 15, 0.2), 'evoparation')     # chia độ bốc hơi từ 0-15 với khoảng cách 0.1
        humidity = ctrl.Antecedent(np.arange(0, 100, 0.2), 'humidity')          # chia độ ẩm từ 0-100(%) với khoảng cách 0.2
        pressure = ctrl.Antecedent(np.arange(990, 1030, 0.1), 'pressure')       # chia áp suất từ 990-1020(.10^2 Pa) với khoảng cách 0.1
        cloud = ctrl.Antecedent(np.arange(0, 8, 1), 'cloud')                    # chia mây từ 0-8 với khoảng cách 1
        temp = ctrl.Antecedent(np.arange(15, 40, 0.1), 'temp')                  # chia nhiệt độ từ 15-38(độ C) với khoảng cách 0.1
        rainfall = ctrl.Consequent(np.arange(0, 120, 0.2), 'rainfall')          # chia lượng mưa từ 0-120(mm) với khoảng cách 0.2 

        evoparation['low'] = fz.trapmf(evoparation.universe, [0, 0, 3, 4])      # độ bốc hơi thấp => mưa nhiều
        evoparation['medium'] = fz.trapmf(evoparation.universe, [3.4, 4, 7, 10])  
        evoparation['high'] = fz.trapmf(evoparation.universe, [8, 12, 15, 15])  # độ bốc hơi quá cao => mưa nhiều

        humidity['low'] = fz.trapmf(humidity.universe, [0, 0, 60, 75])
        humidity['high'] = fz.trapmf(humidity.universe, [65, 80, 100, 100])     # độ ẩm cao mưa nhiều

        pressure['low'] = fz.trapmf(pressure.universe, [990, 990, 1009, 1012])      # áp suất thấp mưa nhiều
        pressure['high'] = fz.trapmf(pressure.universe, [1009, 1012, 1030, 1030])

        cloud['low'] = fz.trapmf(cloud.universe, [0, 0, 5, 7])
        cloud['high'] = fz.trapmf(cloud.universe, [6, 7, 8, 8])                 # nhiều mây mưa nhiều

        temp['low'] = fz.trapmf(temp.universe, [15, 15, 20, 24.2])
        temp['medium'] = fz.trapmf(temp.universe, [23, 25, 29, 32])           # nhiệt độ TB thì mưa cao hơn
        temp['high'] = fz.trapmf(temp.universe, [28.5, 35, 40, 40])

        rainfall['very_low'] = fz.trapmf(rainfall.universe, [0, 0, 2, 4])       # không mưa
        rainfall['low'] = fz.trapmf(rainfall.universe, [3, 5, 8, 12])          # mưa ít
        rainfall['medium'] = fz.trapmf(rainfall.universe, [10, 15, 35, 40])     
        rainfall['high'] = fz.trapmf(rainfall.universe, [35, 45, 120, 120])     # mưa nhiều

        # evoparation.view()
        # humidity.view()
        # pressure.view()
        # cloud.view()
        # temp.view()
        # rainfall.view()


        rules = [
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi thấp
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ thấp
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),

            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi TB
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ thấp
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),

            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi cao
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ thấp
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['low'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),



            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi thấp
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ TB
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['low']),
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['low']),
            ctrl.Rule(evoparation['low'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['medium']),

            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi TB
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ TB
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['low']),
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['low']),
            ctrl.Rule(evoparation['medium'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),

            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi cao
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ TB
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['low']),
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['low']),
            ctrl.Rule(evoparation['high'] & temp['medium'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['high']),


            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi thấp
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ cao
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['low'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),

            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi TB
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ cao
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['medium'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),

            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['low'] , rainfall['very_low']),     # tại bốc hơi cao
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['low'] & pressure['high'] & cloud['high'] , rainfall['very_low']),    # nhiệt độ cao
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['low'] & pressure['low'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['high'] & pressure['high'] & cloud['high'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['low'] , rainfall['very_low']),
            ctrl.Rule(evoparation['high'] & temp['high'] & humidity['high'] & pressure['low'] & cloud['high'] , rainfall['low']),
        ]

        CT = ctrl.ControlSystem(rules)
        self.Defz = ctrl.ControlSystemSimulation( CT )

    def predict(self, evoparation, humidity, pressure, cloud, temp):
        self.Defz.input['evoparation'] = evoparation
        self.Defz.input['humidity'] = humidity
        self.Defz.input['pressure'] = pressure
        self.Defz.input['cloud'] = cloud
        self.Defz.input['temp'] = temp
        self.Defz.compute()
        return self.Defz.output['rainfall']