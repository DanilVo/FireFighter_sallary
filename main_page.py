from command import *
from user_page import *

def enter_user():
    book = openpyxl.open('Data.xlsx', read_only=True)
    sheet = book.active

    for row in range(1,sheet.max_column):
        if entry_name.get() == sheet[row][1].value and entry_passwork.get() == sheet[row][2].value:
            user_interface()
            print('work')
        elif entry_name.get() not in sheet[row][1].value or entry_passwork.get() not in sheet[row][2].value:
            print("error")
    
pro = tk.Tk()
pro.geometry('300x400')
pro.title('Project to porfolio')

global entry_name
global entry_passwork

tk.Label(pro, text='enter you name').grid(sticky='w')
entry_name = tk.Entry()
entry_name.grid(row=0, column=1)
tk.Label(pro, text='enter you password').grid()
entry_passwork = tk.Entry()
entry_passwork.grid(row=1, column=1)

# add (login_enter command)
enter = tk.Button(pro, text='Enter', command=enter_user).grid()
register = tk.Button(pro, text='Registration', command=new_user).grid()


pro.mainloop()

# # add in additional file: registration data

