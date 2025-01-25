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


class PhoneCallDiscardReasonAllowGroupCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``196``
        - ID: ``AFE2B839``

    Parameters:
        encrypted_key (``bytes``):
            N/A

    """

    __slots__: List[str] = ["encrypted_key"]

    ID = 0xafe2b839
    QUALNAME = "types.PhoneCallDiscardReasonAllowGroupCall"

    def __init__(self, *, encrypted_key: bytes) -> None:
        self.encrypted_key = encrypted_key  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonAllowGroupCall":
        # No flags
        
        encrypted_key = Bytes.read(b)
        
        return PhoneCallDiscardReasonAllowGroupCall(encrypted_key=encrypted_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.encrypted_key))
        
        return b.getvalue()
