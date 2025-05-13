import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# This script provides a GUI for selecting a CSV file, cleaning it by removing unwanted columns,
# and saving the cleaned version. It specifically retains the first column and any column containing

# Function to clean the CSV
def clean_csv():
    input_file = filedialog.askopenfilename(title='Select your CSV file', filetypes=[('CSV files', '*.csv')])
    if not input_file:
        messagebox.showinfo('No File Selected', 'Please select a CSV file.')
        return

    try:
        data = pd.read_csv(input_file, header=None, on_bad_lines='skip')

        # Extracting only the first column and any column containing the URL
        columns_to_keep = [0]  # First column

        # Identify columns with the URL
        for col in data.columns:
            if data[col].astype(str).str.contains('https://toresaid.com/api/episode/printtranscript', na=False).any():
                columns_to_keep.append(col)

        # Filter the dataframe
        cleaned_data = data.iloc[:, columns_to_keep]

        # Save the cleaned CSV in the same directory as the input
        output_file = input_file.replace('.csv', '_cleaned.csv')
        cleaned_data.to_csv(output_file, index=False, header=False)

        messagebox.showinfo('Success', f'Cleaned CSV saved as {output_file}')

    except Exception as e:
        messagebox.showerror('Error', str(e))

# Setting up the GUI
root = tk.Tk()
root.title('CSV Cleaner for Transcript Links')
root.geometry('400x200')

label = tk.Label(root, text='CSV Cleaner for Transcript Links', font=('Helvetica', 14))
label.pack(pady=20)

clean_button = tk.Button(root, text='Select and Clean CSV', command=clean_csv, width=25)
clean_button.pack(pady=10)

root.mainloop()
