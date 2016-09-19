#!/usr/bin/env python

import sys
from os import path
from datetime import datetime, timedelta
from win32com.client import Dispatch
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry

def center(win):
	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	x = (win.winfo_screenwidth() // 2) - (width // 2)
	y = (win.winfo_screenheight() // 2) - (height // 2)
	win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def printLabels():
	num_labels = e.get()
	if not num_labels.isnumeric():
		labelmsg.config(text="Plese enter a number!")
		return
	labelmsg.config(text="")
	e.configure(state='disabled')
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
		labelCom.Print(num_labels,False)
		labelCom.EndPrintJob()

		labelmsg.configure(text='Labels printed!')
	except:
		labelmsg.configure(text='An error occurred during printing.')

	e.configure(state='normal')
	submit.configure(state='normal')

curdir = None
if getattr(sys, 'frozen', False):
	# frozen
	curdir = path.dirname(sys.executable)
else:
	# unfrozen
	curdir = path.dirname(path.abspath(__file__))

mylabel = path.join(curdir,'my.label')
root = Tk()
root.geometry('280x100')
root.resizable(width=False, height=False)
root.title('PyDymoLabel by Chip2Bit')
center(root)

label = Label(root, text="How many labels to print?")
e = Entry(root, justify='right')
e.focus_set()
e.insert(0,'1') # 1 is default
labelmsg = Label(root, text="")

num_labels = 0

if not path.isfile(mylabel):
	labelmsg.Label(root,text='Template file my.label does not exist')
	e.configure(state='disabled')
	submit.configure(state='disabled')

submit = Button(root, text ="Print", command = printLabels)

label.pack()
e.pack()
labelmsg.pack()
submit.pack()

root.mainloop()

