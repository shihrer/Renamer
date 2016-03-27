import os

def renamer(root, source, target):
    print("Scanning root folder: " + root)
    for directory, subdirectories, files in os.walk(root, topdown=False):
        print("Scanning : " + directory)
        for file in files:
            if file == source:
                print(file + " -> " + target)
                os.rename(os.path.join(directory, file), os.path.join(directory, target))

if __name__ == "__main__":
    renamer(os.getcwd() + "\\test\\", "Folder.jpg", "cover.jpg")