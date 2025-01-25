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


class StarGiftUpgradePreview(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftUpgradePreview`.

    Details:
        - Layer: ``196``
        - ID: ``167BD90B``

    Parameters:
        sample_attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftUpgradePreview
    """

    __slots__: List[str] = ["sample_attributes"]

    ID = 0x167bd90b
    QUALNAME = "types.payments.StarGiftUpgradePreview"

    def __init__(self, *, sample_attributes: List["raw.base.StarGiftAttribute"]) -> None:
        self.sample_attributes = sample_attributes  # Vector<StarGiftAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradePreview":
        # No flags
        
        sample_attributes = TLObject.read(b)
        
        return StarGiftUpgradePreview(sample_attributes=sample_attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.sample_attributes))
        
        return b.getvalue()
