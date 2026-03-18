import json
import os

FILE = "used_passwords.json"

def check_password_reuse(password):

    if not os.path.exists(FILE):

        with open(FILE, "w") as f:
            json.dump([], f)

    try:
        with open(FILE) as f:
            data = json.load(f)
    except:
        data = []

    reused = password in data

    if not reused:

        data.append(password)

        with open(FILE, "w") as f:
            json.dump(data, f)

    return reused