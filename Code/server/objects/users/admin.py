# first line

# admin.py
from typing import Optional
from datetime import date, datetime
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
        lvl: UserLevel = UserLevel.ADMIN
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    def get_permissions(self):
        return ["manage_content",
                "moderate_content",
                "edit_user",
                "remove_user",
                "access_advanced_search"]

    # =====================
    # METODI DI AMMINISTRAZIONE / CONTENT
    # =====================
    def manage_content(self, content_id: Optional[int] = None):
        print(f"{self.username} can manage content {f'with ID {content_id}' if content_id else ''}.")

    def moderate_content(self, content_id: Optional[int] = None):
        print(f"{self.username} can moderate content {f'with ID {content_id}' if content_id else ''}.")

    def access_all_content(self) -> bool:
        return True

    def edit_user(self, user_id: int, updates: dict):
        success = super().update_user(user_id, updates)
        if success:
            print(f"{self.username} updated user {user_id}.")
        else:
            print(f"Failed to update user {user_id}.")

    def remove_user(self, user_id: int):
        success = super().delete_user(user_id)
        if success:
            print(f"{self.username} removed user {user_id}.")
        else:
            print(f"Failed to remove user {user_id}.")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Admin"]:
        if not data:
            return None
        birthday = data.get("birthday")
        if isinstance(birthday, str):
            birthday = datetime.fromisoformat(birthday).date()
        return cls(
            id=data.get("id"),
            mail=data.get("mail"),
            username=data.get("username"),
            password_hash=data.get("password_hash"),
            birthday=birthday,
            bio=data.get("bio", ""),
            profile_pic=data.get("profile_pic"),
            lvl=UserLevel(data.get("lvl", UserLevel.ADMIN.value))
        )

# last line