import os
def delete_files_in_directory_and_subdirectories(directory_path):
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        print("All files and subdirectories deleted successfully.")
    except OSError:
        print("Error occurred while deleting files and subdirectories.")

directory_path = 'Final'
delete_files_in_directory_and_subdirectories(directory_path)