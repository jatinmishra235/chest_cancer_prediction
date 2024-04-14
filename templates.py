from pathlib import Path
import os

project = 'cancerClassifier'

files = [
    f"{project}/__init__.py",
    f"{project}/components/__init__.py",
    f"{project}/utils/__init__.py",
    f"{project}/config/__init__.py",
    f"{project}/config/configuration.py",
    f"{project}/pipeline/__init__.py",
    f"{project}/entity/__init__.py",
    f"{project}/constants/__init__.py",

    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "app.py",
    "templates/index.html"
]

for file in files:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as obj:
            pass
    else:
        print(f"filepath: {filepath} already exist")