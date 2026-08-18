import csv


def valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


def valid_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False


def clean_data():

    valid_records = []
    invalid_records = []
    duplicate_records = []

    # Set to store unique customer IDs
    seen_ids = set()

    # Open input CSV file
    file = open("customers.csv", "r")

    reader = csv.reader(file)

    # Read header
    header = next(reader)

    for row in reader:

        try:
            # Check for malformed row
            if len(row) != 4:
                invalid_records.append(row)
                continue

            customer_id = row[0].strip()
            name = row[1].strip()
            email = row[2].strip()
            phone = row[3].strip()

            # Check missing fields
            if (
                customer_id == ""
                or name == ""
                or email == ""
                or phone == ""
            ):
                invalid_records.append(row)
                continue

            # Check duplicate record
            if customer_id in seen_ids:
                duplicate_records.append(row)
                continue

            # Check email
            if not valid_email(email):
                invalid_records.append(row)
                continue

            # Check phone
            if not valid_phone(phone):
                invalid_records.append(row)
                continue

            # Record is valid
            valid_records.append(row)

            seen_ids.add(customer_id)

        except Exception:
            invalid_records.append(row)

    file.close()

    # Write valid records
    file = open("cleaned.csv", "w", newline="")

    writer = csv.writer(file)

    writer.writerow(header)

    for row in valid_records:
        writer.writerow(row)

    file.close()

    # Write invalid records
    file = open("errors.csv", "w", newline="")

    writer = csv.writer(file)

    writer.writerow(header)

    for row in invalid_records:
        writer.writerow(row)

    # Add duplicate records to errors file
    for row in duplicate_records:
        writer.writerow(row)

    file.close()

    print("Data cleaning completed.")
    print("Valid records   :", len(valid_records))
    print("Invalid records :", len(invalid_records))
    print("Duplicate records:", len(duplicate_records))
    print("Saved valid data to cleaned.csv")
    print("Saved errors to errors.csv")


clean_data()
