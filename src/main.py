__author__ = 'Edo Freriks'
__app_name__ = 'Escape Group Finance & Risk'
__escape_timer_key__ = '2832232efdccbh'

'''
Basic countdown app to facilitate an escape room type project
'''

import Tkinter as tk

class Testing(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        # Set the time left, 3600 seconds = 60 minutes
        self.time_left = 3600
        self.timer_running = True

    def initialize(self):
        self.time_str = tk.StringVar()
        # create the time display label, give it a large font, label auto-adjusts to the font
        timer_font = ('helvetica', 140)
        self.timer_label = tk.Label(self, textvariable=self.time_str, font=timer_font, bg='white',
                                    fg='red', relief='raised', bd=3).pack(fill='x', padx=10, pady=10)

        # Create the start timer button, remove it after it's clicked
        self.start_button = tk.Button(self, text='Count Start', command=self.start_count_down)
        self.start_button.pack()

        # Set the font for the label and input
        label_font = ('helvetica', 60)

        # Label that contains the explanation
        self.explanation_label_variable = tk.StringVar()
        tk.Label(self, textvariable=self.explanation_label_variable, font=label_font).pack(padx=10, pady=10)
        self.explanation_label_variable.set(
            "Press 'Enter' to enter the code.")

        # The label that will show the result
        self.result_label_variable = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_label_variable, font=label_font, fg='red')
        self.result_label.pack()
        self.result_label_variable.set("")

        # Create the password field
        self.entry_variable = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_variable, font=label_font)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.on_enter)
        self.entry_variable.set(u"Enter password here.")

        # Add a button that enables the user to enter the code
        self.update()

    # start with 60 minutes --> 3600 seconds
    def count_down(self):
        # format as 2 digit integers, fills with zero to the left, divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(self.time_left, 60))
        self.time_str.set(sf)
        # Remove the button
        self.start_button.destroy()
        # Update the time
        if self.time_left <= 0:
            self.time_up()

        # If the timer is running keep counting down
        if self.timer_running:
            # Remove a second from the time
            self.time_left -= 1
            # Delay one second
            self.after(1000, self.count_down)

    def start_count_down(self):
        # Remove the text from the input field
        self.entry_variable.set("")
        # Actually start the countdown
        self.count_down()

    def on_click(self):
        # Process the answer
        self.check_answer(self.entry_variable.get())

    def on_enter(self, event):
        # Process the answer
        self.check_answer(self.entry_variable.get())

    def time_up(self):
        # Stop the time and show feedback
        self.entry.configure(state="disabled")
        self.entry_variable.set("TIME IS UP!")
        self.timer_running = False

    def check_answer(self, answer):
        # Make sure the time has not passed yet
        if self.time_left >= 0:
            if answer.lower() == __escape_timer_key__:
                self.result_label_variable.set("Congratulations, you have escaped!")
                self.result_label.configure(fg='green')

                # Stop the time!
                self.timer_running = False

                # And disable the textfield
                self.entry.configure(state="disabled")
            else:
                self.result_label_variable.set("!!")
                self.result_label_variable.set(self.entry_variable.get() + " is wrong!")

                # Remove a minute from the time, we do not tolerate failure,
                # self.time_left -= 60
        else:
            # And disable the textfield
            self.time_up()

        # Set focus on the entry field
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)

if __name__ == "__main__":
    app = Testing(None)
    app.title(__app_name__)
    app.mainloop()