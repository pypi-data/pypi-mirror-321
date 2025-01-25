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


class BroadcastRevenueWithdrawalUrl(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.stats.BroadcastRevenueWithdrawalUrl`.

    Details:
        - Layer: ``196``
        - ID: ``EC659737``

    Parameters:
        url (``str``):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetBroadcastRevenueWithdrawalUrl
    """

    __slots__: List[str] = ["url"]

    ID = 0xec659737
    QUALNAME = "types.stats.BroadcastRevenueWithdrawalUrl"

    def __init__(self, *, url: str) -> None:
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueWithdrawalUrl":
        # No flags
        
        url = String.read(b)
        
        return BroadcastRevenueWithdrawalUrl(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()
