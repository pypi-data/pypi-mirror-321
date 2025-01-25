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


class GetUserStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``196``
        - ID: ``B502E4A5``

    Parameters:
        msg_id (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`payments.UserStarGifts <pyrogram.raw.base.payments.UserStarGifts>`
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0xb502e4a5
    QUALNAME = "functions.payments.GetUserStarGift"

    def __init__(self, *, msg_id: List[int]) -> None:
        self.msg_id = msg_id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserStarGift":
        # No flags
        
        msg_id = TLObject.read(b, Int)
        
        return GetUserStarGift(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.msg_id, Int))
        
        return b.getvalue()
