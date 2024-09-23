from telethon import TelegramClient
import asyncio

# Use your own values from my.telegram.org
api_id = ''  # Replace with your actual API ID
api_hash = ''  # Replace with your actual API Hash
phone = '+'  # Your phone number with country code
anita_user_id = 6393952158
# Create a client instance
client = TelegramClient('session_1', api_id, api_hash)

async def send_qr_to_scammer(client: TelegramClient, user_id):
    try:
        await client.start( phone=phone ) 
        await client.send_file(user_id,f'images/qr.jpg', caption="")
        print(f"Message sent successfully to user_id {user_id}")
    except Exception as e:
        print(f"Failed to send message: {e}")
    # Disconnect after sending the message
    await client.disconnect()
if __name__ == "__main__":
    asyncio.run(send_qr_to_scammer(client,6393952158))