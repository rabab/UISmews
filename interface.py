
import Tkinter
import Tix 
class simpleapp_tk(Tix.Tk):
    def __init__(self,parent):
        Tix.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()

    def initialize (self):
        #root = Tix.Tk()
        self.grid()
        varcombo = Tix.StringVar() 
        text= Tix.Label(self, text='target')
        text.grid(column=0, row=0, sticky='EW')
        text.pack()
        bal= Tix.Balloon()
        self.enabled= Tix.IntVar()
        self.checkbutton1 = Tix.Checkbutton(self,text = "WSN430", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton1.pack()
        self.checkbutton2 = Tix.Checkbutton(self,text = "WSN430", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton2.pack()
        self.checkbutton3 = Tix.Checkbutton(self,text = "MicaZ", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton3.pack()
        self.checkbutton4 = Tix.Checkbutton(self,text = "Funcard7", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton4.pack()
        self.checkbutton5 = Tix.Checkbutton(self,text = "GBA", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton5.pack()
        self.checkbutton6 = Tix.Checkbutton(self,text = "MBED", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton6.pack()
        self.checkbutton7 = Tix.Checkbutton(self,text = "Linux", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton7.pack()
        self.checkbutton8 = Tix.Checkbutton(self,text = "Skeleton", variable=self.enabled,command=self.OnCheckBoxClick)
        self.checkbutton8.pack()
        combo = Tix.ComboBox(self, editable=1, dropdown=1, variable=varcombo, command = self.Affiche)
        combo.entry.config(state='readonly')  
        combo.insert(0, 'NT') 
        combo.insert(1, 'Linux')
        bal.bind_widget(combo, msg='target')
        combo.pack()
        self.mainloop()

    def OnCheckBoxClick(self):
        iTemp = self.enabled.get()
        print "iTemp %s"%iTemp

    def Affiche(self,evt):
        print varcombo.get()
if __name__== "__main__":
    app=simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
