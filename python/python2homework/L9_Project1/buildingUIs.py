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

        # #################################################################### Frame1
        self.f1 = Frame(master, bg="red", name="frame_1")
        self.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label1 = Label(self.f1, text="Frame 1", bg="red")
        self.label1.pack(fill=BOTH, expand=True)


        ##################################################################### Frame2
        self.f2 = Frame(master, bg="blue", name="frame_2")
        self.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label2 = Label(self.f2, text="Frame 2", bg="blue")
        self.label2.grid(row=0, column=0, columnspan=2, sticky=ALL)
        self.f2.rowconfigure(0, weight=1)
        self.f2.rowconfigure(1, weight=0)
        self.f2.columnconfigure(0, weight=1)
        self.f2.columnconfigure(1, weight=1)

        bred = Button(self.f2, text="Red", command=self.bredhandler)
        bblue = Button(self.f2, text="Blue", command=self.bbluehandler)

        bred.grid(row=1, column=0, sticky=W + E)
        bblue.grid(row=1, column=1, sticky=W + E)

        # #################################################################### Frame3
        # uses grid geometry manager
        self.f3 = Frame(master, name="frame _3")
        self.f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        # ensures that the textdisplay field is maximized while the entry
        # and button row are kept at their minimum size
        self.f3.rowconfigure(1, weight=1)
        self.f3.columnconfigure(0, weight=1)
        self.f3.columnconfigure(1, weight=1)
        self.f3.columnconfigure(2, weight=1)

        # entry and text field
        self.entryfield = Entry(self.f3)
        self.entryfield.grid(row=0, column=0, columnspan=3, sticky=W + E)
        self.textdisplay = Text(self.f3, state=DISABLED, wrap=WORD)
        self.textdisplay.grid(row=1, column=0, columnspan=3, sticky=ALL)

        # adding buttons on the last row of Frame 3
        self.bgreen = Button(self.f3, text="Green", command=self.bgreenhandler)
        self.bblack = Button(self.f3, text="Black", command=self.bblackhandler)
        self.bopen = Button(self.f3, text="Open", command=self.bopenhandler)

        self.bgreen.grid(row=2, column=0, sticky=W + E)
        self.bblack.grid(row=2, column=1, sticky=W + E)
        self.bopen.grid(row=2, column=2, sticky=W +E)


        # Writing text requires the widget to be in an active state
        self.textdisplay.configure(state=NORMAL)
        self.textdisplay.insert(INSERT, "NO FILE LOADED")
        self.textdisplay.configure(state=DISABLED)



        self.label1.bind("<Button-1>", self.mousehandler)
        self.label2.bind("<Button-1>", self.mousehandler)


    ##################################################################### ButtonHandlers
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


    ##################################################################### event handler for mouse clicks in Frame 1/2
    def mousehandler(self, event):
        print("{0} was clicked at x:{1} and y:{2}".format(
            str(event.widget)[1:8], event.x, event.y))
        return "break"


root = Tk()
app = Application(master=root)
app.mainloop()