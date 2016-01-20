import time
import json
import wikipedia
import pyowm
from slackclient import SlackClient

owm = pyowm.OWM('')# replace with your OWM key
token = '' # replace with your slack token

sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("auth.test")

print sc.api_call("chat.postMessage",
                  username='4970WBot',
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
                        try:
                            sc.api_call("chat.postMessage",
                                        username='WikiBot',
                                        as_user='false',
                                        icon_emoji=':bowtie:',
                                        channel=evt["channel"],
                                        text=wikipedia.summary(message[7:]).encode('utf-8'))
                        except:
                            sc.api_call("chat.postMessage",
                                        username='WikiBot',
                                        as_user='false',
                                        icon_emoji=':bowtie:',
                                        channel=evt["channel"],
                                        text="Hmm, I couldn't find that, try another term...")
                    if "weatherBot" in message [:11]:
                    #print owm.daily_forecast("Minneapolis,us")
                        sc.api_call("chat.postMessage",
                                    username='WeatherBot',
                                    as_user='false',
                                    icon_emoji=':cloud:',
                                    channel=evt["channel"],
                                    text= "the current temperature is: " + str(owm.weather_at_place('Minneapolis,us').get_weather().get_temperature('fahrenheit')['temp']) + "F")
