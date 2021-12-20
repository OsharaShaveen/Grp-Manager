from pyrogram import Cilent

bot = Cilent(
    "My Group Manager"
    api_id = 13565869,
    api_hash = "192a656e3e60fa7bacf96d9bfa910f47"
    bot_token = "5004465319:AAGhdY4T2hRHFuE64W-nVoBFg6pSHC5iMX8"
)

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Heya, I Am a Simple Grp Manager Bot.")

bot.run()