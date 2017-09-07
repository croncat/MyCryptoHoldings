# MyCryptoHoldings

A simple system to get stimated value of your holdings in usd.

## Usage:

Add to "cryptos.json" your crypto accounts. You only need to put the public addresses or balances.

## Download and run (linux):

```
$ git clone https://github.com/k0ch/MyCryptoHoldings
$ pip install -r requirements.txt
$ python mch.py
```

## Examples:

```
$ python mch.py
Retrieving data...
TOTAL HOLDINGS: 239986821.98 usd
bitcoin-cash: 5.00000000 (3083.90 usd)
ethereum: 740021.58281975 (239978639.01 usd)
monero: 5.00000000 (589.04 usd)
bitcoin: 1.00000000 (4510.03 usd)
zcash: 0.00000000 (0.00 usd)
```

```
$ python mch.py -j
{
    "total_usd": 239986821.98128572, 
    "coins": {
        "bitcoin-cash": {
            "balance": 5.0, 
            "usd": 3083.8999999999996
        }, 
        "ethereum": {
            "balance": 740021.5828197509, 
            "usd": 239978639.00628573
        }, 
        "monero": {
            "balance": 5.0, 
            "usd": 589.045
        }, 
        "bitcoin": {
            "balance": 1.0, 
            "usd": 4510.03
        }, 
        "zcash": {
            "balance": 0.0, 
            "usd": 0.0
        }
    }
}
```

```
$ python3 mch.py -p
Retrieving data...
TOTAL HOLDINGS: 239986821.98 usd
┌Coins─────────┬───────────────────┬────────────────────┐
│ CURRENCY     │ BALANCE           │ USD                │
├──────────────┼───────────────────┼────────────────────┤
│ ethereum     │ 740021.5828197509 │ 239978639.00628573 │
│ monero       │ 5.0               │ 589.045            │
│ bitcoin-cash │ 5.0               │ 3083.8999999999996 │
│ bitcoin      │ 1.0               │ 4510.03            │
│ zcash        │ 0.0               │ 0.0                │
└──────────────┴───────────────────┴────────────────────┘
```

```
$ python mch.py -i /home/user/holdings.json
Retrieving data...
TOTAL HOLDINGS: 239986821.98 usd
bitcoin-cash: 5.00000000 (3083.90 usd)
ethereum: 740021.58281975 (239978639.01 usd)
monero: 5.00000000 (589.04 usd)
bitcoin: 1.00000000 (4510.03 usd)
zcash: 0.00000000 (0.00 usd)
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
