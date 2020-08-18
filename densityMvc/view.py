import tkinter as tk
from tkinter import ttk, messagebox


class View(tk.Tk):
    PAD = 10
    def __init__(self,controller):
        super().__init__()
        self._buatFrameUtama()
        self._buatMenu()
        self._centerWindow()

    def main(self):
        self.mainloop()

    def _buatFrameUtama(self):
        self.frmUtama = ttk.Frame(self)
        self.frmUtama.pack(padx = self.PAD, pady = self.PAD)

    def _buatMenu(self):
        menu = tk.Menu(self.frmUtama)
        self.config(menu=menu)

        # create the file object)
        file = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self._exit)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Open", command=self._openFile)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        help = tk.Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is _onInfo
        help.add_command(label="Info",command=self._onInfo)

        #added "file" to our menu
        menu.add_cascade(label="Help", menu=help)

    def _exit(self):
        exit()

    def _openFile(self):
        pass

    def _onInfo(self):
       messagebox.showinfo("Information", "It is build by Izan")

    def viewData(self, data):
        msg = tk.Message(self.frmUtama,text=data)
        msg.grid(row=0,column =0)


    def _centerWindow(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth()-width)//2
        y_offset = (self.winfo_screenheight()-height)//2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )