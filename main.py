import subprocess

# Specify the path to the Python file you want to run
python_file_path = "path_to_your_script.py"

try:
    # Run the Python file using subprocess
    subprocess.run(["python", python_file_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running {python_file_path}: {e}")
except FileNotFoundError:
    print(f"Python executable not found. Make sure Python is installed and in your system's PATH.")
