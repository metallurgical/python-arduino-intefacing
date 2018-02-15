import Tkinter as tk
import matplotlib.pyplot as plt

class Application(tk.Frame):
    def __init__(self, master=None):
        self.windowSize(master);
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidget()

    """ Set minimum and maximun size of window """
    def windowSize(self, master=None):
        master.minsize(width=666, height=666)
        master.maxsize(width=1200, height=1000)

    """ Create widget inside current Frame """
    def createWidget(self):
        self.quit_botton = tk.Button(self, text='Quit', command=self.quit)
        self.quit_botton.grid();

master = tk.Tk()
app = Application(master);
app.master.title('Reading data from Arduino Port')
app.mainloop()