import os

def clean_folder(directory):
    """
    Recursively checks a folder and deletes all files that are not .mp4 or .zip.
    :param directory: Path to the folder to clean.
    """
    # Loop through all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            # If it's a folder, recursively clean it
            clean_folder(item_path)
        elif os.path.isfile(item_path):
            # If it's a file, check its extension
            if not (item_path.endswith('.mp4') or item_path.endswith('.zip')):
                try:
                    os.remove(item_path)
                    print(f"Deleted: {item_path}")
                except Exception as e:
                    print(f"Failed to delete {item_path}: {e}")

# Specify the folder to clean
folder_to_clean = os.path.expanduser("~/Downloads/javascript_weird_parts/")

if os.path.exists(folder_to_clean):
    clean_folder(folder_to_clean)
    print("Cleaning complete!")
else:
    print(f"The folder '{folder_to_clean}' does not exist.")

