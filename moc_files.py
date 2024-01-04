import os

def create_test_file(file_number, size_gb):
    destination_folder = "."  # Hardcoded destination folder
    file_name = f'testfile_{file_number}'
    file_path = os.path.join(destination_folder, file_name)
    
    with open(file_path, 'wb') as f:
        f.write(b'\0' * int(size_gb * 1024**3))
    
    print(f'File {file_name} created successfully in {destination_folder}.')

def generate_test_files(num_files, size_gb):
    for i in range(1, num_files + 1):
        create_test_file(i, size_gb)

if __name__ == "__main__":
    num_files_to_generate = int(input("Enter the number of files to generate: "))
    size_per_file_gb = float(input("Enter the size of each file in GB: "))

    generate_test_files(num_files_to_generate, size_per_file_gb)

