__author__ = 'Edo Freriks'
__app_name__ = 'Escape Group Finance & Risk'
__escape_timer_key__ = 'asdasd'

'''
Basic countdown app to facilitate an escape room type project
'''

import Tkinter as tk


class Testing(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.time_left = 0

    def initialize(self):
        # Set a fixed width and height
        self.resizable(width=False, height=False)

        self.time_str = tk.StringVar()
        # create the time display label, give it a large font, label auto-adjusts to the font
        label_font = ('helvetica', 40)
        self.timer_label = tk.Label(self, textvariable=self.time_str, font=label_font, bg='white',
                                    fg='red', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

        # Create the start timer button, remove it after it's clicked
        self.start_button = tk.Button(self, text='Count Start', command=self.count_down)
        self.start_button.pack()

        # Label that contains the explanation
        self.explanation_label_variable = tk.StringVar()
        tk.Label(self, textvariable=self.explanation_label_variable).pack()
        self.explanation_label_variable.set(
            "Press 'Enter' to enter the code and stop the timer. \n If the code is not correct you will lose time!")

        # The label that will show the result
        self.result_label_variable = tk.StringVar()
        tk.Label(self, textvariable=self.result_label_variable).pack()
        self.result_label_variable.set("")

        # Create the password field
        self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_variable)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_enter)
        self.entry_variable.set(u"Enter password here.")

        # Add a button that enables the user to enter the code
        self.update()

    # start with 60 minutes --> 3600 seconds
    def count_down(self, start_time=3600):
        # Reset the time left because we're entering the loop again
        self.time_left = 0

        for self.time_left in range(start_time, -1, -1):
            # format as 2 digit integers, fills with zero to the left, divmod() gives minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(self.time_left, 60))
            self.time_str.set(sf)
            # Remove the button
            self.start_button.destroy()
            self.update()
            # delay one second
            self.after(60)

            if self.time_left <= 0:
                break

    def on_click(self):
        # Process the answer
        self.check_answer(self.entry_variable.get())

    def on_enter(self, event):
        # Process the answer
        self.check_answer(self.entry_variable.get())

    def check_answer(self, answer):
        # Make sure the time has not passed yet
        if self.time_left >= 0:
            if answer == __escape_timer_key__:
                self.result_label_variable.set("CORRECT!")
                # Stop the time! TODO

                # And disable the textfield
                self.entry.configure(state="disabled")
            else:
                self.result_label_variable.set("!!")
                self.result_label_variable.set("WRONG! " + str(self.time_left))
                # Remove a minute from the time, we do not tolerate failure
                # self.count_down(self.time_left - 60)
                calculated_time_left = self.time_left - 60
                self.count_down(0 if calculated_time_left < 0 else calculated_time_left)
                self.entry_variable.set("")
        else:
            # And disable the textfield
            self.entry.configure(state="disabled")
            self.entry_variable.set("TIME IS UP!")

        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)


if __name__ == "__main__":
    app = Testing(None)
    app.title(__app_name__)
    app.mainloop()
