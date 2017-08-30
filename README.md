# MyCryptoHoldings

[This is a POC]

##Usage:

Add to "cryptos.json" your crypto accounts. You only need to put the public addresses. In case of monero and zcash z addresses, right now you can put directly the balance (I don't develop any method to obtain protected balances [for now])

##Example:

cryptos.json:
```
[
	{"currency": "bitcoin", "addr": "15ZrQBTkmxn7nnKUof2FmCmM1nDiosGENQ", "name": "donations"},
	{"currency": "monero", "balance": 5.0, "name": "example"}
]
```

run example:
```
#python mch.py 
Retrieving data...
TOTAL HOLDINGS: 648.20 usd
```

##ToDo:

The program only support BTC, ZEC and XMR for now. If you want, you can add new classes to "account.py" in order to support more currencies and send me a pull request :)
