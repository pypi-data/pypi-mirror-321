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


class UrlAuthResultAccepted(TLObject):  # type: ignore
    """Details about an accepted authorization request, for more info click here »

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``196``
        - ID: ``8F8C0E4E``

    Parameters:
        url (``str``):
            The URL name of the website on which the user has logged in.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["url"]

    ID = 0x8f8c0e4e
    QUALNAME = "types.UrlAuthResultAccepted"

    def __init__(self, *, url: str) -> None:
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultAccepted":
        # No flags
        
        url = String.read(b)
        
        return UrlAuthResultAccepted(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()
