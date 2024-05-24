import json
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import logging

# Your API ID and hash
api_id = "API_ID"
api_hash = 'API_HASH'
phone_number = '+251'  # Your phone number with country code

# Channel username or ID
channel_username = 'tikvahethiopia'

# Keywords for bank ads
bank_ad_keywords = ["Bank_of_Abyssinia", "Abyssinia_Bank", "አቢሲንያ ባንክ", "ግሎባል ባንክ", "ግሎባል_ባንክ", "GlobalBank", "CBE", "አማራ_ባንክ", "Amhara Bank", "ብርሃን_ባንክ", "BerhanBank"]

# Enable logging
logging.basicConfig(level=logging.INFO)

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    logging.info("Client successfully authorized")

    # Get the channel entity
    try:
        channel = await client.get_entity(channel_username)
        logging.info(f"Channel entity fetched: {channel.title}")
    except Exception as e:
        logging.error(f"Failed to get channel entity: {e}")
        return

    offset_id = 0
    limit = 100
    all_messages = []

    while True:
        try:
            history = await client(GetHistoryRequest(
                peer=PeerChannel(channel.id),
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))

            if not history.messages:
                break

            for message in history.messages:
                if any(keyword.lower() in (message.message or "").lower() for keyword in bank_ad_keywords):
                    message_data = {
                        "Date": message.date.strftime('%Y-%m-%d'),
                        "Post link": f"https://t.me/{channel_username}/{message.id}",
                        "View": message.views if message.views is not None else 0,
                        "Post Hour": message.date.strftime('%H:%M'),
                        "Bank": next((keyword for keyword in bank_ad_keywords if keyword.lower() in (message.message or "").lower()), "Unknown"),
                        "Time of day": "AM" if message.date.hour < 12 else "PM"
                    }
                    all_messages.append(message_data)
            
            offset_id = history.messages[-1].id

        except Exception as e:
            logging.error(f"Error fetching messages: {e}")
            break

    logging.info(f"Fetched {len(all_messages)} messages containing the keywords")

    # Save to JSON
    with open('bank_ads.json', 'w', encoding='utf-8') as f:
        json.dump(all_messages, f, ensure_ascii=False, indent=4)

# Run the client
with client:
    client.loop.run_until_complete(main())
