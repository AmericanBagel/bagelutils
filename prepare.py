# Import modules
import os
import sys
import shutil

# Define the list of questions and the strings to be replaced
questions = [
    [
        "What is this data pack's name/main namespace?", "<namespace>"
    ],
    [
        "What is the pack format for this data pack? https://minecraft.fandom.com/wiki/Pack_format#Data_Pack",
        "<pack_format>"
    ]
    [
        "What is a short description of your pack?", "<description>"
    ],
    [
        "Who are you/who is the main author?", "<author>"
    ],
    [
        "Describe yourself/the main author. Make it memorable, brief, catchy, and give it personality. This will be your description in the global data packs advancement page", "<author_description>"
    ]
]

# Define an empty list for the replacements
replacements = []

# Loop through each question and string to be replaced
for question, string in questions:
    # Print the question and get the user input
    answer = input(question + "\n")
    # Append the string and the answer as a sub-list to the replacements list
    replacements.append([string, answer])

# Define the path of the data folder
target_dir_path = "data"

# Define a function that recursively renames files and folders
def rename_files_and_folders(path):
    # Get the list of files and folders in the current path
    items = os.listdir(path)
    # Loop through each item
    for item in items:
        # Get the full path of the item
        item_path = os.path.join(path, item)
        # Check if the item is a file or a folder
        if os.path.isfile(item_path):
            # If it is a file, rename it if it contains any of the strings to be replaced
            for old, new in replacements:
                if old in item:
                    # Get the new file name by replacing the old string with the new one
                    new_item = item.replace(old, new)
                    # Get the full path of the new file name
                    new_item_path = os.path.join(path, new_item)
                    # Rename the file
                    os.rename(item_path, new_item_path)
                    # Print a message to indicate the renaming
                    print(f"Renamed file {item_path} to {new_item_path}")
                    # Update the item path to the new one
                    item_path = new_item_path
            # After renaming the file, open it and read its content
            with open(item_path, "r") as f:
                content = f.read()
            # Loop through each string to be replaced and its replacement
            for old, new in replacements:
                # Check if the content contains the old string
                if old in content:
                    # Replace the old string with the new one in the content
                    content = content.replace(old, new)
                    # Print a message to indicate the replacement
                    print(f"Replaced {old} with {new} in file {item_path}")
            # After replacing all the strings in the content, write it back to the file
            with open(item_path, "w") as f:
                f.write(content)
        elif os.path.isdir(item_path):
            # If it is a folder, rename it if it contains any of the strings to be replaced
            for old, new in replacements:
                if old in item:
                    # Get the new folder name by replacing the old string with the new one
                    new_item = item.replace(old, new)
                    # Get the full path of the new folder name
                    new_item_path = os.path.join(path, new_item)
                    # Rename the folder
                    os.rename(item_path, new_item_path)
                    # Print a message to indicate the renaming
                    print(f"Renamed folder {item_path} to {new_item_path}")
                    # Update the item path to the new one
                    item_path = new_item_path
            # After renaming the folder, call the function recursively on it
            rename_files_and_folders(item_path)

# Call the function on the data folder path
rename_files_and_folders(target_dir_path)

# Tell user that boilerplate is prepared.
print("Finished preparing boilerplate.")

# Check if .git is a directory
if os.path.isdir(".git"):
    # Prompt the user for confirmation
    answer = input("Do you want to remove .git? If you haven't messed with git, you can safely delete it. If you have messed with git, you probably know what you're doing. [y/N] ")
    # Check if the answer is negative
    if answer.lower() in ["n", "no", ""]:
        # Delete .git recursively
        shutil.rmtree(".git")
        print(".git deleted successfully.")

# Prompt the user for confirmation
answer = input(f"Do you want to delete this script? [Y/n] ")

# Get the name of the current script
script_name = os.path.basename(__file__)

# Check if the answer is affirmative
if answer.lower() in ["y", "yes", ""]:
    # Delete the script file
    os.remove(script_name)
    # Exit the program
    sys.exit()