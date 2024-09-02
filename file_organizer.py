import os
import shutil

source_dir = r'C:\Path\To\Your\Unorganized\Folder'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov'],
    'Archives': ['.zip', '.tar', '.gz'],
    'CSS': ['.css'],
    'HTML': ['.html', '.htm'],
    'Python': ['.py'],
    'Others': []
}


def create_directories():
    """
    Creates directories for each type of file defined in the file_types dictionary.
    """
    print("Creating directories...")
    for folder_name in file_types.keys():
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created directory: {folder_path}")


def organize_files():
    """
    Moves files from the source directory to the appropriate folders based on file extensions.
    """
    print("Organizing files...")
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            print(f"Processing file: {filename}")
            move_file(file_path, filename)
        else:
            print(f"Skipped non-file item: {file_path}")


def move_file(file_path, filename):
    """
    Moves a file to the appropriate folder based on its extension.
    """
    file_extension = os.path.splitext(filename)[1].lower()  # Ensure lowercase for matching
    moved = False
    print(f"File extension: {file_extension}")

    for folder_name, extensions in file_types.items():
        if file_extension in extensions:
            destination_folder = os.path.join(source_dir, folder_name)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved file: {file_path} to {destination_path}")
            moved = True
            break

    if not moved:
        others_folder = os.path.join(source_dir, 'Others')
        if not os.path.exists(others_folder):
            os.makedirs(others_folder)
        destination_path = os.path.join(others_folder, filename)
        shutil.move(file_path, destination_path)
        print(f"Moved file: {file_path} to {destination_path}")


if __name__ == "__main__":
    create_directories()
    organize_files()
