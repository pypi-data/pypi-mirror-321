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


class GetTimezonesList(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``196``
        - ID: ``49B30240``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the help.timezonesList.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`help.TimezonesList <pyrogram.raw.base.help.TimezonesList>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x49b30240
    QUALNAME = "functions.help.GetTimezonesList"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTimezonesList":
        # No flags
        
        hash = Int.read(b)
        
        return GetTimezonesList(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()
