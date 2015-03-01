#!/usr/bin/env python

import sys
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
from tkinter import Tk
import tkinter.messagebox as mbox

curdir = None
if getattr(sys, 'frozen', False):
	# frozen
	curdir = path.dirname(sys.executable)
else:
	# unfrozen
	curdir = path.dirname(path.abspath(__file__))

mylabel = path.join(curdir,'my.label')
window = Tk()
window.wm_withdraw()

if not path.isfile(mylabel):
	mbox.showinfo('PyDymoLabel','Template file my.label does not exist')
	sys.exit(1)

try:
	now = datetime.now()
	next = now + timedelta(30)

	labelCom = Dispatch('Dymo.DymoAddIn')
	labelText = Dispatch('Dymo.DymoLabels')
	isOpen = labelCom.Open(mylabel)
	selectPrinter = 'DYMO LabelWriter 450'
	labelCom.SelectPrinter(selectPrinter)

	labelText.SetField('TESTO2', now.strftime('%Y/%m/%d'))
	labelText.SetField('TESTO4', next.strftime('%Y/%m/%d'))

	labelCom.StartPrintJob()
	labelCom.Print(1,False)
	labelCom.EndPrintJob()
except:
	mbox.showinfo('PyDymoLabel','An error occurred during printing.')
	sys.exit(1)

mbox.showinfo('PyDymoLabel','Label printed!')
sys.exit(0)