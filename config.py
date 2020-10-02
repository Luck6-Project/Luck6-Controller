token: str = ''
allow_user: list = ()
exclude: list = ('scripts', '__pycache__', 'scp-079-controller')
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
