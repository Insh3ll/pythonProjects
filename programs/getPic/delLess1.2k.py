#coding=utf-8

import os

def del_files(dir_path):
    for name in os.listdir(dir_path):
        path=os.path.join(dir_path,name)
        if os.path.getsize(path)==1308L:
            os.remove(path)
    return 0

if __name__=='__main__':
    dir_path=raw_input('ipu dir_path:  ')
    del_files(dir_path)
    print 'ok!'

