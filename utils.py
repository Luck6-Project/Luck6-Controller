import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def getInlineKeyboard(buttons, wrap):
    keyboard = []
    row = []
    length = len(buttons)
    for i in range(length):
        row.append(InlineKeyboardButton(text=buttons[i][0], callback_data=buttons[i][1]))
        if (i + 1) % wrap == 0:
            keyboard.append(row.copy())
            row.clear()
    if len(row) != 0:
        keyboard.append(row.copy())
        row.clear()
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def addPrefix(array, prefix, sep):
    return [[array[i][0], prefix + sep + array[i][1]] for i in range(len(array))]

def notAllowed(bot: telepot.Bot, user_id: int):
    pass
    # bot.sendMessage(user_id, '*您无权使用此 Bot*', parse_mode='markdown')

def isRealNone(string: str):
    if len(string.split()) == 0:
        return True
    return False
