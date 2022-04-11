from command import *
from user_page import *

# return an object
def datas(a):
    return a

# converting to list, going thrue all ojects as [list] and checking if it equals to our input, then redirect to user interface
def entry():
    win_name = list(map(datas, open('registration_name.csv')))
    for line in win_name:
        if entry_name.get() in line:
            j = 1
        else:
            print('again')
    win_password = list(map(datas, open('registration_password.csv')))
    for lines in win_password:
        if entry_passwork.get() in lines:
            k = 1
        else:
            print('again123')
    if j & k == 1:
        user_interface()

 
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
enter = tk.Button(pro, text='Enter', command=entry).grid()
register = tk.Button(pro, text='Registration', command=new_user).grid()


pro.mainloop()

# add in additional file: registration data
