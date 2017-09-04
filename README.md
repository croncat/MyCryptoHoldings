# MyCryptoHoldings

A simple system to get stimated value of your holdings in usd.

## Usage:

Add to "cryptos.json" your crypto accounts. You only need to put the public addresses or balances.

## Examples:

```
#python mch.py
Retrieving data...
TOTAL HOLDINGS: 227127228.93 usd
ethereum: 227126684.18 usd
monero: 544.75 usd
bitcoin: 0.00 usd
zcash: 0.00 usd
```

```
#python mch.py -i /home/user/holdings.json
Retrieving data...
TOTAL HOLDINGS: 9445.22 usd
bitcoin-cash: 100.84 usd
monero: 8000.34 usd
bitcoin: 345.22 usd
zcash: 998.82 usd
```

cryptos.json:
```
[
    {"currency": "bitcoin", "addr": "15ZrQBTkmxn7nnKUof2FmCmM1nDiosGENQ", "name": "donations"},
    {"currency": "zcash", "addr": "t1bgE4C2WrdAt5L5Yj3fusJzKMBzJoeh1v7", "name": "donations"},
    {"currency": "ethereum", "addr": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", "name": "eth example"},
    {"currency": "monero", "balance": 5.0, "name": "xmr example"},
    {"currency": "bitcoin-cash", "balance": 5.0, "name": "bcc example"},
    {"currency": "bitcoin", "balance": 1.0, "name": "extra example"}
]
```

## Full supported currencies (retrieving balance from public addresses):

* bitcoin
* zcash
* ethereum

## Complete list of supported currencies (most of them without 'addr' support):

[Link](supported_currencies.md)

## Donations:

* BTC: 15ZrQBTkmxn7nnKUof2FmCmM1nDiosGENQ
* ZEC: t1bgE4C2WrdAt5L5Yj3fusJzKMBzJoeh1v7

## ToDo:

If you want, you can add new classes to "account.py" in order to support more currencies and send me a pull request :)
