from telethon import TelegramClient
import asyncio
import random
import os

# Use your own values from my.telegram.org
api_id = ''  # Replace with your actual API ID
api_hash = ''  # Replace with your actual API Hash
phone = ''  # Your phone number with country code

anita_user_id = 6393952158
vai_user_id = 6149401357

# Create a client instance

message = [
    {'task_no': 1, 'link': 'https://www.instagram.com/p/C_2u4CyAecd/?igsh=NXN6ajM1d3JkbWpy'},
    {'task_no': 2, 'link': 'https://www.instagram.com/reel/C_KlcmfJFNT/?igsh=d3lzZzg1cnF4MDZo'},
    {'task_no': 3, 'link': 'https://www.instagram.com/reel/C_KlcmfJFNT/?igsh=d3lzZzg1cnF4MDZo'}
]

async def submit_task_to_scammer(client,user_id, message):
    # Connect to the client
    await client.start( phone=phone )
    # Get a list of all image files in the 'images' directory
    image_files = [f for f in os.listdir('images') if f.endswith('.jpg')]
    
    try:
        for msg in message:
            # Choose a random image file
            random_image = random.choice(image_files)
            # Remove the chosen image from the list to avoid repetition
            image_files.remove(random_image)
            
            # Send the file with the caption
            await client.send_file(user_id, f'images/{random_image}', caption=f"Task {msg.task_no}")
            await asyncio.sleep(2)
            
            print(f"Message sent successfully to user_id {user_id}")
            
            # If we've used all images, refill the list
            if not image_files:
                image_files = [f for f in os.listdir('images') if f.endswith('.jpg')]
    except Exception as e:
        print(f"Failed to send message: {e}")
    
    # Disconnect after sending the message
    await client.disconnect()

if __name__ == "__main__":
    client = TelegramClient('session_name', api_id, api_hash);
    asyncio.run(submit_task_to_scammer( client,vai_user_id, message))