from TR19.variables import *
import numpy as np


class NTU:
    def __init__(self):
        self.c_min = 0
        self.c_max = 0
        self.c_r = 0
        self.q = 0
        self.q_max = 0
        self.ua = 0
        self.effect = 0
        self.calc_effect = 0
        self.ntu = 0

    def get_ntu(self):
        ntu = self.ua / self.c_min
        self.add_2_temp_data(name='NTU', data=ntu)
        return ntu

    def get_ua_rad(self):
        dT_i = T_h_o - T_h_i
        dT_o = T_h_i - T_c_i
        water_heat_transfer = dT_i/self.q
        air_heat_transfer = dT_o/self.q
        ua = (water_heat_transfer + air_heat_transfer) ** -1
        self.add_2_temp_data(name='UA', data=ua)
        return ua

    @staticmethod
    def get_c_min():
        if C_water > C_air:
            return C_air
        elif C_air > C_water:
            return C_water

    @staticmethod
    def get_c_max():
        if C_water > C_air:
            return C_water
        elif C_air > C_water:
            return C_air

    def get_c_r(self):
        return self.c_min / self.c_max

    def get_q(self):
        q = m_dot_water * c_water * (T_h_o - T_h_i)
        self.add_2_temp_data(name='q', data=q)
        return q

    def get_q_max(self):
        q_max = self.c_min*(T_h_i - T_c_i)
        self.add_2_temp_data(name='q_max', data=q_max)
        return q_max

    def get_effectiveness(self):
        eff = self.q / self.q_max
        self.add_2_temp_data(name='effect', data=eff)
        return eff

    def calc_effectiveness(self):
        effect = 1 - np.exp((1 / self.c_r) * (self.ntu ** 0.22) * (np.exp(-self.c_r * (self.ntu ** 0.78)) - 1))
        self.add_2_temp_data(name='calc_effect', data=effect)
        return effect

    def calc_heat_loss(self):
        q = self.calc_effect * self.   
        self.add_2_temp_data(name='Actual Heat Transfer', data=q)
        return q

    def run_calc(self):
        self.c_min = self.get_c_min()
        self.c_max = self.get_c_max()
        self.c_r = self.get_c_r()
        self.q = self.get_q()
        self.q_max = self.get_q_max()
        self.ua = self.get_ua_rad()
        self.ntu = self.get_ntu()
        self.effect = self.get_effectiveness()
        self.disp_heat = self.calc_heat_loss()
        self.calc_effect = self.calc_effectiveness()
        pd.set_option('display.max_columns', None)
        print('Cr: ' + str(self.c_r))
        print('Mean Effectiveness: ' + str(self.effect.mean()))
        print('Mean Calculated Effectiveness: ' + str(self.calc_effect.mean()))
        print('Mean UA: ' + str(self.ua.mean()))
        print('Mean Heat Loss: ' + str(self.disp_heat.mean()))
        print(temp_data.head())

    def add_2_temp_data(self, name, data):
        temp_data[name] = data


class LMTD:
    pass


if __name__ == '__main__':
    print("These are the Thermal equations please run the User Interface!")

