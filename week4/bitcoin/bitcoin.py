import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
elif sys.argv[1].isalpha():
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    coin = float(sys.argv[1])

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    rate = r.json()['bpi']['USD']['rate'].replace(',', '')
    amount = float(rate) * coin

    print(f"${amount:,.4f}")

except requests.RequestException:
    print("Please try again")