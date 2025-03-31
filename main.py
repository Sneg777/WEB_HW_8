from load_data import load_authors, load_quotes
from search import search_by_author, search_by_tag

if __name__ == "__main__":
    load_authors()
    load_quotes()
    while True:
        command = input("Please, enter command: ").strip()
        if command.startswith("name:"):
            search_by_author(command.split(":")[1].strip())
        elif command.startswith("tag:"):
            search_by_tag(command.split(":")[1].strip())
        elif command == "exit":
            print('Exit ...')
            break
        else:
            print("Wrong command")
