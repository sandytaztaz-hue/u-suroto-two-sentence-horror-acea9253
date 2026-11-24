import os

ENTRY = "My daughter drew our family for school today, and she drew three people. There are only two of us in this house, and the third one is holding my hand."

# The gate: exactly two sentences, 1 to 400 characters, not only whitespace.
assert ENTRY.strip(), "entry must not be blank"
assert len(ENTRY) <= 400, "entry exceeds 400 characters"
assert ENTRY.count(".") == 2, "entry must be exactly two sentences"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
