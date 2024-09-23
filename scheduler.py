import schedule
from datetime import datetime
import pytz
import asyncio
from get_task_from_scammer import get_task_from_scammer
from  submit_task_to_scammer import submit_task_to_scammer
from is_she_asking_qr import is_she_asking_qr
from send_qr_to_scammer import send_qr_to_scammer
from telethon import TelegramClient


anita_scammer_id = 6393952158;
scammer_id = anita_scammer_id;
api_id = '';
api_hash = '' ; 
phone = '' ; 
client = TelegramClient('session_1', api_id, api_hash);
nepal_tz = pytz.timezone('Asia/Kathmandu');



async def health_check(client):
    await client.start( phone=phone )
    print("health check")
    await client.send_message(anita_scammer_id, " service is working")

def healthCheck_async():
    client = TelegramClient('session_1', api_id, api_hash);
    asyncio.run(health_check( client))


# Async function to wrap your task
async def scheduled_task(task_list):
    print("reverse scam started")
    data = await get_task_from_scammer( client,task_list)
    data.reverse()
    print(data)
    if len(data)<2:
        exit()
    await submit_task_to_scammer( client,scammer_id, data)
    print(" anita will ask to enter qr with in 10 min")
    # sleep for 10 min
    await asyncio.sleep(600)
    print("checking id she is asking for qr")
    is_she_asking = await is_she_asking_qr(client,scammer_id)
    if not is_she_asking:
        exit();
    print("sending qr ...")
    await send_qr_to_scammer( client, scammer_id)

# Wrapper function to schedule async task in schedule
def run_async_task_1():
    asyncio.run(scheduled_task([1, 2, 3]))
def run_async_task_2():
    asyncio.run(scheduled_task([7, 8, 9]))
def run_async_task_3():
    asyncio.run(scheduled_task([13, 14, 15]))
def run_async_task_4():
    asyncio.run(scheduled_task([19,20,21]))

# Schedule the job at a specific Nepali time



schedule.every().day.at("09:45").do(healthCheck_async)
schedule.every().day.at("10:10").do(run_async_task_1)
schedule.every().day.at("12:35").do(run_async_task_2)
schedule.every().day.at("15:30").do(run_async_task_3)
schedule.every().day.at("18:08").do(run_async_task_4)
schedule.every().day.at("21:10").do(healthCheck_async)


if __name__ == "__main__":

    run_async_task_1()

# while True:
#     # Get the current time in Nepal (optional, just for monitoring)
#     now = datetime.now(nepal_tz)
#     # Run pending jobs
#     schedule.run_pending()

