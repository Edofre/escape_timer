__author__ = 'Edo Freriks'

'''

'''

import Tkinter as tk
import time


class Testing(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.time_str = tk.StringVar()
        # create the time display label, give it a large font
        # label auto-adjusts to the font
        label_font = ('helvetica', 40)
        tk.Label(self, textvariable=self.time_str, font=label_font, bg='white',
                 fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

        # Create the start timer button, remove it after it's clicked
        tk.Button(self, text='Count Start', command=self.count_down).pack()

        self.labelVariable = tk.StringVar()
        tk.Label(self, textvariable=self.labelVariable).pack()
        self.labelVariable.set("Enter the code to stop the timer. \n If the code is not correct you will lose time!")

        # Add a button that enables the user to enter the code
        tk.Button(self, text='Enter code', command=self.on_click).pack()
        self.update()

    def count_down(self):
        # start with 60 minutes --> 360 seconds
        for t in range(3600, -1, -1):
            # format as 2 digit integers, fills with zero to the left
            # divmod() gives minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            # print(sf)  # test
            self.time_str.set(sf)
            self.update()
            # delay one second
            time.sleep(1)

    def on_click(self):
        self.labelVariable.set(self.entryVariable.get() + " (You clicked the button)")
        self.passwordVariable.set(self.id_generator())
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)


if __name__ == "__main__":
    app = Testing(None)
    app.title(__author__)
    app.mainloop()
