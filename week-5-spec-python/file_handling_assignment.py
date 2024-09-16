# File Creation with Error Handling
try:
    # File Creation: Creating and writing to "my_file.txt"
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, this is week five assignment.\n\n")
        file.write("Line 2: Here is my favorite game: Football, Handball, volleyball.\n\n")
        file.write("Line 3: This is another line with my favorite food:potatoes,beans,meats,rice,banana.\n\n")
    print("File created and written successfully.")

except PermissionError:
    print("Error: You don't have permission to write to this file.")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")

# File Reading and Display with Error Handling
try:
    # Reading the content of "my_file.txt"
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContent of 'my_file.txt' after writing:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending with Error Handling
try:
    # File Appending: Appending more text to "my_file.txt"
    with open("my_file.txt", "a") as file:
        file.write("Line 4: This is an appended line with my favorite subjects: Programing,Chemistry,Environmental sustainability,Mathamatics.\n\n")
        file.write("Line 5: appended line with my phone number: +250782897717.\n\n")
        file.write("Line 6: Appending more lines with my favorite animalls:Caws, Hens,Sheeps,Goats,Rabbits.\n\n")
    print("\nFile appended successfully.")

except PermissionError:
    print("Error: You don't have permission to append to this file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final Reading and Display after Appending with Error Handling
try:
    # Re-reading the file after appending
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nContent of 'my_file.txt' after appending:")
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file after appending: {e}")

finally:
    print("\nFile operations complete.\n\n")
