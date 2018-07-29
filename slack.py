#!/usr/bin/env python
import requests
import sys

URL = 'https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #replace the X's with your actual webhook
UN = 'ZABBIX'
SLACK = ('#' + sys.argv[1])
SUBJECT = sys.argv[2]
MSG = sys.argv[3]

if SUBJECT == 'RECOVERY':
        EMOJI = ':heavy_check_mark:'
        COLOR = '#2de52d'
elif SUBJECT == 'OK':
        EMOJI = ':smile:'
        COLOR =  '#2de52d'
elif SUBJECT == 'PROBLEM':
        EMOJI = ':fire:'
        COLOR = '#ff0000'
else:
        EMOJI = ':ghost:'
        COLOR = '#ffee00'

data = { "channel": SLACK,
        "username": UN,
      "icon_emoji": EMOJI,
     "attachments": [{ "color": COLOR,
            "text": MSG }]
       }

x = requests.post(URL, json=data)
