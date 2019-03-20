# -*- coding: utf-8 -*-

import os
import aliyun_asr
import subprocess


def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for i in files:
            if os.path.splitext(i)[1] == '.WAV' or os.path.splitext(i)[1] == '.wav':
                file_list.append(i)
    return file_list

def call_asr(file):
    accessKeyId = "LTAI7kN9Ybw0eyid"
    accessKeySecret = "CYpRA3wtY4NzL6DWFcZ0rgxnggSq5t"
    appKey = "O00ha9whK1dxP2dk"
    fileLink = "http://audio.luowr.com:5009/download/"
    file_list = file_name(file)
    print(file_list)
    for i in file_list:
        print(i)
        fileLink = fileLink + i
        result = aliyun_asr.fileTrans(accessKeyId,accessKeySecret,appKey,fileLink)
        f = open('/home/gmy/'+os.path.splitext(i)[0]+'.txt','w')
        f.write(str(result))
        f.close()
#音频文件格式转换
def ffmpeg(src_path, dst_path):
    command = "ffmpeg -y -i '{}' -ar 16000  '{}' ".format(src_path, dst_path)
    try:
        subprocess.check_call(command, shell=True)
        is_success = True
    except subprocess.CalledProcessError as e:
        print ("error code: {}! shell command: {}".format(e.returncode, e.cmd))
        is_success = False
    return is_success

# file_list = file_name('/home/gmy/Documents/北京金茂府')
# file_list = file_name('/home/gmy/Documents/test')
# print(file_list)

call_asr('/home/gmy/Documents/test')
