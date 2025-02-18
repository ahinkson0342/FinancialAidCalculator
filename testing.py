import customtkinter as ctk
import os
from PIL import Image, ImageTk
from tkinter import messagebox

# CustomTkinter settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green") 

# Create main window
app = ctk.CTk()
app.title("Financial Aid Calculator")
app.geometry("400x300")  # Window size
app.resizable(False, False)  # Prevent resizing

# changes the window logo to the green river college logo
icon_path = os.path.join("images", "grc-logo.ico")
app.iconbitmap(icon_path)

# app title
title_label = ctk.CTkLabel(app, text="Financial Aid Calculator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

frame = ctk.CTkFrame(app)  # Create a frame for layout
frame.pack(pady=10, padx=20, fill="both", expand=True)

# labels and entries
ctk.CTkLabel(frame, text="Total Program Credits:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ctk.CTkLabel(frame, text="Current GPA:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ctk.CTkLabel(frame, text="Completed Credits:").grid(row=2, column=0, padx=10, pady=5, sticky="w")

total_credits_entry = ctk.CTkEntry(frame, width=150)
current_gpa_entry = ctk.CTkEntry(frame, width=150)
completed_credits_entry = ctk.CTkEntry(frame, width=150)

total_credits_entry.grid(row=0, column=1, padx=10, pady=5)
current_gpa_entry.grid(row=1, column=1, padx=10, pady=5)
completed_credits_entry.grid(row=2, column=1, padx=10, pady=5)

# Output section
output = ctk.CTkLabel(frame, text="Estimated GPA", font=("Arial", 14), fg_color="green4", text_color="white")

# Function to calculate required GPA, not implemented yet
def calculate_required_gpa():
    current_gpa = current_gpa_entry.get()
    output.configure(text=f"Estimated GPA: {current_gpa}")


# calculate button with better hover and pressed colors
calculate_button = ctk.CTkButton(
    app,
    text="Calculate Required GPA",
    command=calculate_required_gpa,
    fg_color=("#2C882B", "#1E661E"),  # Normal and pressed color
    hover_color="#1F731F"
)
calculate_button.pack(pady=20)

output.grid(row=3, column=0, columnspan=2, pady=0)

# runs the app
app.mainloop()