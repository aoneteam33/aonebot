import random
import time
import os 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

scan_button="/root/ref2/video/scanbtn.mp4"
ap_button="/root/ref2/video/APcoundown.mp4"
avantplay_vdo="/root/ref2/video/advantplay.mp4"
lucky_button="/root/ref2/video/LCKY365countdown.mp4"
lucky365_vdo="/root/ref2/video/lky365.mp4"
bng_button="/root/ref2/video/BNGcountdown.mp4"
BNG_vdo="/root/ref2/video/BNG.mp4"
mega_button="/root/ref2/video/mega888countdown.mp4"
MEGA_vdo="/root/ref2/video/MEGA888.mp4"
gfg_button="/root/ref2/video/GFGcountdown.mp4"
GFG_vdo="/root/ref2/video/GFG.mp4"
relax_button="/root/ref2/video/Relaxcountdown.mp4"
RELAX_vdo="/root/ref2/video/RELAX.mp4"
jili_button="/root/ref2/video/JILIcountdown.mp4"
JILI_vdo="/root/ref2/video/JILI.mp4"
jdb_button="/root/ref2/video/JDBcountdown.mp4"
JDB_vdo="/root/ref2/video/JDB.mp4"
nxspin_button="/root/ref2/video/NEXTSPINcountdown.mp4"
NEXTSPIN_vdo="/root/ref2/video/Nextspin.mp4"
habnr_button="/root/ref2/video/HABANEROcountdown.mp4"
HABANERO_vdo="/root/ref2/video/HABAN.mp4"
spadeGm_button="/root/ref2/video/SPADEGAMINGcountdown.mp4"
SPADEGAME_vdo="/root/ref2/video/spadegaming.mp4"
playt_button="/root/ref2/video/PLAYTECHcountdown.mp4"
PLAYTECH_vdo="/root/ref2/video/playtech.mp4"
cq9_button="/root/ref2/video/CQ9countdown.mp4"
CQ9_vdo="/root/ref2/video/cq9.mp4"
kagm_button="/root/ref2/video/KA GAMINGcountdown.mp4"
KAGAMING_vdo="/root/ref2/video/ka.mp4"
pragmatic_button="/root/ref2/video/PPSLOTcountdown.mp4"
PRAGMATIC_vdo="/root/ref2/video/ppslot.mp4"
kiss_button="/root/ref2/video/918 KISScountdown.mp4"
kiss918_vdo="/root/ref2/video/918kiss.mp4"
lion_button="/root/ref2/video/LIONKINGcountdown.mp4"
lion_vdo="/root/ref2/video/lionking.mp4"
live22_button="/root/ref2/video/LIVE22countdown.mp4"
Live_vdo="/root/ref2/video/live22.mp4"


class Advant:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def advpscan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
            
        text1 = f''' 

ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴀᴅᴠᴀɴᴛᴘʟᴀʏ

        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡E❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴀᴅᴠᴀɴᴛᴘʟᴀʏ🎰

Maya:Elemental Totem🔓 {percentage1}%
Dragon Chi's Quest🔓 {percentage2}%        
Wheel of Gems🔓 {percentage3}%
Xmas Gift Delight🔓 {percentage4}%        
Cookie Hunter🔓 {percentage5}%        
Xiang Qi Ways 2🔓 {percentage6}%        
Aztec: Bonus Hunt🔓 {percentage7}%        
Last Samurai🔓 {percentage8}%        
Boom of Prosperity🔓 {percentage9}%
Scale of Heaven: Anubis🔓 {percentage10}%                
Mace of Hercules🔓 {percentage11}%        
DJ FEVER🔓 {percentage12}%        
Jewel Mastermind🔓 {percentage13}%        
PUBG2🔓 {percentage14}%        
World Cup Final🔓 {percentage15}%        
Xiang Qi Ways🔓 {percentage16}%        
Candy Rush🔓 {percentage17}%        
Ninja Legend🔓 {percentage18}%        
Fortune God's Pot🔓 {percentage19}%        
Counter-Terrorists🔓 {percentage20}%'''                        

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
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

        video_message = await client.send_video(chat_id=user_id, video=ap_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=avantplay_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()

  
class Lucky365:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 

ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ʟᴜᴄᴋʏ365
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʟᴜᴄᴋʏ365🎰

Zeus🔓 {percentage1}%        
EgyptQueen🔓 {percentage2}%        
GodOfFortune🔓 {percentage3}%        
GodOfWealth2🔓 {percentage4}%        
FortuneTiger🔓 {percentage5}%        
FootBall🔓 {percentage6}%        
BigMoney🔓 {percentage7}%        
DolphinReef🔓 {percentage8}%        
GreatBlue🔓 {percentage9}%        
RisingFortune🔓 {percentage10}%        
Pyramid🔓 {percentage11}%        
PantherMoon🔓 {percentage12}%        
Hercules🔓 {percentage13}%        
FuwaFortune🔓 {percentage14}%        
Simba🔓 {percentage15}%        
Bomb🔓 {percentage16}%          
NezhaLegeng🔓 {percentage17}%        
AmazingMonkeyKing🔓 {percentage18}%        
Ninja🔓 {percentage19}%        
GoldenLotus🔓 {percentage20}%        
FortuneGod🔓 {percentage21}%        
QinShiHuang🔓 {percentage22}%        
TripleTwister🔓 {percentage23}%        
CrazyMonkey🔓 {percentage24}%        
SilentSamurai🔓 {percentage25}%        
Sparta🔓 {percentage26}%        
ThunderGod🔓 {percentage27}%        
WhiteSanke🔓 {percentage28}%        
Safari🔓 {percentage29}%        
Jungle2🔓 {percentage30}%'''        

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="L365scan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=lucky_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=lucky365_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()

   
class BNG:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 

ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ʙɴɢ
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʙɴɢ🎰
 
3MagicLamps🔓 {percentage1}%
LionCoins🔓 {percentage2}%
3PotsRichesExtra🔓 {percentage3}%
SkyPearls🔓 {percentage4}%
CoinUp🔓 {percentage5}%
AztecFire2🔓 {percentage6}%
LadyFortune🔓 {percentage7}%
CoinVolcano🔓 {percentage8}%
HappyFish🔓 {percentage9}%
GoldNugget🔓 {percentage10}%
CoinStrike🔓 {percentage11}%
EnergyCoins🔓 {percentage12}%
BlackWolf2🔓 {percentage13}%
GreenChilli2🔓 {percentage14}%
SunOfEgypt4🔓 {percentage15}%
MoreMagicApple🔓 {percentage16}%
YohoGold🔓 {percentage17}%
ForestSpirit🔓 {percentage18}%
BuffaloPower2🔓 {percentage19}%
EgyptFire🔓 {percentage20}%
CandyBoom🔓 {percentage21}%
BigHeist🔓 {percentage22}%
OlafViking🔓 {percentage23}%
SherwoodCoins🔓 {percentage24}%
Crown&Diamonds🔓 {percentage25}%
AfricanSpirit🔓 {percentage26}%
FireTemple🔓 {percentage27}%
FireCoins🔓 {percentage28}%
CrystalLand2🔓 {percentage29}%
StickyPigg🔓 {percentage30}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="bngscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=bng_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=BNG_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()

class Mg888:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 

ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴍᴇɢᴀ888 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴍᴇɢᴀ888🎰
 
DragonHero🔓 {percentage1}%
GiftsFromSanta🔓 {percentage2}%
WolfRun🔓 {percentage3}%
GodOfCookery🔓 {percentage4}%
StickyBandits🔓 {percentage5}%
KingOfPop🔓 {percentage6}%
CashNoire🔓 {percentage7}%
DeepTrek🔓 {percentage8}%
SushiOishi🔓 {percentage9}%
Caishen'sGold🔓 {percentage10}%
LotusLegend🔓 {percentage11}%
FortunePanda🔓 {percentage12}%
NativeIndian🔓 {percentage13}%
FortuneCharm🔓 {percentage14}%
CleopatrasRiches🔓 {percentage15}%
ChineseLion🔓 {percentage16}%
TopGun🔓 {percentage17}%
SilentRun🔓 {percentage18}%
Dolphin🔓 {percentage19}%
SeaWorld🔓 {percentage20}%
ThreeKingdoms🔓 {percentage21}%
T-Dex🔓 {percentage22}%
IceLand🔓 {percentage23}%
GreatBlue🔓 {percentage24}%
Safari🔓 {percentage25}%
FortuneTiger🔓 {percentage26}%
GoldenBeauty🔓 {percentage27}%
Santa🔓 {percentage28}%
XmasMagic🔓 {percentage29}%
MidasGoldenTouch🔓 {percentage30}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="Mg888scan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=mega_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=MEGA_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()

 
class Gfg:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(27)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ɢꜰɢ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ɢꜰɢ🎰
 
MahjongWin🔓 {percentage1}%
BuffaloCoin🔓 {percentage2}%
HoldTheSpin🔓 {percentage3}%
HellSpin🔓 {percentage4}%
BonanzaDonut🔓 {percentage5}%
WonHundred🔓 {percentage6}%
Dice🔓 {percentage7}%
FruitStory🔓 {percentage8}%
3x3Egypt🔓 {percentage9}%
ReallyHot2🔓 {percentage10}%
HotLove🔓 {percentage11}%
SunnyCoin2🔓 {percentage12}%
OlympusOfLuck🔓 {percentage13}%
JapaneseCoin🔓 {percentage14}%
CoinWin🔓 {percentage15}%
SuperAce🔓 {percentage16}%
PatricksCoin🔓 {percentage17}%
WitchsLove🔓 {percentage18}%
NekoMaid🔓 {percentage19}%
AdventureOfSinbad🔓 {percentage20}%
GoalLineBaby🔓 {percentage21}%
KitsuneSister🔓 {percentage22}%
XmasMission🔓 {percentage23}%
WorldCupShotting🔓 {percentage24}%
WolfStory🔓 {percentage25}%
JokerTriple🔓 {percentage26}%
WonderlandTreasure🔓 {percentage27}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="gfgtscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=gfg_buton, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=GFG_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()


class Rxg:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER  : ʀᴇʟᴀxɢᴀᴍɪɴɢ
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʀᴇʟᴀxɢᴀᴍɪɴɢ🎰
 
RoyalPotato🔓 {percentage1}%
CloverlandRiches🔓 {percentage2}%
MoneyTrain4🔓 {percentage3}%
RoyalPotato2🔓 {percentage4}%
JokerSplit🔓 {percentage5}%
TerracottaArmy🔓 {percentage6}%
TitanStrike🔓 {percentage7}%
MysticSpelles🔓 {percentage8}%
JokerLoot🔓 {percentage9}%
MoneyTrain3🔓 {percentage10}%
PineOfPlinko🔓 {percentage11}%
HolyHandGrenade🔓 {percentage12}%
CashDefense🔓 {percentage13}%
ShinobiSpirit🔓 {percentage14}%
SafariSun🔓 {percentage15}%
ToriiTumble🔓 {percentage16}%
TempleOfFury🔓 {percentage17}%
SharkWash🔓 {percentage18}%
BeastMode🔓 {percentage19}%
NetGains🔓 {percentage20}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="Rxgscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=relax_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=RELAX_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()


class Jili:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴊɪʟɪ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴊɪʟɪ🎰
 
GemParty🔓 {percentage1}%
SuperRich🔓 {percentage2}%
Medusa🔓 {percentage3}%
RomaX🔓 {percentage4}%
GoldenEmpire🔓 {percentage5}%
MagicLamp🔓 {percentage6}%
FortuneGems🔓 {percentage7}%
Alibaba🔓 {percentage8}%
AgentAce🔓 {percentage9}%
HappyTaxi🔓 {percentage10}%
BoneFortune🔓 {percentage11}%
ThorX🔓 {percentage12}%
BonusHunter🔓 {percentage13}%
JiliCaishen🔓 {percentage14}%
GoldRush🔓 {percentage15}%
JungleKing🔓 {percentage16}%
PirateQueen🔓 {percentage17}%
WildRacer🔓 {percentage18}%
ChinShiHuang🔓 {percentage19}%
BaoBoonChin🔓 {percentage20}%
GodOfMartial🔓 {percentage21}%
ChargeBuffalo🔓 {percentage22}%
BoxingKing🔓 {percentage23}%
PartyNight🔓 {percentage24}%
PharaohTreasure🔓 {percentage25}%
Samba🔓 {percentage26}%
SweetLand🔓 {percentage27}%
HyperBurst🔓 {percentage28}%
ShanghaiBeauty🔓 {percentage29}%
FengShen🔓 {percentage30}%
'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="jiliscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=jili_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=JILI_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()


class Jdb:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴊᴅʙ
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴊᴅʙ🎰
 
DragonSoars🔓 {percentage1}%
OpenSesameMega🔓 {percentage2}%
PoppopCandy🔓 {percentage3}%
FruityBonanza🔓 {percentage4}%
TreasureBowl🔓 {percentage5}%
TrumpCard🔓 {percentage6}%
Kong🔓 {percentage7}%
CaisenComing🔓 {percentage8}%
MoneyBagsMan🔓 {percentage9}%
MoneyBagsMan2🔓 {percentage10}%
BlossonOfWealth🔓 {percentage11}%
OpenSesame2🔓 {percentage12}%
ElementalLinkFire🔓 {percentage13}%
WinningMask2🔓 {percentage14}%
TripleKingkong🔓 {percentage15}%
ChefPanda🔓 {percentage16}%
LuckyFuwa🔓 {percentage17}%
ElementalLinkWater🔓 {percentage18}%
ProsperityTiger🔓 {percentage19}%
BookOfMystery🔓 {percentage20}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="jdbscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=jdb_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=JDB_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class Nxt:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ɴᴇxᴛꜱᴘɪɴ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ɴᴇxᴛꜱᴘɪɴ🎰
 
AztecGoldTreasure🔓 {percentage1}%
Roma2🔓 {percentage2}%
LightningDragon🔓 {percentage3}%
MahjongPhoenix🔓 {percentage4}%
LongLongLong🔓 {percentage5}%
5FortuneStars🔓 {percentage6}%
ProsperityDragon🔓 {percentage7}%
BigCaiShen🔓 {percentage8}%
GoldenWest🔓 {percentage9}%
BuffaloKing🔓 {percentage10}%
PrincessOfRa🔓 {percentage11}%
FortuneToad🔓 {percentage12}%
LightningWoman🔓 {percentage13}%
GoldenFa🔓 {percentage14}%
GoldenWar🔓 {percentage15}%
CandyBonanza🔓 {percentage16}%
ShakeThaiThai🔓 {percentage17}%
CrazyMonkeyDeluxe🔓 {percentage18}%
JokerKing🔓 {percentage19}%
SoccerKing🔓 {percentage20}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="nxtspscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=nxspin_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=NEXTSPIN_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()





class Hbn:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ʜᴀʙᴀɴᴇʀᴏ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʜᴀʙᴀɴᴇʀᴏ🎰
 
VampiresFate🔓 {percentage1} %
HotHotSummer🔓 {percentage2} %
ValentineMonchy🔓 {percentage3} %
FruityMayan🔓 {percentage4} %
Santa'sInn🔓 {percentage5} %
ZeusDeluxe🔓 {percentage6} %
FruityHalloween🔓 {percentage7} %
SlimeParty🔓 {percentage8} %
MeowJanken🔓 {percentage9} %
BikiniIslandDeluxe🔓 {percentage10} %
AtomicKittens🔓 {percentage11} %
WitchesTome🔓 {percentage12} %
LegengOfNezha🔓 {percentage13} %
TootyFruityFruits🔓 {percentage14} %
Siren'sSpell🔓 {percentage15} %
Crystopia🔓 {percentage16} %
TheBigDealDeluxe🔓 {percentage17} %
NaughtyWukong🔓 {percentage18} %
Rainbowmania🔓 {percentage19} %
LaughingBuddha🔓 {percentage20} %'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="hbnrscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=habnr_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=HABANERO_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class Spd:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER  : ꜱᴘᴀᴅᴇɢᴀᴍɪɴɢ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ꜱᴘᴀᴅᴇɢᴀᴍɪɴɢ🎰
 
LegacyOfKongMaxways🔓 {percentage1}%
RoyalKatt🔓 {percentage2}%
Zeus🔓 {percentage3}%
Caishen🔓 {percentage4}%
GoldPanther🔓 {percentage5}%
ClashOfTheGiants🔓 {percentage6}%
888🔓 {percentage7}%
GoldenLotusSE🔓 {percentage8}%
CaishenDeluxeMaxways🔓 {percentage9}%
WildWetWin🔓 {percentage10}%
GoldPantherMaxways🔓 {percentage11}%
TigerDance🔓 {percentage12}%
MuayThaiFighter🔓 {percentage13}%
RichCaiShen🔓 {percentage14}%
RoyaleHouse🔓 {percentage15}%
5FortuneDragons🔓 {percentage16}%
FruitsMania🔓 {percentage17}%
GoldRushCowboys🔓 {percentage18}%
HammerOfThunder🔓 {percentage19}%
IcelandSA🔓 {percentage20}%
PokerWays🔓 {percentage21}%
BrothersKingdom🔓 {percentage22}%
GemstoneRush🔓 {percentage23}%
RoyaleVegas🔓 {percentage24}%
Roma🔓 {percentage25}%
GalaxyGuardian🔓 {percentage26}%
LuckyKoiExclusive🔓 {percentage27}%
LuckyMeow🔓 {percentage28}%
JourneyToTheWild🔓 {percentage29}%
MagicLamp🔓 {percentage30}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="spdgmscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=spadeGm_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=SPADEGAME_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class Pltc:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴘʟᴀʏᴛᴇᴄʜ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴘʟᴀʏᴛᴇᴄʜ🎰
 
AgeOfEgypt🔓 {percentage1}%
AnacondaWild🔓 {percentage2}%
Archer🔓 {percentage3}%
AsianFantasy🔓 {percentage4}%
BoutyOfTheBeanstalk🔓 {percentage5}%
BuffaloBlitz🔓 {percentage6}%
GreatBlue🔓 {percentage7}%
BeachLife🔓 {percentage8}%
BonusBears🔓 {percentage9}%
BaiShi🔓 {percentage10}%
BermudaTriangle🔓 {percentage11}%
CatQueen🔓 {percentage12}%
CashIt🔓 {percentage13}%
CaptainsTreasure🔓 {percentage14}%
CatInVegas🔓 {percentage15}%
FortuneDay🔓 {percentage16}%
FunkyMonkeyJackpot🔓 {percentage17}%
Fortunate5🔓 {percentage18}%
FortuneLion🔓 {percentage19}%
GemQueen🔓 {percentage20}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="pltcscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=playt_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=PLAYTECH_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class Cq9:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(35)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : 𝗖𝗤𝟵 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ​𝗖𝗤𝟵🎰

TreasurePirate🔓 {percentage1}%
Mafia🔓 {percentage2}%
Chicago2🔓 {percentage3}%
TheChickenHouse🔓 {percentage4}%
FootballFeverM🔓 {percentage5}%
StrikerWild🔓 {percentage6}%
BaseballFever🔓 {percentage7}%
Myeong-Ryang🔓 {percentage8}%
NightCity🔓 {percentage9}%
MirrorMirror🔓 {percentage10}%
888CaiShen🔓 {percentage11}%
ThaiPokDeng🔓 {percentage12}%
KOIsaland🔓 {percentage13}%
MrMiser🔓 {percentage14}%
LuckyTigers🔓 {percentage15}%
CoinSpinner🔓 {percentage16}%
LayKrathong🔓 {percentage17}%
FloatingMarket🔓 {percentage18}%
KingKongShake🔓 {percentage19}%
AladdinsLamp🔓 {percentage20}%
KingOfAtlantis🔓 {percentage21}%
XocDia🔓 {percentage22}%
DollarBomb🔓 {percentage23}%
MoneyTree🔓 {percentage24}%
TheCupids🔓 {percentage25}%
AliceRun🔓 {percentage26}%
5Boxing🔓 {percentage27}%
ZeusM🔓 {percentage28}%
Thor🔓 {percentage29}%
Poseidon🔓 {percentage30}%
Apollo🔓 {percentage31}%
Hephaestus🔓 {percentage32}%
FireQueen🔓 {percentage33}%
Hercules🔓 {percentage34}%
Kronos🔓 {percentage35}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="cq9scan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=cq9_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=CQ9_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()
        
        
class Kagm:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(20)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴋᴀ ɢᴀᴍɪɴɢ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴋᴀ ɢᴀᴍɪɴɢ🎰

BonusMania🔓 {percentage1}%
TreasureBowl🔓 {percentage2}%
Luck88🔓 {percentage3}%
GoldenBull🔓 {percentage4}%
Cocorico🔓 {percentage5}%
TreasureTiger🔓 {percentage6}%
KingOfDragon🔓 {percentage7}%
FortuneGanesha🔓 {percentage8}%
ChinesePhoneix🔓 {percentage9}%
Rudolph🔓 {percentage10}%
RomaniSecret🔓 {percentage11}%
Borderland🔓 {percentage12}%
Neonmal🔓 {percentage13}%
OlympusGods🔓 {percentage14}%
Nezha🔓 {percentage15}%
FootballMania🔓 {percentage16}%
DetectiveDee🔓 {percentage17}%
HouYi🔓 {percentage18}%
LionOnRidge🔓 {percentage19}%
Aladdin🔓 {percentage20}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="kagmscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=kagm_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=KAGAMING_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class Prgm:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(32)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ᴘʀᴀɢᴍᴀᴛɪᴄ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ᴘʀᴀɢᴍᴀᴛɪᴄ🎰

Gates of Olympus🔓 {percentage1}%
Starlight Princess🔓 {percentage2}%
Sugar Rush🔓 {percentage3}%
Sweet Bonanza🔓 {percentage4}%
Wisdom of Athena🔓 {percentage5}%
Great Rhino Megaways🔓 {percentage6}%
Sugar Rush Xmas🔓 {percentage7}%
Gates of Gatot Kaca🔓 {percentage8}%
Power of Thor Megaways🔓 {percentage9}%
Starlight Princess 1000🔓 {percentage10}%
Gates of Olympus 1000🔓 {percentage11}%
Sugar Rush 1000🔓 {percentage12}%
Gates of Gatot Kaca 1000🔓 {percentage13}%
3 Buzzing Wilds🔓 {percentage14}%
5 Lions Gold🔓 {percentage15}%
Wild West Gold🔓 {percentage16}%
Bigger Bass Bonanza🔓 {percentage17}%
5 Rabbits Megaways🔓 {percentage18}%
Forge of Olympus🔓 {percentage19}%
Big Bass Christmas Bash🔓 {percentage20}%
Spellbinding Mystery🔓 {percentage21}%
Grace of Ebisu🔓 {percentage22}%
3 Genie Wishes🔓 {percentage23}%
Rujak Bonanza🔓 {percentage24}%
Viking Forge🔓 {percentage25}%
Buffalo King🔓 {percentage26}%
PIZZA PIZZA PIZZA🔓 {percentage27}%
Rise of Samurai Megaways🔓 {percentage28}%
The Dog House🔓 {percentage29}%
Rocket Blast Megaways🔓 {percentage30}%
Twilight Princess🔓 {percentage31}%
The Dog House Megaways🔓 {percentage32}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="prgmpscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=pragmatic_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=PRAGMATIC_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class kis918:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(35)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : 𝟵𝟭𝟴ᴋɪꜱꜱ
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 𝟵𝟭𝟴​ᴋɪꜱꜱ🎰

Wolf Hunters🔓 {percentage1}%
Motorcycle🔓 {percentage2}%
Dragon Maiden🔓 {percentage3}%
Steam Tower🔓 {percentage4}%
Witch🔓 {percentage5}%
JinQianWa🔓 {percentage6}%
Football🔓 {percentage7}%
TopGun🔓 {percentage8}%
Fortune Panda🔓 {percentage9}%
Robin Hood🔓 {percentage10}%
African Wildlife🔓 {percentage11}%
Amanzon🔓 {percentage12}%
Aladdin🔓 {percentage13}%
Ocean Paradise🔓 {percentage14}%
Pirate🔓 {percentage15}%
Pirate Ship🔓 {percentage16}%
MagicalSpin🔓 {percentage17}%
FairyGarden🔓 {percentage18}%
SeaWorld🔓 {percentage19}%
Three Kingdoms🔓 {percentage20}%
Golden Tree🔓 {percentage21}%
Treasure Island🔓 {percentage22}%
God of Wealth🔓 {percentage23}%
Victory🔓 {percentage24}%
T-Rex🔓 {percentage25}%
Big Shot🔓 {percentage26}%
Twister🔓 {percentage27}%
Iceland🔓 {percentage28}%
Highway🔓 {percentage29}%
Panther Moon🔓 {percentage30}%
Samurai🔓 {percentage31}%
GreatBlue🔓 {percentage32}%
Kimochi🔓 {percentage33}%
Boxing🔓 {percentage34}%
Dolphin Reef🔓 {percentage35}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="kissscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=kiss_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=kiss918_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()



class lionk:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(31)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ​ʟɪᴏɴ ᴋɪɴɢ 
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʟɪᴏɴ ᴋɪɴɢ🎰

Zues🔓 {percentage1}%
FaFaFa🔓 {percentage2}%
FaFaFa2🔓 {percentage3}%
EGYPT QUEEN🔓 {percentage4}%
Big Money🔓 {percentage5}%
Rising Fortune🔓 {percentage6}%
Panther Moon🔓 {percentage7}%
Pyramid🔓 {percentage8}%
Queen Of Bounty🔓 {percentage9}%
Beer Party🔓 {percentage10}%
Jungle 2🔓 {percentage11}%
Dragon Fortune🔓 {percentage12}%
Snow Queen🔓 {percentage13}%
Amanzing Monkey King🔓 {percentage14}%
Fortune God🔓 {percentage15}%
Yeb Hsien🔓 {percentage16}%
Lucky Fruit🔓 {percentage17}%
Football🔓 {percentage18}%
Dolphin Reef🔓 {percentage19}%
Highway Kings🔓 {percentage20}%
Simba🔓 {percentage21}%
Crazy Monkey🔓 {percentage22}%
Jungle Jungle🔓 {percentage23}%
Ninja🔓 {percentage24}%
Ocean🔓 {percentage25}%
Safari🔓 {percentage26}%
Hercules🔓 {percentage27}%
Nezha Legend🔓 {percentage28}%
Sango🔓 {percentage29}%
Sparta🔓 {percentage30}%
Great Blue🔓 {percentage31}%'''

        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="lionscan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=lion_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=lion_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()




class live22:
    def __init__(self):
        self.line_percentages = {}
        self.last_update_time = None

    async def scan_query(self, client, callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message.id
        user_mention = callback_query.from_user.mention() if callback_query.from_user else "Unknown User"
        await client.delete_messages(chat_id=user_id, message_ids=message_id)

        if not self.line_percentages or (time.time() - self.last_update_time) > 20:
            self.update_percentages(30)  # Number of lines in the text
        text1 = f''' 
ℹ️ sɪʟᴀ ʙᴇʀsᴀʙᴀʀ {user_mention} ʙᴏᴛ sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴘᴇʀᴍɪɴᴛᴀᴀɴ ᴀɴᴅᴀ

◈➣ STATUS          : Pʀᴏᴄᴇssɪɴɢ
◈➣ GAME PROVIDER   : ʟɪᴠᴇ22
        '''
        # Define the text with placeholders
        text = '''
𝗗𝗢𝗡𝗘❗
𝗜𝗻𝗶 𝗔𝗱𝗮𝗹𝗮𝗵 𝗞𝗲𝗽𝘂𝘁𝘂𝘀𝗮𝗻 𝗣𝗲𝗿𝗮𝘁𝘂𝘀𝗮𝗻 𝗦𝗰𝗮𝗻𝗻𝗶𝗻𝗴 ʟɪᴠᴇ22🎰

Gods Gambit Hade🔓 {percentage1}%
Kingdom of Luck🔓 {percentage2}%
Santas Payday🔓 {percentage3}%
Bloodmoon Amazonia🔓 {percentage4}%
Sanctum of Savanah🔓 {percentage5}%
Mahjong Style🔓 {percentage6}%
Black Pink🔓 {percentage7}%
Kraken Queen🔓 {percentage8}%
Queen Femida🔓 {percentage9}%
The  Great Sorcery🔓 {percentage10}%
Crypto Coin🔓 {percentage11}%
Candy Bomb🔓 {percentage12}%
Dragon FAFAFA🔓 {percentage13}%
Lucky Coins🔓 {percentage14}%
Fortune Dance🔓 {percentage15}%
Panthera Pardus🔓 {percentage16}%
God Of Wealth🔓 {percentage17}%
Feng Shen🔓 {percentage18}%
Dragons Treasure🔓 {percentage19}%
Laughing Buddha🔓 {percentage20}%
Axie Universe🔓 {percentage21}%
Fortune Realm🔓 {percentage22}%
Mobox🔓 {percentage23}%
Apes Squad🔓 {percentage24}%
Ocean🔓 {percentage25}%
Into the Fay: Snowie🔓 {percentage26}%
Into The Fay: Nixie🔓 {percentage27}%
Bonsai of Riches🔓 {percentage28}%
Illuvium🔓 {percentage29}%
Classic Diamond x5🔓 {percentage30}%'''


        lines = text.split('\n')
        updated_text = ''
        for line in lines:
            if '{percentage' in line:
                # Extract the line number from the placeholder
                line_number = int(line.split('{')[1].split('}')[0].replace('percentage', ''))
                line_key = f'Line {line_number}'
                if line_key in self.line_percentages:
                    line = line.replace(f'{{percentage{line_number}}}', str(self.line_percentages[line_key]))
            updated_text += line + '\n'
        keyboard = [
            [
                InlineKeyboardButton("SCAN NOW", callback_data="Livescan")
            ],
            [
                InlineKeyboardButton("Go Back", callback_data="scan_Game"),
                InlineKeyboardButton("Go Home", callback_data="refresh_start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        video_message = await client.send_video(chat_id=user_id, video=live22_button, caption=text1, reply_markup=reply_markup)
        await asyncio.sleep(10)
        await client.delete_messages(chat_id=user_id, message_ids=[video_message.id])
        await client.send_video(chat_id=user_id, video=Live_vdo, caption=updated_text, reply_markup=reply_markup)
        
    def update_percentages(self, num_lines):
        self.line_percentages = {}
        for i in range(num_lines):
            self.line_percentages[f'Line {i+1}'] = random.randint(88, 97)
        self.last_update_time = time.time()


        
  # CREATE INSTANCES For accessing CLASS Conent
Advant_instance = Advant() 
L365_instance = Lucky365()     
BNG_instance = BNG()
Meg_instance = Mg888()
GFG_instance = Gfg()
RELAXG_instance = Rxg()
Jili_instance = Jili()
Jdb_instance = Jdb()
Nxt_instance = Nxt()
Hbn_instance = Hbn()
Spd_instance = Spd()
Pltc_instance = Pltc()
Cq9_instance = Cq9()
Kagm_instance = Kagm()
Prgm_instance = Prgm()
kiss_instance = kis918()
lion_instance = lionk()
Live_instance = live22()
