def get_entries_from_console():
    entries = []
    while True:
        entry = input("Enter a word (or type 'q' to finish): ").strip()
        if entry.lower() == 'q':
            break
        if entry:  # Check if entry is not empty
            entries.append(entry)
    return entries


if __name__ == "__main__":
    inputs = get_entries_from_console()
    print("Entries:", inputs)
