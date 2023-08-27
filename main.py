import requests


data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR").json()

print(data)
print(f"доллар: {data['USD']}")
print(f"eвро:  {data['EUR']}")
print(f"биткоин: {data['BTC']}")








