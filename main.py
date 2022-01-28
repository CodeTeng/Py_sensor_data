#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         main
   Description:  
   Author:       腾腾
   Date:         2022/1/2
-------------------------------------------------------------------------------
   Change Activity:
                 2022/1/2
"""

__author__ = "tengteng"
__version__ = "1.0.0"

import wx
import senserFrame
import tcpclient
import udpclient
import drawline


class MainWindow(senserFrame.SensorFrame):
    def init_memory(self):
        self.start = 0  # 标志启动或者停止采集数据
        # 用于存储实时数据
        self.udpdata = []
        self.tcpdata = []

        for i in range(0, 6):
            self.udpdata.append({})
            self.tcpdata.append({})
        # 记录数据，用于绘制曲线，初始化
        self.clearUDPRecordData()
        self.clearTCPRecordData()

    def selectRadioBoxOnRadioBox(self, event):
        event.Skip()

    def clearUDPRecordData(self):
        self.udpd1_T = []  # 温湿度传感器的温度
        self.udpd1_H = []  # 温湿度传感器的湿度
        self.udpd2 = []  # 静力水准仪2 武隆方向挠度基准点
        self.udpd3 = []  # 静力水准仪3 武隆方向1#引拱挠度
        self.udpd4 = []  # 静力水准仪4 武隆方向挠度
        self.udpd5 = []  # 静力水准仪5 跨中挠度

    def clearTCPRecordData(self):
        self.tcpd1_W = []  # 应变1 微应变值
        self.tcpd1_T = []  # 应变1 温度值
        self.tcpd2_W = []  # 应变2 微应变值
        self.tcpd2_T = []  # 应变2 温度值
        self.tcpd3_W = []  # 应变3 微应变值
        self.tcpd3_T = []  # 应变3 温度值
        self.tcpd4_W = []  # 应变4 微应变值
        self.tcpd4_T = []  # 应变4 温度值
        self.tcpd5_W = []  # 应变5 微应变值
        self.tcpd5_T = []  # 应变5 温度值

    def addUDPDataToRecord(self):
        self.udpd1_T.append(self.udpdata[0]["温度值"])  # 温湿度传感器的温度
        self.udpd1_H.append(self.udpdata[0]["湿度值"])  # 温湿度传感器的湿度
        self.udpd2.append(self.udpdata[1]["水位值"])  # 静力水准仪2 武隆方向挠度基准点
        self.udpd3.append(self.udpdata[2]["水位值"])  # 静力水准仪3 武隆方向1#引拱挠度
        self.udpd4.append(self.udpdata[3]["水位值"])  # 静力水准仪4 武隆方向挠度
        self.udpd5.append(self.udpdata[4]["水位值"])  # 静力水准仪5 跨中挠度

    def addTCPDataToRecord(self):
        self.tcpd1_W.append(self.tcpdata[0]["微应变值"])  # 应变1 微应变值
        self.tcpd1_T.append(self.tcpdata[0]["温度值"])  # 应变1 温度值
        self.tcpd2_W.append(self.tcpdata[1]["微应变值"])  # 应变2 微应变值
        self.tcpd2_T.append(self.tcpdata[1]["温度值"])  # 应变2 温度值
        self.tcpd3_W.append(self.tcpdata[2]["微应变值"])  # 应变3 微应变值
        self.tcpd3_T.append(self.tcpdata[2]["温度值"])  # 应变3 温度值
        self.tcpd4_W.append(self.tcpdata[3]["微应变值"])  # 应变4 微应变值
        self.tcpd4_T.append(self.tcpdata[3]["温度值"])  # 应变4 温度值
        self.tcpd5_W.append(self.tcpdata[4]["微应变值"])  # 应变5 微应变值
        self.tcpd5_T.append(self.tcpdata[4]["温度值"])  # 应变5 温度值

    def startCollectOnButtonClick(self, event):
        if self.start == 0:
            self.start = 1
            # 清空记录数据
            self.clearUDPRecordData()
            self.clearTCPRecordData()
            self.startCollect.SetLabel("停止采集")
        elif self.start == 1:
            self.start = 0
            self.startCollect.SetLabel("启动采集")

    # 定时1s更新数据
    def timerOnTimer(self, event):
        if self.start == 1:
            if self.selectRadioBox.GetSelection() == 0:
                # 获取TCP通道数据
                s1 = tcpclient.getTcpData(self.tcpdata)
                # 显示在文本框
                if s1 != "":
                    self.m_textCtrl1.SetValue(s1)
                    self.addTCPDataToRecord()
            elif self.selectRadioBox.GetSelection() == 1:
                # 获取UDP通道数据
                s1 = udpclient.getUDPData(self.udpdata)
                # 显示在文本框
                if s1 != "":
                    self.m_textCtrl1.SetValue(s1)
                    self.addUDPDataToRecord()
        else:
            self.m_textCtrl1.SetValue("请启动数据采集。")

    def showTheLineButtonClick(self, event):
        if self.start == 1:
            self.m_staticText2.SetLabel("请先关闭 采集通道")
        else:
            self.m_staticText2.SetLabel("")
            st1 = self.m_choice1.GetString(self.m_choice1.GetSelection())
            if self.m_choice1.GetSelection() == 0:
                if len(self.udpd1_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd1_T, st1, "  单位：℃")
            elif self.m_choice1.GetSelection() == 1:
                if len(self.udpd1_H) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd1_H, st1, "  单位：%")
            elif self.m_choice1.GetSelection() == 2:
                if len(self.udpd2) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd2, st1, "  单位：mm")
            elif self.m_choice1.GetSelection() == 3:
                if len(self.udpd3) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd3, st1, "  单位：mm")
            elif self.m_choice1.GetSelection() == 4:
                if len(self.udpd4) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd4, st1, "  单位：mm")
            elif self.m_choice1.GetSelection() == 5:
                if len(self.udpd5) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.udpd5, st1, "  单位：mm")
            elif self.m_choice1.GetSelection() == 6:
                if len(self.tcpd1_W) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd1_W, st1, "  单位：无")
            elif self.m_choice1.GetSelection() == 7:
                if len(self.tcpd1_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd1_T, st1, "  单位：℃")
            elif self.m_choice1.GetSelection() == 8:
                if len(self.tcpd2_W) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd2_W, st1, "  单位：无")
            elif self.m_choice1.GetSelection() == 9:
                if len(self.tcpd2_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd2_T, st1, "  单位：℃")
            elif self.m_choice1.GetSelection() == 10:
                if len(self.tcpd3_W) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd3_W, st1, "  单位：无")
            elif self.m_choice1.GetSelection() == 11:
                if len(self.tcpd3_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd3_T, st1, "  单位：℃")
            elif self.m_choice1.GetSelection() == 12:
                if len(self.tcpd4_W) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd4_W, st1, "  单位：无")
            elif self.m_choice1.GetSelection() == 13:
                if len(self.tcpd4_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd4_T, st1, "  单位：℃")
            elif self.m_choice1.GetSelection() == 14:
                if len(self.tcpd5_W) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd5_W, st1, "  单位：无")
            elif self.m_choice1.GetSelection() == 15:
                if len(self.tcpd5_T) == 0:
                    self.m_staticText2.SetLabel(st1 + "  没有采集数据")
                else:
                    drawline.drawLine(self.tcpd5_T, st1, "  单位：℃")


if __name__ == '__main__':
    app = wx.App()
    main_window = MainWindow(None)
    # 初始化流程参数
    main_window.init_memory()
    # 显示窗口
    main_window.Show()
    app.MainLoop()
