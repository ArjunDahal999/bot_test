from telethon import TelegramClient
import asyncio

# Use your own values from my.telegram.org
api_id = ''  # Replace with your actual API ID
api_hash = ''  # Replace with your actual API Hash
phone = '+'  # Your phone number with country code
payment_msg ='Please provide the QR code of e-sewa wallet to facilitate the financial settlement of commission.'


async def is_she_asking_qr( client,user_id)->bool:
    # Connect to the client
    await client.start(phone=phone)
    try:
        # Fetch all messages between you and the specified user
        messages = await client.get_messages(user_id, limit=100)

        # Print each message
        for message in messages:
            if message.sender_id == user_id:
                if payment_msg in message.text:
                    return True
        await client.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    user_id = 6393952158 
    client = TelegramClient('session_1', api_id, api_hash)
    print(asyncio.run(is_she_asking_qr( client,6149401357)))
