def display_books():
    file = open("books.txt", "r")

    print("\nBOOK LIST")
    print("-" * 70)

    for line in file:
        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) != 5:
            continue

        print(
            "ID:", data[0],
            "| Book:", data[1],
            "| Status:", data[2]
        )

    file.close()


def search_book():
    keyword = input("Enter book name or book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) != 5:
            continue

        book_id = data[0]
        book_name = data[1]

        if keyword.lower() in book_name.lower() or keyword == book_id:

            print("\nBook Found")
            print("Book ID   :", data[0])
            print("Name      :", data[1])
            print("Status    :", data[2])
            print("Issued To :", data[3])
            print("Overdue   :", data[4], "days")

            found = True

    file.close()

    if found == False:
        print("Book not found.")


def issue_book():
    book_id = input("Enter book ID to issue: ")
    student = input("Enter student name: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    found = False
    updated_lines = []

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) != 5:
            continue

        if data[0] == book_id:

            found = True

            if data[2] == "Available":

                data[2] = "Issued"
                data[3] = student
                data[4] = "0"

                print("Book issued successfully.")

            else:
                print("Book is already issued.")

        updated_lines.append(",".join(data) + "\n")

    file = open("books.txt", "w")

    file.writelines(updated_lines)

    file.close()

    if found == False:
        print("Book ID not found.")


def return_book():
    book_id = input("Enter book ID to return: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    found = False
    updated_lines = []

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) != 5:
            continue

        if data[0] == book_id:

            found = True

            if data[2] == "Issued":

                days = int(input("Enter number of overdue days: "))

                fine = days * 5

                print("Overdue Fine: Rs.", fine)

                data[2] = "Available"
                data[3] = "None"
                data[4] = "0"

                print("Book returned successfully.")

            else:
                print("Book is already available.")

        updated_lines.append(",".join(data) + "\n")

    file = open("books.txt", "w")

    file.writelines(updated_lines)

    file.close()

    if found == False:
        print("Book ID not found.")


def main():

    while True:

        print("\n===== LIBRARY MANAGEMENT =====")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_books()

        elif choice == "2":
            search_book()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()
