from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Digital Clock")

def clock():
	timestring=strftime('%H:%M:%S%p\nDay: %a')
	label.config(text=timestring)
	label.after(1000,clock)

label=Label(root, font=("Digital-7",100), background = input('Background:'), foreground = input('Foreground:'))
label.pack(anchor='center')
clock()
root.mainloop()