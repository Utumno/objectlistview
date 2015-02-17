# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------
# TESTING ONLY
#----------------------------------------------------------------------------

import wx
import ObjectListView as olv

# Where can we find the Example module?
import sys
sys.path.append("../Examples")

import ExampleModel
import ExampleImages

class MyFrame(wx.Frame):

	def __init__(self, *args, **kwds):
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)

		self.panel = wx.Panel(self, -1)
		#self.lv = ObjectListView(self.panel, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
		self.lv = olv.GroupListView(
		    self.panel, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
		#self.lv = FastObjectListView(self.panel, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.lv, 1, wx.ALL | wx.EXPAND, 4)
		self.panel.SetSizer(sizer_2)
		self.panel.Layout()

		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_1.Add(self.panel, 1, wx.EXPAND)
		self.SetSizer(sizer_1)
		self.Layout()

		musicImage = self.lv.AddImages(
		    ExampleImages.Music16.GetBitmap(),
		    ExampleImages.Music32.GetBitmap())
		artistImage = self.lv.AddImages(
		    ExampleImages.User16.GetBitmap(),
		    ExampleImages.User32.GetBitmap())

		self.lv.SetColumns([
		    olv.ColumnDefn(
		        "Title", "left", 200, "title",
		        imageGetter=musicImage),
		    olv.ColumnDefn(
		        "Artist", "left", 150, "artist",
		        imageGetter=artistImage),
		    olv.ColumnDefn(
		        "Last Played", "left", 100, "lastPlayed"),
		    olv.ColumnDefn(
		        "Size", "center", 100, "sizeInBytes"),
		    olv.ColumnDefn(
		        "Rating", "center", 100, "rating"), ])

		# self.lv.CreateCheckStateColumn()
		self.lv.SetSortColumn(self.lv.columns[2])
		self.lv.SetObjects(ExampleModel.GetTracks())

		wx.CallLater(50, self.run)

	def run(self):
		printer = olv.ListCtrlPrinter(
		    self.lv,
		    "Playing with ListCtrl Printing")
		printer.ReportFormat = olv.ReportFormat.Normal()
		printer.ReportFormat.WatermarkFormat(over=True)
		printer.ReportFormat.IsColumnHeadingsOnEachPage = True

		#printer.ReportFormat.Page.Add(ImageDecoration(ExampleImages.getGroup32Bitmap(), wx.RIGHT, wx.BOTTOM))

		# printer.PageHeader("%(listTitle)s") # nice idea but not possible
		# at the moment
		printer.PageHeader = "Playing with ListCtrl Printing"
		printer.PageFooter = (
		    "Bright Ideas Software",
		    "%(date)s",
		    "%(currentPage)d of %(totalPages)d")
		printer.Watermark = "Sloth!"

		# printer.PageSetup()
		printer.PrintPreview(self)


app = wx.App(0)
#wx.InitAllImageHandlers()
frame_1 = MyFrame(None, -1, "")
app.SetTopWindow(frame_1)
frame_1.Show()
app.MainLoop()
