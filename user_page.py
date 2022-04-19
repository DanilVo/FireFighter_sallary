import tkinter as tk
import datetime
from command import *

def time_start():
    global x
    x = datetime.datetime.now()
    print(x)

def time_exit():
    global y
    y = datetime.datetime.now()
    tk.Label(user_page,text=y-x).grid(row=1,column=0)
    print(y)

def write_time():
    book = openpyxl.load_workbook('User information.xlsx')
    ws = book.worksheets[row_number]
    ws[row_number+1][0].value = x
    ws[row_number+1][1].value = y
    ws[row_number+1][2].value = y-x
    book.save('User information.xlsx')
    book.close()

def user_interface():
    global user_page
    user_page = tk.Tk()
    user_page.geometry('300x400')
    user_page.title('My profile')

    set_enterence = tk.Button(user_page,text='Start timer',command=time_start )
    set_enterence.grid(row=0,column=0)
    set_exit = tk.Button(user_page,text='Stop timer',command=time_exit )
    set_exit.grid(row=0,column=1)

    

    user_page.mainloop()


