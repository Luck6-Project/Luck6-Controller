import telepot
import config
import os
import time
import utils
from threading import Thread
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

os.chdir('..')

cmd_using = False
set_time = time.time()
limit_command = ('backup', 'upgrade', 'refresh')

def set_using():
    global cmd_using, set_time
    cmd_using = True
    set_time = time.time()

def auto_timeout():
    global cmd_using, set_time
    while True:
        if cmd_using and time.time() - set_time >= 600:
            cmd_using = False
        time.sleep(1)

def combined_command(operation: str, parameter: str):
    return os.getcwd() + '/scripts/' + operation + '.sh ' + parameter

def run_cmd(cmd: str, success: str, chat_id: int):
    global cmd_using
    cmd_return = os.popen(cmd).read()
    if utils.isRealNone(cmd_return):
        bot.sendMessage(chat_id, success)
    else:
        text_length = len(cmd_return)
        loop_cnt = 0
        while text_length >= 4096:
            msg = ''.join(list(cmd_return)[loop_cnt * 4096:(loop_cnt + 1) * 4096])
            loop_cnt += 1
            text_length -= 4096
            bot.sendMessage(chat_id, msg)
        if text_length != 0:
            msg = ''.join(list(cmd_return)[loop_cnt * 4096:len(cmd_return)])
            bot.sendMessage(chat_id, msg)
    cmd = cmd.split()[0]
    cmd = ''.join(list(cmd)[len(os.getcwd()) + 9:len(cmd) - 3])
    if cmd in limit_command:
        print('Set Using False')
        cmd_using = False

def get_dirs():
    files = os.listdir(os.getcwd())
    dirs = []
    for f in files:
        if os.path.isdir(f) and f not in config.exclude:
            dirs.append([f, f])
    return dirs

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if chat_id not in config.allow_user:
        utils.notAllowed(bot, chat_id)
        return None
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, '请选择操作', reply_markup=utils.getInlineKeyboard(config.menu, 3))

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(query_id, from_id, query_data)
    if from_id not in config.allow_user:
        utils.notAllowed(bot, from_id)
        return None
    dirs = get_dirs()
    if query_data == 'start':
        dirs = utils.addPrefix(dirs, 'start', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要启动的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'restart':
        dirs = utils.addPrefix(dirs, 'restart', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要重启的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'stop':
        dirs = utils.addPrefix(dirs, 'stop', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要停止的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'update':
        dirs = utils.addPrefix(dirs, 'update', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要更新的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'status':
        dirs = utils.addPrefix(dirs, 'status', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要查看状态的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'log':
        dirs = utils.addPrefix(dirs, 'log', ':')
        print(dirs)
        bot.sendMessage(from_id, '请选择要查看日志的 Bot', reply_markup=utils.getInlineKeyboard(dirs, 2))
    elif query_data == 'clear':
        Thread(target=run_cmd, args=(combined_command('clear', ''), '成功', from_id)).start()
    elif query_data == 'check':
        Thread(target=run_cmd, args=(combined_command('check', ''), '成功', from_id)).start()
    elif query_data == 'upgrade':
        if not cmd_using:
            set_using()
            Thread(target=run_cmd, args=(combined_command('upgrade', ''), '成功', from_id)).start()
        else:
            bot.sendMessage(from_id, '其他人正在使用')
    elif query_data == 'refresh':
        if not cmd_using:
            set_using()
            Thread(target=run_cmd, args=(combined_command('refresh', ''), '成功', from_id)).start()
        else:
            bot.sendMessage(from_id, '其他人正在使用')
    elif query_data == 'backup':
        if not cmd_using:
            set_using()
            Thread(target=run_cmd, args=(combined_command('backup', ''), '成功', from_id)).start()
        else:
            bot.sendMessage(from_id, '其他人正在使用')
    else:
        str_split = str(query_data).split(':')
        if len(str_split) == 2:
            if str_split[0] == 'start':
                Thread(target=run_cmd, args=(combined_command(str_split[0], str_split[1]), '成功', from_id)).start()
            elif str_split[0] == 'restart':
                Thread(target=run_cmd, args=(combined_command(str_split[0], str_split[1]), '成功', from_id)).start()
            elif str_split[0] == 'stop':
                Thread(target=run_cmd, args=(combined_command(str_split[0], str_split[1]), '成功', from_id)).start()
            elif str_split[0] == 'update':
                Thread(target=run_cmd, args=(combined_command(str_split[0], str_split[1]), '成功', from_id)).start()
            elif str_split[0] == 'status':
                Thread(target=run_cmd, args=(combined_command(str_split[0], str_split[1]), '成功', from_id)).start()
            elif str_split[0] == 'log':
                text = ''
                path = str_split[1] + '/log'
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        lines = f.readlines()
                        for i in range(len(lines)):
                            text += lines[i]
                            if (i + 1) % 40 == 0:
                                bot.sendMessage(from_id, text)
                                text = ''
                        if text != '':
                            bot.sendMessage(from_id, text)
                else:
                    bot.sendMessage(from_id, 'Log 文件不存在')

bot = telepot.Bot(config.token)
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

Thread(target=auto_timeout).start()

while True:
    time.sleep(1)
