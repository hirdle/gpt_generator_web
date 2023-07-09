import requests
import time
from multiprocessing import Process
from datetime import datetime
import config
import pytz

from generate_image import generate_image

import asyncio, os


import telebot
bot = telebot.TeleBot(config.API_TOKEN_TELEGRAM, parse_mode="html")

domain = 'http://127.0.0.1:8000'
# domain = 'https://gpt-tool.ru'

default_domain = f'{domain}/api/channels/'
default_domain_img = f'{domain}/api/images/'

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


def send_wordpress_post(site, title, text):

    url = f'{site}/create_post.php'
    requests.post(url, data={"title": title, "content": text})

    print("Success Wordpress")
    

def send_vk_post(group_id, message):

    url = f'https://api.vk.com/method/wall.post'

    params = {
        'owner_id': group_id,
        'access_token': config.API_TOKEN_VK,
        'message': message,
        'v': '5.131'
    }

    response = requests.post(url, params=params)
    data = response.json()

    if 'error' in data:
        print('Error VK')
    else:
        print(f'Success VK')



def write_post(channel):

    while True:
        publish_time = [i.strip() for i in channel['publish_interval'].split('\n')]
        themes_list = channel['themes'].split('\n')
        template = channel['template']
        overlay = channel['overlay']
        overlay_path = None

        if overlay:
            overlay_path = f'overlays/overlay_{channel["id"]}.jpg'
            overlay_data = requests.get(overlay).content
            with open(overlay_path, 'wb') as handler:
                handler.write(overlay_data)

        if datetime.now(pytz.timezone('Europe/Moscow')).strftime("%H:%M") in publish_time:

            try:
                print("Publishing")

                images = requests.get(default_domain_img).json()

                now_theme = themes_list[0].strip()
                text_post = get_chatgpt_data(template.replace("*Theme*", now_theme))

                images_post = list(filter(lambda x: x['theme']==now_theme and x['channel']==channel["id"], images))
                images_urls = [x['upload'] for x in images_post]
                
                if len(images_urls) > 0:
                    m = bot.send_photo(channel['telegram_id'], images_urls[0])
                else:
                    
                    generate_image(now_theme, overlay_path)
                    
                    m = bot.send_photo(channel['telegram_id'], open(f'images/{now_theme}.png', 'rb'))
                    os.remove(f'images/{now_theme}.png')

                bot.reply_to(m, text_post)

                print('Success Telegram')

                send_wordpress_post(channel['site_link'], now_theme, text_post)
                send_vk_post(channel['vk_id'], text_post)


                themes_list.pop(0)
                
                j={"themes": "\n".join(themes_list).strip()}
                requests.put(f'{default_domain}{channel["id"]}/update/', data=j)

                for i in images_post:
                    requests.delete(f'{default_domain_img}{i["id"]}/delete/')

                time.sleep(60)

            except Exception as e:
                print(e)
                



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
        if channels != last_channels:
            stop_poster_channels()
            time.sleep(60)
            start_poster_channels(channels)
        last_channels = channels

        time.sleep(1800)

if __name__ == "__main__":
    watch_api()
    # generate_image("Привет", "")......