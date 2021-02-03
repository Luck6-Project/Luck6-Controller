token: str = ''
allow_user: list = []
exclude: list = ['scripts', '__pycache__', 'scp-079-controller']
menu: list = [
    ['启动', 'start'],
    ['重启', 'restart'],
    ['停止', 'stop'],
    ['更新', 'update'],
    ['状态', 'status'],
    ['日志', 'log'],
    ['清空日志', 'clear'],
    ['全部状态', 'check'],
    ['全部更新', 'upgrade'],
    ['全部重启', 'refresh'],
    ['全部备份', 'backup'],
]
cmd_list_1: list = [
    'boot',
    'reboot',
    'stop',
    'update',
    'status',
    'log'
]
cmd_list_2: list = [
    'clog',
    'status-all',
    'update-all',
    'reboot-all',
    'backup-all'
]
cmd_mapping: dict = {
    'boot': 'start',
    'reboot': 'restart',
    'stop': 'stop',
    'update': 'update',
    'status': 'status',
    'log': 'log',
    'clog': 'clear',
    'status-all': 'check',
    'update-all': 'upgrade',
    'reboot-all': 'refresh',
    'backup-all': 'backup'
}
