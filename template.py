import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name= "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init___.py",
    f"src/{project_name}/components/__init___.py",
    f"src/{project_name}/utils/__init___.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init___.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init___.py",
    f"src/{project_name}/entity/__init___.py",
    f"src/{project_name}/pipeline/config-entity.py",
    f"src/{project_name}/constants/__init___.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as fr:
            pass
            logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} already exists")