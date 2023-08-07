import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
window.title("Basketball Analysis Results")

# Create a frame to hold the table that will display the results
frame = tk.Frame(window)
frame.pack()


#error: attribution table solution.

attribute_table = tk.Attributes()
attribute_table.add_column("Blocks")
attribute_table.add_column("Turnovers")
attribute_table.add_column("Steals")
attribute_table.add_column("Assists")
attribute_table.add_column("Free Throw Success")
attribute_table.add_column("Free Throw Failed")


# Create a table and add rows and columns for the data that will be displayed
table = tk.Table(attribute_table)
table.grid(row=0, column=0)

# Add data to the table
table.insert(0, ("10", "5", "3", "7", "80%", "20%"))
table.insert(1, ("12", "3", "4", "6", "70%", "30%"))
table.insert(2, ("15", "2", "5", "8", "90%", "10%"))

# Create a button to close the window
close_button = tk.Button(frame, text="Close", command=window.destroy)
close_button.grid(row=1, column=0)



# Run the mainloop
window.mainloop()