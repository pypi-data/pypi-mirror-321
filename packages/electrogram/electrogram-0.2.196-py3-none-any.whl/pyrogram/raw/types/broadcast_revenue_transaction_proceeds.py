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


class BroadcastRevenueTransactionProceeds(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BroadcastRevenueTransaction`.

    Details:
        - Layer: ``196``
        - ID: ``557E2CC4``

    Parameters:
        amount (``int`` ``64-bit``):
            

        from_date (``int`` ``32-bit``):
            

        to_date (``int`` ``32-bit``):
            

    """

    __slots__: List[str] = ["amount", "from_date", "to_date"]

    ID = 0x557e2cc4
    QUALNAME = "types.BroadcastRevenueTransactionProceeds"

    def __init__(self, *, amount: int, from_date: int, to_date: int) -> None:
        self.amount = amount  # long
        self.from_date = from_date  # int
        self.to_date = to_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueTransactionProceeds":
        # No flags
        
        amount = Long.read(b)
        
        from_date = Int.read(b)
        
        to_date = Int.read(b)
        
        return BroadcastRevenueTransactionProceeds(amount=amount, from_date=from_date, to_date=to_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.amount))
        
        b.write(Int(self.from_date))
        
        b.write(Int(self.to_date))
        
        return b.getvalue()
