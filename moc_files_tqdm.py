import os
from tqdm import tqdm

def create_test_file(file_number, size_gb):
    file_name = f'testfile_{file_number}'
    file_path = os.path.join('.', file_name)
    total_bytes = int(size_gb * 1024**3)
    
    with open(file_path, 'wb') as f:
        with tqdm(total=total_bytes, unit='B', unit_scale=True, desc=f'File {file_name}') as pbar:
            chunk_size = 16 * 1024 # You can adjust the chunk size based on your preference (times 1024 B)
            for _ in range(0, total_bytes, chunk_size):
                f.write(b'\0' * chunk_size)
                pbar.update(chunk_size)
    
    print(f'File {file_name} created successfully.')

def generate_test_files(num_files, size_gb):
    for i in range(1, num_files + 1):
        create_test_file(i, size_gb)

if __name__ == "__main__":
    num_files_to_generate = int(input("Enter the number of files to generate: "))
    size_per_file_gb = float(input("Enter the size of each file in GB: "))

    generate_test_files(num_files_to_generate, size_per_file_gb)
