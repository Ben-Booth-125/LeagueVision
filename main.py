import Code.interface.create_window as w
import tkinter as tk

# init UI
window = w.create_window()

confirm_button = tk.Button(
        text="Process file(s)",
        width=25
)
confirm_button.pack()

# register ML processing stuff
confirm_button.bind("<Button-1>", ...)

# run the programs main loop
window.mainloop()
