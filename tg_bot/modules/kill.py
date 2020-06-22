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
      "ഡേവീസേട്ട, കിങ്ഫിഷറിണ്ടാ... ചിൽഡ്...! .",
      "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....😬",
      "ഇത് ഞങ്ങളുടെ പണിസാധനങ്ങളാ രാജാവേ.🔨⛏",
      "കളിക്കല്ലേ കളിച്ചാൽ ഞാൻ തീറ്റിക്കുമെ പുളിമാങ്ങ....😎",
      "മ്മക്ക് ഓരോ ബിയറാ കാച്ചിയാലോ...🥂",
      "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി...😩",
      "കള്ളടിക്കുന്നവനല്ലേ കരിമീനിന്റെ സ്വാദറിയു.....😋",
      "ഡാ വിജയാ നമുക്കെന്താ ഈ ബുദ്ധി നേരത്തെ തോന്നാതിരുന്നത്...!🙄",
      "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!🥰",
      "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....⛪",
      "എനിക്കറിയാം ഇവന്റെ അച്ഛന്റെ പേര് ഭവാനിയമ്മ എന്നാ....😂🤣🤣",
      "ഡാ ദാസാ... ഏതാ ഈ അലവലാതി.....😒",
      "ഉപ്പുമാവിന്റെ ഇംഗ്ലീഷ് സാൾട് മംഗോ ട്രീ.....🤔",
      "മക്കളെ.. രാജസ്ഥാൻ മരുഭൂമിയിലേക്ക് മണല് കയറ്റിവിടാൻ നോക്കല്ലേ.....🥵",
      "നിന്റെ അച്ഛനാടാ പോൾ ബാർബർ....🤒",
      "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി.....🥵",
      "ഇത് കണ്ണോ അതോ കാന്തമോ...👀",
      "നാലാമത്തെ പെഗ്ഗിൽ ഐസ്‌ക്യൂബ്സ് വീഴുന്നതിനു മുൻപ് ഞാൻ അവിടെ എത്തും.....😉",
      "അവളെ ഓർത്ത് കുടിച്ച കല്ലും നനഞ്ഞ മഴയും വേസ്റ്റ്....💔",
      "എന്നോട് പറ ഐ ലവ് യൂ ന്ന്....😘",
      "അല്ല ഇതാര് വാര്യംപിള്ളിയിലെ മീനാക്ഷി അല്ലയോ... എന്താ മോളെ സ്കൂട്ടറില്....🙈 ",
      "കിട്ടിയ  പെണ്ണും  കാട്ടിയ  പെണ്ണും കൂടെ ഇല്ലേലും ജനിപ്പിച്ച പെണ്ണ് കാണും ആജീവനാന്തം 🤰🤱👩‍👦",
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
