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


class CreateConferenceCall(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``196``
        - ID: ``DFC909AB``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            N/A

        key_fingerprint (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "key_fingerprint"]

    ID = 0xdfc909ab
    QUALNAME = "functions.phone.CreateConferenceCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", key_fingerprint: int) -> None:
        self.peer = peer  # InputPhoneCall
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateConferenceCall":
        # No flags
        
        peer = TLObject.read(b)
        
        key_fingerprint = Long.read(b)
        
        return CreateConferenceCall(peer=peer, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.key_fingerprint))
        
        return b.getvalue()
