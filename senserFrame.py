#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
-------------------------------------------------------------------------------
   Name:         senserFrame
   Description:  
   Author:       腾腾
   Date:         2022/1/2
-------------------------------------------------------------------------------
   Change Activity:
                 2022/1/2
"""

__author__ = "tengteng"
__version__ = "1.0.0"

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class SensorFrame
###########################################################################

class SensorFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"交通基础设施传感器仿真系统", pos=wx.DefaultPosition,
                          size=wx.Size(791, 651), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"通道选择：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        wSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        selectRadioBoxChoices = [u"TCP通道", u"UDP通道"]
        self.selectRadioBox = wx.RadioBox(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          selectRadioBoxChoices, 2, wx.RA_SPECIFY_COLS)
        self.selectRadioBox.SetSelection(1)
        self.selectRadioBox.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.selectRadioBox.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
        self.selectRadioBox.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        wSizer1.Add(self.selectRadioBox, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        wSizer1.Add((20, 0), 1, wx.EXPAND, 5)

        self.startCollect = wx.Button(self.m_panel1, wx.ID_ANY, u"启动采集", wx.DefaultPosition, wx.DefaultSize, 0)

        self.startCollect.SetAuthNeeded()
        wSizer1.Add(self.startCollect, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(wSizer1, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.SetMinSize(wx.Size(-1, 400))
        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-2, -1),
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        self.m_textCtrl1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
        self.m_textCtrl1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer4.Add(self.m_textCtrl1, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"数据展示"), wx.VERTICAL)

        sbSizer1.SetMinSize(wx.Size(-1, 100))
        m_choice1Choices = [u"通道1(UDP) 温湿度传感器 温度", u"通道1(UDP) 温湿度传感器 湿度", u"通道1(UDP) 武隆方向挠度基准点 水位",
                            u"通道1(UDP) 武隆方向1#引拱挠度 水位", u"通道1(UDP) 武隆方向挠度 水位", u"通道1(UDP) 跨中挠度 水位",
                            u"通道2(TCP) 主拱跨中1# 微应变值", u"通道2(TCP) 主拱跨中1# 温度值", u"通道2(TCP) 主拱跨中2# 微应变值",
                            u"通道2(TCP) 主拱跨中2# 温度值", u"通道2(TCP) 主拱跨中3# 微应变值", u"通道2(TCP) 主拱跨中3# 温度值",
                            u"通道2(TCP) 主拱跨中4# 微应变值", u"通道2(TCP) 主拱跨中4# 温度值", u"通道2(TCP) 主拱跨中5# 微应变值",
                            u"通道2(TCP) 主拱跨中5# 温度值", wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString]
        self.m_choice1 = wx.Choice(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        self.m_choice1.SetMinSize(wx.Size(400, -1))
        self.m_choice1.SetMaxSize(wx.Size(1000, -1))

        sbSizer1.Add(self.m_choice1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.showButton = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"显示采集值的变化趋势", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sbSizer1.Add(self.showButton, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        sbSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        bSizer3.Add(sbSizer1, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.timer = wx.Timer()
        self.timer.SetOwner(self, wx.ID_ANY)
        self.timer.Start(1000)

        self.Centre(wx.BOTH)

        # Connect Events
        self.selectRadioBox.Bind(wx.EVT_RADIOBOX, self.selectRadioBoxOnRadioBox)
        self.startCollect.Bind(wx.EVT_BUTTON, self.startCollectOnButtonClick)
        self.showButton.Bind(wx.EVT_BUTTON, self.showTheLineButtonClick)
        self.Bind(wx.EVT_TIMER, self.timerOnTimer, id=wx.ID_ANY)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def selectRadioBoxOnRadioBox(self, event):
        event.Skip()

    def startCollectOnButtonClick(self, event):
        event.Skip()

    def showTheLineButtonClick(self, event):
        event.Skip()

    def timerOnTimer(self, event):
        event.Skip()
