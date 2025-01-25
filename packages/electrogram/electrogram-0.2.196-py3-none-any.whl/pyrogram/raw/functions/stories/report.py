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


class Report(TLObject):  # type: ignore
    """Report a story.


    Details:
        - Layer: ``196``
        - ID: ``19D8EB45``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer that uploaded the story.

        id (List of ``int`` ``32-bit``):
            IDs of the stories to report.

        option (``bytes``):
            N/A

        message (``str``):
            Comment for report moderation

    Returns:
        :obj:`ReportResult <pyrogram.raw.base.ReportResult>`
    """

    __slots__: List[str] = ["peer", "id", "option", "message"]

    ID = 0x19d8eb45
    QUALNAME = "functions.stories.Report"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], option: bytes, message: str) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.option = option  # bytes
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Report":
        # No flags
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        option = Bytes.read(b)
        
        message = String.read(b)
        
        return Report(peer=peer, id=id, option=option, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(Bytes(self.option))
        
        b.write(String(self.message))
        
        return b.getvalue()
