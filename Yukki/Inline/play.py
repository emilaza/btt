from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="โฎ",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐ต",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐ฅ",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="โฏ",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐ Daha Fazla",
                callback_data=f"Search {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐ Kapat",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons


def url_markup2(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="๐ต Mรผzik รal",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐ฅ Video Oynat",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐ Kapat",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1๏ธโฃ", callback_data=f"Yukki {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2๏ธโฃ", callback_data=f"Yukki {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3๏ธโฃ", callback_data=f"Yukki {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4๏ธโฃ", callback_data=f"Yukki {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5๏ธโฃ", callback_data=f"Yukki {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="๐ Kapat", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6๏ธโฃ",
                callback_data=f"Yukki {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7๏ธโฃ",
                callback_data=f"Yukki {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8๏ธโฃ",
                callback_data=f"Yukki {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9๏ธโฃ",
                callback_data=f"Yukki {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="๐",
                callback_data=f"Yukki {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="โ Kapat", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def secondary_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="๐ฎ Diฤer Menรผ", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="๐ Kapat", callback_data=f"close"),
        ],
    ]
    return buttons


def secondary_markup2(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(text="๐ Kapat", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ใ--< โ โฎ โฐ โฌ โฆ โง >--ใ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="๐ฎ Diฤer Menรผ", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="๐ Kapat", callback_data=f"close"),
        ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ใ--< โ โฎ โฐ โฌ โฆ โง >--ใ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="๐ฎ Diฤer Menรผ", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="๐ Kapat", callback_data=f"close"),
        ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ใ--< โ โฎ โฐ โฌ โฆ โง >--ใ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="๐ Kapat", callback_data=f"close")],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ใ--< โ โฎ โฐ โฌ โฆ โง >--ใ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="๐ Kapat", callback_data=f"close")],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="โถ๏ธ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="โธ๏ธ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="โญ๏ธ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="โน๏ธ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("๐ Kapat", callback_data="close")],
    ]
)
