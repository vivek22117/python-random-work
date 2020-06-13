import csv


def portfolio_cost(filename, *, errors='warn'):           # * denotes that optional parameter errors will always be called with name
    """
    Calculate the share*price for given data file
    :param errors:
    :param filename:  filename to be read
    :return:  total cost of shares
    """
    if errors not in {'warn', 'raise', 'silent'}:
        raise ValueError("errors must be on of 'warn', 'silent', 'raise'")

    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)              # skip the header line
        for row_no, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', row_no, 'Bad row:', row)
                    print('Row:', row_no, 'Reason:', err)
                elif errors == 'raise':
                    raise ValueError
                else:
                    pass                # Ignores
                continue
            total += row[2]*row[3]
    return total


total_cost = portfolio_cost('data/missing.csv', errors='warn')
print(total_cost)
