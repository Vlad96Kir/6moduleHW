import os
import glob
import shutil

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

path = ""


for extension, folder_name in extensions.items():
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Найдено {len(files)} файла(-ов) с расширением {extension}.")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        os.mkdir(os.path.join(path, folder_name))
        print(f"[+] Создана папка {folder_name}.")

    for file in files:
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        print(f"[*] Перенесён файл '{file}' в {dst}")
        shutil.move(file, dst)