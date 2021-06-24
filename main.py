from tkinter import*
from tkinter.ttk import*
from time import strftime

daydata={
	'Mon': 'Monday',
	'Tue': 'Tuesday',
	'Wed': 'Wednesday',
	'Thu': 'Thursday'
}
formattedday = daydata[strftime('%a')]

def clock():
    timestring=strftime(f'%H:%M:%S%p\nDay: {formattedday}')
    label.config(text=timestring)
    label.after(1000,clock)

root=Tk()
root.title("Digital Clock")

label=Label(root, font=("Digital-7",100), background = input('Background:'), foreground = input('Foreground:'))
label.pack(anchor='center')
clock()
root.mainloop()
