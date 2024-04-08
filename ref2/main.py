import random
import time
import os 
import re
import os
import sqlite3 

from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from gamescan import *


BOT_TOKEN = '6309139476:AAFARbEKS20Eucvfo2VDOv82A2SPNkrztJY'
API_ID = '27951803'
API_HASH = '2396eea2f8fcd76d1d857db1713aa0ef'

# Connect to SQLite database
conn = sqlite3.connect('rfrdb.db', check_same_thread=False)
cursor = conn.cursor()

# Create raffer table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS raffer (
                    username TEXT,
                    uid INTEGER,
                    referid INTEGER PRIMARY KEY,
                    rfrs TEXT
                )''')
conn.commit()

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


app.on_callback_query(filters.regex('^advpscan$'))(Advant_instance.advpscan_query)
app.on_callback_query(filters.regex('^L365scan$')) (L365_instance.scan_query)
app.on_callback_query(filters.regex('^bngscan$')) (BNG_instance.scan_query)
app.on_callback_query(filters.regex('^Mg888scan$')) (Meg_instance.scan_query)
app.on_callback_query(filters.regex('^gfgtscan'))(GFG_instance.scan_query)
app.on_callback_query(filters.regex('^L22scan'))(RELAXG_instance.scan_query)
app.on_callback_query(filters.regex('^jiliscan'))(Jili_instance.scan_query)
app.on_callback_query(filters.regex('^jdbscan'))(Jdb_instance.scan_query)
app.on_callback_query(filters.regex('^nxtspscan'))(Nxt_instance.scan_query)
app.on_callback_query(filters.regex('^hbnrscan'))(Hbn_instance.scan_query)
app.on_callback_query(filters.regex('^spdgmscan'))(Spd_instance.scan_query)
app.on_callback_query(filters.regex('^pltcscan'))(Pltc_instance.scan_query)
app.on_callback_query(filters.regex('^cq9scan'))(Cq9_instance.scan_query)
app.on_callback_query(filters.regex('^kagmscan'))(Kagm_instance.scan_query)
app.on_callback_query(filters.regex('^prgmpscan'))(Prgm_instance.scan_query)
app.on_callback_query(filters.regex('^kissscan'))(kiss_instance.scan_query)
app.on_callback_query(filters.regex('^lionscan'))(lion_instance.scan_query)
app.on_callback_query(filters.regex('^Livescan'))(Live_instance.scan_query)

###Detect of your video 
scangame="/root/ref2/video/Main.mp4"
     ###~~~~~~~~Seperate all of your video according to your Game name. For test i'm using the same video . These video are when user will click on the game button .
    
avantplay_vdo="/root/ref2/video/advantplay.mp4"
lucky365_vdo="/root/ref2/video/lky365.mp4"
BNG_vdo="/root/ref2/video/BNG.mp4"
MEGA_vdo="/root/ref2/video/MEGA888.mp4"
GFG_vdo="/root/ref2/video/GFG.mp4"
RELAX_vdo="/root/ref2/video/RELAX.mp4"
JILI_vdo="/root/ref2/video/JILI.mp4"
JDB_vdo="/root/ref2/video/JDB.mp4"
NEXTSPIN_vdo="/root/ref2/video/Nextspin.mp4"
HABANERO_vdo="/root/ref2/video/HABAN.mp4"
SPADEGAME_vdo="/root/ref2/video/spadegaming.mp4"
PLAYTECH_vdo="/root/ref2/video/playtech.mp4"
CQ9_vdo="/root/ref2/video/cq9.mp4"
KAGAMING_vdo="/root/ref2/video/ka.mp4"
PRAGMATIC_vdo="/root/ref2/video/ppslot.mp4"
kiss918_vdo="/root/ref2/video/918kiss.mp4"
lion_vdo="/root/ref2/video/lionking.mp4"
Live_vdo="/root/ref2/video/live22.mp4"


scan_button="/root/ref2/video/scanbtn.mp4"

 #These are the chat id of the groups or channel you will put in you button
chat_ids = ['-1002102896455', '-1001974309918']  

# How much he gain from each refer 
commission = 0.5 

message_ids = {}

#mention the photo path here >....<
new_start="/root/ref2/photo/TG Part 1 .jpg"
afterjoin_start="/root/ref2/photo/BANNER FREE5 EN.jpg"
affiliate_cmd="/root/ref2/photo/TG Part 3.jpg"




# Function to check if the user is a participant in all chats
async def is_participant(client, user_id):
    for chat_id in chat_ids:
        try:
            # Use the integer form of chat_id directly
            await client.get_chat_member(int(chat_id), user_id)
        except UserNotParticipant:
            return False
    return True

@app.on_message(filters.command(["start"]))
async def start_command(client, message):
    user_id = message.from_user.id
    await check_rfrlq(client, message)
    with open('all_users.txt', 'r') as f:
        users = f.read().splitlines()

    if str(user_id) not in users:  # Convert user_id to string for comparison
        with open('all_users.txt', 'a') as f:
            f.write(f"{user_id}\n")
        print(f"{user_id} Saved")
    else:
        print("User Alrady in database ")

    if await is_participant(client, user_id):
        await send_aflt_menu(client, message)
    else:
        await send_start_menu(client, message)



@app.on_message(filters.command(["broadcast"]))
async def broadcast_command(client, message):
    if not message.reply_to_message:
        await message.reply('Reply to a message to broadcast.')
        return

    s = 0
    with open('all_users.txt', 'r') as f:
        all_users = f.read().splitlines()

    for user_id in all_users:
        try:
            await client.forward_messages(
                chat_id=int(user_id),  # Forward to the user's chat
                from_chat_id=message.chat.id,  # Forward from the original chat
                message_ids=message.reply_to_message.id  # ID of the message to forward
            )
            s += 1
        except Exception as e:
            print(f"Error forwarding message to user {user_id}: {e}")

    await message.reply(f'Broadcasted to {s} users')

@app.on_message(filters.command(['^scan_Game$']))
async def scan_Game_command(client, message):
    user_id = message.from_user.id
    await check_rfrlq(client, message)
    with open('all_users.txt', 'r') as f:
        users = f.read().splitlines()

    if str(user_id) not in users:  # Convert user_id to string for comparison
        with open('all_users.txt', 'a') as f:
            f.write(f"{user_id}\n")
        print(f"{user_id} Saved")
    else:
        print("User Alrady in database ")

    if await is_participant(client, user_id):
        await send_game_menu(client, message)
    else:
        await send_start_menu(client, message)

# Function to handle callback query for refreshing start menu
@app.on_callback_query(filters.regex('^scan_Game$'))
async def refresh_start_menu(client, callback_query):
    user_id = callback_query.from_user.id
    
    # Extract the message ID from the callback query
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    await scanGm_query(client, callback_query)


    
@app.on_callback_query(filters.regex('^scanGm$'))
async def scanGm_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    scannow_text=f'''
🔘sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ

    Username: {user_mention}
 
🔘sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏsk atau web A.P.I Game & IP Address Anda
   
🔘 sɪʟᴀ ᴍᴇɴɢᴜɴɴᴀᴋᴀɴ sᴄᴀɴɴᴇʀ ᴅᴇɴɢᴀɴ ʜᴀɴᴅᴘʜᴏɴᴇ ᴅᴀɴ ʟɪɴᴇ ɪɴᴛᴇʀɴᴇᴛ ʏᴀɴɢ sᴀᴍᴀ ʙᴀɢɪ ᴍᴇɴɢᴇᴋᴀʟᴋᴀɴ ɪᴘ ᴀᴅᴅʀᴇss ᴀɴᴅᴀ ʙᴇʀʜᴜʙᴜɴɢ ᴅᴇɴɢᴀɴ ᴛᴇʟᴇᴛʜᴏɴ
   
🔘 sᴄᴀɴ sᴇʙᴀɴʏᴀᴋ 3 ᴀᴛᴀᴜ 5 ᴋᴀʟɪ! ᴘɪʟɪʜ ᴘᴇʀᴀᴛᴜsᴀɴ 70% ᴋᴇ ᴀᴛᴀs! sᴇɢᴀʟᴀ ᴘᴇʀᴛᴀʀᴜʜᴀɴ ᴀᴛᴀs ʀɪsɪᴋᴏ ᴀɴᴅᴀ sᴇɴᴅɪʀɪ

ℹ️ 𝐬ɪʟᴀ ᴘɪʟɪʜ ᴘɪʟɪʜᴀɴ 𝐬ᴄᴀɴɴᴇʀ ᴅᴇɴɢᴀɴ ᴛᴇᴋᴀɴ ʙᴜᴛᴛᴏɴ  ᴅɪʙᴀᴡᴀʜ! '''

    keyboard = [
        [
            InlineKeyboardButton("PRAGMATIC PLAY", callback_data="prgmp"),
            InlineKeyboardButton("LUCKY365", callback_data="L365")
        ],
        [
            InlineKeyboardButton("BNG", callback_data="bng"),
            InlineKeyboardButton("MEGA888 ", callback_data="Mg888")
        ],
        
        [
            InlineKeyboardButton("ADVANTPLAY", callback_data="Advplay"),
            InlineKeyboardButton("RELAXGAMING", callback_data="L22")
        ],
        
        [
            InlineKeyboardButton("JILI", callback_data="jili"),
            InlineKeyboardButton("JDB", callback_data="jdb")
        ],

        [
            InlineKeyboardButton("NEXTSPIN", callback_data="nxtsp"),
            InlineKeyboardButton("HABANERO", callback_data="hbnr")
        ],

        [
            InlineKeyboardButton("Spadegaming", callback_data="spdgm"),
            InlineKeyboardButton("Playtech", callback_data="pltc")
        ],

        [
            InlineKeyboardButton("CQ9", callback_data="cq9"),
            InlineKeyboardButton("KA Gaming", callback_data="kagm")
        ],

        [
            InlineKeyboardButton("GFG", callback_data="gfgt"),
            InlineKeyboardButton("918KISS", callback_data="918K")
        ],

        [
            InlineKeyboardButton("LION KING", callback_data="lionkg"),
            InlineKeyboardButton("Live22",callback_data="Le22")
        ],

        [
            InlineKeyboardButton("Go Back", callback_data="refresh_start")
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await client.send_video(chat_id=user_id,video=scangame,caption=scannow_text,reply_markup=reply_markup)
    except Exception as e:
        print(f"Start Scn Button error {e}")

# Function to handle callback query for refreshing start menu
@app.on_callback_query(filters.regex('^refresh_start$'))
async def refresh_start_menu(client, callback_query):
    user_id = callback_query.from_user.id
    
    # Extract the message ID from the callback query
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    # Check if the user is a participant
    if await is_participant(client, user_id):
        # Call the start command again
        await send_aflt_menu(client, callback_query)
    else:
        # If the user is not a participant, send the start menu
        await send_start_menu(client, callback_query)


                                #_____________________________1 B   
@app.on_callback_query(filters.regex('^Advplay$'))
async def Adv_query(client, callback_query):
    user_id = callback_query.from_user.id
    
    # Extract the message ID from the callback query
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ ADVANTPLAY sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗔𝗗𝗩𝗔𝗡𝗧𝗣𝗟𝗔𝗬 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="advpscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scan_Game"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=avantplay_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}") 
                                           #__________2 B 

                                           
@app.on_callback_query(filters.regex('^L365$'))
async def L365_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ LUCKY365 sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝐋𝐔𝐂𝐊𝐘𝟑𝟔𝟓 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="L365scan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=lucky365_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                                  #_________________ 3 B
@app.on_callback_query(filters.regex('^bng$'))
async def bng_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)

    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ BNG sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗕𝗡𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="bngscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=BNG_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
        
                                                    # _____________4 B

@app.on_callback_query(filters.regex('^Mg888$'))
async def Mg888_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ MEGA888 sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗠𝗘𝗚𝗔𝟴𝟴𝟴 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="Mg888scan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=MEGA_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                   # ________________5 B

@app.on_callback_query(filters.regex('^gfgt$'))
async def gfgt_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)   
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ GFG sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗚𝗙𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="gfgtscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=GFG_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
 
                                                #____________6 B   
@app.on_callback_query(filters.regex('^L22$'))
async def l22_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ RELAX sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗥𝗘𝗟𝗔𝗫 𝗚𝗔𝗠𝗜𝗡𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="L22scan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=RELAX_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                ## ________________7 B

@app.on_callback_query(filters.regex('^jili$'))
async def jili_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"

    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ JILI sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗝𝗜𝗟𝗜 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="jiliscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=JILI_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                  ##_________________ 8 B 

@app.on_callback_query(filters.regex('^jdb$'))
async def jdb_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"

    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ JDB sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗝𝗗𝗕 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="jdbscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=JDB_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                     #_______________________9B

@app.on_callback_query(filters.regex('^nxtsp$'))
async def nxtsp_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ NEXTSPIN sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗡𝗘𝗫𝗧𝗦𝗣𝗜𝗡 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="nxtspscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=NEXTSPIN_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                                       # ________________ 10 B 
@app.on_callback_query(filters.regex('^hbnr$'))
async def hbrnr_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"

    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ HABANERO sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗛𝗔𝗕𝗔𝗡𝗘𝗥𝗢 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="hbnrscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=HABANERO_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                # __________________________11 B
                                
@app.on_callback_query(filters.regex('^spdgm$'))
async def spdgm_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ Spadegaming sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗦𝗣𝗔𝗗𝗘𝗚𝗔𝗠𝗜𝗡𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="spdgmscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=SPADEGAME_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                # ____________________12 B

@app.on_callback_query(filters.regex('^pltc$'))
async def pltc_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ Playtech sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗣𝗟𝗔𝗬𝗧𝗘𝗖𝗛 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="pltcscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=PLAYTECH_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                                            # _________________ 13 B

@app.on_callback_query(filters.regex('^cq9$'))
async def cq9_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ CQ9 sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗖𝗤𝟵 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="cq9scan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=CQ9_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
                                        # _______________________14 B
                                        
@app.on_callback_query(filters.regex('^kagm$'))
async def kagm_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ KA Gaming sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗞𝗔 𝗚𝗔𝗠𝗜𝗡𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="kagmscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=KAGAMING_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")
        
                                    #  _______________________15 B

@app.on_callback_query(filters.regex('^prgmp$'))
async def prgmp_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ PRAGMATIC PLAY sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗣𝗥𝗔𝗚𝗠𝗔𝗧𝗜𝗖 𝗣𝗟𝗔𝗬 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="prgmpscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=PRAGMATIC_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

@app.on_callback_query(filters.regex('^918K$'))
async def kiss_query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ 𝟵𝟭𝟴𝗸𝗶𝘀𝘀 PLAY sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝟵𝟭𝟴𝗸𝗶𝘀𝘀 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="kissscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=kiss918_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                    #  _______________________16 B

@app.on_callback_query(filters.regex('^lionkg$'))
async def query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ 𝗟𝗜𝗢𝗡 𝗞𝗜𝗡𝗚 PLAY sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗟𝗜𝗢𝗡 𝗞𝗜𝗡𝗚 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="lionscan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=lion_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                    #  _______________________17 B                                    



@app.on_callback_query(filters.regex('^Le22$'))
async def query(client, callback_query):

    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
    message_id = callback_query.message.id
    
    # Delete the old start menu message
    await client.delete_messages(chat_id=user_id, message_ids=message_id)
    
    caption=f'''
Hi {user_mention} sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴋᴇ ᴍᴇɴᴜ ᴜᴛᴀᴍᴀ 𝗟𝗶𝘃𝗲𝟮𝟮 PLAY sᴄᴀɴɴᴇʀ

❗️sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ👍 {user_mention} sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏs atau web A.P.I 𝗟𝗶𝘃𝗲𝟮𝟮 & IP Address Anda

‼️ {user_mention} ᴅɪʟᴀʀᴀɴɢ sᴘᴀᴍ ʙᴏᴛ ʙᴀɢɪ ᴍᴇɴɢᴇʟᴀᴋᴋᴀɴ ɢᴀɴɢɢᴜᴀɴ sᴇʀᴠᴇʀ ᴋᴀᴍɪ 
◽️◽️◽️◽️
🔓{user_mention} ᴜɴᴛᴜᴋ sᴄᴀɴɴɪɴɢ pilih ʙᴜᴛᴛᴏɴ Scan🔥 ᴅɪ ʙᴀᴡᴀʜ'''

    keyboard = [
    
        [
            InlineKeyboardButton("SCAN NOW", callback_data="Livescan")
        ],
        [
            InlineKeyboardButton("Go Back", callback_data="scanGm"),
            InlineKeyboardButton("Go Home", callback_data="refresh_start")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    
    try:
        await client.send_video(chat_id=user_id,video=Live_vdo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Scan Button error {e}")

                                    #  _______________________18 B                                    
####  MAIN DEPENDESIS



# Function to check if the message contains a referral ID and update the database accordingly
async def check_rfrlq(client, message):
    user_id = message.from_user.id
    
    # Check if the message contains text
    if message.text:
        # Check if the message contains a referral ID
        match = re.search(r'/start (\d+)', message.text)
        if match:
            refer_id = int(match.group(1))
            if refer_id != user_id:
                cursor.execute('''SELECT referid, rfrs FROM raffer WHERE referid = ?''', (refer_id,))
                referrer_data = cursor.fetchone()
                if referrer_data:
                    refer_id, rfrs = referrer_data
                    rfrs_str = str(rfrs) if rfrs else ""
                    if str(user_id) not in rfrs_str.split(","):
                        if rfrs:
                            rfrs_str += f",{user_id}"
                        else:
                            rfrs_str = f"{user_id}"
                        cursor.execute('''UPDATE raffer SET rfrs = ? WHERE referid = ?''', (rfrs_str, refer_id))
                        conn.commit()
                        print(f"{user_id} Saved to rfrs of {refer_id}")
                        
                        # Get user information
                        new_user = message.from_user
                        new_user_info = f"Referred new user\nID: {new_user.id}\nUsername: {new_user.username}"
                        
                        # Send message to the refer_id
                        await client.send_message(refer_id, new_user_info)
                        
                    else:
                        print("Already referred someone")
                else:
                    print("Started normally")
            else:
                print("User cannot refer themselves")
        else:
            print("Invalid start command format")
    else:
        print("No text found in the message")


# Function to handle callback query for withdrawal
@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    if callback_query.data == 'withdraw':
        user_id = callback_query.from_user.id
        query_id = callback_query.id
        refer_count = await get_refer_count(user_id)

        total_earned = refer_count * commission
        if total_earned >= 30: ## Set your minimum limit .
            await client.send_message('@tokongadmin', f"User {user_id} wants to withdraw their Affiliate status.") 
            text = f"Please send your Affiliate status screenshot to @tokongadmin."

            await client.send_message(chat_id=user_id, text=text)
            
        else:
            # If the user's balance is too low, send a popup alert
            alert_message = f'''
            Your balance is too low to be able to withdraw. 
                  Minimum limit: RM30.
                  Your balance   : {total_earned}
            '''
            await callback_query.answer(alert_message, show_alert=True)

async def send_aflt_menu(client, message):
    user_mention = message.from_user.mention() if message.from_user else "Unknown User"
    
    if isinstance(message, Message):
        chat_id = message.chat.id
    else:
        chat_id = message.message.chat.id

    
    joined_text = f'''
Hi {user_mention} .

📌𝗕𝘂𝗮𝘁 𝗙𝗿𝗲𝗲 𝗖𝗿𝗲𝗱𝗶𝘁 𝗖𝗼𝗺𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝗦𝗶𝗹𝗮 𝗧𝗲𝗸𝗮𝗻👉 [ /affiliate ]

📌𝗡𝗮𝗸 𝗧𝗲𝗻𝗴𝗼𝗸 𝗣𝗲𝗺𝗮𝗶𝗻 𝗝𝘂𝗱𝗶 𝗢𝗻𝗹𝗶𝗻𝗲 𝗠𝗮𝗹𝗮𝘆𝘀𝗶𝗮 𝗠𝗮𝗶𝗻 𝗔𝗽𝗮 𝗨𝗻𝘁𝘂𝗸 𝗠𝗲𝗻𝗮𝗻𝗴 𝗗𝘂𝗶𝘁. 
👉LINK [ https://t.me/tokong_casino ]

📌𝗗𝗮𝗳𝘁𝗮𝗿 𝗔𝗸𝗮𝘂𝗻 𝗣𝗲𝗺𝗮𝗶𝗻, 𝗞𝗶𝘁𝗮 𝗦𝗮𝗺𝗮-𝗦𝗮𝗺𝗮 𝗕𝗼𝗹𝗲𝗵 𝗠𝗲𝗻𝗮𝗻𝗴 𝗗𝘂𝗶𝘁.💵
👉LINK [ https://bit.ly/3uGHbdE ]
  '''

    keyboard = [
        [InlineKeyboardButton("ᴅᴀꜰᴛᴀʀ ᴀᴋᴀᴜɴ ᴘᴇᴍᴀɪɴ ᴀᴏɴᴇ ꜱᴇɢᴇʀᴀ✅", url="https://bit.ly/3xocKK9")],
        [InlineKeyboardButton("🎰​ꜱᴄᴀɴɴᴇʀ ɢᴀᴍᴇᴛɪᴘꜱ🎰 ", callback_data="scanGm")],
        [InlineKeyboardButton("ᴛᴜᴛᴏʀɪᴀʟ ʀᴇɢɪꜱᴛᴇʀ/ᴅᴇᴘᴏꜱɪᴛ/ᴡɪᴛʜᴅʀᴀᴡ", url="https://t.me/Tutorialaone_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await client.send_photo(chat_id, photo=afterjoin_start, caption=joined_text, reply_markup=reply_markup)
    except Exception as e:
        print(f"Error sending start menu: {e}")


async def send_game_menu(client, message):
    user_mention = message.from_user.mention() if message.from_user else "Unknown User"
    
    if isinstance(message, Message):
        chat_id = message.chat.id
    else:
        chat_id = message.message.chat.id

    scannow_text=f'''
🔘sᴇɢᴀʟᴀ ʙᴇᴛᴛɪɴɢ ᴀᴛᴀs ʀɪsɪᴋᴏ sᴇɴᴅɪʀɪ

    Username: {user_mention}
 
🔘sᴄᴀɴɴᴇʀ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇʟɪʜᴀᴛ ᴋᴀᴅᴀʀ ᴘᴇʀᴀᴛᴜsᴀɴ ᴋᴇᴍᴇɴᴀɴɢᴀɴ sʟᴏᴛ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴋɪᴏsk atau web A.P.I Game & IP Address Anda
   
🔘 sɪʟᴀ ᴍᴇɴɢᴜɴɴᴀᴋᴀɴ sᴄᴀɴɴᴇʀ ᴅᴇɴɢᴀɴ ʜᴀɴᴅᴘʜᴏɴᴇ ᴅᴀɴ ʟɪɴᴇ ɪɴᴛᴇʀɴᴇᴛ ʏᴀɴɢ sᴀᴍᴀ ʙᴀɢɪ ᴍᴇɴɢᴇᴋᴀʟᴋᴀɴ ɪᴘ ᴀᴅᴅʀᴇss ᴀɴᴅᴀ ʙᴇʀʜᴜʙᴜɴɢ ᴅᴇɴɢᴀɴ ᴛᴇʟᴇᴛʜᴏɴ
   
🔘 sᴄᴀɴ sᴇʙᴀɴʏᴀᴋ 3 ᴀᴛᴀᴜ 5 ᴋᴀʟɪ! ᴘɪʟɪʜ ᴘᴇʀᴀᴛᴜsᴀɴ 70% ᴋᴇ ᴀᴛᴀs! sᴇɢᴀʟᴀ ᴘᴇʀᴛᴀʀᴜʜᴀɴ ᴀᴛᴀs ʀɪsɪᴋᴏ ᴀɴᴅᴀ sᴇɴᴅɪʀɪ

ℹ️ 𝐬ɪʟᴀ ᴘɪʟɪʜ ᴘɪʟɪʜᴀɴ 𝐬ᴄᴀɴɴᴇʀ ᴅᴇɴɢᴀɴ ᴛᴇᴋᴀɴ ʙᴜᴛᴛᴏɴ  ᴅɪʙᴀᴡᴀʜ! '''

    keyboard = [
        [
            InlineKeyboardButton("PRAGMATIC PLAY", callback_data="prgmp"),
            InlineKeyboardButton("LUCKY365", callback_data="L365")
        ],
        [
            InlineKeyboardButton("BNG", callback_data="bng"),
            InlineKeyboardButton("MEGA888 ", callback_data="Mg888")
        ],
        
        [
            InlineKeyboardButton("ADVANTPLAY", callback_data="Advplay"),
            InlineKeyboardButton("RELAXGAMING", callback_data="L22")
        ],
        
        [
            InlineKeyboardButton("JILI", callback_data="jili"),
            InlineKeyboardButton("JDB", callback_data="jdb")
        ],

        [
            InlineKeyboardButton("NEXTSPIN", callback_data="nxtsp"),
            InlineKeyboardButton("HABANERO", callback_data="hbnr")
        ],

        [
            InlineKeyboardButton("Spadegaming", callback_data="spdgm"),
            InlineKeyboardButton("Playtech", callback_data="pltc")
        ],

        [
            InlineKeyboardButton("CQ9", callback_data="cq9"),
            InlineKeyboardButton("KA Gaming", callback_data="kagm")
        ],

        [
            InlineKeyboardButton("GFG", callback_data="gfgt"),
            InlineKeyboardButton("918KISS", callback_data="918K")
        ],

        [
            InlineKeyboardButton("LION KING", callback_data="lionkg"),
            InlineKeyboardButton("Live22",callback_data="Le22")
        ],

        [
            InlineKeyboardButton("Go Back", callback_data="refresh_start")
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await client.send_video(chat_id,video=scangame,caption=scannow_text,reply_markup=reply_markup)
    except Exception as e:
        print(f"Start Scn Button error {e}")



# Function to get referral count for a user
async def get_refer_count(user_id):
    cursor.execute('''SELECT rfrs FROM raffer WHERE referid = ?''', (user_id,))
    rfrs_data = cursor.fetchone()
    if rfrs_data:
        rfrs = rfrs_data[0]
        if isinstance(rfrs, str):  # Check if rfrs is a string
            if "," in rfrs:
                # If there are multiple values separated by commas, count them
                return len(rfrs.split(","))
            else:
                # If there's only one value, return 1
                return 1
        else:
            # If rfrs is not a string (e.g., integer), return 0
            return 0
    else:
        # If no data found, return 0
        return 0
# Function to create referral link for a user
async def refer_link_create(client, message):
    chat_id = message.chat.id
    
    CO_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Withdraw", callback_data='withdraw')]
    ])

    # Get the user's ID and username
    user_id = message.from_user.id
    username = message.from_user.username
    user_mention = message.from_user.mention() if message.from_user else "Unknown User"
    
    # Check if the user's user_id already exists in the database
    cursor.execute('''SELECT referid FROM raffer WHERE referid = ?''', (user_id,))
    existing_referral = cursor.fetchone()
    
    if existing_referral:
        # If the user's user_id already exists in the database, retrieve the referral link from the database
        referral_link = f"https://t.me/{(await client.get_me()).username}?start={user_id}"
    else:
        # If the user's user_id does not exist in the database, insert a new row with the referral link
        referral_link = f"https://t.me/{(await client.get_me()).username}?start={user_id}"
        cursor.execute('''INSERT INTO raffer (username, referid) VALUES (?, ?)''', (username, user_id))
        conn.commit()
    
    # Get refer count for the user
    refer_count = await get_refer_count(user_id)
    
    total_earned = refer_count * commission
    
    referral_message = f'''
🎁𝗙𝗿𝗲𝗲 𝗖𝗿𝗲𝗱𝗶𝘁 𝗥𝗠𝟯𝟬 𝗧𝗮𝗻𝗽𝗮 𝗗𝗲𝗽𝗼𝘀𝗶𝘁🎁

👇𝗖𝗼𝗽𝘆 𝗱𝗮𝗻 𝘀𝗵𝗮𝗿𝗲 𝘆𝗼𝘂𝗿 𝗿𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗹𝗶𝗻𝗸👇 {referral_link}
👆👆👆👆👆👆👆
👇𝗦𝗵𝗮𝗿𝗲 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗟𝗶𝗻𝗸 𝗔𝗻𝗱 𝗞𝗲𝗲𝗽𝗮𝗱𝗮 𝗦𝗼𝗰𝗶𝗮𝗹 𝗠𝗲𝗱𝗶𝗮, 𝗔𝘁𝗮𝘂 𝗞𝗲𝗲𝗽𝗮𝗱𝗮 𝗥𝗮𝗸𝗮𝗻-𝗿𝗮𝗸𝗮𝗻 𝗦𝗲𝗸𝗶𝘁𝗮𝗿.
✔𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸
✔𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺
✔𝗪𝗲𝗰𝗵𝗮𝘁
✔𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽/𝗦𝗠𝗦
✔𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺
🤝𝗞𝗮𝘄𝗮𝗻𝗸𝗹𝗶𝗸 𝗔𝗻𝗱𝗮 𝗔𝗸𝗮𝗻𝗶 𝗠𝗲𝗻𝗱𝗮𝗽𝗮𝘁 𝗞𝗼𝗺𝗶𝘀𝗲𝗻 𝗦𝗲𝗯𝗮𝗻𝘆𝗮𝗸 𝗥𝗠𝟬.𝟱𝟬

Name: {user_mention}
ID: {user_id}
Refer Count: {refer_count}
Commission: RM{commission}
Total Earned: RM{total_earned}

⚠️𝗞𝗼𝗺𝗶𝘀𝗲𝗻 𝗠𝗲𝘀𝘁𝗶𝗺𝗲𝗻𝗰𝗮𝗽𝗮𝗶 𝗥𝗠𝟯𝟬 𝗨𝗻𝘁𝘂𝗸 𝗟𝗮𝘆𝗮𝗸 𝗗𝗶𝗸𝗹𝗮𝗶𝗺, 𝗗𝗮𝗻 𝗙𝗿𝗲𝗲 𝗖𝗿𝗲𝗱𝗶𝘁 𝗬𝗮𝗻𝗴 𝗗𝗶𝗸𝗿𝗲𝗱𝗶𝘁𝗸𝗮𝗻 𝗔𝗸𝗮𝗻 𝗗𝗶𝗽𝗶𝗻𝗱𝗮𝗵𝗸𝗮𝗻 𝗞𝗲𝗽𝗮𝗱𝗮 𝗔𝗸𝗮𝘂𝗻 𝗔𝗢𝗡𝗘 𝗣𝗲𝗿𝗺𝗮𝗶𝗻𝗮𝗻.

⚠️Type [ /affiliate ] Di Robot Sini Untuk Check Komision Anda.
    '''
    await client.send_photo(chat_id, photo=affiliate_cmd, caption=referral_message, reply_markup=CO_keyboard)
   
@app.on_message(filters.command("affiliate", prefixes="/"))
async def refer_command(client, message):
    user_id = message.from_user.id

    if await is_participant(client, user_id):
        await refer_link_create(client, message)
    else:
        await send_start_menu(client, message)

# Function to handle /rdel command
@app.on_message(filters.command(["rdel"]))
async def rdel_command(client, message):
    # Extract the user ID from the command
    if len(message.command) == 2:
        refer_id = message.command[1]
        try:
            refer_id = int(refer_id)
        except ValueError:
            await message.reply_text("Invalid user ID provided.")
            return

        # Check if the user ID exists in the database
        cursor.execute('''SELECT rfrs FROM raffer WHERE referid = ?''', (refer_id,))
        referrer_data = cursor.fetchone()
        if referrer_data:
            cursor.execute('''UPDATE raffer SET rfrs = NULL WHERE referid = ?''', (refer_id,))
            conn.commit()
            await message.reply_text("Referrals removed successfully.")
        else:
            await message.reply_text("User not found in the database.")
    else:
        await message.reply_text("Invalid command format. Please provide a user ID.")

# Function to send the start menu
async def send_start_menu(client, message):
    print("User Info from start menu function:", message.from_user)
    user_mention = message.from_user.mention() if message.from_user else "Unknown User"
    
    if isinstance(message, Message):
        chat_id = message.chat.id
    else:
        chat_id = message.message.chat.id

    newuser_text = f''' 
{user_mention}

𝗦𝘁𝗲𝗽 𝟭
𝗦𝗲𝗯𝗲𝗹𝘂𝗺 𝗕𝗼𝗹𝗲𝗵 𝗧𝗲𝗻𝗴𝗼𝗸 𝗞𝗮𝗻𝗱𝘂𝗻𝗴𝗮𝗻 𝗕𝗼𝘁 𝗗𝗮𝗻 𝗗𝗮𝗽𝗮𝘁𝗸𝗮𝗻 𝗙𝗿𝗲𝗲 𝗖𝗿𝗲𝗱𝗶𝘁, 𝗧𝗲𝗸𝗮𝗻 𝗦𝗲𝗺𝘂𝗮 "𝗦𝗮𝘆𝗲 𝗕𝘂𝗸𝗮𝗻 𝗥𝗼𝗯𝗼𝘁🟢" 𝗗𝗶 𝗕𝗮𝘄𝗮𝗵 𝗗𝗮𝗻 𝗦𝗲𝗿𝘁𝗮𝗶 𝗦𝗲𝗺𝘂𝗮 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗞𝗮𝗺𝗶.
    
𝗦𝘁𝗲𝗽 𝟮
❆ 𝗦𝗲𝗹𝗲𝗽𝗮𝘀 𝗦𝗲𝗺𝘂𝗮 𝗟𝗮𝗻𝗴𝗸𝗮𝗵 𝗗𝗶 𝗔𝘁𝗮𝘀 𝗦𝗲𝗹𝗲𝘀𝗮𝗶, 𝗧𝗲𝗸𝗮𝗻 𝗟𝗮𝗴𝗶 👉 [ /start ] '''

    keyboard = [
        [InlineKeyboardButton("1. 𝗧𝗲𝗸𝗮𝗻 𝗦𝗶𝗻𝗶 𝗦𝗮𝘆𝗲 𝗕𝘂𝗸𝗮𝗻 𝗥𝗼𝗯𝗼𝘁🟢", url="https://t.me/TOKONG_CHANNEL")],
        [InlineKeyboardButton("2. 𝗧𝗲𝗸𝗮𝗻 𝗦𝗶𝗻𝗶 𝗦𝗮𝘆𝗲 𝗕𝘂𝗸𝗮𝗻 𝗥𝗼𝗯𝗼𝘁🟢 ", url="https://t.me/tokong_casino")],
        [InlineKeyboardButton("🔞𝗩𝗶𝗱𝗲𝗼 𝗫𝗫𝗫🔞🟢", url="https://t.me/addlist/-ExO3GVAe5I0OTY1")],
        [InlineKeyboardButton("Refresh", callback_data="refresh_start")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the new message with the start menu
    try:
        await client.send_photo(chat_id, photo=new_start, caption=newuser_text, reply_markup=reply_markup)
    except Exception as e:
        print(f"Error sending start menu: {e}")



print("ass")       
if not os.path.exists('all_users.txt'):
    with open('all_users.txt', 'w') as f:
        pass

app.run()
