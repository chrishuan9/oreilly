__author__ = 'chris'
"""Write a GUI-based program that provides two Entry fields, a button and a label. When the button is clicked,
the value of each Entry should (if possible) be converted into a float. If both conversions succeed, the label
should change to the sum of the two numbers. Otherwise it should read "***ERROR***"."""

from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        """Main frame initialisation"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        top_frame = Frame(self)
        self.float_entry1 = Entry(top_frame)
        self.float_entry2 = Entry(top_frame)

        self.float_entry1.pack()
        self.float_entry2.pack()

        top_frame.pack()

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.convertButton = Button(bottom_frame, text="Convert", command=self.convert)
        self.convertButton.pack(side=TOP)

        self.label = Label(bottom_frame, text="Output")
        self.label.pack(side=BOTTOM)

    def convert(self):
        try:
            value_1 = float(self.float_entry1.get())
            value_2 = float(self.float_entry2.get())
            output = value_1 + value_2

        except ValueError:
            output = "***ERROR***"

        self.label.config(text=output)

root = Tk()
app = Application(master=root)
app.mainloop()