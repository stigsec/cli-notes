import json
import os
from datetime import datetime

notesPath = #Your path to a notes.json file, eg. C:\\Personal\\notes.json

def load_notes():
    if not os.path.exists(notesPath):
        return {}
    with open(notesPath, 'r') as f:
        return json.load(f)

def save_notes(notes):
    with open(notesPath, 'w') as f:
        json.dump(notes, f, indent=4)

def delete_all_notes():
    if os.path.exists(notesPath):
        os.remove(notesPath)
        return True
    return False

def delete_specific_note(notes, note_id):
    if note_id in notes:
        del notes[note_id]
        notes = {str(i+1): v for i, (k, v) in enumerate(sorted(notes.items()))}
        save_notes(notes)
        return True
    return False

def update_note_content(notes, note_id, new_text):
    if note_id in notes:
        notes[note_id]['content'] = " ".join(new_text)
        save_notes(notes)
        return True
    return False

def update_note_tag(notes, note_id, new_tag):
    if note_id in notes:
        notes[note_id]['tag'] = new_tag
        save_notes(notes)
        return True
    return False

def search_notes(notes, keyword):
    return {k: v for k, v in notes.items() if keyword.lower() in v['content'].lower()}

def export_notes_to_html(notes, export_path):
    with open(export_path, 'w') as html_file:
        html_file.write("<html><body>\n")
        html_file.write("<h1>Notes</h1>\n")
        html_file.write("<table border='1'>\n")
        html_file.write("<tr><th>ID</th><th>Timestamp</th><th>Tag</th><th>Content</th></tr>\n")
        for note_id, note_data in notes.items():
            html_file.write(f"<tr><td>{note_id}</td><td>{note_data['timestamp']}</td><td>{note_data['tag']}</td><td>{note_data['content']}</td></tr>\n")
        html_file.write("</table>\n")
        html_file.write("</body></html>")
