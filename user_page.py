import tkinter as tk
import datetime
from command import *
# from main_page import user_id

x = 0
def time_start():
    global x
    x = datetime.datetime.now()
    print(x)

y = 0
def time_exit():
    global y
    y = datetime.datetime.now()
    tk.Label(user_page,text=y-x).grid(row=1,column=0)
    print(y)


user_id1 = 0
def user_interface(user_id):
    global user_id1
    global user_page
    user_id1 = user_id
    user_page = tk.Tk()
    user_page.geometry('300x400')
    user_page.title('My profile')

    set_enterence = tk.Button(user_page,text='Start timer',command=time_start )
    set_enterence.grid(row=0,column=0)
    set_exit = tk.Button(user_page,text='Stop timer',command=time_exit )
    set_exit.grid(row=0,column=1)
    set_finish = tk.Button(user_page,text='finish',command=write_time )
    set_finish.grid(row=0,column=2)

    

    user_page.mainloop()


def write_time():
    global user_id1
    book = openpyxl.load_workbook('User information.xlsx')
    ws = book.worksheets[user_id1]
    row_number = ws.max_row
    ws.insert_rows(row_number + 1)
    ws[row_number+1][0].value = x
    ws[row_number+1][1].value = y
    ws[row_number+1][2].value = y-x
    book.save('User information.xlsx')
    book.close()
    print(user_id1)
