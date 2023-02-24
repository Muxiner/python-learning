import os
import sys

image_formats = ['JPG', 'JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']

def batch_rename(path, prefix, ext=None):
    """
    批量重命名指定目录下的文件，使用指定的前缀进行命名。
    :param path: 目录路径
    :param prefix: 文件名前缀
    :param ext: 文件扩展名
    :return: None
    """
    try:
        # 获取目录中的所有文件
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        file_count = 0
        # 统计文件数量
        for filename in files:
            if not filename.startswith("."):
                file_count += 1 

        # print(f"files number: {file_count}")
        # 根据文件数量确定数字个数
        digits = len(str(file_count))

        # 遍历目录中的每个文件，生成新的文件名并进行重命名操作
        for i, filename in enumerate(files):
            # 跳过目录中的子目录和隐藏文件
            if not os.path.isfile(os.path.join(path, filename)) or filename.startswith("."):
                continue
            

            # 生成新的文件名
            # if ext not in image_formats:
            #     ext = os.path.splitext(filename)[1]  # 提取文件扩展名
            # else:
            #     ext = f".{ext}"

            file_ext = os.path.splitext(filename)[1] if ext not in image_formats else f".{ext}"

            new_filename = f"{prefix}_{i+1:0{digits + 2}d}{file_ext}"

            # 重命名文件
            old_path = os.path.join(path, filename)
            new_path = os.path.join(path, new_filename)
            os.rename(old_path, new_path)

            print(f"Task N0.{i+1:0{digits + 2}d}: {filename}\n{'':{digits + 7}}===> {new_filename}")

        print(f"Renamed {file_count} files in total.")

    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    # 获取目录路径和文件名前缀
    path = input("Enter directory path: ").strip()
    prefix = input("Enter file name prefix: ").strip()
    ext = input("Enter new file extension (press Enter to use original file extension): ").strip()

    # 进行批量重命名操作
    batch_rename(path, prefix, ext)
