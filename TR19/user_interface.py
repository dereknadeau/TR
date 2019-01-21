from matplotlib import pyplot as plt
from thermal_equations import NTU, LMTD
# from variables import *

class QueryMode:

    def get_choice(self):
        print('1. NTU Method')
        print('2. LMTD Method')
        val = input('What method would you like to run? (1 or 2)')
        return val


class RunNTU(NTU):
    run()


class RunLMTD(LMTD):
    pass


class Plotter:
    def __init__(self, data):
        self.data = data

    # def plot

if __name__ == '__main__':
    # print("Change variables in variables.py")
    # choice = QueryMode.get_choice
    # if choice == 1:
    #     RunNTU()
    # elif choice == 2:
    #     RunLMTD()
    RunNTU()