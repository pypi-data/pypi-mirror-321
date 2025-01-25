# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebPageAttribute = Union["raw.types.WebPageAttributeStickerSet", "raw.types.WebPageAttributeStory", "raw.types.WebPageAttributeTheme"]


class WebPageAttribute:  # type: ignore
    """Webpage attributes

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPageAttributeStickerSet
            WebPageAttributeStory
            WebPageAttributeTheme
    """

    QUALNAME = "pyrogram.raw.base.WebPageAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
