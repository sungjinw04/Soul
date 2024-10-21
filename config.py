import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "22906249"))
API_HASH = getenv("API_HASH", "a8aa1616cda4920822ee4305908486d6")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7283459459:AAGMJwIjdGYr1dzA-Nbk-hgMzMli1rc24Uw")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","sung_jinwo2")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Levi_Xprobot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "𝐋ᴇᴠɪ 𝐀ᴄᴋᴇʀᴍᴀɴ")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "chico_daddy")
# ---------------------------------------------------------
UPSTREAM_REPO = UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sungjinw04/DAXXMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aditya:0099@cluster0.vvcyc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002182829714))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7292418294))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

#-----------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/eldian_networks")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/eldian_empire")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION1", "BQFdhYkAxX3OHkO5b7FSA4TyD7sZXMS2DifSzekOZMFZumd3IJ7xrF-wKyfSq2F6Fvli_W1xSVMLPhepqS64af82PSyfHdNsRyS2l_5PFWNdX1E7b02XQmAW94QVDJG-o2gD7aFEjQ1TxJ95QS4yh7eyU6uiSmUmxKk6YK1fmnwbXSn9ago-4sE1YEcBUnrkzok5Gv6O6FQ9cenrARkxu8uzLVlqU35-75O0jI0wfcfJ5BLPMNcXWRPMDOBhBC6OIky-r5YUSy3WjYSxwfwFNmVbMqDGwXBJdKDdzgrTJXhOjqCWv7T9qMiXRmtF7dFDTVwwR4mUrdDLMfOjLbR7ICB84Rh1BAAAAAGa3Sc6AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org//file/b49463ae8e0fdecec3744.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org//file/70fb324cda8936a3f9d00.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org//file/be2dd46a1c4b5474c6084.jpg"
STATS_IMG_URL = "https://graph.org//file/b49463ae8e0fdecec3744.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/be2dd46a1c4b5474c6084.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org//file/70fb324cda8936a3f9d00.jpg"
STREAM_IMG_URL = "https://graph.org//file/70fb324cda8936a3f9d00.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org//file/be2dd46a1c4b5474c6084.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/be2dd46a1c4b5474c6084.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org//file/70fb324cda8936a3f9d00.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org//file/b49463ae8e0fdecec3744.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org//file/b49463ae8e0fdecec3744.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
