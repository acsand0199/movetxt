from pathlib import Path

def main():
    # Define the source folder and destination folders
    source_folder_path = Path("C:/Users/sande/Downloads")
    destination_folder_path = Path("C:/Users/sande/OneDrive/Documents/txt Files")

    # Iterate over all files in the source folder
    for source_file in source_folder_path.iterdir():
        if source_file.is_file() and source_file.suffix == ".txt": # Check if it's a .txt file
            destination_file = destination_folder_path / source_file.name # Construct the destination path
            source_file.rename(destination_file) # Move the file to the destination folder

    print("All .txt files have been moved.")

if __name__ == "__main__":
    main()






