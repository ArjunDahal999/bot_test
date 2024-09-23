import asyncio
import re
from telethon import TelegramClient
api_id = ''  
api_hash = ''
channel_id = 2325246987  #scammer channel id
target_sender_id = 6801360266  #scammer id
phone = '+' 
instagram_pattern = r"https?://www\.instagram\.com/[^\s]+"


def extartNumber(text):
    return int(re.search(r'\d+', text).group())


async def get_task_from_scammer( client : TelegramClient, task_no)->list:
    await client.start(phone=phone)
    task_with_links = []
    try:
        messages = await client.get_messages(channel_id, limit=600)
        for message in messages:
            if message.sender_id == target_sender_id:
                task_number_match = re.search(r'Task\s*(\d+)', message.text)  # Use message.text
                if task_number_match:
                    task_number = task_number_match.group(1)
                    links_found = re.findall(instagram_pattern, message.text)  # Use message.text
                    for link in links_found:
                        if extartNumber(task_number)   in task_no:
                            task_with_links.append({'task_no': extartNumber(task_number), 'link': link})
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.disconnect()

    return task_with_links 

if __name__ == "__main__":
    messages = asyncio.run( get_task_from_scammer([7,8,9]))
    print(messages)
   

