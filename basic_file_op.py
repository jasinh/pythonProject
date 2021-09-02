from os import walk, mkdir, remove
import os
import time
from shutil import copy, move, rmtree


path = 'txt'
count = 0
files100 = []


class Found(Exception):
    pass


try:
    for filepath, folders, files in walk(path):


            # for file in files:
            #     if '.ini' in file:
            #         if os.path.exists(r'txt'):
            #             print(os.path.join(filepath,file))
            #             copy(os.path.join(filepath,file),os.path.join(r'txt',file))
            #
            #             if len(os.listdir(r'txt')) == 100:
            #                 print(os.listdir(r'txt'))
            #                 raise Found
            #         else:
            #             print('不存在，创建')
            #             mkdir(r'txt')
            #             copy(os.path.join(filepath, file), os.path.join(r'txt', file))
            #             if len(os.listdir(r'txt'))==100:
            #                 print(os.listdir(r'txt'))
            #                 raise Found
        # for file in files:
        #     size=os.path.getsize(os.path.join(filepath,file))/1024/1024
        #     if size >100:
        #         # print(os.path.join(filepath,file),size,'M')
        #         files100.append(file)
        #         count+=1
        #     if count==5:
        #         raise Found
        for file in files:
            createtime = os.path.getmtime(os.path.join(filepath, file))
            #print(os.path.join(filepath,file),type(createtime))
            real_time=time.localtime(createtime)
            dt=time.strftime("%Y-%m-%d %H:%M",real_time)
            #print(dt)
            target_time='2020-09-08 10:30'
            time_array=time.strptime(target_time,"%Y-%m-%d %H:%M")
            my_target_time=float(time.mktime(time_array))
            if createtime>my_target_time:
                print(file,dt)
                try:
                    copy(os.path.join(filepath,file),os.path.join('zip',file))
                except FileNotFoundError:
                    mkdir('zip')
                    copy(os.path.join(filepath,file),os.path.join('zip',file))

    raise Found
except Found:
    #rmtree('zip')
    pass
