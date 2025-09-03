# first line

from typing import Optional, List
from datetime import date
from server.objects.users.root import Root, UserLevel

class Admin(Root):
    def __init__(
        self,
        id: int,
        mail: str,
        username: str,
        password_hash: str,
        birthday: date,
        bio: Optional[str] = "",
        profile_pic: Optional[str] = None,
        followers: Optional[List[int]] = None,
        followed: Optional[List[int]] = None,
        lvl: UserLevel = UserLevel.ADMIN
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

    def get_permissions(self) -> List[str]:
        return ["manage_content", "moderate_content", "edit_user", "remove_user", "access_advanced_search"]

    def can_post_content(self) -> bool:
        return True

    # =====================
    # METODI DI AMMINISTRAZIONE REALE
    # =====================
    def manage_content(self):
        print(f"{self.username} can manage content (upload/edit/delete).")
        # qui puoi aggiungere logica reale di gestione contenuti

    def moderate_content(self):
        print(f"{self.username} can moderate content.")
        # logica reale di moderazione

    def edit_user(self, user_id: int, updates: dict):
        if self.is_admin(self.id):
            success = self.update_user(user_id, updates)
            if success:
                print(f"{self.username} updated user {user_id}.")
            else:
                print(f"Failed to update user {user_id}.")
        else:
            raise PermissionError("Solo admin può modificare utenti.")

    def remove_user(self, user_id: int):
        if self.is_admin(self.id):
            success = self.delete_user(user_id)
            if success:
                print(f"{self.username} removed user {user_id}.")
            else:
                print(f"Failed to remove user {user_id}.")
        else:
            raise PermissionError("Solo admin può rimuovere utenti.")

    def access_all_content(self):
        print(f"{self.username} can access own and moderatable content.")
        # qui puoi aggiungere logica reale per accedere a contenuti

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Admin"]:
        if not data:
            return None
        birthday = data.get("birthday")
        # Converti stringa in date se serve
        if isinstance(birthday, str):
            from datetime import datetime
            birthday = datetime.fromisoformat(birthday).date()
        return cls(
            id=data.get("id"),
            mail=data.get("mail"),
            username=data.get("username"),
            password_hash=data.get("password_hash"),
            birthday=birthday,
            bio=data.get("bio", ""),
            profile_pic=data.get("profile_pic"),
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.ADMIN.value))
        )

# last line