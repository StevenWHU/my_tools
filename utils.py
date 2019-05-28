#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2019/5/28 21:29
# @Author  : Steven Chai
# @File    : utils.py
# @Software: PyCharm


import numpy as np
from tqdm import tqdm

# 写内容到txt
def save_as_txt(path, content):
    """
    将指定内容保存到指定的txt文件中。
    :param path: 指定的txt文件路径。
    :param content: 要保存的内容，可以是字符串类型（string）或者numpy数组类型。
    :return:
    """
    if type(content) == str:
        mode = 1
        with open(path, "w") as f:
            f.write(content)
    elif type(content) == np.ndarray:
        mode = 2
        np.savetxt(fname=path, X=content)
    else:
        raise ValueError
    return print("Saving file:'", path, "'in mode:", mode)

# list去重
def duplicate_removal(source_list):
    """
    去除list中的重复元素。
    :param source_list: 输入待处理的list
    :return: 去重的新list。
    """
    em_list = list()
    for li in tqdm(source_list):
        if li not in em_list:
            em_list.append(li)
    return em_list

# 检查文件是否存在
def fileExistCheck(file_path):
    """
    check the specific file weather exists or not. If not, raise the error.
    :param file_path: file path.
    :return:
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError