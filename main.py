import os
import shutil
import sys

CATEGORIES = {
    'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'videos': ['AVI', 'MP4', 'MOV', 'MKV'],
    'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
    'archives': ['ZIP', 'GZ', 'TAR']
}

unknown_extensions = []
known_extensions = []


def create_category_folders(folder_path):
    for category in CATEGORIES.keys():
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)


def process_folder(folder_path):
    global known_extensions
    global unknown_extensions

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file_path)
            extension = extension.upper()[1:] if extension else ''  # Убираем точку из расширения

            known_category = None
            for category, extensions in CATEGORIES.items():
                if extension in extensions:
                    known_category = category
                    break

            if known_category:
                known_extensions.append(extension)
                new_file_name = file if '.' in file else file + extension
                new_file_path = os.path.join(folder_path, known_category, new_file_name)
                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                shutil.move(file_path, new_file_path)
            else:
                unknown_extensions.append(extension)

    # Удаляем пустые папки
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


if __name__ == '__main__':
    target_folder = "Путь к папке"

    create_category_folders(target_folder)
    process_folder(target_folder)

    print('Список файлов в каждой категории:')
    for category in CATEGORIES.keys():
        category_path = os.path.join(target_folder, category)
        if os.path.exists(category_path):
            files = os.listdir(category_path)
            print(f'{category}: {", ".join(files)}')

    print('Перечень известных расширений:')
    print(', '.join(set(known_extensions)))

    print('Перечень неизвестных расширений:')
    print(', '.join(set(unknown_extensions)))
