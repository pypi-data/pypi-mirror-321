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


class ConvertStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``196``
        - ID: ``72770C83``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0x72770c83
    QUALNAME = "functions.payments.ConvertStarGift"

    def __init__(self, *, msg_id: int) -> None:
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConvertStarGift":
        # No flags
        
        msg_id = Int.read(b)
        
        return ConvertStarGift(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
