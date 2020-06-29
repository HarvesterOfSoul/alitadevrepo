import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
      "You can be the first person to step on the sun. Have a try.",
      "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
      "Try to spend one day in a coffin and it will be yours forever.",
      "You should try hot bath in a volcano.",
      "An active volcano is the best swimming pool for you.",
      "You should try playing snake and ladders, with real snakes and no ladders.",
      "Launch yourself into outer space while forgetting oxygen on Earth.",
      "I heard phosgene is poisonous but I guess you won't mind inhaling it for fun.",
      "Try playing catch and throw with nitroglycerin. It's fun",
      "You can stay underwater for the rest of your life without coming back up.",
      "How about you stop breathing for like 1 day?",
      "Try provoking a tiger while you both are in a cage.",
      "God was searching for you. You should leave to meet him.",
      "Go give your 100%! Now, go donate blood.",
      "Try jumping from a hundred story building, but you can do it only once.",
      "You should donate your brain seeing that you never used it.",
      "Volunteer for target in an firing range.",
      " Head shots are fun. Get yourself one !!",
      "You should try swimming with great white sharks.",
      "You should paint yourself red and run in a bull marathon.",

  )

@run_async
def kill(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /kill  😩
"""

__mod_name__ = "Killing Commands"

KILL_HANDLER = DisableAbleCommandHandler("kill", kill)

dispatcher.add_handler(KILL_HANDLER)
