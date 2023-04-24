import os
import pandas as pd

list = []
dir = "D:\PycharmProjects\policy_try\output"
for root, dir, file in os.walk(dir):
    for b in file:
        #print(b) # 只是打印文件名
        list.append(b)


result = pd.DataFrame(list)
result.to_csv('tmp/list.csv',header=False,encoding='GBK')


def rename():
    i = 0
    path = r"D:\PycharmProjects\policy_try\output"
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    num = len(files)  # 查看政策数量

    filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
    for files in filelist:   #遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)    #原来的文件路径
        if os.path.isdir(Olddir):       #如果是文件夹则跳过
                continue
        filename = 'policy'     #文件名
        filetype = '.csv'        #文件扩展名
        Newdir = os.path.join(path, filename + str(i) + filetype)   #新的文件路径
        os.rename(Olddir, Newdir)    #重命名
    return True

if __name__ == '__main__':
    rename()