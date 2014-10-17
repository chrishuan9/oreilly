__author__ = 'chris'
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

        #using pack manager inside the frame for the label
        self.label3 = Label(self.f3, text="Frame 3", bg="green")
        self.label3.pack(fill=BOTH, expand=True)


        #Frame 4 for the buttons
        self.f4 = Frame(master, bg="white", name="frame_4")
        self.f4.grid(row=2, column=0, rowspan=1, columnspan=5, sticky=ALL)
        #Buttons
        for c in range(5):
            button = Button(self.f4, text="Button {0}".format(c + 1, ))
            button.pack(side=LEFT, fill=BOTH, expand=TRUE)


        # event handler for mouse click
        def mousehandler(event):
            print("{0} was clicked at x:{1} and y:{2}".format(
                str(event.widget)[1:8], event.x, event.y))
            return "break"

        self.label1.bind("<Button-1>", mousehandler)
        self.label2.bind("<Button-1>", mousehandler)


root = Tk()
app = Application(master=root)
app.mainloop()