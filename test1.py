import  os
import sys

def get_file(path):
    """
    获得路径下的所有文件
    :param path: 路径
    :return:
    """

    for root, dirs, files in os.walk(path):
        # print(files)
        return files


if __name__ == '__main__':
    s= get_file("I:/昆明龙阳/DDD贷")
    for file in s:
        true_path = os.path.join("I:/昆明龙阳/DDD贷", file)
        fsizes = os.path.getsize(true_path) /1024
        if fsizes < 1:
            print(file, str(round(fsizes) + 1) + "KB")
        else:
            print(file, str(round(fsizes)) + "KB")




