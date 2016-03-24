#-*- coding:utf-8 -*-

"""我的第一个窗体程序"""

import wx
import imageop

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

class MyFrame(wx.Frame):
	def __init__(self, parent = None, title = u'收银系统', size = wx.DefaultSize, pos = wx.DefaultPosition):
		wx.Frame.__init__(self, parent, title = title, size = size, pos = pos, style = wx.DEFAULT_FRAME_STYLE)

		#面板
		panel = wx.Panel(self)
		panel.SetBackgroundColour('White')

		#按钮
		button = wx.Button(panel, label = u'对话...', size = (100, 30), pos = (20, 20))

		#状态栏、工具栏
		self.CreateStatusBar()
		self.toolBar = self.CreateToolBar()

		#菜单
		self.menuBar = wx.MenuBar()
		menu1 = wx.Menu()
		textMenuItem = menu1.Append(id = wx.ID_ANY, text = u'文本', help = u'输入文本')
		colorMenuItem = menu1.Append(id = wx.ID_ANY, text = u'选择颜色', help = u'请从列表中选择颜色')

		self.menuBar.Append(menu1, title = u'菜单')
		self.SetMenuBar(self.menuBar)

		#事件
		self.Bind(wx.EVT_BUTTON, self.OnClick, button)
		self.Bind(wx.EVT_MENU, self.OnText, textMenuItem)
		self.Bind(wx.EVT_MENU, self.OnChoice, colorMenuItem)
		self.Bind(wx.EVT_LEFT_DCLICK, self.DoubleClick, panel)

	def DoubleClick(self, e):
		print u'双击'

	def OnClick(self, e):
		dlg = wx.MessageDialog(None, message = u'确定要执行以下操作吗？', caption = u'删除提示', style = wx.YES|wx.NO)
		if dlg.ShowModal() == wx.ID_YES:
			print 'yes'
		else:
			print 'no'
		dlg.Destroy()

	def OnChoice(self, e):
		dlg = wx.SingleChoiceDialog(None, message = u'请选择你喜欢的颜色：', caption = u'颜色', choices = [u'红色', u'蓝色', u'绿色'], style = wx.OK|wx.CANCEL)
		if dlg.ShowModal() == wx.ID_OK:
			print dlg.GetStringSelection()
		dlg.Destroy()

	def OnText(self, e):
		dlg = wx.TextEntryDialog(None, message = u'请输入姓名：', caption = u'姓名', style = wx.OK|wx.CANCEL)
		if dlg.ShowModal() == wx.ID_OK:
			val = dlg.GetValue()
			print val
		dlg.Destroy()

	def OnButton(self, e):
		self.Close()


if __name__ == '__main__':
	app = MyApp(False)
	app.MainLoop()
