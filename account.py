import requests

class Account:
    #static use only
    cmc = None

    currency = ""
    name = ""
    addr = ""
    balance = 0.0
    balance_usd = 0.0

    def __init__(self, crypto):
        self.currency = crypto['currency']
        if 'name' in crypto:
            self.name = crypto['name']
        if 'addr' in crypto:
            self.addr = crypto['addr']
        if 'balance' in crypto:
            self.balance = crypto['balance']

    def factory(crypto):
        type = crypto['currency']
        if type == "bitcoin": return BitcoinAccount(crypto)
        if type == "zcash": return ZcashAccount(crypto)
        if type == "monero": return MoneroAccount(crypto)
        if type == "ethereum": return EthereumAccount(crypto)
        assert 0, "Bad account creation: " + type
    factory = staticmethod(factory)

    def fill_balance(self):
        raise NotImplementedError()

    def fill_usd_balance(self):
        if Account.cmc is None:
            url = 'https://api.coinmarketcap.com/v1/ticker/'
            Account.cmc = requests.get(url)
        for curr in Account.cmc.json():
            if curr['id'] == self.currency:
                self.balance_usd = float(curr['price_usd']) * self.balance


class BitcoinAccount(Account):
    
    def fill_balance(self):
        if self.addr is not "":
            url = 'https://blockchain.info/rawaddr/%s' %self.addr
            btc_rsp = requests.get(url)
            if btc_rsp.json():
                self.balance = float(btc_rsp.json()['final_balance'])
                #from satoshi to btc
                self.balance *= 0.00000001


class ZcashAccount(Account):

    def fill_balance(self):
        if self.addr is not "":
            url = 'https://api.zcha.in/v2/mainnet/accounts/%s' %self.addr
            zec_rsp = requests.get(url)
            if zec_rsp.json():
                self.balance = float(zec_rsp.json()['balance'])


class MoneroAccount(Account):

    def fill_balance(self):
        return


class EthereumAccount(Account):

    def fill_balance(self):
        if self.addr is not "":
            url = 'https://api.etherscan.io/api?' \
                  'module=account&action=balance&address=%s' %self.addr
            eth_rsp = requests.get(url)
            if eth_rsp.json():
                self.balance = float(eth_rsp.json()['result'])
                self.balance *= 0.000000000000000001
