import tkinter as tk

# Create main window only
root = tk.Tk()
root.title("Simple UI")
root.geometry("600x800")  # Window size 600x800

# Configure grid: 3 rows and 3 columns to equally expand
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)


# Start the application
root.mainloop()
