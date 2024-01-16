import re

transactions = [{'type': 'purchase', 'amount': 50, 'date': '2024-01-14'},
                {'type': 'sale', 'amount': 30.5, 'date': '2024-01-15'}]

transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']


# Mach eine Liste aus den transactions
def list_of(my_key):
    amount_values = [transaction['amount'] for transaction in transactions]
    return amount_values


print(list_of('amount\n'))


# Summe der transaktionen aus liste
def sum_up(my_type):
    Summe = [transaction['amount'] for transaction in transactions
             if transaction['type'] == my_type]
    return (sum(Summe))


# alle die an einem bestimmten Tag gemacht wurden
def findall(my_key, datum):
    trans_gestern = [transaction for transaction in transactions
                     if transaction[my_key] == datum]
    return trans_gestern


def is_valid_data_format(date_strings):
    date_pattern = re.compile(
        r'^\d{4}-\d{2}-\d{2}$')  # ^ = Anfang \d = 4 bestimmte character dann  "-" dann \d = 2 bestimmte chars "-" \d wieder 2 bestimmte chars $Ende von String
    # doestnt check for day/month order
    return bool(date_pattern.match(date_strings))


my_transactions = findall('date', '2024-01-14')
print('\n', my_transactions)
print(len(my_transactions), '\n')

income = sum_up('purchase')
expenses = sum_up('sale')
print('income', income)
print('expenses', expenses)

if (income > expenses):
    print('You made money')
else:
    print('you lost money')

my_date = my = my_transactions[0]['date']
print(my_transactions[0]['date'])
print(type(my_date))
print(is_valid_data_format(my_date))