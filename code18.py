# Write a program to demonstrate Safe File Processor with Custom Exception Hierarchy.
import traceback

# Custom exception classes
class FileFormatError(Exception):
    pass

class FileNotFoundErrorCustom(Exception):
    pass


file = None

try:
    # Open the file
    file = open("data.txt", "r")

    # Read file contents
    data = file.read().strip()

    if not data:
        raise FileFormatError("File is empty!")

    # Parse data as integers
    try:
        numbers = [int(x) for x in data.split()]
    except ValueError:
        raise FileFormatError("File contains invalid data!")

except FileNotFoundError:
    print("Error: File not found!")

except FileFormatError as e:
    print("File Format Error:", e)
    traceback.print_exc()

except Exception as e:
    print("Unexpected Error:", e)
    traceback.print_exc()

else:
    print("File read successfully!")
    print("Numbers:", numbers)

finally:
    if file is not None:
        file.close()
        print("File closed safely.")

    print("Program execution completed.")