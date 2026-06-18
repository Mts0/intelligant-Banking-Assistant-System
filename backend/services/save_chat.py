import json


FOLDER = "backend/database"
def save_chat(data: dict) -> str :
    path = f"{FOLDER}/chat_storage.json"
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

            return {"response": "SAVED"}
    
    except:
        return {"response": "NO SAVED!"}
    

def get_chats():
    path = f"{FOLDER}/chat_storage.json"
    try:
        with open(path, "r") as f:
            json_data = json.load(f)

            return {"response": json_data}

    except:
        return {"response": "ERROR!"}
