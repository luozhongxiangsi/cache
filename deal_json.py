import json
import os


def get_info(path):
    with open(path, 'r', encoding='utf-8')\
     as f:
        all_info = []
        json_data = f.read()
        dict_data = json.loads(json_data)
        # 表名称
        table_name = dict_data.get('tableName')
        # print(table_name)
        # 表备注
        table_comment = dict_data.get('displayName')
        # print(table_comment)
        tables_comment_dict = json.loads(dict_data['dataDesc'])
        # print(tables_comment_dict)
        tmp = [table_name, table_comment]
        all_info.append(tmp)
        for a_colum in tables_comment_dict.keys():
            colum_comment = tables_comment_dict.get(a_colum).get('title')
            # print(a_colum, colum_comment)
            cell_info = [a_colum, colum_comment]
            all_info.append(cell_info)
        print(all_info)


def get_all_files(root_path):
    """
    获得全部json文件的路径
    root_path: json文件所在的路径
    return all_files: 所有的文件的全路径
    """
    all_files = []
    tmp_list = []
    for root, dirs, files in os.walk(root_path):
        for a_file in files:
            tmp_list.append(os.path.join(root + '/', a_file))
        all_files = [x for x in tmp_list if x.endswith('.mod')]
    return all_files


if __name__ == "__main__":
    all_files = get_all_files('C:/Users/nianfou/Desktop/module')
    for file in all_files:
        get_info(file)
