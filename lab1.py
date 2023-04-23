# todo: Необходимо реализовать консольную утилиту marge.py которая реализует функцию слияния
# содержимого файлов определенного типа с указанного каталога в один файл json при задании параметров:
# ./ marge.py -v --root_dir=ROOT_FOLDER output.json
# 
# Где:
# output.json Исходный файл
# --root_dir  Директория для обработки
# 
# Структура каталогов выглядит следующим образом:
# ROOT_FOLDER   -->   A  ---  w.txt
                        #  -  x.txt
                    # B  ---  z.txt
                        #  -  y.txt
# 
# Результат: в файле output.json
# {
  # "VectorTelemetry": {
    # "w": 74.72395045538597,
    # "x": 74.72395045538597,
    # "y": 74.72395045538597,
    # "z": 74.72395045538597
  # }
# }
# Примечание: О запуске и окончании утилиты информировать пользователя через логгер.
# 
# Перед тем как написать утилиту нужно решить локальные подзадачи в папке simple.
# 1. Посмотреть как работает логгер
# 2. Разобраться с передачей аргументов программе через коммандную строку
# 3. Понять как работает обход папок
# Далее соединить полученные знания в утилите merge.py

from argparse import ArgumentParser
import logging
import os
import json

def find_files(catalog, f):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name.endswith(f)]
    return find_files

version = "0.0.1"
parser = ArgumentParser(prog="merge", description="Merge files content to json file", epilog="Go have fun")
parser.add_argument('output', help="name of an output file")
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--root_dir", help="set the root directory containing original files")

args = parser.parse_args()

logger = logging.getLogger()
logger.name = "merge.py"
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(logging.INFO)

logger.info("Starting...")

files_to_merge = find_files(args.root_dir, '.txt')

output_dict = dict()

for file in files_to_merge:
    with open(file, "r") as f:
        output_dict[file.split('/')[-1].split('.')[0]] = f.read()

output_file = args.output
output_dict = {"VectorTelemetry": output_dict}

with open(output_file, "w") as out_file:
    json.dump(output_dict, out_file)

logger.info("All done")

