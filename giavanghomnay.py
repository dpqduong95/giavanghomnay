import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from telegram import Bot

# Define a function to fetch the gold prices
def get_gold_prices():
    url = 'https://hoikimhoancamau.com/index/banggiavangcamau'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', {'class': 'table_gia'})
    rows = table.find_all('tr')
    gold_prices = ''
    for row in rows[1:]:
        cols = row.find_all('td')
        print(cols)
        name = row.find('th').get_text()+' '+cols[0].get_text()
        buy_price = cols[1].get_text()
        sell_price = cols[2].get_text()
        gold_prices += f'{name}: {buy_price} / {sell_price}\n'
    gold_prices += f'Nguồn: https://hoikimhoancamau.com'
    return gold_prices

# Define a handler function that will be called when a user sends a message to the bot
def gold_prices_handler(update, context):
    gold_prices = get_gold_prices()
    #Bot.send_message(chat_id='-497019034', text=gold_prices)
    bot = Bot(token='6095286729:AAF-67TOLJ45SfTx-tUi7ce5xBCmNBvMWhI')
    bot.sendMessage(chat_id='-497019034', text=gold_prices)


# Create a bot and register the handler function
updater = Updater(token='6095286729:AAF-67TOLJ45SfTx-tUi7ce5xBCmNBvMWhI')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('gold', gold_prices_handler))

# Start the bot
updater.start_polling()

# print(get_gold_prices())