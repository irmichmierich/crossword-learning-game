import json

file_path = "../data/terms.json"
with open(file_path, "r") as file:
    terms = json.load(file)

for term, definition in terms.items():
    print(f"{term}: {definition}")