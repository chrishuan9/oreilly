__author__ = 'chris'
import os
import logging

"""
Starting with the project you created at the end of the last lesson,
add components to the existing framework so that:
-- When the areas occupied by  Frame 1 or Frame 2 are clicked
with mouse button 1, the program should print which frame was clicked
and the X and Y coordinates (relative to the Frame).
-- Frame 3 should contain an Entry and a Text widget. When the button now
labeled "Open" is clicked, the content of the Entry should be used as a file
name, and the content of the file (if any) displayed in the Text widget.
-- The Entry and Text widgets should completely fill Frame 3 and continue to
do so even as the application window is resize.
-- The color of the text displayed in Frame 3's Text widget should change
appropriately when the "Red," "Blue," "Green," or "Black" buttons are clicked.
 +---------------------+--------------------------------+
 |                     |                                |
 |                     |                                |
 |                     |                                |
 |      Frame 1        |                                |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 +---------------------+               Frame 3          |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 |     Frame 2         |                                |
 |                     |                                |
 |                     |                                |
 +----------+----------+----------+----------+----------+
 |    Red   |   Blue   |  Green   |  Black   |   Open   |
 +----------+----------+----------+----------+----------+
 """
from tkinter import *

ALL = N + S + W + E


class Application(Frame):
    def __init__(self, master=None):
        """
        init setups the complete ui with all frames - consider refactoring
        and extracting to separate methods
        """
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(2, weight=3)
        self.grid(sticky=ALL)

        # Frame1
        self.f1 = Frame(master, bg="red", name="frame_1")
        self.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label1 = Label(self.f1, text="Frame 1", bg="red")
        self.label1.pack(fill=BOTH, expand=True)


        #Frame2
        self.f2 = Frame(master, bg="blue", name="frame_2")
        self.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label2 = Label(self.f2, text="Frame 2", bg="blue")
        self.label2.pack(fill=BOTH, expand=True)


        #Frame 3
        self.f3 = Frame(master, bg="green", name="frame _3")
        self.f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        # using pack manager inside the frame for the entry and text widget
        self.entryfield = Entry(self.f3)
        self.textdisplay = Text(self.f3, state=DISABLED, wrap=WORD, )
        self.entryfield.pack(side=TOP, fill=X)
        self.textdisplay.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Writing text requires the widget to be in an active state
        self.textdisplay.configure(state=NORMAL)
        self.textdisplay.insert(INSERT, "NO FILE LOADED")
        self.textdisplay.configure(state=DISABLED)

        #Frame 4 for the buttons
        self.f4 = Frame(master, bg="white", name="frame_4")
        self.f4.grid(row=2, column=0, rowspan=1, columnspan=5, sticky=ALL)

        #Buttons
        bred = Button(self.f4, text="Red", command=self.bredhandler)
        bblue = Button(self.f4, text="Blue", command=self.bbluehandler)
        bgreen = Button(self.f4, text="Green", command=self.bgreenhandler)
        bblack = Button(self.f4, text="Black", command=self.bblackhandler)
        bopen = Button(self.f4, text="Open", command=self.bopenhandler)

        bred.pack(side=LEFT, fill=X, expand=TRUE)
        bblue.pack(side=LEFT, fill=X, expand=TRUE)
        bgreen.pack(side=LEFT, fill=X, expand=TRUE)
        bblack.pack(side=LEFT, fill=X, expand=TRUE)
        bopen.pack(side=LEFT, fill=X, expand=TRUE)

        self.label1.bind("<Button-1>", self.mousehandler)
        self.label2.bind("<Button-1>", self.mousehandler)


    # ButtonHandler
    def bredhandler(self):
        self.textdisplay.configure(fg="red")
        return "break"

    def bbluehandler(self):
        self.textdisplay.configure(fg="blue")
        return "break"

    def bgreenhandler(self):
        self.textdisplay.configure(fg="green")
        return "break"

    def bblackhandler(self):
        self.textdisplay.configure(fg="black")
        return "break"

    def bopenhandler(self):
        self.textdisplay.configure(state=NORMAL)
        # {Line}.{Column} where Line count starts at 1 and
        # column count at 0
        self.textdisplay.delete(1.0, END)
        self.textdisplay.insert(INSERT, "LOADING FILE")
        self.textdisplay.configure(state=DISABLED)
        filename = self.entryfield.get()

        # tries to read file from current directory
        try:
            fi = open(filename, 'r')
            textToShow = fi.read()
            self.textdisplay.configure(state=NORMAL)
            self.textdisplay.delete(1.0, END)
            self.textdisplay.insert(INSERT, textToShow)
            self.textdisplay.configure(state=DISABLED)
        except FileNotFoundError:
            self.textdisplay.configure(state=NORMAL)
            self.textdisplay.delete(1.0, END)
            self.textdisplay.insert(INSERT, "*** File Not Found ***")
            self.textdisplay.configure(state=DISABLED)
        return "break"


    # event handler for mouse click
    def mousehandler(self, event):
        print("{0} was clicked at x:{1} and y:{2}".format(
            str(event.widget)[1:8], event.x, event.y))
        return "break"


root = Tk()
app = Application(master=root)
app.mainloop()