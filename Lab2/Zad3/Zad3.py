import os

ROOT = 'C:\Dir1'
MAX_SIZE_BYTES = 1024 * 1024
for root, dirs, files in os.walk(ROOT):
    for file in files:
        file_path = os.path.join(root, file)
        if os.stat(file_path).st_size < MAX_SIZE_BYTES:
            print(file_path)
