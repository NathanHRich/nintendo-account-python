import os
from pprint import pprint
import requests


def get_transactions():
    url = "https://ec.nintendo.com/api/my/transactions"
    limit = '100'
    params = {'limit': limit, 'offset': '0'}
    headers = {
        'cookie': f'JSESSIONID={os.environ["SESSION_ID"]}',
    }
    all_transactions = []
    while params:
        response = requests.get(url, headers=headers, params=params).json()
        if 'error' in response.keys():
            print(response)
            exit(0)
        all_transactions += response['transactions']
        cur_length = response['length'] + response['offset']
        if cur_length < response['total']:
            params = {'limit': limit, 'offset': str(cur_length)}
        else:
            params = None
    return all_transactions


if __name__ == '__main__':
    transactions = get_transactions()
    transactions = sorted(transactions, key=lambda i: i['date'])
    # pprint(transactions)
    total = 0
    for tran in transactions:
        if 'amount' in tran.keys():
            print(f"\nTitle: {tran['title']}\n"
                  f"Cost: {tran['amount']['formatted_value']}\n"
                  f"Date: {tran['date']}")
            total += float(tran['amount']['raw_value'])
    print('\n-----------------------------------------------------------------------------------\n')
    print(f'Total Titles: {len(transactions)}')
    print(f'Total Cost: ${round(total, round(2))}')
