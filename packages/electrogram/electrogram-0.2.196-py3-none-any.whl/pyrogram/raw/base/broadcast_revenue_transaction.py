# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BroadcastRevenueTransaction = Union["raw.types.BroadcastRevenueTransactionProceeds", "raw.types.BroadcastRevenueTransactionRefund", "raw.types.BroadcastRevenueTransactionWithdrawal"]


class BroadcastRevenueTransaction:  # type: ignore
    """

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BroadcastRevenueTransactionProceeds
            BroadcastRevenueTransactionRefund
            BroadcastRevenueTransactionWithdrawal
    """

    QUALNAME = "pyrogram.raw.base.BroadcastRevenueTransaction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
