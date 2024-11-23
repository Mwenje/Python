def read_write_file(input_file, output_file, input_data):
    try:
        with open(input_file, "r") as file:
            data = file.read()

        modified_data = data.capitalize()

        with open(output_file, mode="w") as outfile:
            outfile.write(input_data + "\n" + modified_data)
            # outfile.write(modified_data)

        print(f"File successfully modified and save as '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print(f"Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def user_given_file():
    input_filename = input("Please enter the name of the input file: \n")
    output_filename = input("Please enter the name of the output file: \n")
    input_data = input("Please enter data to you want to store in the file: \n")

    read_write_file(input_filename, output_filename, input_data)


user_given_file()
