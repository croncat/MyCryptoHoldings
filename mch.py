import argparse
import json

from account import Account
from account import BitcoinAccount
from account import ZcashAccount
from account import OtherAccount

parser = argparse.ArgumentParser(description='MyCryptoHoldings [MCH]')
parser.add_argument('-i', '--input', type=str, default='./cryptos.json',
                    help='input json (default: \"./cryptos.json\")')
parser.add_argument('-j', '--json', action='store_true', 
                    help='print a json object')
parser.add_argument('-p', '--pretty', action='store_true', help='table print')

def total_holdings(accounts):
    outobj = {}
    outobj["coins"] = {}
    outobj["total_usd"] = 0
    for account in accounts:
        account.fill_balance()
        account.fill_usd_balance()
        key = str(account.currency)
        if key in outobj["coins"]:
            outobj["coins"][key]["usd"] += account.balance_usd
            outobj["coins"][key]["balance"] += account.balance
        else:
            outobj["coins"][key] = {}
            outobj["coins"][key]["usd"] = account.balance_usd
            outobj["coins"][key]["balance"] = account.balance
        outobj["total_usd"] += account.balance_usd;
    return outobj

def print_holdings(holdings):
    print('TOTAL HOLDINGS: %.2f usd' % holdings["total_usd"])
    for key, value in holdings["coins"].items():
        print('%s: %.8f (%.2f usd)' % (key, value["balance"], value["usd"]))

def pretty_print_holdings(holdings):
    from terminaltables import SingleTable
    table_data = [["CURRENCY", "BALANCE", "USD"]]
    for key, value in holdings["coins"].items():
        table_data.append([key, value["balance"], value["usd"]])
    table = SingleTable(table_data, "Coins")
    print('TOTAL HOLDINGS: %.2f usd' % holdings["total_usd"])
    print(table.table)

def my_crypto_holdings():
    args = parser.parse_args()
    with open(args.input) as json_data:
        cryptos = json.load(json_data)
        if (not args.json):
            print('Retrieving data...')
        accounts = [Account.factory(i) for i in cryptos]
        holdings = total_holdings(accounts)
        if (args.json):
            print(json.dumps(holdings, indent=4))
        elif (args.pretty):
            pretty_print_holdings(holdings)
        else:
            print_holdings(holdings)

if __name__ == '__main__':
    my_crypto_holdings()
