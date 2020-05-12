import pandas as pd
import numpy as np
import os


def get_all_tables_info():
    all_tables_info = []
    data = pd.read_excel('C:/Users/nianfou/Desktop/p2p2.xlsx')
    table_infos = list(zip(data['A'], data['B']))
    for table_info in table_infos:
        if table_info[1] is not np.nan and table_info[1] != 'VIEW':
            all_tables_info.append(table_info)
    return all_tables_info


def rename_tables(all_tables_info):
    for a_list in all_tables_info:
        root_path = 'C:/Users/nianfou/Desktop/DD贷/P2P2'
        old_path = os.path.join(root_path+'/', a_list[0]+'.csv')
        new_file_name = str(a_list[0])+str(a_list[1])+'.csv'
        new_path = os.path.join(root_path+'/', new_file_name)
        try:
            os.rename(old_path, new_path)
        except Exception:
            print('{}重命名失败，请重新命名。备注为{}'.format(str(a_list[0]), a_list[1]))


if __name__ == "__main__":
    c = get_all_tables_info()
    rename_tables(c)
