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


class StarGiftUnique(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGift`.

    Details:
        - Layer: ``196``
        - ID: ``6A1407CD``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        num (``int`` ``32-bit``):
            N/A

        owner_id (``int`` ``64-bit``):
            N/A

        attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`):
            N/A

        availability_issued (``int`` ``32-bit``):
            N/A

        availability_total (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "title", "num", "owner_id", "attributes", "availability_issued", "availability_total"]

    ID = 0x6a1407cd
    QUALNAME = "types.StarGiftUnique"

    def __init__(self, *, id: int, title: str, num: int, owner_id: int, attributes: List["raw.base.StarGiftAttribute"], availability_issued: int, availability_total: int) -> None:
        self.id = id  # long
        self.title = title  # string
        self.num = num  # int
        self.owner_id = owner_id  # long
        self.attributes = attributes  # Vector<StarGiftAttribute>
        self.availability_issued = availability_issued  # int
        self.availability_total = availability_total  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUnique":
        # No flags
        
        id = Long.read(b)
        
        title = String.read(b)
        
        num = Int.read(b)
        
        owner_id = Long.read(b)
        
        attributes = TLObject.read(b)
        
        availability_issued = Int.read(b)
        
        availability_total = Int.read(b)
        
        return StarGiftUnique(id=id, title=title, num=num, owner_id=owner_id, attributes=attributes, availability_issued=availability_issued, availability_total=availability_total)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        b.write(Int(self.num))
        
        b.write(Long(self.owner_id))
        
        b.write(Vector(self.attributes))
        
        b.write(Int(self.availability_issued))
        
        b.write(Int(self.availability_total))
        
        return b.getvalue()
