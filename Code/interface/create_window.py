import tkinter as tk
import tkinter.filedialog as tkfd


def create_window():
    # basic window config
    window = tk.Tk()
    window.title = "League Vision"

    # create widgets
    title = tk.Label(
            text="Select your Clips:",
            height=5
    )
    selection_label = tk.Label(
            text="None"
    )
    selection_button = tk.Button(
            text="Select file(s)",
            width=25
    )

    # pack widgets into window
    title.pack()
    selection_label.pack()
    selection_button.pack()

    # lazy declaration because scoping is cancer in python
    def open_file(event):
        """Opens the file(s) for submission to ML models"""

        paths = tkfd.askopenfilenames(
                filetypes=[("Video Files", "*.mp4"), ]
        )

        if not paths:
            return
        # read the files etc

        # then set text to show selected files
        selection_label["text"] = '\n'.join(paths)

    # bind non-processing event handlers
    selection_button.bind(
            "<Button-1>",
            open_file
    )

    return window
