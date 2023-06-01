import os
import glob
import shutil
import transliterate

extensions = {
    "jpg": "images",
    "jpeg": "images",
    "png": "images",
    "svg": "images",
    "pdf": "doc",
    "xlsx": "doc",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "doc": "doc",
    "docx": "doc",
    "txt": "doc",
    "pptx": "doc",
    "mp3": "audio",
    "wav": "audio",
    "ogg": "audio",
    "amr": "audio",
    "mp4": "video",
    "avi": "video",
    "mov": "video",
    "mkv": "video",
}


def transliterate_path(path):
    return transliterate.translit(path, reversed=True)


def process_files(path):
    for extension, folder_name in extensions.items():
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        print(f"[*] Знайдено {len(files)} файлів з розширенням {extension}.")

        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            os.mkdir(os.path.join(path, folder_name))
            print(f"[+] Створено теку {folder_name}.")

        for file in files:
            basename = os.path.basename(file)
            dst_folder = os.path.join(path, folder_name)
            dst = os.path.join(dst_folder, basename)
            print(f"[*] Переміщено файл '{file}' до {dst}")
            shutil.move(file, dst)

    for root, dirs, _ in os.walk(path, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            process_files(folder_path)

    for root, dirs, _ in os.walk(path, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f"[-] Видалено порожню теку '{folder_path}'.")


if __name__ == "__main__":
    # Жорстко закодований шлях до теки
    path = r"C:\Users\VLAD\Documents\MyFolder"

    # Транслітерація шляху до теки
    path = transliterate_path(path)

    # Починаємо обробку файлів
    process_files(path)
