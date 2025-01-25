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


class InputInvoiceStarGiftUpgrade(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``196``
        - ID: ``5EBE7262``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        keep_original_details (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["msg_id", "keep_original_details"]

    ID = 0x5ebe7262
    QUALNAME = "types.InputInvoiceStarGiftUpgrade"

    def __init__(self, *, msg_id: int, keep_original_details: Optional[bool] = None) -> None:
        self.msg_id = msg_id  # int
        self.keep_original_details = keep_original_details  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftUpgrade":
        
        flags = Int.read(b)
        
        keep_original_details = True if flags & (1 << 0) else False
        msg_id = Int.read(b)
        
        return InputInvoiceStarGiftUpgrade(msg_id=msg_id, keep_original_details=keep_original_details)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.keep_original_details else 0
        b.write(Int(flags))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
