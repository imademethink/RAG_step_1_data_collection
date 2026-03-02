# tell top 10 operations to be done on a text file using Python

# 1. Opening and Closing Files (automatically)
# 2. Reading the Entire Content
# 3. Reading Line-by-Line
# 4. Reading All Lines into a List
# 5. Writing to a File
# 6. Appending Content to a file
# 7. Navigating with Seek and Tell
# 8. Renaming, Deleting, if Exists Files
# 9. Copying and Moving Files
# 10. Search and Replace text within File





# 1. Opening and Closing Files (automatically)
with open("example.txt", "r") as file:
    # Operations go here
    pass


# 2. Reading the Entire Content
with open("example.txt", "r") as file:
    content = file.read()

# 3. Reading Line-by-Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes trailing newlines

# 4. Reading All Lines into a List
with open("example.txt", "r") as file:
    lines = file.readlines()

# 5. Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")

# 6. Appending Content to a file
with open("example.txt", "a") as file:
    file.write("Adding a new line.\n")



# 7. Navigating with Seek and Tell
with open("example.txt", "w") as f:
    f.write("Line One\nLine Two\nLine Three")

with open("example.txt", "r") as f:
    print(f"Initial position: {f.tell()}")  # Should be 0

    # Read the first line
    line1 = f.readline()
    print(f"Read: {line1.strip()} | New position: {f.tell()}")

    # Seek back to the beginning
    f.seek(0)
    print(f"Position after seek(0): {f.tell()}")

    # Jump to a specific byte (e.g., skip 'Line ')
    f.seek(5)
    print(f"Reading from byte 5: {f.read(3)}")  # Prints 'One'







# 8. Renaming, Deleting, if Exists Files
import os
try:
    os.rename("old.txt", "new.txt")
    print("File renamed successfully.")
except FileNotFoundError:
    print("Error: The source file does not exist.")

# Delete 'new.txt'
if os.path.exists("new.txt"):
    os.remove("new.txt")
    print("File deleted.")
else:
    print("The file does not exist.")






# 9. Copying Files
import shutil
# Basic copy: permission bits preserved, metadata lost
shutil.copy("source.txt", "destination_folder/")
# Copy with metadata: preserves timestamps and permissions
shutil.copy2("source.txt", "backup.txt")






# 9. Copying and Moving Files
import shutil
# Move file to a new directory (and optionally rename it)
shutil.move("old_location/data.txt", "new_location/new_name.txt")




# 10. Search and Replace text within File
file_path = "example.txt"
search_text = "old_word"
replace_text = "new_word"

with open(file_path, "r") as file:
    data = file.read()

# Replace all occurrences
data = data.replace(search_text, replace_text)

with open(file_path, "w") as file:
    file.write(data)



# 10. (part 2) Search and Replace text within File
import fileinput
for line in fileinput.input("example.txt", inplace=True):
    # Print writes directly back to the file
    print(line.replace("search_term", "replacement"), end="")




