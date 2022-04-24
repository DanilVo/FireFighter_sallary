from tkinter import *

class Window:

    def __init__(self, height, width, title='NewWindow'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+300+300')

    def widget(self, text='', bg=""):
        self.label = Label(self.root,bg='yellow',text='123')
        self.label.pack()
        print("ok")

    def widget_button(self, text=''):
        self.button = Button(self.root,text='hello')
        self.button.pack()

    def run(self):
        # self.widget()
        self.root.mainloop()

    def child_window(self,width, height, title='ChildWindow'):
        child_window(self.root, width, height, title='ChildWindow')


class child_window:
    def __init__(self, parent, width, height, title='NewWindow'):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+300+300')

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

window = Window(200,200)
window.widget(text='123',bg='green')
window.widget_button()
# window.child_window(300,300)
window.run()