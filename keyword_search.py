import os


def search_keyword():

    keyword = input("Enter keyword to search: ")

    found = False

    files = os.listdir()

    for filename in files:

        if filename.endswith(".txt"):

            file = open(filename, "r")

            line_number = 0

            for line in file:

                line_number = line_number + 1

                if keyword.lower() in line.lower():

                    print("\nFile:", filename)
                    print("Line Number:", line_number)
                    print("Line:", line.strip())

                    found = True

            file.close()

    if found == False:
        print("\nKeyword not found in any file.")


search_keyword()
