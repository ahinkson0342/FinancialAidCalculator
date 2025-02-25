import customtkinter as ctk
import sys
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from backend import calculate

# CustomTkinter settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Create main window
app = ctk.CTk()
app.title("Financial Aid Calculator")
app.geometry("600x500") 
app.resizable(True, True) 

# Get correct directory path when running as a PyInstaller bundle
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # PyInstaller temp directory
else:
    base_path = os.path.abspath(os.path.dirname(__file__))

# Change the window logo to the green river college logo
icon_path = os.path.join(base_path, "images", "calculator.ico")
icon_image = Image.open(icon_path)

# Set the window icon
app.iconphoto(False, ImageTk.PhotoImage(icon_image))

# App title
title_label = ctk.CTkLabel(app, text="Financial Aid Calculator", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

frame = ctk.CTkFrame(app) 
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Labels and entries
ctk.CTkLabel(frame, text="Total Program Credits:", font=("Arial", 18)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
ctk.CTkLabel(frame, text="Completed Credits:", font=("Arial", 18)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
ctk.CTkLabel(frame, text="Current GPA:", font=("Arial", 18)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
ctk.CTkLabel(frame, text="Target GPA:", font=("Arial", 18)).grid(row=3, column=0, padx=10, pady=5, sticky="w")

total_credits_entry = ctk.CTkEntry(frame, width=150, font=("Arial", 18))
completed_credits_entry = ctk.CTkEntry(frame, width=150, font=("Arial", 18))
current_gpa_entry = ctk.CTkEntry(frame, width=150, font=("Arial", 18))
target_gpa_entry = ctk.CTkEntry(frame, width=150, font=("Arial", 18))

total_credits_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
completed_credits_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
current_gpa_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
target_gpa_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Set the default value for target GPA
target_gpa_entry.insert(0, "2.0")

# Output section
output = ctk.CTkLabel(frame, text="Required GPA : ", font=("Arial", 20), fg_color="green4", text_color="white")

# Function to show the help pop-up
def show_help():
    messagebox.showinfo("Help", "This calculator calculates the GPA a student needs to achieve with their remaining credits to reach a minimum 2.0 CGPA")


# Add "?" help icon in the top right corner
help_button = ctk.CTkButton(
    app, 
    text="?", 
    command=show_help, 
    font=("Arial", 20), 
    width=40, 
    height=40, 
    corner_radius=20,
    fg_color="lightblue",
    hover_color="blue",
    text_color="white"
)

# Initially place the button
help_button.place(x=app.winfo_width() - 195, y=10)



# Function to calculate required GPA, not implemented yet
def calculate_required_gpa():
    total_credits = int(total_credits_entry.get())
    completed_credits = int(completed_credits_entry.get())
    current_gpa = float(current_gpa_entry.get())
    target_gpa = float(target_gpa_entry.get())
    result = calculate(total_credits, completed_credits, target_gpa, current_gpa)
    output.configure(text=f"Estimated GPA: {result}")


# Calculate button with better hover and pressed colors
calculate_button = ctk.CTkButton(
    app,
    text="Calculate Required GPA",
    command=calculate_required_gpa,
    fg_color=("#2C882B", "#1E661E"), 
    hover_color="#1F731F",
    font=("Arial", 20),
    width=300,
    height=60,
    corner_radius=20 
)
calculate_button.pack(pady=20)

# Center the output label
output.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

# Configure grid to allow stretching
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Run the app
app.mainloop()
