import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
window.title("Basketball Analysis Program")

# Create a frame to hold the input fields and the submit button
frame = tk.Frame(window)
frame.pack()

# Create a label for each of the input fields
tk.Label(frame, text="Blocks").grid(row=0, column=0)
tk.Label(frame, text="Turnovers").grid(row=1, column=0)
tk.Label(frame, text="Steals").grid(row=2, column=0)
tk.Label(frame, text="Assists").grid(row=3, column=0)
tk.Label(frame, text="Free Throw Success").grid(row=4, column=0)
tk.Label(frame, text="Free Throw Failed").grid(row=5, column=0)

# Create an entry field for users to enter their data
blocks_entry = tk.Entry(frame)
blocks_entry.grid(row=0, column=1)
turnovers_entry = tk.Entry(frame)
turnovers_entry.grid(row=1, column=1)
steals_entry = tk.Entry(frame)
steals_entry.grid(row=2, column=1)
assists_entry = tk.Entry(frame)
assists_entry.grid(row=3, column=1)
free_throw_success_entry = tk.Entry(frame)
free_throw_success_entry.grid(row=4, column=1)
free_throw_failed_entry = tk.Entry(frame)
free_throw_failed_entry.grid(row=5, column=1)

# Create a submit button[[]]
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=6, column=0)
blocks_entry = tk.Entry(frame)
# Create a function to process the data entered by the user
def submit():
    # Get the data from the input fields
    blocks = blocks_entry.get()

blocks_entry.grid(row=0, column=1)
submit()

#staged commit test