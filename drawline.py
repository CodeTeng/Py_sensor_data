#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         drawLine
   Description:  
   Author:       腾腾
   Date:         2022/1/7
-------------------------------------------------------------------------------
   Change Activity:
                 2022/1/7
"""

__author__ = "tengteng"
__version__ = "1.0.0"

import matplotlib.pyplot as plt


def drawLine(squares, titleName, unit):
    # 设置图标标题 并给坐标轴加上标签
    plt.rc("font", family='YouYuan')
    plt.plot(squares, linewidth=2)
    plt.title(titleName, fontsize=24)
    plt.xlabel("时间", fontsize=14)
    plt.ylabel("值"+unit, fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.show()

