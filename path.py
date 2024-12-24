import os

def find_folders_with_set_000(root_dir, output_file):
    """
    Find all folders containing 'set.000' folder starting from root_dir
    and write their paths to output_file.
    """
    with open(output_file, 'w') as file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            if "set.000" in dirnames:
                file.write(f'"{dirpath}",\n')

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    # Output file name
    output_file = "path.txt"
    # Find and write paths containing 'set.000' to the file
    find_folders_with_set_000(current_directory, output_file)
