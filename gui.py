import tkinter as tk
from tkinter import ttk

def show_toast(message, duration=5000):
    # Create a transparent, top-level window
    toast = tk.Toplevel()
    toast.overrideredirect(True)  # Remove window decorations
    toast.attributes('-topmost', True)  # Always on top
    toast.attributes('-alpha', 0.9)  # Semi-transparency # brightness manage
    
    # Center the toast on the screen
    screen_width = toast.winfo_screenwidth() 
    screen_height = toast.winfo_screenheight()
    width, height = 300, 50
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    toast.geometry(f"{width}x{height}+{x}+{y+400}")
    
    # Style the popup
    frame = ttk.Frame(toast, padding=10, style="Toast.TFrame")
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text=message, style="Toast.TLabel", anchor="center")
    label.pack(expand=True)

    # Automatically close the toast after the specified duration
    toast.after(duration, toast.destroy)

