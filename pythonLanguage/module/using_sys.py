#!/usr/bin/python3
# 文件名: using_sys.py

import sys


print("命令行参数个数为:", len(sys.argv), "个参数。")
for i in range(len(sys.argv)):
    print("参数", i, ":", sys.argv[i])


print("Python 路径为:", sys.path, "个参数。")