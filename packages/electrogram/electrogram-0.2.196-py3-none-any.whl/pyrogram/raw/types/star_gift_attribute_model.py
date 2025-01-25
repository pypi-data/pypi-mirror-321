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


class StarGiftAttributeModel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``196``
        - ID: ``39D99013``

    Parameters:
        name (``str``):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        rarity_permille (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["name", "document", "rarity_permille"]

    ID = 0x39d99013
    QUALNAME = "types.StarGiftAttributeModel"

    def __init__(self, *, name: str, document: "raw.base.Document", rarity_permille: int) -> None:
        self.name = name  # string
        self.document = document  # Document
        self.rarity_permille = rarity_permille  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeModel":
        # No flags
        
        name = String.read(b)
        
        document = TLObject.read(b)
        
        rarity_permille = Int.read(b)
        
        return StarGiftAttributeModel(name=name, document=document, rarity_permille=rarity_permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        b.write(self.document.write())
        
        b.write(Int(self.rarity_permille))
        
        return b.getvalue()
