from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ρεяsσnαℓ ❄",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="❄ gℓσвαℓ ❄", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄ cℓσsε ❄", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ тσρ 10 ℓιsт ❄", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ σωn ❄", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ gℓσвαℓ ❄", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="❄ gυℓυρ ❄", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ вαcк ❄", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❄ cℓσsε ❄", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ αυ∂ισ ❄", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="❄ vι∂εσ ❄", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄ вαcк ❄", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="❄ cℓσsε ❄", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ тσρ 10 ℓιsт ❄", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ ρεяsσnαℓ ❄", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ gℓσвαℓ ❄", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="❄ gяσυρ ❄", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="❄ вαcк ❄", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❄ cℓσsε ❄", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ вαcк ❄",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="❄ cℓσsε ❄", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❄ ∂εℓεтε ❄",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄вαcк ❄",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="❄ cℓσsε ❄",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❄ cℓσsε ❄",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
