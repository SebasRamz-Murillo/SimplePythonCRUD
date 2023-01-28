import os

file_path = "cliente.json"

# Split the file name and extension
file_name, file_ext = os.path.splitext(file_path)

# Remove the extension

print(file_name)
print(file_path)
