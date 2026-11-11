
class script(object):
    HELP_TXT = """<b>ʜᴇʏ</b> {}

<b>ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""

    CAPTION_TXT = """<b><u>📝  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ</u></b>

<b>⦿ /set_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
<b>⦿ /see_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
<b>⦿ /del_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>"""

    THUMBNAIL_TXT = """<b><u>🖼️  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>

<b>⦿ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sɪᴍᴘʟʏ ʙʏ sᴇɴᴅɪɴɢ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴇ....</b>

<b>⦿ /viewthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>
<b>⦿ /delthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>"""

    ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ :</b> {}
<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'>Python 3</a>
<b>📚 ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 sᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/RudraMoviez'>Rudra Moviez</a>
<b>🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/CallAdminRMBot'>Surya Developer</a>

<b>♻️ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ :</b> @CallAdminRMBot"""

    DONATE_TXT = """
<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>

ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 10 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

<b>🛍 ᴜᴘɪ ɪᴅ:</b> <code>suryabm18@axl</code>

<b>📸 sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴅᴏɴᴀᴛɪᴏɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ</b> """

    ADMIN_TXT = """<b><u>🦋 ᴀᴅᴍɪɴ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ʜᴇʀᴇ</u></b>

<b>⦿ /users - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ᴛᴏᴛᴀʟ ᴜsᴇʀs</b>
<b>⦿ /allids - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ᴀʟʟ ᴜsᴇʀs ɪᴅs</b>
<b>⦿ /broadcast - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜsᴇʀs</b>
<b>⦿ /warn - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀ ᴜsᴇʀ</b>
<b>⦿ /resetpower - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇsᴇᴛ ᴜsᴇʀ ᴘᴏᴡᴇʀ</b>
<b>⦿ /ceasepower - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄᴇᴀsᴇ ᴜsᴇʀ ᴘᴏᴡᴇʀ</b>
<b>⦿ /addpremium - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀᴅᴅ ᴘʀᴇᴍɪᴜᴍ ᴛᴏ ᴜsᴇʀs</b>
<b>⦿ /restart - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴀʟʟ ᴘʀᴏᴄᴇss ᴀɴᴅ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ</b>"""

    METADATA_TXT = """<b><u>🖼️  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ</u></b>

ғᴏʀ ᴇxᴀᴍᴘʟᴇ :-

<code>ʙʏ @CallAdminRMBot</code>

💬 ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ @CallAdminRMBot
"""


# Jishu Developer
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
