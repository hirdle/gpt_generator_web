import requests
import time
from multiprocessing import Process
from datetime import datetime
import config

import telebot
bot = telebot.TeleBot(config.API_TOKEN_TELEGRAM, parse_mode="html")

default_domain = 'http://gpt-generator.na4u.ru/api/channels/'

poster_processes = []


def get_chatgpt_data(prompt):

    error = ""

    try:
        url = "https://api.openai.com/v1/chat/completions"

        prompt = [{"role": "user", "content": prompt}]

        data = {
            "model": "gpt-3.5-turbo",
            "messages": prompt,
            "max_tokens": 1000,
            "temperature": 0,
        }

        headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+config.API_TOKEN_OPENAI}
        r = requests.post(url, headers=headers, json=data)

        error = r.text.strip()

        return r.json()['choices'][-1]['message']['content'].strip()

    except Exception as e:
        print(error)
        return f"Возникли некоторые трудности."

def write_post(channel):

    while True:
        publish_time = channel['publish_interval'].split('\n')
        themes_list = channel['themes'].split('\n')
        template = channel['template']

        print(datetime.now().strftime("%H:%M"))
        
        if datetime.now().strftime("%H:%M") in publish_time:

            try:

                


                now_theme = themes_list[0]

                print(now_theme)
                
                # if now_theme.strip() != "":

                text_post = get_chatgpt_data(template.replace("*Theme*", now_theme))

                print(text_post)

                bot.send_message(channel['telegram_id'], text_post)

                themes_list.pop(0)
                channel['themes'] = "\n".join(themes_list).strip()
                requests.put(f'{default_domain}{channel["id"]}/update/', data=channel)

                time.sleep(60)

            except:
                pass



def start_channel(channel):
    t = Process(target=write_post, args=[channel])
    t.start()
    return t

def start_poster_channels(channels):
    for i in channels:
        t = start_channel(i)
        poster_processes.append(t)

def stop_poster_channels():
    global poster_processes

    for i in poster_processes:
        i.terminate()
        i.join()
    
    poster_processes = []


def get_channels():
    return requests.get(default_domain).json()

def watch_api():
    last_channels = None
    channels = None
    
    while True:
        channels = get_channels()
        # print(channels)
        if channels != last_channels:
            stop_poster_channels()
            start_poster_channels(channels)
            print("OK")
        last_channels = channels
        time.sleep(3)
print("OK")
start_poster_channels(get_channels())
watch_api()