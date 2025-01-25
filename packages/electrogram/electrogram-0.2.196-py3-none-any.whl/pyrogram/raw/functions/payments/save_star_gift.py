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


class SaveStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``196``
        - ID: ``92FD2AAE``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        unsave (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["msg_id", "unsave"]

    ID = 0x92fd2aae
    QUALNAME = "functions.payments.SaveStarGift"

    def __init__(self, *, msg_id: int, unsave: Optional[bool] = None) -> None:
        self.msg_id = msg_id  # int
        self.unsave = unsave  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveStarGift":
        
        flags = Int.read(b)
        
        unsave = True if flags & (1 << 0) else False
        msg_id = Int.read(b)
        
        return SaveStarGift(msg_id=msg_id, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unsave else 0
        b.write(Int(flags))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
