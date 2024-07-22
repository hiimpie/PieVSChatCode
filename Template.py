from Twitch import cmd, Bot
from Xbox import *
bot = Bot()

# ============================
# TEMPLATE - Refer to ReadME for Functions and button listings!!!
# ============================

@cmd(bot, "cmdname")
def act(msg):
  print(msg)

if __name__ == "__main__":
    bot.run()
