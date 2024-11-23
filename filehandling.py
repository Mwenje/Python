import os


def create_file(file_name):
    try:
        with open(file_name, "w") as f:
            f.write("Hello, world!\n")
        print(f"File {file_name} created successfully")
    except IOError:
        print(f"Error creating file {file_name}")


def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print(f"Error reading file {file_name}")


def append_file(file_name, text):
    try:
        with open(file_name, "a") as f:
            f.write(text + "\n")
            print(f"Text appended to file {file_name} successfully.")
    except IOError:
        print(f"Error appending to file {file_name}")


def rename_file(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
        print(f"File {file_name} renamed to {new_file_name} successfully")
    except IOError:
        print(f"Error renaming file {file_name}")


def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File {file_name} deleted successfully")
    except IOError:
        print(f"Error deleting file {file_name}")


if __name__ == "__main__":
    file_name = "my_file1.txt"
    new_file_name = "new_my_file1.txt"

    # create_file(file_name)
    # read_file(file_name)
    # append_file(file_name=file_name, text="This is some additional text.\n")
    # read_file(file_name)
    # rename_file(file_name, new_file_name)
    # read_file(new_file_name)
    delete_file(new_file_name)
