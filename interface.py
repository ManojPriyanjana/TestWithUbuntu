import tkinter as tk

# Create main window only
root = tk.Tk()
root.title("Simple UI")
root.geometry("600x800")  # Window size 600x800

# Configure grid: 3 rows and 3 columns to equally expand
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Button 1 - Top-left
btn1 = tk.Button(root, text="Button 1")
btn1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Button 2 - Top-center
btn2 = tk.Button(root, text="Button 2")
btn2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# Button 3 - Top-right
btn3 = tk.Button(root, text="Button 3")
btn3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)


# Start the application
root.mainloop()
