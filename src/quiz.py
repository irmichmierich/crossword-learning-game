import json
import random

# Load terms from JSON file
file_path = "../data/terms.json"
with open(file_path, "r") as file:
    terms = json.load(file)

# Convert dict to list of (term, definition) tuples
items = list(terms.items())

# Shuffle so quiz order is random
random.shuffle(items)

score = 0
print("git ISMS Term Quiz")
print("---------------------")

for term, definition in items:
    print(f"\nDefinition: {definition}")
    answer = input("Your answer: ").strip()

    if answer.lower() == term.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is: {term}")

print(f"\nFinal score: {score}/{len(items)}")