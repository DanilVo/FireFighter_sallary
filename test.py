from cProfile import label
from socketserver import DatagramRequestHandler
from tkinter import *
from turtle import left

class Window:

    def __init__(self, height, width, title='NewWindow'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+300+300')
        self.text = ''

    def add_text(self, text):
        self.text = text

    def draw_widget(self):
        # top_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=300)
        # buttom_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=300)
        # top_frame.pack()
        # buttom_frame.pack()

        # l1 =Label(self.root,width = 30, height = 2, bg = 'red', text="first") 
        # l2 = Label(self.root,width = 30, height = 2, bg = 'orange', text="second")

        # l1.place(x=10,y=10)
        # l2.place(in_=l1,x=10,y=10)

        Label(self.root,width = 30, height = 2, bg = 'red', text="first").grid(row=0,column=0)
        Label(self.root,width = 30, height = 2, bg = 'orange', text="second").grid(row=0,column=1)
        Label(self.root,width = 30, height = 2, bg = 'yellow', text="third").grid(row=1,column=0)
        Label(self.root,width = 30, height = 2, bg = 'green', text="fourth").grid(row=1,column=1)
    def widget_button(self):
        self.button = Button(self.root,text=self.text)
        self.button.pack()

    def run(self):
        self.draw_widget()
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

if __name__=="__main__":
    window = Window(500,500)
    window.run()

