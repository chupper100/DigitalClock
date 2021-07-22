from tkinter import*
from tkinter.ttk import*
from time import strftime

def choose_lang():
	user_choice=input('en: English, vi: Vietnamese')
	user_choice=user_choice.lower()
	lang_data={
	'en': 'English',
	'vi': 'Vietnamese'
	}
	user_choice=lang_data[user_choice]
	print('You choosed', user_choice)
	return user_choice

def lang_en(word):
	data_en={
		'Mon': 'Monday',
		'Tue': 'Tuesday',
		'Wed': 'Wednesday',
		'Thu': 'Thursday',
		'Fri': 'Friday',
		'Sat': 'Saturday',
		'Sun': 'Sunday'
		}

def lang_vi(word):
	data_vi={
		'Monday': 'Thứ hai',
		'Tuesday': 'Thứ ba',
		'Wednesday': 'Thứ tư',
		'Thursday': 'Thứ năm',
		'Friday': 'Thứ sáu',
		'Saturday': 'Thứ bảy',
		'Sunday': 'Chủ nhật',
}
	translate_data=data[word]
	return translate_data

formattedday = daydata_eng[strftime('%a')]

def lang_vi(word):
	content=daydata_eng
	data={
		'Monday': 'Thứ hai',
		'Tuesday': 'Thứ ba',
		'Wednesday': 'Thứ tư',
		'Thursday': 'Thứ năm',
		'Friday': 'Thứ sáu',
		'Saturday': 'Thứ bảy',
		'Sunday': 'Chủ nhật',
}
	translate_data=data[word]
	return translate_data

def clock():
    timestring=strftime(f'%H:%M:%S%p\nNgày: {translate_vi()}')
    label.config(text=timestring)
    label.after(1000,clock)

root=Tk()
root.title("Digital Clock")

label=Label(root, font=("Digital-7",100), background = input('Background:'), foreground = input('Foreground:'))
label.pack(anchor='center')
clock()
root.mainloop()
#End
