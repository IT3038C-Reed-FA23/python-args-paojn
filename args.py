import os
import argparse

def list_files_and_directories(directory):
    # Check if the directory exists
    if os.path.exists(directory):
        # list items in the directory
        dir_contents = os.listdir(directory)
        for item in dir_contents:
            print(item)
    else:
        print(f"The directory '{directory}' does not exist.")

def delete_file_or_directory(path):
    try:
        # Check if the file or directory exists
        if os.path.exists(path):
            # check if the path is a file or directory
            if os.path.isfile(path):
                # delete the file
                os.remove(path)
                print(f"File '{path}' has been deleted.")
            elif os.path.isdir(path):
                # delete the directory
                os.rmdir(path)
                print(f"Directory '{path}' has been deleted.")
        else:
            print(f"The file or directory '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_file_or_directory(old_path, new_name):
    try:
        # Check if the file or directory exists
        if os.path.exists(old_path):
            # get the directory of the old path and join it to the new name
            new_path = os.path.join(os.path.dirname(old_path), new_name)
            # Rename the file or directory
            os.rename(old_path, new_path)
            print(f"Renamed '{old_path}' to '{new_path}'.")
        else:
            print(f"The file or directory '{old_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_file_by_name(directory, filename):
    # Check if the directory exists
    if os.path.exists(directory):
        found = False
        for root, dirs, files in os.walk(directory):
            if filename in files:
                print(f"File '{filename}' found in '{root}'.")
                found = True
        # If you don't find the file, print a message
        if not_found:
            print(f"File '{filename}' not found in '{directory}'.")
    else:
        print(f"The directory '{directory}' does not exist.")

def main():
    # Make an arugment parser with the description "File and directory manipulation script"
    parser = argparse.ArgumentParser(description="File and directory manipulation script")
    # Add a positional argument for the directory with the help text "The target directory for the action"
    parser.add_argument("directory", help="The target directory for the action")
    # Add an argument "--list" with the action "store_true" and the help text "List files and directories"
    parser.add_argument("--list", action="store_true", help="List files and directories")
    # Add an argument "--delete" with the help text "Delete a file or directory"
    parser.add_argument("--delete", help="Delete a file or directory")
    # Add an argument "--rename" with the help text "Rename a file or directory"
    parser.add_argument("--rename", help="Rename a file or directory")
    # Add an argument "--search" with the help text "Search for a file by name"
    parser.add_argument("--search", help="Search for a file by name")

    # Parse the arguments
    args = parser.parse_args()

    if args.list:
        list_files_and_directories(args.directory)
    elif args.delete:
        delete_file_or_directory(args.delete)
    elif args.rename:
        rename_file_or_directory(args.directory, args.rename)
    elif args.search:
        search_file_by_name(args.directory, args.search)
    else:
        print("No action specified. Use --help for usage instructions.")

if __name__ == "__main__":
    main()
