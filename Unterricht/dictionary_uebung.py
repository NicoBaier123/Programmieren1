import re

transactions = [
    {'type': 'purchase', 'amount': 50, 'date': '2024-01-15'},
    {'type': 'sale', 'amount': 30.5, 'date': '2024-01-15'}
]
transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']


# using list comprehension
def list_of(my_key):
    amount_values = [transaction['my_key'] for transaction in transactions]
    print(list_of('amount'))
    return amount_values


def sum_up(my_type):
    Summe = [transaction['amount'] for transaction in transactions
             if transaction['type'] == my_type]
    return (sum(Summe))


income = sum_up('purchase')
expenses = sum_up('sale')
print('income=', income)
print('expenses=', expenses)

if (income > expenses):
    print('You made money')
else:
    print('You lost money!')


def find_all(my_key, my_value):
    values = [transaction for transaction in transactions if
              transaction[my_key] == my_value]
    return (values)


my_transactions = find_all('date', '2024-01-14')
print(my_transactions)
print(len(my_transactions))


def is_valid_date_format(date_string):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(date_pattern.match(date_string))

#if len(my_transactions)>0:
my_date = my_transactions[0]['date']
print(my_transactions[0]['date'])
print(type(my_date))
print(is_valid_date_format(my_date))
