#coding=utf-8

import os
import time
import datetime
from settings import IMAGE_RESOURCES

def _(msg):
    return msg

def make_file_path():
    today = datetime.date.today()
    year = today.year
    month = today.month
    path = "%s/%i/%i" % (IMAGE_RESOURCES, year, month)
    if not os.path.exists(path):
        os.makedirs(path)

    return path

def make_file_name(extension=""):
    ''' 随机生成图片名称 '''
    path = make_file_path()
    timestamp = time.time()
    file_name = "%s/%s.%s" % (path, timestamp, extension)
    return file_name
