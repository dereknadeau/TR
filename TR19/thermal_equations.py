import variables


class NTU:
    def __init__(self):


    def get_ntu(self, U, A):
        return (U * A) / self.c_min

    def get_ua_rad(self):
        dT_i = T_h_o - T_h_i
        dT_o = T_h_i - T_c_i
        water_heat_transfer = dT_i/q
        air_heat_transfer = dT_o/q
        return ()

    def get_C_min(self):
        if C_water > C_air:
            return C_air
        elif C_air > C_water:
            return C_water

    def get_q_max(self):
        return self.c_min*(self.T_h_i - T_c_i)

    def get_effectiveness(self):
        return q / self.q_max

    def run(self):
        self.c_min = self.get_C_min()
        self.q_max = self.get_q_max()
        self.ua = self.get_ua_rad()
        self.effect = self.get_effectiveness()

class LMTD:
    pass


if __name__ == '__main__':
    print("These are the Thermal equations please run the User Interface!")