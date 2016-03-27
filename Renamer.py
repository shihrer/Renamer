import os


def renamer(root, source, target, case=False):
    print("Scanning root folder: " + root)
    for directory, subdirectories, files in os.walk(root, topdown=False):
        print("Scanning : " + directory)
        for file in files:
            if not case:
                file = file.lower()
            if file == source:
                print(file + " -> " + target)
                os.rename(os.path.join(directory, file), os.path.join(directory, target))

if __name__ == "__main__":
    directory_exists = False
    root = None
    while not directory_exists:
        # Get root directory
        root = input("Enter directory to scan > ")
        directory_exists = os.path.isdir(root)

    # Get source file name
    source = input("Enter filename to change > ")
    # Get target file name
    target = input("Enter target filename > ")

    confirmation = input("Are you sure you want to scan the directory at {} and rename {} to {}? Y/N > ".format(os.path.abspath(root), source, target))

    if confirmation[0].lower() == "y":
        renamer(root, source, target, False)
