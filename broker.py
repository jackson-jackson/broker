import requests
import sqlite3
import datetime

# create timestamp variable
date = datetime.datetime.now()
datestamp = str(date.strftime('%Y-%m-%d:%H.%M.%S'))


def database():
    conn = sqlite3.connect('broker.db')
    c = conn.cursor()

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS transactionDetails(datestamp, customer, currency, amount, fee, priceAfterFee, amountOfCrypto)')

    def data_entry():
        c.execute("INSERT INTO transactionDetails (datestamp, customer, currency, amount, fee, priceAfterFee, amountOfCrypto) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (datestamp, customer, currency, amount, fee, cad_price_after_fee, total_currency))
        conn.commit()

    create_table()
    data_entry()
    c.close()
    conn.close()


while True:
    # gather details of details of transaction
    print('\nWho is the buyer?')
    customer = input()

    print('\nAre they buying ETH or BTC?')
    currency = input()

    # get live market data from coinmarketcap.com
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
    print('\nHow much would they like to buy?')
    amount = input()
    print("\nWhat's your fee? (Integers only (i.e., 2, 5, 10))")
    raw_fee = input()
    fee = float(raw_fee) / 100 + 1

    # calculate CAD price after fee
    cad_price_after_fee = float(json_price_cad) * float(fee)

    # print quote
    print('\n::::::::::::::: YOUR QUOTE :::::::::::::::\n')
    price_currency = 'Price per ' + currency + ' (in CAD) = ${:0.2f}'. format(cad_price_after_fee)
    print(price_currency)
    total_currency = float(amount) / float(cad_price_after_fee)
    you_receive = 'You receive {:0.5f} '.format(
        total_currency) + currency + ' for ${}'.format(amount)
    print(you_receive)
    print('\n::::::::::::::: YOUR QUOTE :::::::::::::::\n')

    print('Save transaction details to database? y/n')
    save_to_db = input()
    if save_to_db == 'y':
        database()

    # ask to repeat
    print('\nGet new quote? y/n')
    answer = input()
    if answer == 'n':
        exit()
