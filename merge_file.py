import os

def walk_dir(dir_path):
    file_paths = []
    files = os.listdir(dir_path)

    for file in files:
        file_path = os.path.join(dir_path, file)
        
        if os.path.isdir(file_path):
            file_paths += walk_dir(file_path)
        else:
            file_paths.append(file_path)
    
    return file_paths

file_paths = walk_dir('text')

with open("wiki.txt", "w", encoding='utf-8') as f:
    for file_path in file_paths:
        with open(file_path, "r", encoding='utf-8') as f2:
            f.write(f2.read())