from calendar import c
from logging import root
from command import *
from user_page import user_interface
from tkinter import *
# def enter_user():
#     book = openpyxl.open('Data.xlsx', read_only=True)
#     sheet = book.active

#     for row in range(1,sheet.max_row):
#         if entry_name.get() == sheet[row][1].value and entry_passwork.get() == sheet[row][2].value:
#             user_interface(sheet[row][0].value)
#             print('work')
#         else:
#             print('User not found')

# pro = tk.Tk()
# pro.geometry('300x400')
# pro.title('Project to porfolio')

# global entry_name
# global entry_passwork

# tk.Label(pro, text='enter you name').grid(sticky='w')
# entry_name = tk.Entry(pro)
# entry_name.grid(row=0, column=1)
# tk.Label(pro, text='enter you password').grid()
# entry_passwork = tk.Entry(pro)
# entry_passwork.grid(row=1, column=1)

# # add (login_enter command)
# tk.Button(pro, text='Enter', command=enter_user).grid()
# tk.Button(pro, text='Registration', command=new_user).grid()

# pro.mainloop()

# # add in additional file: registration data

class Main_user:
    """Program user interface"""
    def __init__(self, height, width, title='sallary'):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+300+300')
        self.text = ''
        # self.row = 2
        # self.column = 1

    def add_text(self,text):
        self.text = text

    def make_label(self):
        Label(self.root,text=self.text).grid(row=1, column=2)
        
        
        

    def run_mainloop(self):
        self.root.mainloop()
        print('good')

window = Main_user(300,400)
window.add_text(text='hello')
window.make_label()
window.run_mainloop()        