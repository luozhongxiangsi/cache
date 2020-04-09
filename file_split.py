# coding:utf-8
import os


def file_find(path):
    os.chdir(path)
    all_list = os.listdir(path)
    for one in all_list:
        true_path = os.path.join(one)
        print(os.path.isdir(true_path))
        print(true_path)


def find_file(path):
    """
    找到当前路径下的所有文件，排除文件夹
    :param path: 需要判断的路径
    :return: 返回文件列表
    """
    file_list = []
    all_list = os.listdir(path)
    for one in all_list:
        true_path = os.path.abspath(one)
        #print(true_path)
        if os.path.isfile(one):
            print(one)
            file_list.append(one)
    return file_list


# def find_all_file_names(path):
#     all_file_names = os.listdir(path)
#     return all_file_names


def find_all_file_names(file_dir):
    """
    找到当前路径下的当前路径下所有非目录子文件

    :param file_dir:路径
    :return: all_file  所有的非目录子文件
    """
    all_files = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            all_files.append(file)
    # print(len(all_file))
    return all_files


def file_fileter(file_type, *file_names):
    for file in file_names:
        print(type(str(file)))
        print((str(file)).endswith(file_type))



if __name__ == '__main__':
    c = find_all_file_names('D:/2019-0199/root')
    #print(c)
    file_fileter('txt', c)

