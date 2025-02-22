import tkinter as tk
from time import strftime

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # Format for 12-hour clock
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1000 milliseconds (1 second)

# Create a window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time with a specific font size in pt
label = tk.Label(root, font=("Algerian", 50), background="black", foreground="red")
label.pack(anchor='center')

# Call the time function to update every second
time()

# Run the clock
root.mainloop()