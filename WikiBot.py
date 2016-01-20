import time
import json
import wikipedia
from slackclient import SlackClient

token = '' # replace with your slack token

sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("auth.test")

print sc.api_call("chat.postMessage",
            username='wikiBot',
            as_user='false',
            icon_emoji=':bowtie:',
            channel="C0JT331L0",
            text="Hello World!")

if sc.rtm_connect():
    while True:
        time.sleep(1);
        new_evts = sc.rtm_read()
        for evt in new_evts:
          print(evt)
          if "type" in evt:
            if evt["type"] == "message" and "text" in evt:
              message=evt["text"]
              if "wikiBot" in message[ :8]:
                  print message[7:]
                  print sc.api_call("chat.postMessage",
                              username='WikiBot',
                              as_user='false',
                              icon_emoji=':bowtie:',
                              channel=evt["channel"],
                              text=wikipedia.summary(message[7:]).encode('utf-8'))
