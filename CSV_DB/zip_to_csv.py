import os
import zipfile

# Define the paths to the input and output folders
input_folder = 'zip_files'
output_folder = 'csv_files'

# Ensure the output folder exists, create it if necessary
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.zip'):
        # Create a full path to the input ZIP file
        input_file_path = os.path.join(input_folder, filename)

        # Extract the filename without the extension
        base_filename = os.path.splitext(filename)[0]

        # Create a full path to the output CSV file
        output_file_path = os.path.join(output_folder, base_filename + '.csv')

        try:
            # Extract the ZIP file
            with zipfile.ZipFile(input_file_path, 'r') as zip_ref:
                zip_ref.extractall(output_folder)
            print(f"Extracted '{filename}' to '{output_file_path}'")
        except Exception as e:
            print(f"Error extracting '{filename}': {str(e)}")

print("Extraction completed.")
