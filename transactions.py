import os
from pprint import pprint
import requests


def get_transactions():
    url = "https://ec.nintendo.com/api/my/transactions"

    params = {'limit': '100', 'offset': '0'}

    headers = {
        'cookie': f'JSESSIONID={os.environ["SESSION_ID"]}',
    }

    response = requests.get(url, headers=headers, params=params)
    # print(response.json())

    return response.json()


if __name__ == '__main__':
    transactions_response = get_transactions()
    transactions = transactions_response['transactions']
    total = 0
    # print(transactions)
    print(f'Total games: {transactions_response["total"]}')
    # pprint(transactions[0])
    for tran in transactions:
        if 'amount' in tran.keys():
            # print(f"{tran['title']} {tran['amount']['formatted_value']}\t{tran['date']}")
            total += float(tran['amount']['raw_value'])
    print(f'\nTotal Amount: ${round(total, 2)}')
    #
    # response1 = requests.get('https://accounts.nintendo.com/login')
    # print(response1.text)


