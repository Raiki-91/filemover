# File Mover
## Overview
The File Mover is a simple and efficient utility designed to quickly move files and folders from one directory to another. It provides an intuitive graphical user interface (GUI) that allows users to select source and destination folders, create custom subfolders, and move files with ease. This tool is ideal for users who frequently manage files across different directories and want a streamlined process without the complexities of a full file management system.
The application is built using Python and Tkinter for the GUI and packaged into a standalone executable, so it doesn't require Python or any other dependencies to be installed on the user's machine.

### Why Use File Mover?
In many scenarios, users need a fast and straightforward way to move files and folders without the overhead of a full-featured file manager. Examples include:

Organizing project files into specific directories.
Moving downloaded files to designated folders.
Sorting and categorizing files based on their content or type.
The File Mover addresses this need by providing:

Simplicity: A minimalistic interface focused on the core function—moving files and folders.
Efficiency: Quickly select source and destination folders, create subfolders, and move files in just a few clicks.
Cross-platform support: Works on Windows, macOS, and Linux.

### Features
Select Source and Destination Folders: The user can choose both the source and destination directories for moving files.
Custom Subfolder Creation: Allows the user to create a custom-named subfolder within the destination directory.
Move Files and Folders: Moves individual files and entire directories while preserving the original folder structure.
Standalone Executable: The program is packaged as a standalone executable for ease of distribution and use without needing Python installed.
How to Use
Running the Program
Download the Executable:

Download the .exe file (for Windows) or the appropriate binary for macOS/Linux.

### Using the Application
Select the Source Folder: Click the "Select Source Folder" button to choose the folder containing the files or directories you want to move.

Select the Destination Folder: Click the "Select Destination Folder" button to choose where you want the files to be moved.

Name the New Folder: A dialog will prompt you to enter a name for the new subfolder that will be created in the destination directory.

Move Files: After selecting both the source and destination folders and entering the subfolder name, click "Move Files" to move the selected files and directories.

###F eatures in Action
Subfolder Creation: When you enter a custom folder name, the program creates that folder in the destination directory and moves all files and directories from the source into it.
Moving Folders: The program can move not only individual files but also entire directories, preserving the original folder structure.
Development
This application is written in Python and uses the following libraries:

Tkinter: For the GUI interface.
Shutil: For file and folder movement operations.
Pathlib: For cross-platform file path handling. 
PyInstaller: For packaging the Python script into an executable.
Requirements
If you want to run the script from source (without the executable), you will need:

Python 3.x installed on your system.
Tkinter (usually bundled with Python on most platforms).

### License
This project is licensed under the following terms:

#### Free for Personal Use: You are free to use this software for personal, non-commercial purposes without explicit permission from the author.
#### Non-commercial Use: The use of this software in commercial products, services, or other for-profit applications is not permitted without prior written consent from the author.
#### Modifications: You are free to modify and adapt the software for personal use, but redistribution of modified versions is subject to the same license terms.
#### Attribution: If you share or reference this project, please provide proper attribution to the original author.

For any inquiries regarding commercial use or special permissions, please contact the author.

