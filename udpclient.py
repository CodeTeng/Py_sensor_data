#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         udpclient
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


def getUDPData(list):
    names = ["环境温湿度", "武隆方向挠度基准点", "武隆方向1#引拱挠度", "武隆方向挠度", "跨中挠度"]
    udp = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM,
                        socket.IPPROTO_UDP)
    udp.setsockopt(socket.SOL_SOCKET,
                   socket.SO_REUSEADDR,
                   1)
    udp.settimeout(5)

    s1 = ""
    try:
        udp.connect(('demo-monitor.igong.com', 8001))
    except:
        print("连接UDP server失败！")
        sys.exit(1)

    try:
        # 循环获取5个站定的数据
        for index in range(1, 6):
            # 生成modbus 发送采集指令
            cmd = struct.pack('b', index)
            if index == 1:
                cmd += b'\x03\x00\x01\x00\x02'
            else:
                cmd += b'\x03\x00\x01\x00\x01'

            crc = crc16(cmd)
            cmd += crc
            udp.send(cmd)
            try:
                # 接收数据
                data, addr = udp.recvfrom(8192)
            except socket.timeout:
                print("UDP获取数据超时")
                sys.exit(1)
            # 接收数据校验
            crc = data[-2:]
            if crc != crc16(data[:-2]):
                print("UDP获取数据 CRC16校验失败！")
                sys.exit(2)
            # 将modbus的数据解析
            s1 += "测试点：" + names[index-1] + "\r\n"
            if index == 1:
                # 有两个寄存器的值 解包
                wd, sd = struct.unpack(">ii", data[4:12])
                wd = wd / 100.0
                s1 += "温湿度传感器" + str(index) + "："
                s1 += "温度值：" + str(wd) + "℃ "
                s1 += "湿度值：" + str(sd) + "%\r\n"
                list[0]["温度值"] = wd
                list[0]["湿度值"] = sd
            else:
                # 只有一个寄存器的值
                wd = struct.unpack('>i', data[4:8])
                s1 += "静力水准仪" + str(index) + ": "
                s1 += "水位值：" + str(wd[0]) + "mm\r\n"
                list[index-1]["水位值"] = wd
            print(wd, sd)

    finally:
        udp.close()

    return s1
