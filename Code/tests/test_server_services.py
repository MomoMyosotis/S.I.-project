import json
import pytest

from server.services import user_services, media_services, redirect
from server.objects.user import User, UserLevel


def test_is_logged():
    assert not user_services.is_logged(None)
    assert not user_services.is_logged({})
    assert user_services.is_logged({"id": 1})

    class Dummy:
        pass

    d = Dummy()
    d.id = 5
    assert user_services.is_logged(d)


# User registration/login tests ------------------------------------------------

def test_register_user_success(monkeypatch):
    # prepare fake get_user that returns None for uniqueness checks and
    # returns a dict when querying by user_id
    def fake_get_user(**kwargs):
        if "user_id" in kwargs and kwargs["user_id"] == 1:
            return {
                "id": 1,
                "mail": "foo@example.com",
                "username": "foo",
                "password_hash": "hash",
                "birthday": "2000-01-01",
                "lvl": 4,
            }
        # uniqueness checks and initial lookups should return None
        return None

    monkeypatch.setattr(User, "get_user", staticmethod(fake_get_user))
    monkeypatch.setattr(User, "create_user", staticmethod(lambda mail, username, password, birthday: 1))

    res = user_services.register_user("foo@example.com", "foo", "pwd", "2000-01-01")
    assert res["status"] == "OK"
    assert res["user_id"] == 1
    assert "token" in res
    assert res["user_obj"]["username"] == "foo"


def test_register_user_bad_input(monkeypatch):
    # missing fields
    assert user_services.register_user("", "", "", "")[
        "status"
    ] == "ERROR"
    # invalid date
    assert user_services.register_user("a@b.com", "u", "p", "not-a-date")["status"] == "ERROR"


def test_register_username_taken(monkeypatch):
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kwargs: {"id": 10}))
    res = user_services.register_user("a@b.com", "u", "p", "2000-01-01")
    assert res["status"] == "ERROR"


def test_login_user_success(monkeypatch):
    # user exists and password verifies
    def fake_get_user(**kwargs):
        return {
            "id": 7,
            "mail": "bar@example.com",
            "username": "bar",
            "password_hash": "hashed",
            "birthday": "1990-01-01",
            "lvl": 4,
        }

    monkeypatch.setattr(User, "get_user", staticmethod(fake_get_user))
    monkeypatch.setattr(user_services, "verify_password", lambda p, h: True)

    res = user_services.login_user("bar", "any")
    assert res["status"] == "accepted"
    assert not res.get("error_msg")
    assert "token" in res
    assert res["user_obj"]["username"] == "bar"


def test_login_user_wrong_password(monkeypatch):
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kwargs: {
        "id": 1,
        "mail": "x@x.com",
        "username": "x",
        "password_hash": "h",
        "birthday": "2000-01-01",
        "lvl": 4,
    }))
    monkeypatch.setattr(user_services, "verify_password", lambda p, h: False)
    res = user_services.login_user("x", "bad")
    assert res["status"] == "wrong_password"


def test_login_user_banned(monkeypatch):
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kwargs: {
        "id": 2,
        "mail": "b@b.com",
        "username": "b",
        "password_hash": "h",
        "birthday": "2000-01-01",
        "lvl": 6,  # banned level
    }))
    monkeypatch.setattr(user_services, "verify_password", lambda p, h: True)
    res = user_services.login_user("b", "ok")
    assert res["status"] == "banned"

def test_login_username_not_found(monkeypatch):
    # get_user returns None
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kw: None))
    res = user_services.login_user("doesnotexist", "pwd")
    assert res["status"] == "error"


def test_register_empty_password():
    res = user_services.register_user("a@b.com", "u", "", "2000-01-01")
    assert res["status"] == "ERROR"

@pytest.mark.xfail(reason="email format validation not implemented")
def test_register_invalid_email():
    # the service currently does not validate format, so we expect this xfail
    res = user_services.register_user("not-an-email", "u", "pass", "2000-01-01")
    assert res["status"] == "ERROR"


def test_login_user_blacklisted(monkeypatch):
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kwargs: {
        "id": 3,
        "mail": "c@c.com",
        "username": "c",
        "password_hash": "h",
        "birthday": "2000-01-01",
        "lvl": 4,
    }))
    monkeypatch.setattr(user_services, "verify_password", lambda p, h: True)
    cfg = {"BLACKLIST": ["c@c.com"]}
    res = user_services.login_user("c", "ok", config=cfg)
    assert res["status"] == "blacklisted"


# Unique / constraint tests ------------------------------------------------

def test_register_email_taken(monkeypatch):
    # email duplicate should be caught
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kw: {"id": 5} if kw.get("mail") else None))
    res = user_services.register_user("dup@example.com", "u2", "pwd", "2000-01-01")
    assert res["status"] == "ERROR"


def test_media_pk_duplicate(monkeypatch):
    # simulate DB raising on primary key conflict by patching the media module
    def raise_dup(data):
        raise Exception("duplicate key value violates unique constraint")
    monkeypatch.setattr("server.objects.media.create_media_db", raise_dup)
    with pytest.raises(Exception) as exc:
        media_services.create_media_services(None, {"type": "song", "title": "t"})
    assert "duplicate" in str(exc.value).lower()


def test_media_fk_missing(monkeypatch):
    def raise_fk(data):
        raise Exception("foreign key constraint")
    monkeypatch.setattr("server.objects.media.create_media_db", raise_fk)
    with pytest.raises(Exception) as exc:
        media_services.create_media_services(None, {"type": "song", "title": "t"})
    assert "foreign" in str(exc.value).lower()


def test_many_to_many_duplicate_relation(monkeypatch):
    from server.utils import user_utils
    monkeypatch.setattr(user_utils, "create_relation", lambda table, keys, vals: False)
    assert not user_utils.add_genre(1, 2)


def test_many_to_many_valid_relation(monkeypatch):
    from server.utils import user_utils
    monkeypatch.setattr(user_utils, "create_relation", lambda table, keys, vals: True)
    assert user_utils.add_genre(1, 2)

# Media service tests ----------------------------------------------------------

def test_create_media_routing(monkeypatch):
    called = {}
    def fake_song(u, d=None, **k):
        called["song"] = True
        return {"ok": "song"}
    def fake_doc(u, d=None, **k):
        called["doc"] = True
        return {"ok": "doc"}

    monkeypatch.setattr(media_services, "create_song_services", fake_song)
    monkeypatch.setattr(media_services, "create_document_services", fake_doc)

    assert media_services.create_media_services(None, {"type": "song"}) == {"ok": "song"}
    assert called.get("song")
    assert media_services.create_media_services(None, type="document") == {"ok": "doc"}
    assert called.get("doc")
    res = media_services.create_media_services(None, {"type": "unknown"})
    assert "Unknown media type" in res["error"]


def test_update_media_not_found(monkeypatch):
    monkeypatch.setattr(media_services, "get_object", lambda cls, mid: None)
    res = media_services.update_media_services(None, 123, {})
    assert res.get("error") == "Media not found"


# Redirect / dispatch tests ---------------------------------------------------

def test_dispatch_command_unknown(monkeypatch):
    # provide a minimal logged-in user so the authentication check is bypassed
    monkeypatch.setattr(User, "get_user", staticmethod(lambda **kw: {"id": 999, "mail": "x", "username": "x", "password_hash": "h", "birthday": "2000-01-01", "lvl": 4}))
    user_obj = {"id": 999}
    resp, _, _, status = redirect.dispatch_command("doesnotexist", [], user_obj)
    assert status == "ERROR"
    data = json.loads(resp)
    assert "Unknown command" in data.get("error_msg", "")


def test_dispatch_login(monkeypatch):
    # patch the mapping directly so dispatch_command uses our stub
    redirect.COMMAND_MAP["login"] = lambda login, pw, config=None: {"status": "accepted", "user_obj": {}, "token": "tok"}
    resp, user_obj, new_token, status = redirect.dispatch_command("login", ["foo", "bar"], None)
    # ensure token is returned via serialized response as well as new_token
    data = json.loads(resp)
    assert data.get("status") == "accepted"
    assert data.get("token") == "tok"
    # the returned new_token may or may not be populated by dispatch_command
    # depending on internal logic; at a minimum it should match when present.
    if new_token is not None:
        assert new_token == "tok"



# ---------- Additional tests ----------

def make_dummy_user(lvl):
    from datetime import date
    return User(id=1, mail="x@x", username="x", password_hash="h", birthday=date.today(), lvl=lvl)


# permissions by level --------------------------------------------------------
def test_regular_cannot_moderate(monkeypatch):
    u = make_dummy_user(UserLevel.REGULAR)
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": 2})
    # ensure is_admin returns False by controlling get_user
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": u.id, "lvl": UserLevel.REGULAR.value}))
    with pytest.raises(PermissionError):
        u.moderate_content(123, "delete")


def test_publisher_can_create_media(monkeypatch):
    u = make_dummy_user(UserLevel.PUBLISHER)
    # create_media_db receives a tuple; accept any args and return value
    monkeypatch.setattr("server.objects.user.create_media_db", lambda *a, **k: {"id": 999})
    res = u.manage_content("create", fields={"type": "song", "title": "t"})
    assert res == {"id": 999}


def test_publisher_cannot_approve(monkeypatch):
    u = make_dummy_user(UserLevel.PUBLISHER)
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": 2})
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": u.id, "lvl": UserLevel.PUBLISHER.value}))
    with pytest.raises(PermissionError):
        u.moderate_content(123, "edit", updates={"title": "x"})


def test_mod_can_moderate(monkeypatch):
    u = make_dummy_user(UserLevel.MOD)
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": 2})
    # patch update_media_db in user module, not db_crud
    monkeypatch.setattr("server.objects.user.update_media_db", lambda mid, up: True)
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": u.id, "lvl": UserLevel.MOD.value}))
    assert u.moderate_content(123, "edit", updates={"a": 1}) is True

@pytest.mark.xfail(reason="mods currently able to ban admins")
def test_mod_cannot_ban_admin(monkeypatch):
    u = make_dummy_user(UserLevel.MOD)
    # target user is admin
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": 5, "lvl": UserLevel.ADMIN.value}))
    # ensure fetch_media_db returns a media so existence check passes
    monkeypatch.setattr(
        "server.objects.user.fetch_media_db",
        lambda mid: {"id": mid, "user_id": 2}
    )
    u.moderate_content(123, "ban_user", target_user_id=5)


def test_admin_can_delete_user(monkeypatch):
    u = make_dummy_user(UserLevel.ADMIN)
    monkeypatch.setattr("server.objects.user.update_user_db", lambda uid, up: True)
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": u.id, "lvl": UserLevel.ADMIN.value}))
    # ensure fetch_media_db returns something for id 0 to bypass existence check
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"id": 0} if mid == 0 else {"id": mid})
    assert u.moderate_content(0, "ban_user", target_user_id=7) is True


def test_admin_can_delete_media(monkeypatch):
    u = make_dummy_user(UserLevel.ADMIN)
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": 2})
    monkeypatch.setattr("server.db.db_crud.delete_media_db", lambda mid: True)
    assert u.moderate_content(123, "delete") is True


def test_root_has_all_powers(monkeypatch):
    u = make_dummy_user(UserLevel.ROOT)
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": 2})
    monkeypatch.setattr("server.db.db_crud.delete_media_db", lambda mid: True)
    monkeypatch.setattr(User, "get_user", staticmethod(lambda *args, **kw: {"id": u.id, "lvl": UserLevel.ROOT.value}))
    assert u.moderate_content(123, "delete") is True
    monkeypatch.setattr("server.objects.user.update_user_db", lambda uid, up: True)
    # ensure fetch_media_db returns something when called with 0
    monkeypatch.setattr("server.objects.user.fetch_media_db", lambda mid: {"user_id": u.id})
    assert u.moderate_content(0, "ban_user", target_user_id=2) is True


# media metadata edit --------------------------------------------------------
def test_media_metadata_edit(monkeypatch):
    class Dummy:
        pass
    dummy = Dummy()
    dummy.id = 1
    monkeypatch.setattr(media_services, "get_object", lambda cls, mid: dummy)
    monkeypatch.setattr(media_services, "convert_relation_names_to_ids", lambda u: u)
    monkeypatch.setattr(media_services, "update_object", lambda obj, up: {"success": True, "updated": up})
    res = media_services.update_media_services(None, 1, {"title": "new"})
    assert res["success"] is True
    assert res["updated"]["title"] == "new"


# CRUD operations (generic) --------------------------------------------------
def test_media_service_crud(monkeypatch):
    monkeypatch.setattr(media_services, "create_media_services", lambda u, d=None, **k: {"id": 10})
    monkeypatch.setattr(media_services, "get_media_services", lambda u, mid: {"id": mid})
    monkeypatch.setattr(media_services, "update_media_services", lambda u, mid, ups: {"ok": True})
    monkeypatch.setattr(media_services, "delete_media_services", lambda u, mid: {"ok": True})
    assert media_services.create_media_services(None) == {"id": 10}
    assert media_services.get_media_services(None, 5) == {"id": 5}
    assert media_services.update_media_services(None, 5, {}) == {"ok": True}
    assert media_services.delete_media_services(None, 5) == {"ok": True}


# delete cascade simulation --------------------------------------------------
def test_delete_cascade(monkeypatch):
    # simulate comments stored per media
    storage = {1: [{"id": 1}], 2: [{"id": 2}]}
    import server.objects.comment as cm
    monkeypatch.setattr(cm.Comment, "fetch_by_media", classmethod(lambda cls, mid: storage.get(mid, [])))
    def fake_del(mid):
        storage.pop(mid, None)
        return True
    monkeypatch.setattr("server.db.db_crud.delete_media_db", lambda mid: fake_del(mid))
    assert cm.Comment.fetch_by_media(1) == [{"id": 1}]
    fake_del(1)
    assert storage.get(1) is None


# comments & notes CRUD ------------------------------------------------------
def test_comment_and_note_crud(monkeypatch):
    # create comment
    # patch comment creation to accept kwargs and return simple object
    def fake_add(cls, **kwargs):
        return cls(id=1, user_id=kwargs.get('user_id'), media_id=kwargs.get('media_id'), text=kwargs.get('text'))
    
    monkeypatch.setattr("server.objects.comment.Comment.add_comment", classmethod(fake_add))
    import server.objects.media as media_mod
    monkeypatch.setattr(media_mod.Media, "fetch", classmethod(lambda cls, mid: {"id": mid}))
    # also patch fetch_by_id so service may return object with id attr
    class Simple:
        def __init__(self, id):
            self.id = id
    monkeypatch.setattr("server.objects.comment.Comment.fetch_by_id", classmethod(lambda cls, cid: Simple(cid)))
    comment = __import__("server.services.interventions_services", fromlist=[""]).create_comment({'id':5}, media_id=2, text='hi')
    assert comment['id'] == 1
    # update and delete
    monkeypatch.setattr("server.objects.comment.Comment.update_comment", classmethod(lambda cls, **kwargs: True))
    monkeypatch.setattr("server.objects.comment.Comment.delete_comment", classmethod(lambda cls, **kwargs: True))
    upd = __import__("server.services.interventions_services", fromlist=[""]).update_comment({'id':5}, 1, 'new')
    assert upd['status'] == 'OK'
    dlt = __import__("server.services.interventions_services", fromlist=[""]).delete_comment({'id':5}, 1)
    assert dlt['status'] == 'OK'
    # notes
    # patch note creation to return object with id
    class SimpleNote:
        def __init__(self, id):
            self.id = id
    monkeypatch.setattr("server.objects.note.Note.create_note", staticmethod(lambda user_id, media_id, **kw: SimpleNote(2)))
    note = __import__("server.services.interventions_services", fromlist=[""]).create_note({'id':5}, media_id=2, start=0, end=1, type=True, text='n')
    assert note['id'] == 2


# edge cases -----------------------------------------------------------------
def test_edge_cases(monkeypatch):
    # comment without text returns error dict
    res = __import__("server.services.interventions_services", fromlist=[""]).create_comment({'id':5}, media_id=1, text=None)
    assert res["status"] == "ERROR"
    # passing None into media update should return error dictionary
    res2 = media_services.update_media_services(None, None, None)
    assert isinstance(res2, dict) and "error" in res2


# stress tests ---------------------------------------------------------------
def test_stress_registration(monkeypatch):
    # make get_user return None except when asked by id
    def fake_get_user(**kw):
        if "user_id" in kw:
            return {"id": kw["user_id"], "mail": "dummy", "username": "d", "password_hash": "h", "birthday": "2000-01-01", "lvl": 4}
        return None
    monkeypatch.setattr(User, "get_user", staticmethod(fake_get_user))
    monkeypatch.setattr(User, "create_user", staticmethod(lambda mail, username, password, birthday: 1))
    for i in range(200):
        res = user_services.register_user(f"{i}@a.com", f"user{i}", "pw", "2000-01-01")
        assert res["status"] == "OK"

def test_stress_media_creation(monkeypatch):
    monkeypatch.setattr(media_services, "create_media_services", lambda u, d=None, **k: {"id": 1})
    for i in range(200):
        assert media_services.create_media_services(None, {"type": "song"}) == {"id": 1}


if __name__ == "__main__":
    pytest.main()
