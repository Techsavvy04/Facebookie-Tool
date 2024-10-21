import json

# Nội dung JSON
data = {
    "autoaddfacebookie": {
        "status": "Hoạt động",
        "source":"https://raw.githubusercontent.com/Techsavvy04/Facebookie-Tool/refs/heads/main/AutoAdd.py"
    }
}

# Tạo file JSON
with open('status.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("File JSON đã được tạo.")
