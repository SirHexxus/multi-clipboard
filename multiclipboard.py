#!/usr/bin/env python3

import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def list_data(filepath):
    data = load_data(filepath)
    print(data)


def main():
    if len(sys.argv) == 2:
        command = sys.argv[1].lower()
        data = load_data(SAVED_DATA)
        if command == "save":
            key = input("Enter a key: ")
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
        elif command == "copy":
            key = input("Enter a key: ")
            if key in data:
                clipboard.copy(data[key])
                print("Copied to clipboard")
            else:
                print("Key not found")
        elif command == "clear":
            key = input("Enter a key: ")
            if key in data:
                del data[key]
                save_data(SAVED_DATA, data)
                print(f"Cleared {key}")
            else:
                print("Key not found")
        elif command == "list":
            list_data(SAVED_DATA)
        else:
            print('Invalid command')
    else:
        print('Invalid number of arguments')


if __name__ == "__main__":
    main()
