from pathlib import Path
import shutil
from tkinter import Tk, Label, Button, filedialog, messagebox, simpledialog
from datetime import datetime

def move_file_GUI(src_folder, dest_base_folder, new_folder_name=None, subfolder_name='raw data'):
    try:
        # Convert to Path objects for cross-platform handling
        src_folder = Path(src_folder)
        dest_base_folder = Path(dest_base_folder)

        # Ensure source folder exists
        if not src_folder.exists():
            messagebox.showerror("Error", f"Source folder '{src_folder}' does not exist.")
            return
        
        # If no folder name is given, default to current timestamp
        if not new_folder_name:
            new_folder_name = datetime.now().strftime('%Y_%m_%d_%H%:M:%S')
        
        # Create destination folder
        new_folder_path = dest_base_folder / new_folder_name
        if not new_folder_path.exists():
            new_folder_path.mkdir(parents=True)  # Create directory tree if none exists
    
        # Create subdirectory named "raw data"
        subfolder_path = new_folder_path / subfolder_name
        if not subfolder_path.exists():
            subfolder_path.mkdir()

        # Move files and directories from source to subfolder in the newly created directory
        for item in src_folder.iterdir():  # Iterate through the directory
            dest_path = subfolder_path / item.name
            if item.is_file():
                # Move file
                shutil.move(str(item), str(dest_path))
            elif item.is_dir():
                # Move directory (including all its contents)
                shutil.move(str(item), str(dest_path))
        
        messagebox.showinfo("Success", f"Files and folders successfully moved to {subfolder_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        source_label.config(text=folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        destination_label.config(text=folder_selected)

def move_file_action():
    src_folder = source_label.cget('text')
    dest_folder = destination_label.cget('text')

    # Ensure both source and destination are selected
    if not src_folder or src_folder == "No source folder selected":
        messagebox.showerror("Error", "Please select a source folder.")
        return
    
    if not dest_folder or dest_folder == "No destination folder selected":
        messagebox.showerror("Error", "Please select a destination folder.")
        return
    
    # Ask user for a new folder name via dialog
    new_folder_name = simpledialog.askstring("Input", "Please enter the name for the new folder:")
    if not new_folder_name:  # If no input, show an error and return
        messagebox.showerror("Error", "No folder name provided.")
        return
    
    # Move files only after both folders are selected and folder name is provided
    move_file_GUI(src_folder, dest_folder, new_folder_name)

# Initialize the Tkinter window

root = Tk()
root.title("File Mover")

source_label = Label(root, text="No source folder selected")
source_label.pack(pady=5)

source_button = Button(root, text='Select Source Folder', command=select_source_folder)
source_button.pack(pady=5)

destination_label = Label(root, text='No destination folder selected')
destination_label.pack(pady=5)

destination_button = Button(root, text="Select Destination Folder", command=select_destination_folder)
destination_button.pack(pady=5)

move_button = Button(root, text='Move Files', command=move_file_action)
move_button.pack(pady=20)

root.mainloop()
