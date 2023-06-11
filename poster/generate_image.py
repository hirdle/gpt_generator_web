from telethon import TelegramClient, events
from PIL import Image
import time
import os

overlay = Image.open("overlay.png")
overlay = overlay.resize((768, 768))

api_id = 26766111
api_hash = "fc3e1cc249f4986fc9f616805a7320e0"
bot_name = "kandinsky21_bot"

client = TelegramClient("my_account", api_id, api_hash)


current_name = ""

async def send_prompt(prompt):
    await client.send_message(bot_name, "Генерация по тексту")
    time.sleep(1)
    await client.send_message(bot_name, prompt)
    time.sleep(1)
    await client.send_message(bot_name, "без стиля")
    time.sleep(1)


async def imagine(prompt, overlay):

    # while True:
    #     if "Добавил в очередь на генерацию изображения." not in client.iter_messages(bot_name)[-1].text:
    #         break
    #     time.sleep(5)

            
    
    await send_prompt(prompt)

    @client.on(events.NewMessage(chats=bot_name))
    async def my_handler(event):
        if "Результат генерации по запросу " in str(event.message.message):
            path = await event.download_media(file="images/")
            
            

            img = Image.open(path)
            os.remove(path)
            new_img = Image.new("RGBA", (768, 768), (255, 255, 255, 0))
            new_img.paste(img, (0, 0))

            nonlocal overlay
            
            if overlay:
                overlay = Image.open(overlay)
                overlay = overlay.resize((768, 768))
                new_img.alpha_composite(overlay)

            new_img.save(f"images/{prompt}.png")


            client.disconnect()

    await client.run_until_disconnected()






def generate_image(prompt, overlay):
    with client:
        client.loop.run_until_complete(imagine(prompt, overlay))

