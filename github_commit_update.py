import json, time, sys
from requests import get, post

token = str(sys.argv[1])
main = json.loads(get("https://api.github.com/repos/Luck6-Project/Luck6-Docs/commits/main").content)
text = "#update #docs #" + main['commit']['author']['name'].replace('_', '') + \
       ' \n\n🔨 [' + main['sha'][0:7] + '](https://github.com/Luck6-Project/Luck6-Docs/commit/' + \
       main['sha'] + '): ' + main['commit']['message']
push_content = {'chat_id': '-1001341765556', 'disable_web_page_preview': 'True' ,'parse_mode': 'markdown',
                'text': text}
url = 'https://api.telegram.org/bot' + token + '/sendMessage'
push_content['chat_id'] = '-1001341765556'
time.sleep(1)
try:
    main_req = get(url, data=push_content)
except:
    pass
print(main['sha'] + " ok！")
