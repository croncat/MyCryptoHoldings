import json

from account import Account
from account import BitcoinAccount
from account import ZcashAccount
from account import MoneroAccount

def my_crypto_holdings():
    with open('cryptos.json') as json_data:
        cryptos = json.load(json_data)
        print('Retrieving data...')
        accounts = [Account.factory(i) for i in cryptos]

        total_usd = 0
        for account in accounts:
            account.fill_balance()
            account.fill_usd_balance()
            total_usd += account.balance_usd; 

        print('TOTAL HOLDINGS: %.2f usd' % total_usd)

if __name__ == '__main__':
    my_crypto_holdings()