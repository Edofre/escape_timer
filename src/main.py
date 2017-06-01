__author__ = 'Edo Freriks'
__app_name__ = 'Escape Group Finance & Risk'

'''

'''

import Tkinter as tk

class Testing(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        ## Set a fixed width and height
        self.resizable(width=False, height=False)

        self.time_str = tk.StringVar()
        # create the time display label, give it a large font
        # label auto-adjusts to the font
        label_font = ('helvetica', 40)
        self.timer_label = tk.Label(self, textvariable=self.time_str, font=label_font, bg='white',
                 fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

        # Create the start timer button, remove it after it's clicked
        self.start_button = tk.Button(self, text='Count Start', command=self.count_down)
        self.start_button.pack()

        # Label that contains the explanation
        self.explanationLabelVariable = tk.StringVar()
        tk.Label(self, textvariable=self.explanationLabelVariable).pack()
        self.explanationLabelVariable.set(
            "Press 'Enter' to enter the code and stop the timer. \n If the code is not correct you will lose time!")

        # The label that will show the result
        self.resultLabelVariable = tk.StringVar()
        tk.Label(self, textvariable=self.resultLabelVariable).pack()
        self.resultLabelVariable.set("")

        # Create the password field
        self.entryVariable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entryVariable)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_enter)
        self.entryVariable.set(u"Enter password here.")

        # Add a button that enables the user to enter the code
        tk.Button(self, text='Enter code', command=self.on_click).pack()
        self.update()

    def count_down(self):
        # start with 60 minutes --> 3600 seconds
        for t in range(3600, -1, -1):
            # format as 2 digit integers, fills with zero to the left
            # divmod() gives minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            # print(sf)  # test
            self.time_str.set(sf)
            # Remove the button
            self.start_button.destroy()
            self.update()
            # delay one second
            self.after(60)

    def on_click(self):
        # self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.check_answer(self.entryVariable.get())

    def on_enter(self, event):
        # self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.check_answer(self.entryVariable.get())

    def check_answer(self, answer):
        if answer == 'asdasd':
            self.resultLabelVariable.set("CORRECT!")
        else:
            self.resultLabelVariable.set("WRONG!")
            # Remove 5 minutes from the time, we do not tolerate failure

        self.entryVariable.set("")
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

if __name__ == "__main__":
    app = Testing(None)
    app.title(__app_name__)
    app.mainloop()
