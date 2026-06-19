import json
import os

FOLDER = "backend/database"


def save_chat(data: dict):
    path = f"{FOLDER}/chat_storage.json"

    try:
        # إذا لم يكن الملف موجوداً أنشئ قائمة فارغة
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    chats = json.load(f)
                except json.JSONDecodeError:
                    chats = []
        else:
            chats = []

        # إضافة المحادثة الجديدة
        chats.append(data)

        # حفظ جميع المحادثات
        with open(path, "w", encoding="utf-8") as f:
            json.dump(chats, f, ensure_ascii=False, indent=4)

        return {"response": "SAVED"}

    except Exception as e:
        return {"response": f"ERROR: {str(e)}"}


def get_chats():
    path = f"{FOLDER}/chat_storage.json"

    try:
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        return {"response": json_data}

    except Exception as e:
        return {"response": f"ERROR: {str(e)}"}