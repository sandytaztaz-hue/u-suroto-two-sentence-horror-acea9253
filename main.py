import os

ENTRY = "My daughter drew our family for school today, and she drew three people. There are only two of us in this house, and the third one is holding my hand."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
