
C:\Users\LENOVO\Desktop\prj\I.S\Code\server>python ft.py

=== REGISTER / LOGIN ===
[DEBUG][dispatch_command] START - command=register_user, args=['quackerina7550@example.com', 'quackerina7550', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(340, 'quackerina7550@example.com', 'quackerina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(340, 'quackerina7550@example.com', 'quackerina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.6792s
[DEBUG][register_user] ARGS=['quackerina7550@example.com', 'quackerina7550', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 340, "user_obj": {"id": 340, "username": "quackerina7550", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "6169401bf1f32380ffdbf938e513b0e1"}

[DEBUG][dispatch_command] START - command=register_user, args=['bassettina7550@example.com', 'bassettina7550', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.5455s
[DEBUG][register_user] ARGS=['bassettina7550@example.com', 'bassettina7550', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=341, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 341, "user_obj": {"id": 341, "username": "bassettina7550", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "7814e0682a631b1d65de9f63826561fa"}

[DEBUG][dispatch_command] START - command=login_user, args=['quackerina7550', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(340, 'quackerina7550@example.com', 'quackerina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.0736s
[DEBUG][login_user] ARGS=['quackerina7550', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 340, "username": "quackerina7550", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "7dea5514fcdac9e8a7596eddde6c503d", "error_msg": null}

[DEBUG][dispatch_command] START - command=login_user, args=['bassettina7550', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.0731s
[DEBUG][login_user] ARGS=['bassettina7550', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=341, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 341, "username": "bassettina7550", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "cc98a39b517c3d5c463f51c58bd49d74", "error_msg": null}


=== FOLLOW / FOLLOWERS / FOLLOWED ===
[TEST] Follow user
[DEBUG][dispatch_command] START - command=follow_user, args=['bassettina7550'], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(340, 'quackerina7550@example.com', 'quackerina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s) (340, 341)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550', 'bassettina7550@example.com')]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][follow_user] STATUS=OK, TIME=1.1500s
[DEBUG][follow_user] ARGS=['bassettina7550']
[DEBUG][follow_user] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=1
[DEBUG][follow_user] RESPONSE="FOLLOWED"

[RESULT] After follow, user_obj: {'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}

[TEST] Get followed
[DEBUG][dispatch_command] START - command=get_followed, args=[], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}
[DEBUG] get_followed called with user_id=340 (type=<class 'int'>)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550', 'bassettina7550@example.com')]
[DEBUG] raw followed: [{'id': 341, 'username': 'bassettina7550', 'mail': 'bassettina7550@example.com'}]
[DEBUG][get_followed] STATUS=OK, TIME=0.1764s
[DEBUG][get_followed] ARGS=[]
[DEBUG][get_followed] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=1
[DEBUG][get_followed] RESPONSE=[{"id": 341, "username": "bassettina7550", "mail": "bassettina7550@example.com"}]

[RESULT] Followed list: [{"id": 341, "username": "bassettina7550", "mail": "bassettina7550@example.com"}]

[TEST] Get followers (as None user)
[DEBUG][dispatch_command] START - command=get_followers, args=[], user_obj=None
[DEBUG][get_followers] STATUS=OK, TIME=0.0016s
[DEBUG][get_followers] ARGS=[]
[DEBUG][get_followers] USER_OBJ=None
[DEBUG][get_followers] RESPONSE={"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": null}

[RESULT] Followers list: {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": null}

[TEST] Unfollow user
[DEBUG][dispatch_command] START - command=unfollow_user, args=['bassettina7550'], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(340, 'quackerina7550@example.com', 'quackerina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(341, 'bassettina7550@example.com', 'bassettina7550', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM user_follow WHERE follower_id = %s AND followed_id = %s (340, 341)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][unfollow_user] STATUS=OK, TIME=1.1403s
[DEBUG][unfollow_user] ARGS=['bassettina7550']
[DEBUG][unfollow_user] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][unfollow_user] RESPONSE="UNFOLLOWED"

[RESULT] After unfollow, user_obj: {'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}


=== MEDIA CRUD ===
[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano neutro', 'year': 2020}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano neutro', 'year': 2020}
[DEBUG][create_object] cls=Song, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano neutro', 'year': 2020}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano neutro', 'year': 2020}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=None, year=2020, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano neutro>
[DEBUG][create_object] Object built from dict: <Song id=None, title=Brano neutro>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Song id=None, title=Brano neutro>
[DEBUG][Media.save] Called on <Song id=None, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=None, title=Brano neutro> -> {'media_id': None, 'type': 'song', 'title': 'Brano neutro', 'user_id': 340, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:31.446807', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano neutro', 'user_id': 340, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:31.446807', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=250
[DEBUG][Media.save] Result from create_media_db={'id': 250}
[DEBUG][Media.save] Assigned new media_id=250
[DEBUG][Media.save] Syncing relations for <Song id=250, title=Brano neutro>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (250,)
[DEBUG][Media.save] END for <Song id=250, title=Brano neutro>
[DEBUG][create_object] Object saved: <Song id=250, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=250, title=Brano neutro> -> {'media_id': 250, 'type': 'song', 'title': 'Brano neutro', 'user_id': 340, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:31.446807', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=2.1177s
[DEBUG][create_song] ARGS=[{'title': 'Brano neutro', 'year': 2020}]
[DEBUG][create_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_song] RESPONSE={"media_id": 250, "type": "song", "title": "Brano neutro", "user_id": 340, "year": 2020, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:31.446807", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false}

[DEBUG][dispatch_command] START - command=get_song, args=[250], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=250
[DEBUG][get_object] cls=Song, object_id=250
[DEBUG][Media.fetch] Called cls=Song, media_id=250
[DEBUG] fetch_one success: (250, 'song', 340, 'Brano neutro', 2020, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 250, 'type': 'song', 'user_id': 340, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 340, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), 'is_author': False, 'is_performer': False, 'media_id': 250}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=song, year=2020, user_id=340, kwargs={'recording_date': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Song id=250, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=250, title=Brano neutro>
[DEBUG][Media.fetch] Built object=<Song id=250, title=Brano neutro>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=250, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=250, title=Brano neutro> -> {'media_id': 250, 'type': 'song', 'title': 'Brano neutro', 'user_id': 340, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:31.535152', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=0.3676s
[DEBUG][get_song] ARGS=[250]
[DEBUG][get_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_song] RESPONSE={"media_id": 250, "type": "song", "title": "Brano neutro", "user_id": 340, "year": 2020, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:31.535152", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false}

[DEBUG][dispatch_command] START - command=delete_song, args=[250], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=250
[DEBUG][get_object] cls=Song, object_id=250
[DEBUG][Media.fetch] Called cls=Song, media_id=250
[DEBUG] fetch_one success: (250, 'song', 340, 'Brano neutro', 2020, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 250, 'type': 'song', 'user_id': 340, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 340, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 31, 535152), 'is_author': False, 'is_performer': False, 'media_id': 250}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=song, year=2020, user_id=340, kwargs={'recording_date': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Song id=250, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=250, title=Brano neutro>
[DEBUG][Media.fetch] Built object=<Song id=250, title=Brano neutro>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=250, title=Brano neutro>
[DEBUG][delete_object] Deleting object <Song id=250, title=Brano neutro>
[DEBUG][Media.delete] Called on <Song id=250, title=Brano neutro>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (250,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (250,)
[DEBUG][Media.delete] Deleted media_id=250
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano neutro>
[DEBUG][delete_song] STATUS=OK, TIME=4.2930s
[DEBUG][delete_song] ARGS=[250]
[DEBUG][delete_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_song] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano di riferimento'}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano di riferimento'}
[DEBUG][create_object] cls=Song, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano di riferimento'}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano di riferimento'}
[DEBUG][Media.__init__] Called with title=Brano di riferimento, type=None, year=None, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano di riferimento>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano di riferimento>
[DEBUG][create_object] Object built from dict: <Song id=None, title=Brano di riferimento>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Song id=None, title=Brano di riferimento>
[DEBUG][Media.save] Called on <Song id=None, title=Brano di riferimento>
[DEBUG][Media.to_dict] <Song id=None, title=Brano di riferimento> -> {'media_id': None, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:38.252795', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:38.252795', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=251
[DEBUG][Media.save] Result from create_media_db={'id': 251}
[DEBUG][Media.save] Assigned new media_id=251
[DEBUG][Media.save] Syncing relations for <Song id=251, title=Brano di riferimento>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (251,)
[DEBUG][Media.save] END for <Song id=251, title=Brano di riferimento>
[DEBUG][create_object] Object saved: <Song id=251, title=Brano di riferimento>
[DEBUG][Media.to_dict] <Song id=251, title=Brano di riferimento> -> {'media_id': 251, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:38.252795', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=1.8091s
[DEBUG][create_song] ARGS=[{'title': 'Brano di riferimento'}]
[DEBUG][create_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_song] RESPONSE={"media_id": 251, "type": "song", "title": "Brano di riferimento", "user_id": 340, "year": null, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:38.252795", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false}

[DEBUG][dispatch_command] START - command=create_document, args=[{'title': 'Resistenza', 'year': 1958, 'doc_type': 'score', 'file_format': 'pdf', 'references': [251], 'is_author': True}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Document, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Resistenza', 'year': 1958, 'doc_type': 'score', 'file_format': 'pdf', 'references': [251], 'is_author': True}
[DEBUG][Media.__init__] Called with title=Resistenza, type=None, year=1958, user_id=None, kwargs={'doc_type': 'score', 'file_format': 'pdf'}
[DEBUG][Media.__init__] Extra attr: doc_type=score
[DEBUG][Media.__init__] Extra attr: file_format=pdf
[DEBUG][Media.__init__] Finished -> <Document id=None, title=Resistenza>
[DEBUG][create_object] Object built from dict: <Document id=None, title=Resistenza>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Document id=None, title=Resistenza>
[DEBUG][Media.save] Called on <Document id=None, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=None, title=Resistenza> -> {'media_id': None, 'type': 'document', 'title': 'Resistenza', 'user_id': 340, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:40.056645', 'genres': [], 'authors': [], 'performers': [], 'references': [251], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'document', 'title': 'Resistenza', 'user_id': 340, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:40.056645', 'genres': [], 'authors': [], 'performers': [], 'references': [251], 'is_author': True, 'is_performer': False, 'pages': None, 'format': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=252
[DEBUG] Inserted document for media_id=252
[DEBUG] Linked media_id=252 to reference_id=251
[DEBUG][Media.save] Result from create_media_db={'id': 252}
[DEBUG][Media.save] Assigned new media_id=252
[DEBUG][Media.save] Syncing relations for <Document id=252, title=Resistenza>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (252,)
[DEBUG][Media.save] END for <Document id=252, title=Resistenza>
[DEBUG][create_object] Object saved: <Document id=252, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=252, title=Resistenza> -> {'media_id': 252, 'type': 'document', 'title': 'Resistenza', 'user_id': 340, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:40.056645', 'genres': [], 'authors': [], 'performers': [], 'references': [251], 'is_author': True, 'is_performer': False}
[DEBUG][create_document] STATUS=OK, TIME=0.7693s
[DEBUG][create_document] ARGS=[{'title': 'Resistenza', 'year': 1958, 'doc_type': 'score', 'file_format': 'pdf', 'references': [251], 'is_author': True}]
[DEBUG][create_document] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_document] RESPONSE={"media_id": 252, "type": "document", "title": "Resistenza", "user_id": 340, "year": 1958, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:40.056645", "genres": [], "authors": [], "performers": [], "references": [251], "is_author": true, "is_performer": false, "pages": null, "format": null}

[DEBUG][dispatch_command] START - command=get_document, args=[252], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=252
[DEBUG][Media.fetch] Called cls=Document, media_id=252
[DEBUG] fetch_one success: (252, 'document', 340, 'Resistenza', 1958, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 40, 147327), True, False)
[DEBUG][Media.fetch] Data from DB={'id': 252, 'type': 'document', 'user_id': 340, 'title': 'Resistenza', 'year': 1958, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 40, 147327), 'is_author': True, 'is_performer': False}
[DEBUG][Media.__init__] Called with title=Resistenza, type=document, year=1958, user_id=340, kwargs={'id': 252, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=252
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Document id=None, title=Resistenza>
[DEBUG][Media.fetch] Built object=<Document id=None, title=Resistenza>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(252, 251)]
[DEBUG][get_object] Retrieved object=<Document id=None, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=None, title=Resistenza> -> {'media_id': None, 'type': 'document', 'title': 'Resistenza', 'user_id': 340, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:40.147327', 'genres': [], 'authors': [], 'performers': [], 'references': [251], 'is_author': True, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=0.3278s
[DEBUG][get_document] ARGS=[252]
[DEBUG][get_document] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_document] RESPONSE={"media_id": null, "type": "document", "title": "Resistenza", "user_id": 340, "year": 1958, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:40.147327", "genres": [], "authors": [], "performers": [], "references": [251], "is_author": true, "is_performer": false, "pages": null, "format": null}

[DEBUG][dispatch_command] START - command=delete_document, args=[252], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=252
[DEBUG][Media.fetch] Called cls=Document, media_id=252
[DEBUG] fetch_one success: (252, 'document', 340, 'Resistenza', 1958, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 40, 147327), True, False)
[DEBUG][Media.fetch] Data from DB={'id': 252, 'type': 'document', 'user_id': 340, 'title': 'Resistenza', 'year': 1958, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 40, 147327), 'is_author': True, 'is_performer': False}
[DEBUG][Media.__init__] Called with title=Resistenza, type=document, year=1958, user_id=340, kwargs={'id': 252, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=252
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Document id=None, title=Resistenza>
[DEBUG][Media.fetch] Built object=<Document id=None, title=Resistenza>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(252, 251)]
[DEBUG][get_object] Retrieved object=<Document id=None, title=Resistenza>
[DEBUG][delete_object] Deleting object <Document id=None, title=Resistenza>
[DEBUG][Media.delete] Called on <Document id=None, title=Resistenza>
[DEBUG][delete_object] Deleted object <Document id=None, title=Resistenza>
[DEBUG][delete_document] STATUS=OK, TIME=0.5403s
[DEBUG][delete_document] ARGS=[252]
[DEBUG][delete_document] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_document] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=delete_song, args=[251], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=251
[DEBUG][get_object] cls=Song, object_id=251
[DEBUG][Media.fetch] Called cls=Song, media_id=251
[DEBUG] fetch_one success: (251, 'song', 340, 'Brano di riferimento', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 38, 339208), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 251, 'type': 'song', 'user_id': 340, 'title': 'Brano di riferimento', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 38, 339208), 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 340, 'title': 'Brano di riferimento', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 38, 339208), 'is_author': False, 'is_performer': False, 'media_id': 251}
[DEBUG][Media.__init__] Called with title=Brano di riferimento, type=song, year=None, user_id=340, kwargs={'recording_date': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Song id=251, title=Brano di riferimento>
[DEBUG][Media.from_dict] Built object=<Song id=251, title=Brano di riferimento>
[DEBUG][Media.fetch] Built object=<Song id=251, title=Brano di riferimento>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=251, title=Brano di riferimento>
[DEBUG][delete_object] Deleting object <Song id=251, title=Brano di riferimento>
[DEBUG][Media.delete] Called on <Song id=251, title=Brano di riferimento>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (251,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (251,)
[DEBUG][Media.delete] Deleted media_id=251
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano di riferimento>
[DEBUG][delete_song] STATUS=OK, TIME=4.1018s
[DEBUG][delete_song] ARGS=[251]
[DEBUG][delete_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_song] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][create_object] cls=Song, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][Media.__init__] Called with title=Audio Test, type=None, year=None, user_id=None, kwargs={'format': 'mp3', 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][Media.__init__] Extra attr: format=mp3
[DEBUG][Media.__init__] Extra attr: instruments=['Piano']
[DEBUG][Media.__init__] Extra attr: recording_date=2024-01-01
[DEBUG][Media.__init__] Extra attr: recording_place=Roma
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Audio Test>
[DEBUG][create_object] Object built from dict: <Song id=None, title=Audio Test>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Song id=None, title=Audio Test>
[DEBUG][Media.save] Called on <Song id=None, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=None, title=Audio Test> -> {'media_id': None, 'type': 'song', 'title': 'Audio Test', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:45.832678', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Audio Test', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:45.832678', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=253
[DEBUG] Added performer_id=1 to media_id=253
[DEBUG][Media.save] Result from create_media_db={'id': 253}
[DEBUG][Media.save] Assigned new media_id=253
[DEBUG][Media.save] Syncing relations for <Song id=253, title=Audio Test>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (253,)
[DB ERROR execute] can't adapt type 'dict'
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (253,)
[DEBUG][Media.save] END for <Song id=253, title=Audio Test>
[DEBUG][create_object] Object saved: <Song id=253, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=253, title=Audio Test> -> {'media_id': 253, 'type': 'song', 'title': 'Audio Test', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:45.832678', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=2.3436s
[DEBUG][create_song] ARGS=[{'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}]
[DEBUG][create_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_song] RESPONSE={"media_id": 253, "type": "song", "title": "Audio Test", "user_id": 340, "year": null, "description": null, "link": null, "duration": 120, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:45.832678", "genres": [], "authors": [], "performers": [{"name": "Alice", "type": "external"}], "references": [], "is_author": false, "is_performer": false}

[DEBUG][dispatch_command] START - command=get_song, args=[253], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=253
[DEBUG][get_object] cls=Song, object_id=253
[DEBUG][Media.fetch] Called cls=Song, media_id=253
[DEBUG] fetch_one success: (253, 'song', 340, 'Audio Test', None, None, None, 120, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 253, 'type': 'song', 'user_id': 340, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 340, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), 'is_author': False, 'is_performer': False, 'media_id': 253}
[DEBUG][Media.__init__] Called with title=Audio Test, type=song, year=None, user_id=340, kwargs={'recording_date': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Song id=253, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=253, title=Audio Test>
[DEBUG][Media.fetch] Built object=<Song id=253, title=Audio Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=253, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=253, title=Audio Test> -> {'media_id': 253, 'type': 'song', 'title': 'Audio Test', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:46.030715', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=0.4240s
[DEBUG][get_song] ARGS=[253]
[DEBUG][get_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_song] RESPONSE={"media_id": 253, "type": "song", "title": "Audio Test", "user_id": 340, "year": null, "description": null, "link": null, "duration": 120, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:46.030715", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false}

[DEBUG][dispatch_command] START - command=delete_song, args=[253], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=253
[DEBUG][get_object] cls=Song, object_id=253
[DEBUG][Media.fetch] Called cls=Song, media_id=253
[DEBUG] fetch_one success: (253, 'song', 340, 'Audio Test', None, None, None, 120, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 253, 'type': 'song', 'user_id': 340, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 340, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 46, 30715), 'is_author': False, 'is_performer': False, 'media_id': 253}
[DEBUG][Media.__init__] Called with title=Audio Test, type=song, year=None, user_id=340, kwargs={'recording_date': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Song id=253, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=253, title=Audio Test>
[DEBUG][Media.fetch] Built object=<Song id=253, title=Audio Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=253, title=Audio Test>
[DEBUG][delete_object] Deleting object <Song id=253, title=Audio Test>
[DEBUG][Media.delete] Called on <Song id=253, title=Audio Test>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (253,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (253,)
[DEBUG][Media.delete] Deleted media_id=253
[DEBUG][delete_object] Deleted object <Song id=None, title=Audio Test>
[DEBUG][delete_song] STATUS=OK, TIME=4.0294s
[DEBUG][delete_song] ARGS=[253]
[DEBUG][delete_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_song] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=create_video, args=[{'title': 'Video Test', 'link': 'https://youtu.be/test', 'duration': 300, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Video, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Video Test', 'link': 'https://youtu.be/test', 'duration': 300, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}
[DEBUG][Media.__init__] Called with title=Video Test, type=None, year=None, user_id=None, kwargs={'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}
[DEBUG][Media.__init__] Extra attr: instruments=['Guitar']
[DEBUG][Media.__init__] Extra attr: recording_date=2024-02-01
[DEBUG][Media.__init__] Extra attr: recording_place=Milano
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Video Test>
[DEBUG][create_object] Object built from dict: <Video id=None, title=Video Test>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Video id=None, title=Video Test>
[DEBUG][Media.save] Called on <Video id=None, title=Video Test>
[DEBUG][Media.to_dict] <Video id=None, title=Video Test> -> {'media_id': None, 'type': 'video', 'title': 'Video Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:52.637168', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'video', 'title': 'Video Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:52.637168', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False, 'director': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=254
[DEBUG] Added performer_id=1 to media_id=254
[DEBUG][Media.save] Result from create_media_db={'id': 254}
[DEBUG][Media.save] Assigned new media_id=254
[DEBUG][Media.save] Syncing relations for <Video id=254, title=Video Test>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (254,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (254,)
[DB ERROR execute] can't adapt type 'dict'
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (254,)
[DEBUG][Media.save] END for <Video id=254, title=Video Test>
[DEBUG][create_object] Object saved: <Video id=254, title=Video Test>
[DEBUG][Media.to_dict] <Video id=254, title=Video Test> -> {'media_id': 254, 'type': 'video', 'title': 'Video Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:52.637168', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_video] STATUS=OK, TIME=2.0931s
[DEBUG][create_video] ARGS=[{'title': 'Video Test', 'link': 'https://youtu.be/test', 'duration': 300, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}]
[DEBUG][create_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_video] RESPONSE={"media_id": 254, "type": "video", "title": "Video Test", "user_id": 340, "year": null, "description": null, "link": "https://youtu.be/test", "duration": 300, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:52.637168", "genres": [], "authors": [], "performers": [{"name": "Alice", "type": "external"}], "references": [], "is_author": false, "is_performer": false, "director": null}

[DEBUG][dispatch_command] START - command=get_video, args=[254], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=254
[DEBUG][Media.fetch] Called cls=Video, media_id=254
[DEBUG] fetch_one success: (254, 'video', 340, 'Video Test', None, None, 'https://youtu.be/test', 300, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 52, 731639), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 254, 'type': 'video', 'user_id': 340, 'title': 'Video Test', 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 52, 731639), 'is_author': False, 'is_performer': False}
[DEBUG][Media.__init__] Called with title=Video Test, type=video, year=None, user_id=340, kwargs={'id': 254, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=254
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Video Test>
[DEBUG][Media.fetch] Built object=<Video id=None, title=Video Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=None, title=Video Test>
[DEBUG][Media.to_dict] <Video id=None, title=Video Test> -> {'media_id': None, 'type': 'video', 'title': 'Video Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:52.731639', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=0.5263s
[DEBUG][get_video] ARGS=[254]
[DEBUG][get_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_video] RESPONSE={"media_id": null, "type": "video", "title": "Video Test", "user_id": 340, "year": null, "description": null, "link": "https://youtu.be/test", "duration": 300, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:52.731639", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false, "director": null}

[DEBUG][dispatch_command] START - command=delete_video, args=[254], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=254
[DEBUG][Media.fetch] Called cls=Video, media_id=254
[DEBUG] fetch_one success: (254, 'video', 340, 'Video Test', None, None, 'https://youtu.be/test', 300, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 52, 731639), False, False)
[DEBUG][Media.fetch] Data from DB={'id': 254, 'type': 'video', 'user_id': 340, 'title': 'Video Test', 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 52, 731639), 'is_author': False, 'is_performer': False}
[DEBUG][Media.__init__] Called with title=Video Test, type=video, year=None, user_id=340, kwargs={'id': 254, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=254
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Video Test>
[DEBUG][Media.fetch] Built object=<Video id=None, title=Video Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=None, title=Video Test>
[DEBUG][delete_object] Deleting object <Video id=None, title=Video Test>
[DEBUG][Media.delete] Called on <Video id=None, title=Video Test>
[DEBUG][delete_object] Deleted object <Video id=None, title=Video Test>
[DEBUG][delete_video] STATUS=OK, TIME=0.8288s
[DEBUG][delete_video] ARGS=[254]
[DEBUG][delete_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_video] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=create_video, args=[{'title': 'Concerto Test', 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'is_performer': True}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Video, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Concerto Test', 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=None, year=None, user_id=None, kwargs={'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]}
[DEBUG][Media.__init__] Extra attr: recording_date=2024-01-01
[DEBUG][Media.__init__] Extra attr: recording_place=Milano
[DEBUG][Media.__init__] Extra attr: tracklist=[{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Concerto Test>
[DEBUG][create_object] Object built from dict: <Video id=None, title=Concerto Test>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Video id=None, title=Concerto Test>
[DEBUG][Media.save] Called on <Video id=None, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=None, title=Concerto Test> -> {'media_id': None, 'type': 'video', 'title': 'Concerto Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:56.106383', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'video', 'title': 'Concerto Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:56.106383', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True, 'director': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=255
[DEBUG][Media.save] Result from create_media_db={'id': 255}
[DEBUG][Media.save] Assigned new media_id=255
[DEBUG][Media.save] Syncing relations for <Video id=255, title=Concerto Test>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (255,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (255,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (255,)
[DEBUG][Media.save] END for <Video id=255, title=Concerto Test>
[DEBUG][create_object] Object saved: <Video id=255, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=255, title=Concerto Test> -> {'media_id': 255, 'type': 'video', 'title': 'Concerto Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:56.106383', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][create_video] STATUS=OK, TIME=2.1171s
[DEBUG][create_video] ARGS=[{'title': 'Concerto Test', 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'is_performer': True}]
[DEBUG][create_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_video] RESPONSE={"media_id": 255, "type": "video", "title": "Concerto Test", "user_id": 340, "year": null, "description": null, "link": "https://youtu.be/concert", "duration": 400, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:56.106383", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": true, "director": null}

[DEBUG][dispatch_command] START - command=get_video, args=[255], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=255
[DEBUG][Media.fetch] Called cls=Video, media_id=255
[DEBUG] fetch_one success: (255, 'video', 340, 'Concerto Test', None, None, 'https://youtu.be/concert', 400, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 56, 304825), False, True)
[DEBUG][Media.fetch] Data from DB={'id': 255, 'type': 'video', 'user_id': 340, 'title': 'Concerto Test', 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 56, 304825), 'is_author': False, 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=video, year=None, user_id=340, kwargs={'id': 255, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=255
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Concerto Test>
[DEBUG][Media.fetch] Built object=<Video id=None, title=Concerto Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=None, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=None, title=Concerto Test> -> {'media_id': None, 'type': 'video', 'title': 'Concerto Test', 'user_id': 340, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:56.304825', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][get_video] STATUS=OK, TIME=0.6564s
[DEBUG][get_video] ARGS=[255]
[DEBUG][get_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_video] RESPONSE={"media_id": null, "type": "video", "title": "Concerto Test", "user_id": 340, "year": null, "description": null, "link": "https://youtu.be/concert", "duration": 400, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:56.304825", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": true, "director": null}

[DEBUG][dispatch_command] START - command=delete_video, args=[255], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=255
[DEBUG][Media.fetch] Called cls=Video, media_id=255
[DEBUG] fetch_one success: (255, 'video', 340, 'Concerto Test', None, None, 'https://youtu.be/concert', 400, None, None, None, None, datetime.datetime(2025, 9, 8, 9, 40, 56, 304825), False, True)
[DEBUG][Media.fetch] Data from DB={'id': 255, 'type': 'video', 'user_id': 340, 'title': 'Concerto Test', 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 8, 9, 40, 56, 304825), 'is_author': False, 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=video, year=None, user_id=340, kwargs={'id': 255, 'recording_date': None}
[DEBUG][Media.__init__] Extra attr: id=255
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Concerto Test>
[DEBUG][Media.fetch] Built object=<Video id=None, title=Concerto Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=None, title=Concerto Test>
[DEBUG][delete_object] Deleting object <Video id=None, title=Concerto Test>
[DEBUG][Media.delete] Called on <Video id=None, title=Concerto Test>
[DEBUG][delete_object] Deleted object <Video id=None, title=Concerto Test>
[DEBUG][delete_video] STATUS=OK, TIME=0.5274s
[DEBUG][delete_video] ARGS=[255]
[DEBUG][delete_video] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_video] RESPONSE={"success": true}

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano Autore', 'authors': [{'id': 340, 'type': 'user'}], 'is_author': True}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Autore', 'authors': [{'id': 340, 'type': 'user'}], 'is_author': True}
[DEBUG][create_object] cls=Song, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Autore', 'authors': [{'id': 340, 'type': 'user'}], 'is_author': True}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano Autore', 'authors': [{'id': 340, 'type': 'user'}], 'is_author': True}
[DEBUG][Media.__init__] Called with title=Brano Autore, type=None, year=None, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano Autore>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano Autore>
[DEBUG][create_object] Object built from dict: <Song id=None, title=Brano Autore>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Song id=None, title=Brano Autore>
[DEBUG][Media.save] Called on <Song id=None, title=Brano Autore>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Autore> -> {'media_id': None, 'type': 'song', 'title': 'Brano Autore', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:59.432301', 'genres': [], 'authors': [{'id': 340, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano Autore', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:59.432301', 'genres': [], 'authors': [{'id': 340, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=256
[DEBUG] ERROR in create_media_db: can't adapt type 'dict'
[DEBUG][Media.save] Result from create_media_db=None
[DEBUG][Media.save] Assigned new media_id=None
[DEBUG][Media.save] Syncing relations for <Song id=None, title=Brano Autore>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (None,)
[DB ERROR execute] can't adapt type 'dict'
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (None,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (None,)
[DEBUG][Media.save] END for <Song id=None, title=Brano Autore>
[DEBUG][create_object] Object saved: <Song id=None, title=Brano Autore>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Autore> -> {'media_id': None, 'type': 'song', 'title': 'Brano Autore', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:40:59.432301', 'genres': [], 'authors': [{'id': 340, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=2.2816s
[DEBUG][create_song] ARGS=[{'title': 'Brano Autore', 'authors': [{'id': 340, 'type': 'user'}], 'is_author': True}]
[DEBUG][create_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_song] RESPONSE={"media_id": null, "type": "song", "title": "Brano Autore", "user_id": 340, "year": null, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:40:59.432301", "genres": [], "authors": [{"id": 340, "type": "user"}], "performers": [], "references": [], "is_author": true, "is_performer": false}

[DEBUG][dispatch_command] START - command=get_song, args=[None], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=None
[DEBUG][get_object] cls=Song, object_id=None
[DEBUG][Media.fetch] Called cls=Song, media_id=None
[DEBUG][Media.fetch] Data from DB=None
[DEBUG][Media.fetch] No data found -> returning None
[DEBUG][get_object] Retrieved object=None
[DEBUG][get_song] STATUS=OK, TIME=0.1754s
[DEBUG][get_song] ARGS=[None]
[DEBUG][get_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_song] RESPONSE=null

[DEBUG][dispatch_command] START - command=delete_song, args=[None], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=None
[DEBUG][get_object] cls=Song, object_id=None
[DEBUG][Media.fetch] Called cls=Song, media_id=None
[DEBUG][Media.fetch] Data from DB=None
[DEBUG][Media.fetch] No data found -> returning None
[DEBUG][get_object] Retrieved object=None
[DEBUG][delete_song_services] Song not found
[DEBUG][delete_song] STATUS=OK, TIME=0.0734s
[DEBUG][delete_song] ARGS=[None]
[DEBUG][delete_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_song] RESPONSE={"error": "Song not found"}

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano Performer', 'performers': [{'id': 340, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Performer', 'performers': [{'id': 340, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}
[DEBUG][create_object] cls=Song, user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Performer', 'performers': [{'id': 340, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano Performer', 'performers': [{'id': 340, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Brano Performer, type=None, year=None, user_id=None, kwargs={'instruments': ['Violin']}
[DEBUG][Media.__init__] Extra attr: instruments=['Violin']
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano Performer>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano Performer>
[DEBUG][create_object] Object built from dict: <Song id=None, title=Brano Performer>
[DEBUG][create_object] Set obj.user_id=340
[DEBUG][create_object] Saving object <Song id=None, title=Brano Performer>
[DEBUG][Media.save] Called on <Song id=None, title=Brano Performer>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Performer> -> {'media_id': None, 'type': 'song', 'title': 'Brano Performer', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:01.971510', 'genres': [], 'authors': [], 'performers': [{'id': 340, 'type': 'user'}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano Performer', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:01.971510', 'genres': [], 'authors': [], 'performers': [{'id': 340, 'type': 'user'}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=257
[DEBUG] ERROR in create_media_db: ERRORE:  la INSERT o l'UPDATE sulla tabella "media_performances" viola il vincolo di chiave esterna "media_performances_performer_id_fkey"
DETAIL:  La chiave (performer_id)=(340) non è presente nella tabella "performers".

[DEBUG][Media.save] Result from create_media_db=None
[DEBUG][Media.save] Assigned new media_id=None
[DEBUG][Media.save] Syncing relations for <Song id=None, title=Brano Performer>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (None,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (None,)
[DB ERROR execute] can't adapt type 'dict'
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (None,)
[DEBUG][Media.save] END for <Song id=None, title=Brano Performer>
[DEBUG][create_object] Object saved: <Song id=None, title=Brano Performer>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Performer> -> {'media_id': None, 'type': 'song', 'title': 'Brano Performer', 'user_id': 340, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:01.971510', 'genres': [], 'authors': [], 'performers': [{'id': 340, 'type': 'user'}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][create_song] STATUS=OK, TIME=2.1001s
[DEBUG][create_song] ARGS=[{'title': 'Brano Performer', 'performers': [{'id': 340, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}]
[DEBUG][create_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][create_song] RESPONSE={"media_id": null, "type": "song", "title": "Brano Performer", "user_id": 340, "year": null, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:41:01.971510", "genres": [], "authors": [], "performers": [{"id": 340, "type": "user"}], "references": [], "is_author": false, "is_performer": true}

[DEBUG][dispatch_command] START - command=get_song, args=[None], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=None
[DEBUG][get_object] cls=Song, object_id=None
[DEBUG][Media.fetch] Called cls=Song, media_id=None
[DEBUG][Media.fetch] Data from DB=None
[DEBUG][Media.fetch] No data found -> returning None
[DEBUG][get_object] Retrieved object=None
[DEBUG][get_song] STATUS=OK, TIME=0.0712s
[DEBUG][get_song] ARGS=[None]
[DEBUG][get_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][get_song] RESPONSE=null

[DEBUG][dispatch_command] START - command=delete_song, args=[None], user_obj={'id': 340, 'username': 'quackerina7550', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=None
[DEBUG][get_object] cls=Song, object_id=None
[DEBUG][Media.fetch] Called cls=Song, media_id=None
[DEBUG][Media.fetch] Data from DB=None
[DEBUG][Media.fetch] No data found -> returning None
[DEBUG][get_object] Retrieved object=None
[DEBUG][delete_song_services] Song not found
[DEBUG][delete_song] STATUS=OK, TIME=0.1693s
[DEBUG][delete_song] ARGS=[None]
[DEBUG][delete_song] USER_OBJ ID=340, FOLLOWERS=0, FOLLOWED=0
[DEBUG][delete_song] RESPONSE={"error": "Song not found"}


=== ACCESS WITHOUT LOGIN ===
[DEBUG][dispatch_command] START - command=get_followers, args=[], user_obj=None
[DEBUG][get_followers] STATUS=OK, TIME=0.0020s
[DEBUG][get_followers] ARGS=[]
[DEBUG][get_followers] USER_OBJ=None
[DEBUG][get_followers] RESPONSE={"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": null}

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'X', 'year': 0}], user_obj=None
[DEBUG][create_song_services] user_obj=None, data={'title': 'X', 'year': 0}
[DEBUG][create_object] cls=Song, user_obj=None, data={'title': 'X', 'year': 0}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'X', 'year': 0}
[DEBUG][Media.__init__] Called with title=X, type=None, year=0, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=X>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=X>
[DEBUG][create_object] Object built from dict: <Song id=None, title=X>
[DEBUG][create_object] Saving object <Song id=None, title=X>
[DEBUG][Media.save] Called on <Song id=None, title=X>
[DEBUG][Media.to_dict] <Song id=None, title=X> -> {'media_id': None, 'type': 'song', 'title': 'X', 'user_id': None, 'year': 0, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:04.347547', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'X', 'user_id': None, 'year': 0, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:04.347547', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=258
[DEBUG][Media.save] Result from create_media_db={'id': 258}
[DEBUG][Media.save] Assigned new media_id=258
[DEBUG][Media.save] Syncing relations for <Song id=258, title=X>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (258,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (258,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (258,)
[DEBUG][Media.save] END for <Song id=258, title=X>
[DEBUG][create_object] Object saved: <Song id=258, title=X>
[DEBUG][Media.to_dict] <Song id=258, title=X> -> {'media_id': 258, 'type': 'song', 'title': 'X', 'user_id': None, 'year': 0, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-08T09:41:04.347547', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=2.0192s
[DEBUG][create_song] ARGS=[{'title': 'X', 'year': 0}]
[DEBUG][create_song] USER_OBJ=None
[DEBUG][create_song] RESPONSE={"media_id": 258, "type": "song", "title": "X", "user_id": null, "year": 0, "description": null, "link": null, "duration": null, "location": null, "additional_info": null, "stored_at": null, "created_at": "2025-09-08T09:41:04.347547", "genres": [], "authors": [], "performers": [], "references": [], "is_author": false, "is_performer": false}


=== CONCURRENCY LOGIN (8 parallel) ===
[DEBUG][dispatch_command] START - command=register_user, args=['user06383@example.com', 'user06383', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user16383@example.com', 'user16383', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user26383@example.com', 'user26383', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user36383@example.com', 'user36383', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user46399@example.com', 'user46399', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user56399@example.com', 'user56399', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user66399@example.com', 'user66399', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user76399@example.com', 'user76399', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(342, 'user06383@example.com', 'user06383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(343, 'user16383@example.com', 'user16383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(345, 'user66399@example.com', 'user66399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(349, 'user56399@example.com', 'user56399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(348, 'user76399@example.com', 'user76399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(342, 'user06383@example.com', 'user06383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.7798s
[DEBUG][register_user] ARGS=['user06383@example.com', 'user06383', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=342, FOLLOWERS=0, FOLLOWED=0
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(344, 'user46399@example.com', 'user46399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 342, "user_obj": {"id": 342, "username": "user06383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "1ecc1780270c56a4dfaeb9e3ba7c174a"}

[DEBUG][dispatch_command] START - command=login_user, args=['user06383', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(346, 'user36383@example.com', 'user36383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(343, 'user16383@example.com', 'user16383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG][register_user] STATUS=OK, TIME=0.8638s
[DEBUG] db_get_following result: [(345, 'user66399@example.com', 'user66399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] ARGS=['user16383@example.com', 'user16383', 'pass1234', '2000-01-01']
[DEBUG][register_user] STATUS=OK, TIME=0.8535s
[DEBUG][register_user] ARGS=['user66399@example.com', 'user66399', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=343, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] USER_OBJ ID=345, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 345, "user_obj": {"id": 345, "username": "user66399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "75df06449bbb902ba6154173e35b30ba"}
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 343, "user_obj": {"id": 343, "username": "user16383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "341dd68e52d916862c7d356e237b6b88"}

[DEBUG][dispatch_command] START - command=login_user, args=['user66399', 'pass1234'], user_obj=None

[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=login_user, args=['user16383', 'pass1234'], user_obj=None
[DEBUG] db_get_following result: [(347, 'user26383@example.com', 'user26383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(348, 'user76399@example.com', 'user76399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.8983s
[DEBUG][register_user] ARGS=['user76399@example.com', 'user76399', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=348, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 348, "user_obj": {"id": 348, "username": "user76399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "151afe8fb92324e253512db7ec566cd3"}

[DEBUG][dispatch_command] START - command=login_user, args=['user76399', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(349, 'user56399@example.com', 'user56399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.9682s
[DEBUG][register_user] ARGS=['user56399@example.com', 'user56399', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=349, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 349, "user_obj": {"id": 349, "username": "user56399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "8db3a7235fc1ddfca6f22155be8c625a"}

[DEBUG][dispatch_command] START - command=login_user, args=['user56399', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(346, 'user36383@example.com', 'user36383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=1.0109s
[DEBUG][register_user] ARGS=['user36383@example.com', 'user36383', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=346, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 346, "user_obj": {"id": 346, "username": "user36383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "235dc76758ae98bbcdae30316fc92423"}
[DEBUG] fetch_all returned 1 rows

[DEBUG][dispatch_command] START - command=login_user, args=['user36383', 'pass1234'], user_obj=None
[DEBUG] db_get_following result: [(344, 'user46399@example.com', 'user46399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG][register_user] STATUS=OK, TIME=1.0243s
[DEBUG][register_user] ARGS=['user46399@example.com', 'user46399', 'pass1234', '2000-01-01']
[DEBUG] db_get_following result: [(342, 'user06383@example.com', 'user06383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] USER_OBJ ID=344, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 344, "user_obj": {"id": 344, "username": "user46399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "5ec1bbc5668eae39520dd594435851aa"}

[DEBUG][dispatch_command] START - command=login_user, args=['user46399', 'pass1234'], user_obj=None
[DEBUG][login_user] STATUS=OK, TIME=0.2319s
[DEBUG][login_user] ARGS=['user06383', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=342, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 342, "username": "user06383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "1ae09abf1de1436f057a7da2716497b9", "error_msg": null}

[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(345, 'user66399@example.com', 'user66399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.2067s
[DEBUG] fetch_all returned 1 rows
[DEBUG][login_user] ARGS=['user66399', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=345, FOLLOWERS=0, FOLLOWED=0
[DEBUG] db_get_following result: [(343, 'user16383@example.com', 'user16383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 345, "username": "user66399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "157911a71869cddd8ad674ed975289b8", "error_msg": null}
[DEBUG] fetch_all returned 1 rows

[DEBUG] db_get_following result: [(348, 'user76399@example.com', 'user76399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG][login_user] STATUS=OK, TIME=0.2102s
[DEBUG] db_get_following result: [(347, 'user26383@example.com', 'user26383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] ARGS=['user16383', 'pass1234']
[DEBUG][login_user] STATUS=OK, TIME=0.1799s
[DEBUG][login_user] USER_OBJ ID=343, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] ARGS=['user76399', 'pass1234']
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 343, "username": "user16383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "821df56233dccd7f70d42fa8c4bef42f", "error_msg": null}
[DEBUG][login_user] USER_OBJ ID=348, FOLLOWERS=0, FOLLOWED=0

[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 348, "username": "user76399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "ad6d35c98576ea2d8b50fa991d4e50ba", "error_msg": null}
[DEBUG][register_user] STATUS=OK, TIME=1.1118s

[DEBUG][register_user] ARGS=['user26383@example.com', 'user26383', 'pass1234', '2000-01-01']
[DEBUG][register_user] USER_OBJ ID=347, FOLLOWERS=0, FOLLOWED=0
[DEBUG][register_user] RESPONSE={"status": "OK", "user_id": 347, "user_obj": {"id": 347, "username": "user26383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "e14853526a852f50d3934710be19a4d2"}

[DEBUG][dispatch_command] START - command=login_user, args=['user26383', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(349, 'user56399@example.com', 'user56399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1712s
[DEBUG][login_user] ARGS=['user56399', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=349, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 349, "username": "user56399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "8c752ce52a06735df9bdeb3ed7e16ac3", "error_msg": null}

[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(344, 'user46399@example.com', 'user46399', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(346, 'user36383@example.com', 'user36383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1630s
[DEBUG][login_user] ARGS=['user36383', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=346, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 346, "username": "user36383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "06f0429eb8268efd55babb504cf8d300", "error_msg": null}

[DEBUG][login_user] STATUS=OK, TIME=0.1427s
[DEBUG][login_user] ARGS=['user46399', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=344, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 344, "username": "user46399", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "a039477b60ca0f31cd4d5b864d1fcd94", "error_msg": null}

[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(347, 'user26383@example.com', 'user26383', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1007s
[DEBUG][login_user] ARGS=['user26383', 'pass1234']
[DEBUG][login_user] USER_OBJ ID=347, FOLLOWERS=0, FOLLOWED=0
[DEBUG][login_user] RESPONSE={"status": "accepted", "user_obj": {"id": 347, "username": "user26383", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "076a647c5e5a8c404bfb3f84f4eab51c", "error_msg": null}

Got 8 tokens out of 8

=== DONE ===

=== TEST SUMMARY ===
Total commands: 49
Avg time per command: 0.9698s
Errors: 0 (0.00%)
Total time: 47.52s

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>