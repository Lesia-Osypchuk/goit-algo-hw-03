import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            dest_subdir = os.path.join(dest_dir, extension)

            # Перевірка, чи існує піддиректорія, якщо ні - створити
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)

            dest_path = os.path.join(dest_subdir, file)
            try:
                shutil.copy2(source_path, dest_path)
                print(f"Copied {source_path} to {dest_path}")
            except Exception as e:
                print(f"Error copying {source_path}: {e}")

def recursive_copy(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            recursive_copy(item_path, dest_dir)
        elif os.path.isfile(item_path):
            copy_files(source_dir, dest_dir)

def main():
    parser = argparse.ArgumentParser(description='Recursive file copying and sorting.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory.')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Path to the destination directory. Default is "dist".')
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    recursive_copy(source_dir, dest_dir)

if __name__ == "__main__":
    main()