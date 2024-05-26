import random
import pyperclip

# Config
csv_file_path = 'entries.txt'

# Read entries from a CSV file
def read_entries_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        entries = file.read().splitlines()
    return entries

# Copy entries to clipboard one at a time
def copy_entries_to_clipboard(entries):
    for i, entry in enumerate(entries):
        pyperclip.copy(entry)
        input(f"Copied entry {i+1}/{sample_size} to clipboard: {entry}")

# Script
entries = read_entries_from_csv(csv_file_path)
sample_size = 24
selected_entries = random.sample(entries, sample_size)
copy_entries_to_clipboard(selected_entries)