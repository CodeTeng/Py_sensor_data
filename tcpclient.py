#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         tcpclient
   Description:  
   Author:       腾腾
   Date:         2022/1/2
-------------------------------------------------------------------------------
   Change Activity:
                 2022/1/2
"""

__author__ = "tengteng"
__version__ = "1.0.0"

import socket
import sys
import struct


def hextobytes(x):
    if not isinstance(x, str):
        x = str(x, 'ascii')
    return bytes.fromhex(x)


def crc16(x):
    u"""
    @summary: 计算CRC16值
    @param x: bytes
    @return: 返回2字节值，类似：b'\x7B\x2A'。
    """
    if not isinstance(x, bytes):
        raise ValueError('Parameter must be a bytes type')
    b = 0xA001
    a = 0xFFFF
    for byte in x:
        a = a ^ byte
        for _ in range(8):
            last = a % 2
            a = a >> 1
            if last == 1:
                a = a ^ b
    aa = '0' * (6 - len(hex(a))) + hex(a)[2:]
    ll, hh = int(aa[:2], 16), int(aa[2:], 16)
    rtn = '%x' % (hh * 256 + ll & 0xffff)
    while len(rtn) < 4:
        rtn = '0' + rtn
    rtn = hextobytes(rtn)
    return rtn


def getTcpData(list):
    tcp = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM,
                        socket.IPPROTO_TCP)
    tcp.setsockopt(socket.SOL_SOCKET,
                   socket.SO_REUSEADDR,
                   1)
    tcp.settimeout(5)
    s1 = ""
    try:
        tcp.connect(("demo-monitor.igong.com", 8002))
    except:
        print("连接TCP server失败！")
        sys.exit(1)
    try:
        # cmd = '010300010002'
        # cmd = bytes.fromhex(cmd)
        # 循环获取5个站点的数据
        for index in range(1, 6):
            # 生成modbus 发送采集的指令
            cmd = struct.pack('b', index)
            cmd += b'\x03\x00\x01\x00\x02'
            crc = crc16(cmd)
            cmd += crc
            tcp.send(cmd)
            try:
                data = tcp.recv(8192)
            except socket.timeout:
                print("TCP获取数据超时")
                sys.exit(1)
            crc = data[-2:]
            if crc != crc16(data[:-2]):
                print("TCP获取数据CRC16校验失败")
                sys.exit(2)
            # 接收数据 解包
            yb, wd = struct.unpack('>ii', data[4:12])
            yb = yb / 100.0
            wd = wd / 100.0

            s1 += "测试点：主拱跨中" + str(index) + "#应变\r\n"
            s1 += "微应变值：" + str(yb) + " "
            s1 += "温度值：" + str(wd) + "℃\r\n"
            list[index-1]["微应变值"] = yb
            list[index-1]["温度值"] = wd
            print(yb, wd)
    finally:
        tcp.close()

    return s1
