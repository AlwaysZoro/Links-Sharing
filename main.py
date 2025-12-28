from bot import Bot
import pyrogram.utils

# Set a very low minimum channel ID to avoid 'peer id invalid'
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

Bot().run()
