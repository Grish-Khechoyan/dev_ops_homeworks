from telegram import Bot

TOKEN = Bot info: {'id': 123456789, 'is_bot': True, 'first_name': 'YourBotName', 'username': 'YourBotUsername'}  # replace with new token

bot = Bot(token=TOKEN)
print("Bot info:", bot.get_me())