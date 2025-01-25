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


class GetSavedDialogs(TLObject):  # type: ignore
    """Returns the current saved dialog list, see here » for more info.


    Details:
        - Layer: ``196``
        - ID: ``5381D21A``

    Parameters:
        offset_date (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here (top_message ID used for pagination)

        offset_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Offset peer for pagination

        limit (``int`` ``32-bit``):
            Number of list elements to be returned

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        exclude_pinned (``bool``, *optional*):
            Exclude pinned dialogs

    Returns:
        :obj:`messages.SavedDialogs <pyrogram.raw.base.messages.SavedDialogs>`
    """

    __slots__: List[str] = ["offset_date", "offset_id", "offset_peer", "limit", "hash", "exclude_pinned"]

    ID = 0x5381d21a
    QUALNAME = "functions.messages.GetSavedDialogs"

    def __init__(self, *, offset_date: int, offset_id: int, offset_peer: "raw.base.InputPeer", limit: int, hash: int, exclude_pinned: Optional[bool] = None) -> None:
        self.offset_date = offset_date  # int
        self.offset_id = offset_id  # int
        self.offset_peer = offset_peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # long
        self.exclude_pinned = exclude_pinned  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedDialogs":
        
        flags = Int.read(b)
        
        exclude_pinned = True if flags & (1 << 0) else False
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_peer = TLObject.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetSavedDialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash, exclude_pinned=exclude_pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_pinned else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
