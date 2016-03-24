#-*- coding:utf-8 -*-

"""我的第一个窗体程序"""

import wx
import namemodel

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

class MyFrame(wx.Frame):
	def __init__(self, parent = None, title = u'收银系统', size = wx.DefaultSize, pos = wx.DefaultPosition):
		wx.Frame.__init__(self, parent, title = title, size = size, pos = pos, style = wx.DEFAULT_FRAME_STYLE)

		self.textFields = {}

		#面板
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('White')

		#按钮
		button = wx.Button(self.panel, label = u'对话...', size = (100, 30), pos = (20, 20))
		self.Bind(wx.EVT_BUTTON, self.OnButton, button)

		#状态栏、工具栏
		self.statusBar = self.CreateStatusBar()
		self.toolBar = self.CreateToolBar()

		#设置状态栏
		self.statusBar.SetFieldsCount(3)
		self.statusBar.SetStatusWidths([-1, -2, -3])

		#菜单
		menuBar = wx.MenuBar()
		self.SetMenuBar(menuBar)

		menuFile = wx.Menu()
		menuTool = wx.Menu()
		menuEdit = wx.Menu()
		menuBar.Append(menuFile, title = u'文件')
		menuBar.Append(menuTool, title = u'编辑')
		menuBar.Append(menuEdit, title = u'工具')

		menuColor = wx.Menu()
		menuColor.AppendCheckItem(id = wx.ID_ANY, text = u'红色')
		menuColor.AppendCheckItem(id = wx.ID_ANY, text = u'蓝色')
		menuColor.AppendCheckItem(id = wx.ID_ANY, text = u'黄色')

		menuCommonColor = wx.Menu()
		menuCommonColor.Append(id = wx.ID_ANY, text = u'黑色', kind = wx.ITEM_CHECK)
		menuCommonColor.Append(id = wx.ID_ANY, text = u'白色', kind = wx.ITEM_CHECK)
		menuCommonColor.Append(id = wx.ID_ANY, text = u'红色', kind = wx.ITEM_CHECK)

		menuColor.AppendMenu(id = wx.ID_ANY, text = u'常用色', submenu = menuCommonColor)

		menuFormat = wx.Menu()
		menuFormat.AppendRadioItem(id = wx.ID_ANY, text = 'txt')
		menuFormat.AppendRadioItem(id = wx.ID_ANY, text = 'jpg')
		menuFormat.AppendRadioItem(id = wx.ID_ANY, text = 'gif')

		menuFile.AppendMenu(id = wx.ID_ANY, text = u'颜色', submenu = menuColor)
		menuFile.AppendMenu(id = wx.ID_ANY, text= u'格式', submenu = menuFormat)

		self.textFields['first_name'] = wx.TextCtrl(self.panel, id = wx.ID_ANY)
		self.textFields['last_name']  = wx.TextCtrl(self.panel, id = wx.ID_ANY,pos = (200, 0))

		#事件
		self.Bind(wx.EVT_LEFT_DCLICK, self.DoubleClick, self.panel)
		self.panel.Bind(wx.EVT_MOTION, self.OnMotion)

		self.nameModel = namemodel.NameModel('', '')
		self.nameModel.addListener(self.OnUpdate)

	def OnUpdate(self, model):
		self.textFields['first_name'].SetValue(model.firstName)
		self.textFields['last_name'].SetValue(model.lastName)

	def DoubleClick(self, e):
		print u'双击'

	def OnMotion(self, e):
		self.statusBar.SetStatusText(str(e.GetPosition()), 2)
		e.Skip()

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
		first = u'李';
		last = u'雷';
		self.nameModel.set(first, last)


if __name__ == '__main__':
	app = MyApp(False)
	app.MainLoop()
