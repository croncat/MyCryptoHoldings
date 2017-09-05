import argparse
import json

from terminaltables import SingleTable

from account import Account
from account import BitcoinAccount
from account import ZcashAccount
from account import OtherAccount

parser = argparse.ArgumentParser(description='MyCryptoHoldings [MCH]')
parser.add_argument('-i', '--input', type=str, default='./cryptos.json',
                    help='input json (default: \"./cryptos.json\")')

def total_holdings(accounts):
    total_usd = 0
    crypto_totals = {}
    for account in accounts:
        account.fill_balance()
        account.fill_usd_balance()
        key = str(account.currency)
        if key in crypto_totals:
            crypto_totals[key] += account.balance_usd
        else:
            crypto_totals[key] = account.balance_usd
        total_usd += account.balance_usd;
    return total_usd, crypto_totals

def print_accounts_info(accounts):
    total, crypto_totals = total_holdings(accounts)
    table_data = [ ["CURRENCY", "USD"] ]    

    for key, value in crypto_totals.items():
        #print('%s: %.2f usd' % (key, value))
        table_data.append([key, value])

    table_data.append(["TOTAL HOLDINGS", total])

    table = SingleTable(table_data, "Summary")
    print(table.table)

def my_crypto_holdings():
    args = parser.parse_args()
    with open(args.input) as json_data:
        cryptos = json.load(json_data)
        print('Retrieving data...')
        accounts = [Account.factory(i) for i in cryptos]
        print_accounts_info(accounts)

if __name__ == '__main__':
    my_crypto_holdings()
