import pandas as pd
import os 
import numpy as np


i90_df = pd.read_excel('/Users/dexw/Desktop/GCN-Application/MPO_Dataset/i90_mass_pike.xls', sheet_name=None, header=5)

# def get_speed(df_dict:dict):
#     limit = len(df_dict) - 1
#     start = 0
#     ret_df = []
#     while start < limit:
#         key = 'Table '+str((start+1))
#         df_dict[key] = df_dict[key].drop([0])
#         df_dict[key] = df_dict[key].drop([len(df_dict[key])-1])
#         print(df_dict[key].head(1))
#         ret_df.append(df_dict[key])
#         start += 2
#     first_half = pd.concat(ret_df[0]+ret_df[2], axis=1, ignore_index=True)
#     return pd.concat(ret_df, ignore_index=True)


def get_speed(df_dict:dict):
    limit = len(df_dict) - 1
    start = 0
    ret_df = []
    while start <= limit:
        key = 'Table '+str((start+1))
        print(df_dict[key])
        df_dict[key] = df_dict[key].drop([0])
        df_dict[key] = df_dict[key].drop([len(df_dict[key])])
        print(df_dict[key])
        ret_df.append(df_dict[key].reset_index(drop=True))

        start += 2
    # for i in range(len(ret_df)):
    #     ret_df[i] = ret_df[i].reset_index(drop=True)
    time = np.append(ret_df[0].columns.values, ret_df[1].columns.values) 
    first_half = pd.concat([ret_df[0],ret_df[1]], axis=1, ignore_index=True)
    #print(first_half.shape)
    second_half = pd.concat([ret_df[2],ret_df[3]], axis=1, ignore_index=True)
    #print(second_half.shape)
    combined = pd.concat([first_half, second_half], axis=0, ignore_index=True)
    combined.columns = time
    return combined

import os 

data_dir = 'MPO_Dataset/'
file_lst = [f for f in os.listdir(data_dir) if f.endswith('.xls')]
speed_df_combined = []
travel_times_df_combined = []

# for file in file_lst:
file = "i495_north.xls"
file_path = os.path.join(data_dir, file)
df_dict = pd.read_excel(file_path, sheet_name=None, header=5)
# speed_df_combined.append(get_speed(df_dict))
ret = get_speed(df_dict)
print(ret.head(2))