import os
import subprocess
python_command = "python"

# Function to create a test directory structure
def create_test_directory_structure():
    test_dir = "test_directory"
    os.makedirs(test_dir, exist_ok=True)

    # Create some files and directories
    os.makedirs(os.path.join(test_dir, "subdir1"), exist_ok=True)
    os.makedirs(os.path.join(test_dir, "subdir2"), exist_ok=True)

    with open(os.path.join(test_dir, "file1.txt"), "w") as file:
        file.write("This is file 1 content.")

    with open(os.path.join(test_dir, "file2.txt"), "w") as file:
        file.write("This is file 2 content.")

    with open(os.path.join(test_dir, "file3.txt"), "w") as file:
        file.write("This is file 3 content.")

    return test_dir

# Function to clean up the test directory structure
def cleanup_test_directory_structure(test_dir):
    if os.path.exists(test_dir):
        subprocess.run(["rm", "-r", test_dir])

# Test listing files and directories
def test_list_files_and_directories():
    test_dir = create_test_directory_structure()
    result = subprocess.run([python_command, "args.py", test_dir, "--list"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert "file1.txt" in result.stdout
    assert "file2.txt" in result.stdout
    assert "file3.txt" in result.stdout
    assert "subdir1" in result.stdout
    assert "subdir2" in result.stdout
    assert "The directory" not in result.stderr  # No errors

# Test deleting a file or directory
def test_delete_file_or_directory():
    test_dir = create_test_directory_structure()
    result = subprocess.run([python_command, "args.py", os.path.join(test_dir, "file1.txt"), "--delete", os.path.join(test_dir, "file1.txt")], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert f"File '{os.path.join(test_dir, 'file1.txt')}' has been deleted." in result.stdout
    assert not os.path.exists(os.path.join(test_dir, "file1.txt"))
    assert "The file or directory" not in result.stderr  # No errors

# Test renaming a file or directory
def test_rename_file_or_directory():
    test_dir = create_test_directory_structure()
    result = subprocess.run([python_command, "args.py", os.path.join(test_dir, "file2.txt"), "--rename", "renamed_file.txt"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert "Renamed" in result.stdout
    assert "file2.txt" not in os.listdir(test_dir)
    assert "renamed_file.txt" in os.listdir(test_dir)
    assert "The file or directory" not in result.stderr  # No errors

# Test searching for a file by name
def test_search_file_by_name():
    test_dir = create_test_directory_structure()
    result = subprocess.run([python_command, "args.py", test_dir, "--search", "file3.txt"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert f"File 'file3.txt' found in '{test_dir}'" in result.stdout
    assert "The directory" not in result.stderr  # No errors

if __name__ == "__main__":
    test_list_files_and_directories()
    test_delete_file_or_directory()
    test_rename_file_or_directory()
    test_search_file_by_name()
    cleanup_test_directory_structure("test_directory")
