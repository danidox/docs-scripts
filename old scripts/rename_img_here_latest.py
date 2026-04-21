import os

# Get the current working directory (the folder where this script is run)
folder_path = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(folder_path):
    # Skip folders — only process files
    if not os.path.isfile(filename):
        continue

    # Check if the file starts with 'latest-'
    if filename.startswith("latest-"):
        # Replace only the first occurrence of 'latest' with 'activities'
        new_filename = filename.replace("latest", "activities", 1)

        # Rename the file
        os.rename(filename, new_filename)
        print(f"Renamed: {filename} → {new_filename}")

print("✅ All matching files in this folder have been renamed.")
