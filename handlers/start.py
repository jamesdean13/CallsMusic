from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am Swifties Music Bot, a bot that lets you play music in @Swiftiesworld voice chat.
This bot is created by @TayLife. 
Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Creator", url="https://t.me/taylife"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/swiftiesworld"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/taylorswift13fanpage"
                    ),
                    InlineKeyboardButton(
                        "Discography 😈", url="https://t.me/taylorflac"

                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
