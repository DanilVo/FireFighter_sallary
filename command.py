import tkinter as tk


# refers to to (submite_but) to add data
def registration_data():
    win_name = open('registration_name.csv', 'a')
    win_name.write(f'{name_entry.get()}\n')
    win_name.close()

    win_password = open('registration_password.csv', 'a')
    win_password.write(f'{password_entry.get()}\n')
    win_password.close()

def new_user():

    global name_entry
    global password_entry

    register_window = tk.Tk()
    register_window.title('registration')
    register_window.geometry('300x400')

    name_lable = tk.Label(register_window, text="enter your name:")
    name_lable.grid(row=0,column=0)
    name_entry = tk.Entry(register_window)
    name_entry.grid(row=0,column=1)
    
    password_lable = tk.Label(register_window, text="enter your password:")
    password_lable.grid(row=1,column=0)
    password_entry = tk.Entry(register_window)
    password_entry.grid(row=1,column=1)


    submite_but = tk.Button(register_window,text='Save new user!', command= registration_data)
    submite_but.grid(row=2,column=0)

    register_window.mainloop()

