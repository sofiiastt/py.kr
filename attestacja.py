import json
import datetime

def create_note():
    title = input("type notes title: ")
    body = input("type notes body: ")
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    print("the note was successfully saved")

def read_notes():
    filter_date = input(" type the date for filtered_notes (yyyy-mm-dd): ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(filter_date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"title: {note['title']}")
            print(f"body: {note['body']}")
            print(f"date/timestamp: {note['timestamp']}")
            print("-----------")
    else:
        print("the notes weren't found with this date")

def edit_note():
    note_id = int(input("Type ID notes for edit: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("type the new title for the note: ")
            new_body = input("type the new body for the note: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().isoformat()
            print("the note was successfully edited")
            return
    print("the note with current ID was not found")

def delete_note():
    note_id = int(input("Type ID Note to delete: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("the note was successfully deleted")
            return
    print("the note with current ID was not found")
try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = []

while True:
    print("available commands:")
    print("1. add note")
    print("2. read notes with filtered date")
    print("3. edit note")
    print("4. delete note")
    print("5. exit")

    choice = input("type the number of command: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
    
        with open("notes.json", "w") as file:
            json.dump(notes, file, indent=4)
        break
    else:
        print("Wrong command. Please, choose correct command.")
