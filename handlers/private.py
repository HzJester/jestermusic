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

Beni grubunuza ekleyin ve özgürce müzik çalın!

Şuanda desteklediğim komutlar:

✳️ /oynat  -  Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.

✳️ /durdur -  Sesli Sohbet Müziğini Duraklat.

✳️ /devam  -  Sesli Sohbet Müziğine Devam Et.

✳️ /atla   -  Sesli Sohbette Çalan Geçerli Müziği Atlar.

✳️ /bitir  -  Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.

✳️ /bul    -  Müziği bulup gruba gönderir. Örnek /bul ezhel geceler.**
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
                        "➕ Gruba Ekle ➕", url="https://t.me/ZmoniosMusicBot?startgroup=true"
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


