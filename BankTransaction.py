def read_transactions():
    transactions = []

    file = open("transactions.csv", "r")

    # Skip header
    file.readline()

    for line in file:
        line = line.strip()

        data = line.split(",")

        transaction = {
            "account": data[0],
            "type": data[1],
            "amount": float(data[2]),
            "date": data[3]
        }

        transactions.append(transaction)

    file.close()

    return transactions


def calculate_totals(transactions):
    total_deposits = 0
    total_withdrawals = 0

    for transaction in transactions:

        if transaction["type"] == "Deposit":
            total_deposits += transaction["amount"]

        elif transaction["type"] == "Withdrawal":
            total_withdrawals += transaction["amount"]

    balance = total_deposits - total_withdrawals

    return total_deposits, total_withdrawals, balance


def find_largest_transaction(transactions):
    largest = transactions[0]

    for transaction in transactions:

        if transaction["amount"] > largest["amount"]:
            largest = transaction

    return largest


def find_suspicious_transactions(transactions):
    suspicious = []

    for transaction in transactions:

        if transaction["amount"] > 100000:
            suspicious.append(transaction)

    return suspicious


def display_results(
    total_deposits,
    total_withdrawals,
    balance,
    largest,
    suspicious
):

    print("\nBANK TRANSACTION ANALYZER")
    print("-" * 50)

    print("Total Deposits    :", total_deposits)
    print("Total Withdrawals :", total_withdrawals)
    print("Current Balance   :", balance)

    print("\nLargest Transaction:")
    print("Account :", largest["account"])
    print("Type    :", largest["type"])
    print("Amount  :", largest["amount"])
    print("Date    :", largest["date"])

    print("\nSuspicious Transactions:")

    if len(suspicious) == 0:
        print("No suspicious transactions found.")

    else:
        for transaction in suspicious:
            print(
                transaction["account"],
                transaction["type"],
                transaction["amount"],
                transaction["date"]
            )


def main():

    transactions = read_transactions()

    total_deposits, total_withdrawals, balance = \
        calculate_totals(transactions)

    largest = find_largest_transaction(transactions)

    suspicious = find_suspicious_transactions(transactions)

    display_results(
        total_deposits,
        total_withdrawals,
        balance,
        largest,
        suspicious
    )


main()
