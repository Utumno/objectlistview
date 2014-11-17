import wtc
import unittest
import wx
from datetime import datetime, date, time

import sys
sys.path.append("..")
from ObjectListView.CellEditor import BooleanEditor, DateEditor, DateTimeEditor, TimeEditor

#----------------------------------------------------------------------------

class TestBooleanEditor(wtc.WidgetTestCase):

    def testBasics(self):
        self.editor = BooleanEditor(self.frame)
        self.editor.SetValue(False)
        self.assertEqual(self.editor.GetValue(), False)
        self.editor.SetValue(True)
        self.assertEqual(self.editor.GetValue(), True)

#----------------------------------------------------------------------------

class TestDateEditor(wtc.WidgetTestCase):

    def testBasics(self):
        self.editor = DateEditor(self.frame)
        dt = date.today()
        self.editor.SetValue(dt)
        self.assertEqual(self.editor.GetValue(), dt)

#----------------------------------------------------------------------------

class TestDateTimeEditor(wtc.WidgetTestCase):


    def testBasics(self):
        self.editor = DateTimeEditor(self.frame, 0)
        dt = datetime.now().replace(microsecond=0)
        self.editor.SetValue(dt)
        self.assertEqual(self.editor.GetValue(), dt)

    def testParsingWithYear(self):
        self.editor = DateTimeEditor(self.frame, 0)
        tests = [
            ("31/12/2007 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31/12/2007 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31/12/2007 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31/12/2007 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("12/31/2007 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("12/31/2007 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("12/31/2007 23:59", datetime(2007, 12, 31, 23, 59)),
            ("12/31/2007 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("31-Dec-2007 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31-Dec-2007 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31-Dec-2007 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31-Dec-2007 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("31 December 2007 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31 December 2007 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31 December 2007 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31 December 2007 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("Dec 31, 2007 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("Dec 31, 2007 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("Dec 31, 2007 23:59", datetime(2007, 12, 31, 23, 59)),
            ("Dec 31, 2007 11:59 pm", datetime(2007, 12, 31, 23, 59)),
        ]
        for (txt, dt) in tests:
            #print txt
            self.editor.SetValue(txt)
            self.assertEqual(self.editor.GetValue(), dt)

    def testParsingWithoutYear(self):
        self.editor = DateTimeEditor(self.frame, 0)
        tests = [
            ("31/12 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31/12 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31/12 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31/12 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("12/31 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("12/31 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("12/31 23:59", datetime(2007, 12, 31, 23, 59)),
            ("12/31 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("31-Dec 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31-Dec 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31-Dec 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31-Dec 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("31 December 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("31 December 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("31 December 23:59", datetime(2007, 12, 31, 23, 59)),
            ("31 December 11:59 pm", datetime(2007, 12, 31, 23, 59)),
            ("Dec 31 23:59:59", datetime(2007, 12, 31, 23, 59, 59)),
            ("Dec 31 11:59:59 pm", datetime(2007, 12, 31, 23, 59, 59)),
            ("Dec 31 23:59", datetime(2007, 12, 31, 23, 59)),
            ("Dec 31 11:59 pm", datetime(2007, 12, 31, 23, 59)),
        ]
        thisYear = datetime.now().year
        for (txt, dt) in tests:
            #print txt
            self.editor.SetValue(txt)
            self.assertEqual(self.editor.GetValue(), dt.replace(year=thisYear))

#----------------------------------------------------------------------------

class TestTimeEditor(wtc.WidgetTestCase):

    def testBasics(self):
        self.editor = TimeEditor(self.frame, 0)
        t = datetime.now().time().replace(microsecond=0)
        self.editor.SetValue(t)
        self.assertEqual(self.editor.GetValue(), t)

#======================================================================
# MAINLINE

if __name__ == '__main__':
    unittest.main()
