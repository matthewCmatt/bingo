import random
import pyperclip

# Path to the CSV file containing entries
csv_file_path = 'entries.txt'

# Function to read entries from a CSV file
def read_entries_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        entries = file.read().splitlines()
    return entries

entries = read_entries_from_csv(csv_file_path)

sample_size = 24
selected_entries = random.sample(entries, sample_size)

# Function to copy entries to clipboard one at a time
def copy_entries_to_clipboard(entries):
    for i, entry in enumerate(entries):
        pyperclip.copy(entry)
        input(f"Copied entry {i+1}/{sample_size} to clipboard: {entry}")

copy_entries_to_clipboard(selected_entries)