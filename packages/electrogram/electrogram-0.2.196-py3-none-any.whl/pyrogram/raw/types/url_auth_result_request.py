from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UrlAuthResultRequest(TLObject):  # type: ignore
    """Details about the authorization request, for more info click here »

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``196``
        - ID: ``92D33A0E``

    Parameters:
        bot (:obj:`User <pyrogram.raw.base.User>`):
            Username of a bot, which will be used for user authorization. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        domain (``str``):
            The domain name of the website on which the user will log in.

        request_write_access (``bool``, *optional*):
            Whether the bot would like to send messages to the user

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access"]

    ID = 0x92d33a0e
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot: "raw.base.User", domain: str, request_write_access: Optional[bool] = None) -> None:
        self.bot = bot  # User
        self.domain = domain  # string
        self.request_write_access = request_write_access  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultRequest":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        bot = TLObject.read(b)
        
        domain = String.read(b)
        
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.domain))
        
        return b.getvalue()
