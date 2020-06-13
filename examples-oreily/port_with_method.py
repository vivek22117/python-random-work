import csv
import glob


def portfolio_cost(file_name):
    """
     Compute total share*price for the csv file provided
    :param file_name: name of the file
    :return: total cost of portfolio
    """

    total = 0.0
    with open(file_name, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)                # skip the first line from file as header
        for row in rows:
            row[2] = int(row[2])
            row[3] = float(row[3])
            total += row[2]*row[3]
    return total


files = glob.glob('data/portfolio*.csv')
for filename in files:
    print(filename, portfolio_cost(filename))

total_cost = portfolio_cost('data/portfolio.csv')
print('Total cost: ', total_cost)

