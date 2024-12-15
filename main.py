import argparse
from datetime import datetime
from notes_helper import *

notesPath = #Your path to a notes.json file, eg. C:\\Personal\\notes.json

parser = argparse.ArgumentParser(description="Simple and quick CLI notes app", epilog="by stigsec")
subparsers = parser.add_subparsers(dest='mode', help="Mode of operation")

read_parser = subparsers.add_parser('read', help="Read notes")
read_parser.add_argument('number', type=int, nargs='?', default=None, help="Number of notes to read. Use a negative number to read oldest notes.")
read_parser.add_argument('--tag', help="Filter notes by tag")

add_parser = subparsers.add_parser('add', help="Add a new note")
add_parser.add_argument('note', nargs='+', help="The note to add")
add_parser.add_argument('--tag', help="Tag for the note", default="general")

subparsers.add_parser('del', help="Delete all notes")

delnote_parser = subparsers.add_parser('delnote', help="Delete a specific note")
delnote_parser.add_argument('id', help="ID of the note to delete")

edit_parser = subparsers.add_parser('edit', help="Edit an existing note")
edit_parser.add_argument('id', help="ID of the note to edit")
edit_parser.add_argument('new_text', nargs='+', help="New text for the note")

edittag_parser = subparsers.add_parser('edittag', help="Edit the tag of an existing note")
edittag_parser.add_argument('id', help="ID of the note to edit the tag for")
edittag_parser.add_argument('new_tag', help="New tag for the note")

search_parser = subparsers.add_parser('search', help="Search for notes containing a keyword")
search_parser.add_argument('keyword', help="The keyword to search for")

export_parser = subparsers.add_parser('export', help="Export notes to an HTML file")
export_parser.add_argument('export_path', help="Path to save the HTML file")

args = parser.parse_args()

match args.mode:
    case 'read':
        notes = load_notes()
        notes_list = list(notes.items())
        
        if args.tag:
            notes_list = [note for note in notes_list if note[1]['tag'].lower() == args.tag.lower()]
        
        if args.number is None:
            notes_to_display = notes_list
        elif args.number > 0:
            notes_to_display = notes_list[-args.number:]
        else:
            notes_to_display = notes_list[:abs(args.number)]
        
        if notes_to_display:
            for note_id, note_data in notes_to_display:
                print(f"{note_id}: [{note_data['tag']}] {note_data['content']}")
        else:
            print("No notes found.")

    case 'add':
        notes = load_notes()
        note_id = str(len(notes) + 1)
        notes[note_id] = {
            "content": " ".join(args.note),
            "tag": args.tag,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        save_notes(notes)
        print("Note added successfully.")

    case 'del':
        if delete_all_notes():
            print("All notes deleted successfully.")
        else:
            print("No notes to delete.")

    case 'delnote':
        notes = load_notes()
        if delete_specific_note(notes, args.id):
            print("Note deleted and IDs adjusted successfully.")
        else:
            print("Invalid note ID.")

    case 'edit':
        notes = load_notes()
        if update_note_content(notes, args.id, args.new_text):
            print("Note updated successfully.")
        else:
            print("Invalid note ID.")

    case 'edittag':
        notes = load_notes()
        if update_note_tag(notes, args.id, args.new_tag):
            print("Tag updated successfully.")
        else:
            print("Invalid note ID.")

    case 'search':
        notes = load_notes()
        results = search_notes(notes, args.keyword)
        if results:
            print("Matching notes:")
            for note_id, note_data in results.items():
                print(f"{note_id}: [{note_data['tag']}] {note_data['content']}")
        else:
            print("No matching notes found.")

    case 'export':
        notes = load_notes()
        export_notes_to_html(notes, args.export_path)
        print(f"Notes exported to {args.export_path}.")

    case _:
        parser.print_help()
