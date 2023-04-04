import tkinter as tk
from tkinter import filedialog
from gcode_generator import generate_square_gcode, generate_circle_gcode

class GCodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("G-Code Generator")

        
        # create labels and input fields for length and feedrate
        self.length_label = tk.Label(master, text="Length:", font=("Helvetica", 14), bg="#f0f0f0", padx=10, pady=5, width=10, anchor="w")
        self.length_label.pack()

        self.length_entry = tk.Entry(master, font=("Helvetica", 14), borderwidth=2, relief="groove", border=2, width=10)
        self.length_entry.pack()

        self.feedrate_label = tk.Label(master, text="Feedrate:", font=("Helvetica", 14), bg="#f0f0f0", padx=10, pady=5, width=10, anchor="w")
        self.feedrate_label.pack()

        self.feedrate_entry = tk.Entry(master, font=("Helvetica", 14), borderwidth=2, relief="groove", border=2, width=10)
        self.feedrate_entry.pack()


        # create buttons for generating square and circle G-code
        self.square_button = tk.Button(master, text="Generate Square G-Code", command=self.generate_square_gcode, bg="blue", fg="white",font=("Helvetica", 10))
        self.square_button.pack(padx=5, pady=5)

        self.circle_button = tk.Button(master, text="Generate Circle G-Code", command=self.generate_circle_gcode, bg="blue", fg="white",font=("Helvetica", 10))
        self.circle_button.pack(padx=5, pady=5)

        # create text box to display G-code
        self.gcode_textbox = tk.Text(master, height=20, width=50)
        self.gcode_textbox.pack(padx=5, pady=5)

        # create button for saving G-code to file
        self.save_button = tk.Button(master, text="Save G-Code to File", command=self.save_gcode_to_file, bg="blue", fg="white",font=("Helvetica", 10))
        self.save_button.pack(padx=5, pady=5)

    def generate_square_gcode(self):
        length = float(self.length_entry.get())
        feedrate = float(self.feedrate_entry.get())
        gcode = generate_square_gcode(length, feedrate)
        self.gcode_textbox.delete("1.0", tk.END)
        self.gcode_textbox.insert(tk.END, gcode)
        

    def generate_circle_gcode(self):
        diameter = float(self.length_entry.get())
        feedrate = float(self.feedrate_entry.get())
        gcode = generate_circle_gcode(diameter, feedrate)
        self.gcode_textbox.delete("1.0", tk.END)
        self.gcode_textbox.insert(tk.END, gcode)
        

    def save_gcode_to_file(self):
        # get file name and location from user
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("G-code files", "*.gcode"), ("all files", "*.*")))

        # write G-code to file
        with open(filename, "w") as f:
            f.write(self.gcode_textbox.get(1.0, tk.END))

root = tk.Tk()
gui = GCodeGeneratorGUI(root)
root.mainloop()
