import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Organelle Data
organelles = {
    "Mitochondrion": {
        "Functions": [
            "Powerhouse of the cell.",
            "Produces ATP through cellular respiration.",
            "Regulates cellular metabolism.",
            "Stores calcium for cell signaling.",
            "Helps in apoptosis (programmed cell death)."
        ],
        "Diagram": "mitochondria.jpg"
    },
    "Nucleus": {
        "Functions": [
            "Contains the cell's genetic material.",
            "Regulates gene expression.",
            "Controls cell growth and reproduction.",
            "Stores chromatin (DNA and proteins).",
            "Synthesizes ribosomal RNA (rRNA)."
        ],
        "Diagram": "nucleus.jpg"
    },
    "Endoplasmic Reticulum": {
        "Functions": [
            "Synthesizes proteins (Rough ER).",
            "Synthesizes lipids (Smooth ER).",
            "Transports synthesized molecules within the cell.",
            "Detoxifies chemicals (Smooth ER).",
            "Stores calcium for cellular activities."
        ],
        "Diagram": "Endoplasmic-Reticulum.jpg"
    },
    "Golgi Apparatus": {
        "Functions": [
            "Modifies proteins and lipids.",
            "Sorts and packages molecules for transport.",
            "Synthesizes certain macromolecules.",
            "Forms lysosomes.",
            "Involved in secretion of cell products."
        ],
        "Diagram": "Golgi-Apparatus.jpg"
    },
    "Lysosome": {
        "Functions": [
            "Breaks down waste materials.",
            "Digests worn-out organelles.",
            "Recycles cellular components.",
            "Defends against invading pathogens.",
            "Helps in cell renewal processes."
        ],
        "Diagram": "lysosome.jpg"
    },
}

# Function to display organelle details
def show_details():
    organelle = organelle_select.get()
    if organelle:
        # Display the functions in bullet points
        functions = organelles[organelle]["Functions"]
        function_text = "Functions:\n\n" + "\n".join(f"• {func}" for func in functions)
        info_label.config(text=function_text)
        info_label.pack(pady=15)
        
        # Display the diagram
        image = Image.open(organelles[organelle]["Diagram"])
        image = image.resize((300, 200))
        img = ImageTk.PhotoImage(image)
        diagram_label.config(image=img)
        diagram_label.image = img
        diagram_label.pack(pady=10)

# Tkinter Window
root = tk.Tk()
root.title("Intelligent Tutoring System for Biology")
root.geometry("600x600")
root.configure(bg="#D6EAF8")

# Custom style for ttk.Combobox
style = ttk.Style()
style.theme_use("default")  # Use default theme for customizations
style.configure(
    "TCombobox", 
    fieldbackground="#D6EAF8",  # Background color of the field
    background="#D6EAF8",      # Dropdown list background color
    foreground="#2874A6",      # Text color
    font=("Helvetica", 12)
)

# Header
header = tk.Label(root, text="Intelligent Tutoring System for Biology", font=("Helvetica", 18, "bold"), bg="#2874A6", fg="#D6EAF8", pady=10)
header.pack(fill="x")
subheading = tk.Label(root, text="You will learn about organelles in animal cell", font=("Helvetica", 14), bg="#D6EAF8", fg="#2874A6", pady=5)
subheading.pack()

# Organelle Definition
org_def_label = tk.Label(
    root,
    text="Organelles are specialized structures within a cell that perform specific functions, much like organs in a body.",
    font=("Helvetica", 12),
    fg="#2874A6",
    bg="#D6EAF8",
    wraplength=550,
    justify="left",
)
org_def_label.pack(pady=10)

# Dropdown Menu
frame = tk.Frame(root, bg="#D6EAF8")
frame.pack(pady=20)
organelle_label = tk.Label(frame, text="Select Organelle you want to learn about:", font=("Helvetica", 12), fg="#2874A6", bg="#D6EAF8")
organelle_label.grid(row=0, column=0, padx=10)

organelle_select = ttk.Combobox(frame, values=list(organelles.keys()), font=("Helvetica", 12), width=20, style="TCombobox")
organelle_select.grid(row=0, column=1, padx=10)

show_button = tk.Button(frame, text="Show Details", font=("Helvetica", 11), bg="#2874A6", fg="white", command=show_details)
show_button.grid(row=0, column=2, padx=10)

# Information Section (Initially Hidden)
info_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#D6EAF8", justify="left", wraplength=400)

# Diagram Section (Initially Hidden)
diagram_label = tk.Label(root, bg="#D6EAF8")

# Start Tkinter Loop
root.mainloop()
