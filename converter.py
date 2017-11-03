import requests


def get_price(coin):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}/?convert=CAD'.format(coin)
    json_data = requests.get(url).json()
    btc = json_data[0]
    json_price_cad = btc['price_cad']
    return json_price_cad


while True:

    currency1 = input('\nWhat currency are you converting?\n')
    currency2 = input('\nWhat currency are you converting to?\n')
    amount = input('\nHow much of the currency do I need?\n')

    # get live market data from coinmarketcap.com
    if currency1 in ('neo', 'NEO'):
        currency1_price = get_price('neo')
    if currency1 in ('omg', 'OMG'):
        currency1_price = get_price('omisego')
    if currency2 in('eth', 'ETH'):
        currency2_price = get_price('ethereum')
    if currency2 in ('btc', 'BTC'):
        currency2_price = get_price('bitcoin')

    total_currency2 = float(amount) / float(currency2_price)
    total_currency1 = float(amount) / float(currency1_price)

    print('\nYou need {:0.5f} '.format(total_currency1) + currency1 + ' to buy {:0.5f} '.format(total_currency2) + currency2)

    print('\nGet new quote? [y/N]')
    answer = input()
    if answer in ('n', 'N'):
        exit()
