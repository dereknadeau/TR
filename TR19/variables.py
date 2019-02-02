import pandas as pd
# The following should be interpolated to ensure more accurate calculations  currently not using this
# rho_air

m_dot_water = 0.25              # Regular Water @ 15 L/min, which roughly converts to 0.25 kg/s
total_area_he = 1.8555        # m^2  This is going to be the A_o area of both radiators
cross_area = 0.14683*0.21375    #
c_water = 4.187                 # Regular Water @ ***** in kJ/kgK
c_air = 1.00                    # Air @ ***** kJ/kgK
m_dot_air = 1.117               # Air @ ***** kg/s @ 11 mph?
C_water = m_dot_water * c_water
C_air = m_dot_air * c_air
fan_airflow = 579/3600          # Air @ 0 mm H20 converted to m^3/s
rho_air = 1.164                 # Air @ 300K and atmospheric pressure kg/m^3
idle_m_dot_air = rho_air * fan_airflow


# data_file_path = ''  # This should be read in as a dataframe and have that information transformed using the other given values
data_file = r'C:\Users\Derek\Documents\School\TerpsRacing\New_O2_Cal.csv'
df = pd.read_csv(data_file)
df['Air Temp Out'] = df['Air Temp (F)'] + 10
tps = df
T_c_o = df['Air Temp Out']
T_h_o = df['Coolant Temp (F)']
T_h_i = df['ECT IN (F)']
T_c_i = df['Air Temp (F)']
temp_data = df[['Time (sec)', 'TPS (%)', 'Coolant Temp (F)', 'ECT IN (F)', 'Air Temp (F)', 'Air Temp Out']].copy()
temp_data.rename(columns={'Coolant Temp (F)': 'Coolant -- Hot',
                          'ECT IN (F)': 'Coolant -- Cold',
                          'Air Temp (F)': 'Air -- Cold',
                          'Air Temp Out': 'Air -- Hot'},
                 inplace=True)

# For right now we do not have a way of accurately measuring the power put into the engine so we are going to assume
# a constant value using the 1/3 rule and the fact that we drive with the 1st and 2nd gears mainly. Fuel HP = 55HP
# 55/3 = 13.6712 kW
# q = 13.67
# This value could also be mass flow * specific heat * Delta T

# temp_i_water = 210  # Column Name or index number
# temp_o_water = 190  # Column Name or index number
# temp_o_air = 35     # Column Name or index number
# temp_i_air = 25     # Column Name or index number

# hot_fluid = 'water'
# cold_fluid = 'air'