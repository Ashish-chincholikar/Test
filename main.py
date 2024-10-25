import tkinter as tk
from tkinter import filedialog, messagebox
import apriori as ap  # Assuming apriori.py contains the apriori function
import pandas as pd
import fp_growth as fpg
import sys

dataset = None

def load_dataset(file_path, message):
    global dataset
    # Load the dataset from the specified file path
    dataset = pd.read_csv(file_path, encoding='latin-1')

    # Display a popup message indicating that the dataset is loaded
    messagebox.showinfo("Message Box", f"Success {message}")

def display_dataset():
    global dataset
    if dataset is None:
        messagebox.showinfo("No Dataset", "Please load the dataset first.")
    else:
        # Clear the previous content in the text widget
        text.delete(1.0, tk.END)

        # Display the dataset in the text widget
        text.insert(tk.END, dataset.head(1000).to_string(index=False))

def clear_text():
    text.delete(1.0, tk.END)
    text_frame.pack_forget()

def load_reduced_dataset():
    file_path = "Reduced_dataset.csv"  # Specify the file path of the reduced dataset
    load_dataset(file_path, "The dataset is now reduced.")

def load_cleaned_dataset():
    file_path = "Cleaned_dataset.csv"  # Specify the file path of the cleaned dataset
    load_dataset(file_path, "The dataset is now cleaned.")

def load_transformed_dataset():
    file_path = "transformed_dataset.csv"  # Specify the file path of the transformed dataset
    load_dataset(file_path, "The dataset is now Transformed.")

def load_final_preprocessed_dataset():
    file_path = "final_dataset.csv"  # Specify the file path of the final preprocessed dataset
    load_dataset(file_path, "The dataset is now finally preprocessed.")

def run_apriori_algorithm():
    # Placeholder function for running Apriori algorithm
    messagebox.showinfo("Apriori Algorithm", "Apriori algorithm is running...")

def run_fp_growth_algorithm():
    # Placeholder function for running FP-Growth algorithm
    messagebox.showinfo("FP-Growth Algorithm", "FP-Growth algorithm is running...")

def exit_application():
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Dataset Viewer")
root.geometry("1000x800")

# Create a button to load the dataset
load_button = tk.Button(root, text="Load Dataset", width=15, command=lambda: load_dataset(filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]), ""))
load_button.grid(row=0, column=0, padx=5, pady=5)

# Create a button to run Apriori algorithm
apriori_button = tk.Button(root, text="Apriori", width=15, command=ap.apriori_)
apriori_button.grid(row=1, column=0, padx=5, pady=5)

# Create a button to run FP-Growth algorithm
fp_growth_button = tk.Button(root, text="FP-Growth", width=15, command=fpg.fpgrowth_)
fp_growth_button.grid(row=1, column=1, padx=5, pady=5)

# Create a button to display the dataset
display_button = tk.Button(root, text="Display Dataset", width=15, command=display_dataset)
display_button.grid(row=1, column=2, padx=5, pady=5)

# Create a button to clear the text area
clear_button = tk.Button(root, text="Clear", width=15, command=clear_text)
clear_button.grid(row=1, column=3, padx=5, pady=5)

# Create buttons for loading specific datasets
load_reduced_button = tk.Button(root, text="Reduce Dataset", width=15, command=load_reduced_dataset)
load_reduced_button.grid(row=0, column=1, padx=5, pady=5)

load_cleaned_button = tk.Button(root, text="Clean Dataset", width=15, command=load_cleaned_dataset)
load_cleaned_button.grid(row=0, column=2, padx=5, pady=5)

load_transformed_button = tk.Button(root, text="Transformed Dataset", width=15, command=load_transformed_dataset)
load_transformed_button.grid(row=0, column=3, padx=5, pady=5)

# Create a button to load the final preprocessed dataset
load_final_preprocessed_button = tk.Button(root, text="Final Preprocess Dataset", width=20, command=load_final_preprocessed_dataset)
load_final_preprocessed_button.grid(row=0, column=4, padx=5, pady=5)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", width=20, command=exit_application)
exit_button.grid(row=1, column=4, padx=5, pady=5)

# Create a text frame to hold the text widget and scrollbars
text_frame = tk.Frame(root)
text_frame.grid(row=2, column=0, columnspan=7, sticky="nsew", padx=5, pady=5)

# Create a horizontal scrollbar
xscrollbar = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create a vertical scrollbar
yscrollbar = tk.Scrollbar(text_frame)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget for displaying the dataset
text = tk.Text(text_frame, wrap=tk.NONE, width=50, height=10, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
text.pack(expand=True, fill="both")

# Configure the scrollbars to scroll the text widget
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

# Configure grid weights to make the text frame expandable
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)

# Start the Tkinter event loop
root.mainloop()
