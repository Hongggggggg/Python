import os

file_name = 'File.txt'

#新建，若已存在则直接覆盖
with open(file_name, 'w', encoding = 'utf-8') as f:
    f.write("朝辞白帝彩云间\n小丑竟在我身边\n")
    f.write("两岸猿声啼不住\n小丑已行万里路\n")
    '''
    直接创建后光标默认在文件结尾
    f.seek(0)#将光标置0位
    print(f.readline())
    '''

#读
with open(file_name, 'r', encoding = 'utf-8') as f:
    for line in f:
        print(line, end = '')


#追加内容
with open(file_name, 'a+', encoding = 'utf-8') as f:
    print("===========append=============")
    f.write("垂死病中惊坐起\n小丑竟是我自己\n")
    f.seek(0)#将光标置0位
    for line in f:
        print(line, end = '')

#判断文件是否存在
print(os.path.exists(file_name))

#判断文件夹是否存在
#os.path.exists(test_dir)
