import os


PATH_DIR_REF = "docs/references"
PATH_DIR_PROMPT = "backend/prompts"

def read_prompt(path):
    path_prompt = f"{PATH_DIR_PROMPT}/{path}"
    with open(path_prompt, "r") as f:
        prompt = f.read()
    return {"prompt": prompt}


def loader_file(path: str):
    path_file = f"{PATH_DIR_REF}/{path}"
    with open(path_file, "r") as f:
        file = f.read()
    return {"data": file}


def list_dir(path=PATH_DIR_REF):
    extract_file = os.listdir(path)
    files = []

    for file in extract_file:
        files.append(file)
    
    return files