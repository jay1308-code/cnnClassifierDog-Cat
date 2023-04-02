import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s:%(message)s:]')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,file_name = os.path.split(filepath)

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating file dir:[{file_dir}] for file:[{file_name}]")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"wb") as f:
            pass
            logging.info(f"Creating empty file:[{file_name}]")

    else:
        logging.info(f"[{file_name}] is already exists")        


