# policy_text_analyse

```python
import os
import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
import wordcloud

path = "D:\PycharmProjects\policy_try\source_policy" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
num = len(files)    #查看政策数量

jieba.load_userdict('data\custom.txt')

stopword=[]
with open('data\stopword.txt','r',encoding='utf-8') as f :
    for line in f.readlines():
        l = line.strip()
        if l == '\\n':  #换行符
            l = '\n'
        if l == '\\u3000' : #制表符
            l = '\u3000'
        stopword.append(l)



for i in range(0,num):
    with open('source_policy/'+str(files[i]), "r",encoding='utf-8') as f:    #打开文件
        a = f.read()   #读取文件
        cut = jieba.lcut(a)
        x = np.array(cut)    #将分好的此列表转为数组
        y = np.array(stopword)   #将停用词转为数组
        z = x[~np.in1d(x,y)]
        k = [i for i in z if len(i)>1 ]
        result = pd.DataFrame(k).groupby(0).size().sort_values(ascending=False) [:200]
        result.to_csv('output/'+str(files[i])+'.csv',header=False,encoding='GBK')

```

    Building prefix dict from the default dictionary ...
    Loading model from cache C:\Users\Allen\AppData\Local\Temp\jieba.cache
    Loading model cost 0.447 seconds.
    Prefix dict has been built successfully.



```python
import os
list = []
dir = "D:\PycharmProjects\policy_try\output"
for root, dir, file in os.walk(dir):
    for b in file:
        #print(b) # 只是打印文件名
        list.append(b)
```


```python
result = pd.DataFrame(list)
result.to_csv('tmp/list.csv',header=False,encoding='GBK')
```


```python
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
```
