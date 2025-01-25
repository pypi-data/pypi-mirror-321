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


class UpdateBotPurchasedPaidMedia(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``196``
        - ID: ``283BD312``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        payload (``str``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "payload", "qts"]

    ID = 0x283bd312
    QUALNAME = "types.UpdateBotPurchasedPaidMedia"

    def __init__(self, *, user_id: int, payload: str, qts: int) -> None:
        self.user_id = user_id  # long
        self.payload = payload  # string
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotPurchasedPaidMedia":
        # No flags
        
        user_id = Long.read(b)
        
        payload = String.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotPurchasedPaidMedia(user_id=user_id, payload=payload, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.payload))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
