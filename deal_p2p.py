import os   
import re  


def get_table_comment():
    all_tablesname = []
    with open('C:/Users/nianfou/Desktop/test.txt', 'rb', ) as f:
        all_string = f.read()
        c = (all_string.decode('utf-8'))
        all_tables = c.split(';')
        for a_table in all_tables:
            if a_table.startswith('\r\nCREATE'):
                table_name = re.search('`(.*?)`', a_table).group().strip('`')
                comment = re.search("CHARSET=utf8 COMMENT='(.*)'", a_table)
                if comment is not None:
                    comment = re.search("CHARSET=utf8 COMMENT='(.*)'", a_table).group(1)
                else:
                    pass
                tmp = list((table_name, comment))
                # print(tmp)
                all_tablesname.append(tmp)
    print(len(all_tablesname))            
    return all_tablesname


def rename_tables(all_tablesname):
    for root, dirs, files in os.walk('J:/保山正在做的数据/DD贷/P2P'):
        for a_file in files:
            print(os.path.join(root+'/', a_file))
            for a_list in all_tablesname:
                if a_list[1] is not None:
                    old_path = os.path.join(root+'/', a_list[0])
                    new_file_name = a_list[0].split('.')[0]+a_list[1]+'.csv'
                    new_path = os.path.join(root+'/', new_file_name)
                    print(old_path, new_path)


if __name__ == "__main__":
    c = get_table_comment()
    rename_tables(c)