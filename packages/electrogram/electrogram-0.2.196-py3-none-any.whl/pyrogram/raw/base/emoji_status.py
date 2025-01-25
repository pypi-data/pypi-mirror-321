# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiStatus = Union["raw.types.EmojiStatus", "raw.types.EmojiStatusEmpty", "raw.types.EmojiStatusUntil"]


class EmojiStatus:  # type: ignore
    """Emoji status

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiStatus
            EmojiStatusEmpty
            EmojiStatusUntil
    """

    QUALNAME = "pyrogram.raw.base.EmojiStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
