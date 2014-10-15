__author__ = 'chris'
"""
Write a GUI-based program to build a window layout as shown below.
When the frame is resized,the buttons should stay the same height and
expand sideways. Frame 1 and Frame 2 should always be the same height
and width as each other, and Frame 3 should be half as wide again as they are
(i.e. 150% wider, as shown below). Labeling each Frame is optional / good exercise.

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
 | Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |

"""

from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(2, weight=3)
        self.grid(sticky=ALL)


        #Frame1
        self.f1 = Frame(master,bg="red")
        self.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label1 = Label(self.f1, text="Frame 1", bg="red")
        self.label1.pack(fill=BOTH,expand=True)


        #Frame2
        self.f2 = Frame(master,bg="blue")
        self.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label2 = Label(self.f2, text="Frame 2", bg="blue")
        self.label2.pack(fill=BOTH,expand=True)


        #Frame 3
        self.f3 = Frame(master,bg="green")
        self.f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        #using pack manager inside the frame for the label
        self.label3 = Label(self.f3, text="Frame 3", bg="green")
        self.label3.pack(fill=BOTH,expand=True)


        #Frame 4 for the buttons
        self.f4 = Frame(master,bg="white")
        self.f4.grid(row=2, column=0, rowspan=1, columnspan=5, sticky=ALL)
        #Buttons
        for c in range(5):
            button = Button(self.f4, text="Button {0}".format(c+1,))
            button.pack(side=LEFT, fill=BOTH, expand=TRUE)

root = Tk()
app = Application(master=root)
app.mainloop()