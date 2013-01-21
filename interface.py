import Tkinter
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()

    def initialize self:
        (self).grid()
        self .entryVariable= Tkinter.StringVar()
        self.entry1=Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry2=Tkinter.Entry(self)
        self.entry1.grid(column=1, row=0, sticky='EW')
        self.entry2.grid(column=1, row=1, sticky='EW')
        self.entry1.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here")

        button= Tkinter.Button(self, text=u"click me !", command=self.OnButtonClick)
        button.grid(column=2, row=0)

        self.labelVariable= Tkinter.StringVar()
        label= Tkinter.Label(self,textvariable=self.labelVariable, text="here", anchor="w", fg="white", bg="blue")
        self.grid_columnconfigure(0, weight=1)
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry1.focus_set()
        self.entry1.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set("you clicked the boutton !")
        self.entry1.focus_set()
        self.entry1.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set("you pressed enter !")
        self.entry1.focus_set()
        self.entry1.selection_range(0, Tkinter.END)

if __name__== "__main__":
    app=simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
