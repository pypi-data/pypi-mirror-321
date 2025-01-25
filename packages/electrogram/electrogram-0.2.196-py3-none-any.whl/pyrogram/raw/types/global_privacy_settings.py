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


class GlobalPrivacySettings(TLObject):  # type: ignore
    """Global privacy settings

    Constructor of :obj:`~pyrogram.raw.base.GlobalPrivacySettings`.

    Details:
        - Layer: ``196``
        - ID: ``734C4CCB``

    Parameters:
        archive_and_mute_new_noncontact_peers (``bool``, *optional*):
            Whether to archive and mute new chats from non-contacts

        keep_archived_unmuted (``bool``, *optional*):
            Whether unmuted chats will be kept in the Archive chat list when they get a new message.

        keep_archived_folders (``bool``, *optional*):
            Whether unmuted chats that are always included or pinned in a folder, will be kept in the Archive chat list when they get a new message. Ignored if keep_archived_unmuted is set.

        hide_read_marks (``bool``, *optional*):
            

        new_noncontact_peers_require_premium (``bool``, *optional*):
            

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetGlobalPrivacySettings
            account.SetGlobalPrivacySettings
    """

    __slots__: List[str] = ["archive_and_mute_new_noncontact_peers", "keep_archived_unmuted", "keep_archived_folders", "hide_read_marks", "new_noncontact_peers_require_premium"]

    ID = 0x734c4ccb
    QUALNAME = "types.GlobalPrivacySettings"

    def __init__(self, *, archive_and_mute_new_noncontact_peers: Optional[bool] = None, keep_archived_unmuted: Optional[bool] = None, keep_archived_folders: Optional[bool] = None, hide_read_marks: Optional[bool] = None, new_noncontact_peers_require_premium: Optional[bool] = None) -> None:
        self.archive_and_mute_new_noncontact_peers = archive_and_mute_new_noncontact_peers  # flags.0?true
        self.keep_archived_unmuted = keep_archived_unmuted  # flags.1?true
        self.keep_archived_folders = keep_archived_folders  # flags.2?true
        self.hide_read_marks = hide_read_marks  # flags.3?true
        self.new_noncontact_peers_require_premium = new_noncontact_peers_require_premium  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GlobalPrivacySettings":
        
        flags = Int.read(b)
        
        archive_and_mute_new_noncontact_peers = True if flags & (1 << 0) else False
        keep_archived_unmuted = True if flags & (1 << 1) else False
        keep_archived_folders = True if flags & (1 << 2) else False
        hide_read_marks = True if flags & (1 << 3) else False
        new_noncontact_peers_require_premium = True if flags & (1 << 4) else False
        return GlobalPrivacySettings(archive_and_mute_new_noncontact_peers=archive_and_mute_new_noncontact_peers, keep_archived_unmuted=keep_archived_unmuted, keep_archived_folders=keep_archived_folders, hide_read_marks=hide_read_marks, new_noncontact_peers_require_premium=new_noncontact_peers_require_premium)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.archive_and_mute_new_noncontact_peers else 0
        flags |= (1 << 1) if self.keep_archived_unmuted else 0
        flags |= (1 << 2) if self.keep_archived_folders else 0
        flags |= (1 << 3) if self.hide_read_marks else 0
        flags |= (1 << 4) if self.new_noncontact_peers_require_premium else 0
        b.write(Int(flags))
        
        return b.getvalue()
