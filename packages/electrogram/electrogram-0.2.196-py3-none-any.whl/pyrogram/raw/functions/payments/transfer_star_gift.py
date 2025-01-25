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


class TransferStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``196``
        - ID: ``333FB526``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        to_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["msg_id", "to_id"]

    ID = 0x333fb526
    QUALNAME = "functions.payments.TransferStarGift"

    def __init__(self, *, msg_id: int, to_id: "raw.base.InputUser") -> None:
        self.msg_id = msg_id  # int
        self.to_id = to_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TransferStarGift":
        # No flags
        
        msg_id = Int.read(b)
        
        to_id = TLObject.read(b)
        
        return TransferStarGift(msg_id=msg_id, to_id=to_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(self.to_id.write())
        
        return b.getvalue()
