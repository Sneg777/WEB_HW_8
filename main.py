from load_data import load_authors, load_quotes
from search import search_by_author, search_by_tag, search_by_tags

if __name__ == "__main__":
    load_authors()
    load_quotes()
    while True:
        command = input("Please, enter the command: ").strip()
        if command.startswith("name:"):
            search_by_author(command.split(":")[1].strip())
        elif command.startswith("tag:"):
            search_by_tag(command.split(":")[1].strip())
        elif command.startswith("tags:"):
            search_by_tags(command.split(":")[1].strip())
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Wrong command")
