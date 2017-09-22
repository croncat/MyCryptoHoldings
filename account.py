import requests


class Account:
    # static use only
    cmc = None

    currency = ""
    name = ""
    addr = ""
    balance = 0.0
    balance_usd = 0.0
    wallet_addr = ""

    def __init__(self, crypto):
        self.currency = crypto['currency']
        if 'name' in crypto:
            self.name = crypto['name']
        if 'addr' in crypto:
            self.addr = crypto['addr']
        if 'balance' in crypto:
            self.balance = crypto['balance']
        if 'wallet_addr' in crypto:
            self.wallet_addr = crypto['wallet_addr']

    def factory(crypto):

        type = crypto['currency']
        if type == "bitcoin":
            return BitcoinAccount(crypto)
        elif type == "zcash":
            return ZcashAccount(crypto)
        elif type == "ethereum":
            return EthereumAccount(crypto)
        elif type == "aeon":
            return AeonAccount(crypto)
        elif type == "monero":
            return MoneroAccount(crypto)
        else:
            return OtherAccount(crypto)
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
            url = 'https://blockchain.info/rawaddr/%s' % self.addr
            btc_rsp = requests.get(url)
            if btc_rsp.json():
                self.balance = float(btc_rsp.json()['final_balance'])
                # from satoshi to btc
                self.balance *= 0.00000001


class ZcashAccount(Account):

    def fill_balance(self):
        if self.addr is not "":
            url = 'https://api.zcha.in/v2/mainnet/accounts/%s' % self.addr
            zec_rsp = requests.get(url)
            if zec_rsp.json():
                self.balance = float(zec_rsp.json()['balance'])


class EthereumAccount(Account):

    def fill_balance(self):
        if self.addr is not "":
            url = 'https://api.etherscan.io/api?' \
                  'module=account&action=balance&address=%s' % self.addr
            eth_rsp = requests.get(url)
            if eth_rsp.json():
                self.balance = float(eth_rsp.json()['result'])
                self.balance *= 0.000000000000000001


class AeonAccount(Account):

    def fill_balance(self):
        if self.balance != 0.0:
            return self.balance

        if self.wallet_addr is not "":
            jsoncontent = b'{"jsonrpc":"2.0","id":"0","method":"getbalance"}'
            headers = {'Content-Type': 'application/json'}
            try:
                aeon_rsp = requests.post(
                    self.wallet_addr + '/json_rpc',
                    headers=headers,
                    data=jsoncontent)
                if aeon_rsp.json():
                    self.balance = float(
                        aeon_rsp.json().get(
                            "result", 0).get(
                            'balance', 0))
                    self.balance *= 0.000000000001
            except requests.exceptions.ConnectionError as e:
                msg = (
                    "Getting {currency}'s balance have failed with this message:"
                    "\n{message}\n").format(
                    currency=self.currency, message=e)
                print(msg)


class MoneroAccount(AeonAccount):
    pass


class OtherAccount(Account):

    def fill_balance(self):
        return
