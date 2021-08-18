from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Merhab, ben {bn} 🎵

Grubunuzun sesli aramasında müzik çalabilirim. Developed by [Jester](https://t.me/sarikola).

Beni grubunuza ekleyin ve özgürce müzik çalın!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Owner 🛠", url="https://t.me/sarikola")
                  ],[
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/zmonios"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/zmoniosbots"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Gruba Ekle ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Grup Müzik Çalar Çevrimiçi ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Kanal", url="https://t.me/zmoniosbots")
                ]
            ]
        )
   )


