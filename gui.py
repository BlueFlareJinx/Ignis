import tkinter as tk
from tkinter import ttk

def show_toast(message, duration=5000):
    # Create a transparent, top-level window
    toast = tk.Toplevel()
    toast.overrideredirect(True)  # Remove window decorations
    toast.attributes('-topmost', True)  # Always on top
    toast.attributes('-transparentcolor', 'white')  # Make white transparent

    # Center the toast on the screen
    screen_width = toast.winfo_screenwidth()
    screen_height = toast.winfo_screenheight()
    width, height = 300, 50
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    toast.geometry(f"{width}x{height}+{x}+{y+400}")

    # Create a Canvas for rounded corners
    canvas = tk.Canvas(toast, width=width, height=height, bg="white", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    backgroundColor = "#002b36"

    # Draw a rounded rectangle
    corner_radius = 15
    canvas.create_rectangle(
        corner_radius, 0,
        width - corner_radius, height,
        fill=backgroundColor, outline=backgroundColor
    )
    canvas.create_rectangle(
        0, corner_radius,
        width, height - corner_radius,
        fill=backgroundColor, outline=backgroundColor
    )
    canvas.create_oval(
        0, 0, 2 * corner_radius, 2 * corner_radius,
        fill=backgroundColor, outline=backgroundColor
    )
    canvas.create_oval(
        width - 2 * corner_radius, 0, width, 2 * corner_radius,
        fill=backgroundColor, outline=backgroundColor
    )
    canvas.create_oval(
        0, height - 2 * corner_radius, 2 * corner_radius, height,
        fill=backgroundColor, outline=backgroundColor
    )
    canvas.create_oval(
        width - 2 * corner_radius, height - 2 * corner_radius, width, height,
        fill=backgroundColor, outline=backgroundColor
    )

    # Add a message label
    label = tk.Label(
        canvas, text=message, bg=backgroundColor, fg="#839496", font=("Cascadia Mono", 15), anchor="center"
    )
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Automatically close the toast after the specified duration
    toast.after(duration, toast.destroy)

