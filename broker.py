import requests

while True:
    print('\nBuy ETH or BTC?')
    currency = input()

    # get live market data
    if currency == 'eth' or currency == 'ETH':
        main_api = 'https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=CAD'
        json_data = requests.get(main_api).json()
        btc = json_data[0]
        json_price_cad = btc['price_cad']
    if currency == 'btc' or currency == 'BTC':
        main_api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=CAD'
        json_data = requests.get(main_api).json()
        btc = json_data[0]
        json_price_cad = btc['price_cad']

    # gather more details about the transaction
    print('\nHow much would you like to buy?')
    amount = input()
    print("\nWhat's your fee? (in %)")
    raw_fee = input()
    fee = float(raw_fee) / 100 + 1

    # calculate CAD price after fee
    cad_price_after_fee = float(json_price_cad) * float(fee)

    # print quote
    print('\n::::::::::::::: YOUR QUOTE :::::::::::::::\n')
    price_currency = 'Price per ' + currency + ' (in CAD) = ${:0.2f}'. format(cad_price_after_fee)
    print(price_currency)
    total_currency = float(amount) / float(cad_price_after_fee)
    you_receive = 'You receive {:0.5f} '.format(total_currency) + currency + ' for ${}'.format(amount)
    print(you_receive)
    print('\n::::::::::::::: YOUR QUOTE :::::::::::::::\n')

    # ask to repeat
    print('Get new quote? yes/no')
    answer = input()
    if answer == 'no':
        exit()
