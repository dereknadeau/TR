from matplotlib import pyplot as plt
from TR19.thermal_equations import NTU, LMTD
from TR19.variables import *


class QueryMode:

    def get_choice(self):
        print('1. NTU Method')
        print('2. LMTD Method')
        val = input('What method would you like to run? (1 or 2)')
        return val


class RunNTU(NTU):

    def __init__(self):
        NTU.__init__(self)

    def run_ntu(self):
        self.run_calc()
        save_data()
        full_plotter()


class RunLMTD(LMTD):
    pass


def full_plotter():
    fig = plt.figure(figsize=(18, 9))
    ax = fig.subplots()
    temp_data.plot(ax=ax, y='Coolant -- Hot', color='r')
    temp_data.plot(ax=ax, y='Coolant -- Cold', color='b')
    temp_data.plot(ax=ax, y='Air -- Cold', color='g')
    temp_data.plot(ax=ax, y='Air -- Hot', color='k')
    plt.axhline(y=225, linewidth=2, color='r')
    plt.title('Test Data (2018)')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (F)')
    plt.savefig(r'C:\Users\Derek\Documents\School\TerpsRacing\full_scale.png')
    plt.close(fig)
    fig2 = plt.figure(figsize=(18, 9))
    ax2 = fig2.subplots()
    temp_data.plot(ax=ax2, y='Actual Heat Transfer')
    plt.title('Heat Loss for Single Radiator (2018)')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (F)')
    plt.savefig(r'C:\Users\Derek\Documents\School\TerpsRacing\Heat_Loss.png')
    plt.close(fig2)


def run_plotter():
    print(temp_data['Time (sec)'][0].count())


def save_data():
    filename = r'C:\Users\Derek\Documents\School\TerpsRacing\processed_data.csv'
    hdf_filename = r'C:\Users\Derek\Documents\School\TerpsRacing\processed_data.h5'
    temp_data.to_csv(filename)
    temp_data.to_hdf(path_or_buf=hdf_filename, key='temp_data', mode='w', format='table')


if __name__ == '__main__':
    # print("Change variables in variables.py")
    # choice = QueryMode.get_choice
    # if choice == 1:
    #     RunNTU()
    # elif choice == 2:
    #     RunLMTD()
    method1 = RunNTU()
    method1.run_ntu()
