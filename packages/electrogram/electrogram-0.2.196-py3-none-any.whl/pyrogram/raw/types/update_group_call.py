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


class UpdateGroupCall(TLObject):  # type: ignore
    """A new groupcall was started

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``196``
        - ID: ``97D64341``

    Parameters:
        call (:obj:`GroupCall <pyrogram.raw.base.GroupCall>`):
            Info about the group call or livestream

        chat_id (``int`` ``64-bit``, *optional*):
            The channel/supergroup where this group call or livestream takes place

    """

    __slots__: List[str] = ["call", "chat_id"]

    ID = 0x97d64341
    QUALNAME = "types.UpdateGroupCall"

    def __init__(self, *, call: "raw.base.GroupCall", chat_id: Optional[int] = None) -> None:
        self.call = call  # GroupCall
        self.chat_id = chat_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCall":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b) if flags & (1 << 0) else None
        call = TLObject.read(b)
        
        return UpdateGroupCall(call=call, chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chat_id is not None else 0
        b.write(Int(flags))
        
        if self.chat_id is not None:
            b.write(Long(self.chat_id))
        
        b.write(self.call.write())
        
        return b.getvalue()
