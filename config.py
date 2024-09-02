#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24440741"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "eda231ff278ef43dc36164de83ee8fd6")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002169438785"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "XynoFT")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1833463223"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://megadiwani:gnTnDjCx1jB9W9hg@cluster0.ak69r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-2238297424"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-2159673469"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "1"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @otakuflix_network\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/cosmic_freak>sᴜʙᴀʀᴜ</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>subaru</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_cruise_netflix>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/webseries_flix>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/pornhwaocean>ᴘᴏʀɴʜᴡᴀs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/cosmic_freak>subaru</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "1833463223").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @OtakuFlix_Network</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! TIME NHI HAI MERE PAS BAKWAS KE LIYE!!"

ADMINS.append(OWNER_ID)
ADMINS.append(1833463223)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
