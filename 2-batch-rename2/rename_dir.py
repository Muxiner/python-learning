import os
import sys

image_formats = ['JPG', 'JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'HEIC', 'CR2', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']

def list_dir(dir_path):
    try:
        dirs_list = [os.path.join(dir_path, dir_item) for dir_item in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, dir_item))]
        file_list = [os.path.join(dir_path, file_item) for file_item in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file_item))]
        if len(dirs_list) > 0:
            for dir_item in dirs_list:
                list_dir(dir_item)
        if len(file_list) > 0:
            rename_files(dir_path)

    except OSError as os_error:
        print(f"Error: {os_error}")
        sys.exit(1)

def rename_files(dir_path):
    try:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        file_count = 0
        # 统计文件数量
        for filename in files:
            if not filename.startswith("."):
                file_count += 1 

        digits = len(str(file_count))

        file_count = 0
        prefix = "IMG"
        tryagain = False
        # 遍历目录中的每个文件，生成新的文件名并进行重命名操作
        for i, filename in enumerate(files):
            # 跳过目录中的子目录和隐藏文件
            # if not os.path.isfile(os.path.join(path, filename)) or filename.startswith("."):
            if filename.startswith("."):
                continue
            
            if os.path.splitext(filename)[1][1:] not in image_formats:
                continue
            file_ext = os.path.splitext(filename)[1]

            
            new_filename = f"{prefix}_{i+1:0{digits}d}{file_ext}"

            # 重命名文件
            old_path = os.path.join(dir_path, filename)
            new_path = os.path.join(dir_path, new_filename)

            if filename != new_filename:
               if os.path.exists(new_path): 
                    os.rename(new_path, os.path.join(dir_path, f"temp{i+1:0{digits}d}{file_ext}"))
                    tryagain = True
               os.rename(old_path, new_path)
            # elif filename != new_filename:
            #     os.rename(old_path, new_path)
            # print(f"Task N0.{i+1:0{digits + 2}d}: {filename}\n{'':{digits + 7}}===> {new_filename}")

            file_count += 1

        print(f"Path: {dir_path} \nRenamed {file_count} files in total.")
        if tryagain:
            rename_files(dir_path)



    except OSError as os_error:
        print(f"Error: {os_error}")
        sys.exit(1)


if __name__ == '__main__':
    path = input("Input Path:").strip()
    list_dir(path)
