
# CLI Notes App

A simple and lightweight CLI notes app.

## Features

- **Read Notes**: View the latest, oldest, or all notes with optional tag filtering.
- **Add Notes**: Quickly add new notes with a tag.
- **Edit Notes**: Modify the content or tag of an existing note.
- **Delete Notes**: Remove specific notes or delete all notes at once.
- **Search Notes**: Find notes containing a specific keyword.
- **Export Notes**: Export all notes to an HTML file for easy viewing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/stigsec/cli-notes.git
    cd cli-notes
    ```

2. Edit the notesPath variable in both python scripts:
   ```bash
   notesPath = #Your path to a notes.json file, eg. C:\\Personal\\notes.json
   ```

## Usage

### Add a New Note
```bash
python main.py add Your note here --tag your-tag
```

### Read Notes
- Read all notes:
    ```bash
    python main.py read
    ```
- Read the last 5 notes:
    ```bash
    python main.py read 5
    ```
- Read the first 5 notes:
    ```bash
    python main.py read -5
    ```
- Read notes filtered by tag:
    ```bash
    python main.py read --tag your-tag
    ```

### Delete Notes
- Delete all notes:
    ```bash
    python main.py del
    ```
- Delete a specific note:
    ```bash
    python main.py delnote <note-id>
    ```

### Edit Notes
- Edit note content:
    ```bash
    python main.py edit <note-id> New content here
    ```
- Edit note tag:
    ```bash
    python main.py edittag <note-id> new-tag
    ```

### Search Notes
```bash
python main.py search keyword
```

### Export Notes to HTML
```bash
python main.py export <path-to-export-html>
```

## File Structure

- `main.py`: Main script for interacting with the CLI.
- `notes_helper.py`: Helper functions for managing notes.
- `notes.json`: JSON file where notes are stored.

## Notes Path Configuration

You can modify the `notesPath` directly in the source code (required both in main.py and notes_helper.py).

## ToDo

 - Note pinning
 - CLI color coding
 - Notes encryption
 - Interactive shell mode
 - Statistics
 - More export options
 - Backup
 - Customization options

## License

MIT License. See [LICENSE](LICENSE) for more details.

---

Developed by stigsec
