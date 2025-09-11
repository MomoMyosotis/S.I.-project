
C:\Users\LENOVO\Desktop\prj\I.S\Code\server>python ft.py

=== REGISTER / LOGIN ===
[DEBUG][dispatch_command] START - command=register_user, args=['quackerina9374@example.com', 'quackerina9374', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(92, 'quackerina9374@example.com', 'quackerina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(92, 'quackerina9374@example.com', 'quackerina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.6627s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=register_user, args=['bassettina9374@example.com', 'bassettina9374', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.4901s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['quackerina9374', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(92, 'quackerina9374@example.com', 'quackerina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.0718s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['bassettina9374', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1848s, TAG=OK, ERROR=None

=== FOLLOW / FOLLOWERS / FOLLOWED ===
[TEST] Follow user
[DEBUG][dispatch_command] START - command=follow_user, args=['bassettina9374'], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(92, 'quackerina9374@example.com', 'quackerina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s) (92, 93)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374', 'bassettina9374@example.com')]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][follow_user] STATUS=OK, TIME=1.3558s, TAG=OK, ERROR=None
[RESULT] After follow, user_obj: {'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}

[TEST] Get followed
[DEBUG][dispatch_command] START - command=get_followed, args=[], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}
[DEBUG] get_followed called with user_id=92 (type=<class 'int'>)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374', 'bassettina9374@example.com')]
[DEBUG] raw followed: [{'id': 93, 'username': 'bassettina9374', 'mail': 'bassettina9374@example.com'}]
[DEBUG][get_followed] STATUS=OK, TIME=0.1842s, TAG=OK, ERROR=None
[RESULT] Followed list: [{"id": 93, "username": "bassettina9374", "mail": "bassettina9374@example.com"}]

[TEST] Get followers (as None user)
[DEBUG][dispatch_command] START - command=get_followers, args=[], user_obj=None
[DEBUG][dispatch_command] ERROR - User is not logged in, access denied for command get_followers
[DEBUG][get_followers] STATUS=ERROR, TIME=0.0024s, TAG=EXPECTED, ERROR={"error_msg": "User is not logged in. Please log in to proceed."}
[RESULT] Followers list: {"error_msg": "User is not logged in. Please log in to proceed."}

[TEST] Unfollow user
[DEBUG][dispatch_command] START - command=unfollow_user, args=['bassettina9374'], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 1, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(92, 'quackerina9374@example.com', 'quackerina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(93, 'bassettina9374@example.com', 'bassettina9374', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM user_follow WHERE follower_id = %s AND followed_id = %s (92, 93)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][unfollow_user] STATUS=OK, TIME=1.1746s, TAG=OK, ERROR=None
[RESULT] After unfollow, user_obj: {'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}


=== MEDIA CRUD ===

MEDIA CASE_1

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano neutro', 'year': 2020}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano neutro', 'year': 2020}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano neutro', 'year': 2020}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=None, year=2020, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano neutro>
[DEBUG][Media.save] Called on <Song id=None, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=None, title=Brano neutro> -> {'media_id': None, 'type': 'song', 'title': 'Brano neutro', 'user_id': 92, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:43.548528', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano neutro', 'user_id': 92, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:43.548528', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=98
[DEBUG][Media.save] Result from create_media_db={'id': 98}
[DEBUG][Media.save] Assigned new media_id=98
[DEBUG][Media.save] Syncing relations for <Song id=98, title=Brano neutro>
[DEBUG][Media.save] END for <Song id=98, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=98, title=Brano neutro> -> {'media_id': 98, 'type': 'song', 'title': 'Brano neutro', 'user_id': 92, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:43.548528', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=0.2055s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_song, args=[98], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=98
[DEBUG][get_object] cls=Song, object_id=98
[DEBUG][Media.fetch] Called cls=Song, media_id=98
[DEBUG] fetch_one success: (98, 'song', 92, 'Brano neutro', 2020, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), False, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 98, 'type': 'song', 'user_id': 92, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': [], 'media_id': 98}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=song, year=2020, user_id=92, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=98, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=98, title=Brano neutro>
[DEBUG][Media.fetch] Built object=<Song id=98, title=Brano neutro>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=98, title=Brano neutro>
[DEBUG][Media.to_dict] <Song id=98, title=Brano neutro> -> {'media_id': 98, 'type': 'song', 'title': 'Brano neutro', 'user_id': 92, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:43.726685', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=0.3044s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_song, args=[98], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=98
[DEBUG][get_object] cls=Song, object_id=98
[DEBUG][Media.fetch] Called cls=Song, media_id=98
[DEBUG] fetch_one success: (98, 'song', 92, 'Brano neutro', 2020, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), False, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 98, 'type': 'song', 'user_id': 92, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano neutro', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 43, 726685), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': [], 'media_id': 98}
[DEBUG][Media.__init__] Called with title=Brano neutro, type=song, year=2020, user_id=92, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=98, title=Brano neutro>
[DEBUG][Media.from_dict] Built object=<Song id=98, title=Brano neutro>
[DEBUG][Media.fetch] Built object=<Song id=98, title=Brano neutro>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=98, title=Brano neutro>
[DEBUG][delete_object] Deleting object <Song id=98, title=Brano neutro>
[DEBUG][Media.delete] Called on <Song id=98, title=Brano neutro>
[DEBUG] fetch_one success: (98,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (98,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (98,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (98,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (98,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (98,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (98,)
[DEBUG][Media.delete] Deleted media_id=98
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano neutro>
[DEBUG][delete_song] STATUS=OK, TIME=4.3576s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_2

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano di riferimento'}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano di riferimento'}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano di riferimento'}
[DEBUG][Media.__init__] Called with title=Brano di riferimento, type=None, year=None, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano di riferimento>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano di riferimento>
[DEBUG][Media.save] Called on <Song id=None, title=Brano di riferimento>
[DEBUG][Media.to_dict] <Song id=None, title=Brano di riferimento> -> {'media_id': None, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.432321', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.432321', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=99
[DEBUG][Media.save] Result from create_media_db={'id': 99}
[DEBUG][Media.save] Assigned new media_id=99
[DEBUG][Media.save] Syncing relations for <Song id=99, title=Brano di riferimento>
[DEBUG][Media.save] END for <Song id=99, title=Brano di riferimento>
[DEBUG][Media.to_dict] <Song id=99, title=Brano di riferimento> -> {'media_id': 99, 'type': 'song', 'title': 'Brano di riferimento', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.432321', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=0.1172s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=create_document, args=[{'title': 'Resistenza', 'year': 1958, 'doc_type': 'score', 'file_format': 'pdf', 'references': [99], 'is_author': True}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Document, user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Resistenza', 'year': 1958, 'doc_type': 'score', 'file_format': 'pdf', 'references': [99], 'is_author': True}
[DEBUG][Media.__init__] Called with title=Resistenza, type=None, year=1958, user_id=None, kwargs={'doc_type': 'score', 'file_format': 'pdf'}
[DEBUG][Media.__init__] Extra attr: doc_type=score
[DEBUG][Media.__init__] Extra attr: file_format=pdf
[DEBUG][Media.__init__] Finished -> <Document id=None, title=Resistenza>
[DEBUG][create_object] Object built from dict: <Document id=None, title=Resistenza>
[DEBUG][create_object] Set obj.user_id=92
[DEBUG][create_object] Saving object <Document id=None, title=Resistenza>
[DEBUG][Media.save] Called on <Document id=None, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=None, title=Resistenza> -> {'media_id': None, 'type': 'document', 'title': 'Resistenza', 'user_id': 92, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.550332', 'genres': [], 'authors': [], 'performers': [], 'references': [99], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'document', 'title': 'Resistenza', 'user_id': 92, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.550332', 'genres': [], 'authors': [], 'performers': [], 'references': [99], 'is_author': True, 'is_performer': False, 'pages': None, 'format': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=100
[DEBUG] Inserted document for media_id=100
[DEBUG] Linked media_id=100 to reference_id=99
[DEBUG][Media.save] Result from create_media_db={'id': 100}
[DEBUG][Media.save] Assigned new media_id=100
[DEBUG][Media.save] Syncing relations for <Document id=100, title=Resistenza>
[DEBUG][Media.save] END for <Document id=100, title=Resistenza>
[DEBUG][create_object] Object saved: <Document id=100, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=100, title=Resistenza> -> {'media_id': 100, 'type': 'document', 'title': 'Resistenza', 'user_id': 92, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.550332', 'genres': [], 'authors': [], 'performers': [], 'references': [99], 'is_author': True, 'is_performer': False}
[DEBUG][create_document] STATUS=OK, TIME=0.2605s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_document, args=[100], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=100
[DEBUG][Media.fetch] Called cls=Document, media_id=100
[DEBUG] fetch_one success: (100, 'document', 92, 'Resistenza', 1958, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 48, 773922), True, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 100, 'type': 'document', 'user_id': 92, 'title': 'Resistenza', 'year': 1958, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 48, 773922), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Resistenza, type=document, year=1958, user_id=92, kwargs={'id': 100, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=100
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=100, title=Resistenza>
[DEBUG][Media.fetch] Built object=<Document id=100, title=Resistenza>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(100, 99)]
[DEBUG][get_object] Retrieved object=<Document id=100, title=Resistenza>
[DEBUG][Media.to_dict] <Document id=100, title=Resistenza> -> {'media_id': 100, 'type': 'document', 'title': 'Resistenza', 'user_id': 92, 'year': 1958, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:48.773922', 'genres': [], 'authors': [], 'performers': [], 'references': [99], 'is_author': True, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=0.4641s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_document, args=[100], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=100
[DEBUG][Media.fetch] Called cls=Document, media_id=100
[DEBUG] fetch_one success: (100, 'document', 92, 'Resistenza', 1958, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 48, 773922), True, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 100, 'type': 'document', 'user_id': 92, 'title': 'Resistenza', 'year': 1958, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 48, 773922), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Resistenza, type=document, year=1958, user_id=92, kwargs={'id': 100, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=100
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=100, title=Resistenza>
[DEBUG][Media.fetch] Built object=<Document id=100, title=Resistenza>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(100, 99)]
[DEBUG][get_object] Retrieved object=<Document id=100, title=Resistenza>
[DEBUG][delete_object] Deleting object <Document id=100, title=Resistenza>
[DEBUG][Media.delete] Called on <Document id=100, title=Resistenza>
[DEBUG] fetch_one success: (100,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (100,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (100,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (100,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (100,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (100,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (100,)
[DEBUG][Media.delete] Deleted media_id=100
[DEBUG][delete_object] Deleted object <Document id=None, title=Resistenza>
[DEBUG][delete_document] STATUS=OK, TIME=4.2917s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_song, args=[99], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=99
[DEBUG][get_object] cls=Song, object_id=99
[DEBUG][Media.fetch] Called cls=Song, media_id=99
[DEBUG] fetch_one success: (99, 'song', 92, 'Brano di riferimento', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 48, 518779), False, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 99, 'type': 'song', 'user_id': 92, 'title': 'Brano di riferimento', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 48, 518779), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano di riferimento', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 48, 518779), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': [], 'media_id': 99}
[DEBUG][Media.__init__] Called with title=Brano di riferimento, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=99, title=Brano di riferimento>
[DEBUG][Media.from_dict] Built object=<Song id=99, title=Brano di riferimento>
[DEBUG][Media.fetch] Built object=<Song id=99, title=Brano di riferimento>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=99, title=Brano di riferimento>
[DEBUG][delete_object] Deleting object <Song id=99, title=Brano di riferimento>
[DEBUG][Media.delete] Called on <Song id=99, title=Brano di riferimento>
[DEBUG] fetch_one success: (99,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (99,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (99,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (99,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (99,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (99,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (99,)
[DEBUG][Media.delete] Deleted media_id=99
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano di riferimento>
[DEBUG][delete_song] STATUS=OK, TIME=4.6588s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_3

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG] fetch_one success: (1, 'Alice', None)
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Audio Test', 'format': 'mp3', 'duration': 120, 'performers': [{'type': 'external', 'id': 1, 'name': 'Alice'}], 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][Media.__init__] Called with title=Audio Test, type=None, year=None, user_id=None, kwargs={'format': 'mp3', 'instruments': ['Piano'], 'recording_date': '2024-01-01', 'recording_place': 'Roma'}
[DEBUG][Media.__init__] Extra attr: format=mp3
[DEBUG][Media.__init__] Extra attr: instruments=['Piano']
[DEBUG][Media.__init__] Extra attr: recording_date=2024-01-01
[DEBUG][Media.__init__] Extra attr: recording_place=Roma
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Audio Test>
[DEBUG][Media.save] Called on <Song id=None, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=None, title=Audio Test> -> {'media_id': None, 'type': 'song', 'title': 'Audio Test', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:58.323378', 'genres': [], 'authors': [], 'performers': [{'type': 'external', 'id': 1, 'name': 'Alice'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Audio Test', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:58.323378', 'genres': [], 'authors': [], 'performers': [{'type': 'external', 'id': 1, 'name': 'Alice'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=101
[DEBUG][Media.save] Result from create_media_db={'id': 101}
[DEBUG][Media.save] Assigned new media_id=101
[DEBUG][Media.save] Syncing relations for <Song id=101, title=Audio Test>
[DEBUG][Media.save] END for <Song id=101, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=101, title=Audio Test> -> {'media_id': 101, 'type': 'song', 'title': 'Audio Test', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:58.323378', 'genres': [], 'authors': [], 'performers': [{'type': 'external', 'id': 1, 'name': 'Alice'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=0.2937s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_song, args=[101], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=101
[DEBUG][get_object] cls=Song, object_id=101
[DEBUG][Media.fetch] Called cls=Song, media_id=101
[DEBUG] fetch_one success: (101, 'song', 92, 'Audio Test', None, None, None, 120, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), False, False, 1, None)
[DEBUG][Media.fetch] Data from DB={'id': 101, 'type': 'song', 'user_id': 92, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}]}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}], 'media_id': 101}
[DEBUG][Media.__init__] Called with title=Audio Test, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': 1}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=1
[DEBUG][Media.__init__] Finished -> <Song id=101, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=101, title=Audio Test>
[DEBUG][Media.fetch] Built object=<Song id=101, title=Audio Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(33, 101, 1, None)]
[DEBUG][get_object] Retrieved object=<Song id=101, title=Audio Test>
[DEBUG][Media.to_dict] <Song id=101, title=Audio Test> -> {'media_id': 101, 'type': 'song', 'title': 'Audio Test', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': 120, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:13:58.504725', 'genres': [], 'authors': [], 'performers': [1], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=0.5033s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_song, args=[101], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=101
[DEBUG][get_object] cls=Song, object_id=101
[DEBUG][Media.fetch] Called cls=Song, media_id=101
[DEBUG] fetch_one success: (101, 'song', 92, 'Audio Test', None, None, None, 120, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), False, False, 1, None)
[DEBUG][Media.fetch] Data from DB={'id': 101, 'type': 'song', 'user_id': 92, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}]}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Audio Test', 'year': None, 'description': None, 'link': None, 'duration': 120, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 13, 58, 504725), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}], 'media_id': 101}
[DEBUG][Media.__init__] Called with title=Audio Test, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': 1}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=1
[DEBUG][Media.__init__] Finished -> <Song id=101, title=Audio Test>
[DEBUG][Media.from_dict] Built object=<Song id=101, title=Audio Test>
[DEBUG][Media.fetch] Built object=<Song id=101, title=Audio Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(33, 101, 1, None)]
[DEBUG][get_object] Retrieved object=<Song id=101, title=Audio Test>
[DEBUG][delete_object] Deleting object <Song id=101, title=Audio Test>
[DEBUG][Media.delete] Called on <Song id=101, title=Audio Test>
[DEBUG] fetch_one success: (101,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (101,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (101,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (101,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (101,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (101,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (101,)
[DEBUG][Media.delete] Deleted media_id=101
[DEBUG][delete_object] Deleted object <Song id=None, title=Audio Test>
[DEBUG][delete_song] STATUS=OK, TIME=4.0304s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_4

[DEBUG][dispatch_command] START - command=create_video, args=[{'title': 'Video Test', 'link': 'https://youtu.be/test', 'duration': 300, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Video, user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Video Test', 'link': 'https://youtu.be/test', 'duration': 300, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}
[DEBUG][Media.__init__] Called with title=Video Test, type=None, year=None, user_id=None, kwargs={'instruments': ['Guitar'], 'recording_date': '2024-02-01', 'recording_place': 'Milano'}
[DEBUG][Media.__init__] Extra attr: instruments=['Guitar']
[DEBUG][Media.__init__] Extra attr: recording_date=2024-02-01
[DEBUG][Media.__init__] Extra attr: recording_place=Milano
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Video Test>
[DEBUG][create_object] Object built from dict: <Video id=None, title=Video Test>
[DEBUG][create_object] Set obj.user_id=92
[DEBUG][create_object] Saving object <Video id=None, title=Video Test>
[DEBUG][Media.save] Called on <Video id=None, title=Video Test>
[DEBUG][Media.to_dict] <Video id=None, title=Video Test> -> {'media_id': None, 'type': 'video', 'title': 'Video Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:03.089086', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'video', 'title': 'Video Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:03.089086', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False, 'director': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=102
[DEBUG][Media.save] Result from create_media_db={'id': 102}
[DEBUG][Media.save] Assigned new media_id=102
[DEBUG][Media.save] Syncing relations for <Video id=102, title=Video Test>
[DEBUG][Media.save] END for <Video id=102, title=Video Test>
[DEBUG][create_object] Object saved: <Video id=102, title=Video Test>
[DEBUG][Media.to_dict] <Video id=102, title=Video Test> -> {'media_id': 102, 'type': 'video', 'title': 'Video Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:03.089086', 'genres': [], 'authors': [], 'performers': [{'name': 'Alice', 'type': 'external'}], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_video] STATUS=OK, TIME=0.1210s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_video, args=[102], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=102
[DEBUG][Media.fetch] Called cls=Video, media_id=102
[DEBUG] fetch_one success: (102, 'video', 92, 'Video Test', None, None, 'https://youtu.be/test', 300, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 3, 176131), False, False, 1, None)
[DEBUG][Media.fetch] Data from DB={'id': 102, 'type': 'video', 'user_id': 92, 'title': 'Video Test', 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 3, 176131), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}]}
[DEBUG][Media.__init__] Called with title=Video Test, type=video, year=None, user_id=92, kwargs={'id': 102, 'recording_date': None, 'performer_id': 1}
[DEBUG][Media.__init__] Extra attr: id=102
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=1
[DEBUG][Media.__init__] Finished -> <Video id=102, title=Video Test>
[DEBUG][Media.fetch] Built object=<Video id=102, title=Video Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(34, 102, 1, None)]
[DEBUG][get_object] Retrieved object=<Video id=102, title=Video Test>
[DEBUG][Media.to_dict] <Video id=102, title=Video Test> -> {'media_id': 102, 'type': 'video', 'title': 'Video Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:03.176131', 'genres': [], 'authors': [], 'performers': [1], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=0.4146s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_video, args=[102], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=102
[DEBUG][Media.fetch] Called cls=Video, media_id=102
[DEBUG] fetch_one success: (102, 'video', 92, 'Video Test', None, None, 'https://youtu.be/test', 300, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 3, 176131), False, False, 1, None)
[DEBUG][Media.fetch] Data from DB={'id': 102, 'type': 'video', 'user_id': 92, 'title': 'Video Test', 'year': None, 'description': None, 'link': 'https://youtu.be/test', 'duration': 300, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 3, 176131), 'is_author': False, 'is_performer': False, 'performer_id': 1, 'performers': [{'id': 1, 'type': 'user'}]}
[DEBUG][Media.__init__] Called with title=Video Test, type=video, year=None, user_id=92, kwargs={'id': 102, 'recording_date': None, 'performer_id': 1}
[DEBUG][Media.__init__] Extra attr: id=102
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=1
[DEBUG][Media.__init__] Finished -> <Video id=102, title=Video Test>
[DEBUG][Media.fetch] Built object=<Video id=102, title=Video Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(34, 102, 1, None)]
[DEBUG][get_object] Retrieved object=<Video id=102, title=Video Test>
[DEBUG][delete_object] Deleting object <Video id=102, title=Video Test>
[DEBUG][Media.delete] Called on <Video id=102, title=Video Test>
[DEBUG] fetch_one success: (102,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (102,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (102,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (102,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (102,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (102,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (102,)
[DEBUG][Media.delete] Deleted media_id=102
[DEBUG][delete_object] Deleted object <Video id=None, title=Video Test>
[DEBUG][delete_video] STATUS=OK, TIME=4.4613s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_5

[DEBUG][dispatch_command] START - command=create_video, args=[{'title': 'Concerto Test', 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'is_performer': True}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_object] cls=Video, user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Concerto Test', 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=None, year=None, user_id=None, kwargs={'recording_date': '2024-01-01', 'recording_place': 'Milano', 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]}
[DEBUG][Media.__init__] Extra attr: recording_date=2024-01-01
[DEBUG][Media.__init__] Extra attr: recording_place=Milano
[DEBUG][Media.__init__] Extra attr: tracklist=[{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]
[DEBUG][Media.__init__] Finished -> <Video id=None, title=Concerto Test>
[DEBUG][create_object] Object built from dict: <Video id=None, title=Concerto Test>
[DEBUG][create_object] Set obj.user_id=92
[DEBUG][create_object] Saving object <Video id=None, title=Concerto Test>
[DEBUG][Media.save] Called on <Video id=None, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=None, title=Concerto Test> -> {'media_id': None, 'type': 'video', 'title': 'Concerto Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': '[{"song_title": "Song1", "start_time": 0, "end_time": 200, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]}, {"song_title": "Song2", "start_time": 200, "end_time": 400, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}]', 'stored_at': None, 'created_at': '2025-09-11T03:14:08.104245', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True, 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'video', 'title': 'Concerto Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': '[{"song_title": "Song1", "start_time": 0, "end_time": 200, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]}, {"song_title": "Song2", "start_time": 200, "end_time": 400, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}]', 'stored_at': None, 'created_at': '2025-09-11T03:14:08.104245', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True, 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}], 'director': None}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=103
[DEBUG][Media.save] Result from create_media_db={'id': 103}
[DEBUG][Media.save] Assigned new media_id=103
[DEBUG][Media.save] Syncing relations for <Video id=103, title=Concerto Test>
[DEBUG][Media.save] END for <Video id=103, title=Concerto Test>
[DEBUG][create_object] Object saved: <Video id=103, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=103, title=Concerto Test> -> {'media_id': 103, 'type': 'video', 'title': 'Concerto Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': '[{"song_title": "Song1", "start_time": 0, "end_time": 200, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]}, {"song_title": "Song2", "start_time": 200, "end_time": 400, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}]', 'stored_at': None, 'created_at': '2025-09-11T03:14:08.104245', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True, 'tracklist': [{'song_title': 'Song1', 'start_time': 0, 'end_time': 200, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Guitar']}, {'song_title': 'Song2', 'start_time': 200, 'end_time': 400, 'performers': [{'name': 'Alice', 'type': 'external'}], 'instruments': ['Piano']}]}
[DEBUG][create_video] STATUS=OK, TIME=0.2249s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_video, args=[103], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=103
[DEBUG][Media.fetch] Called cls=Video, media_id=103
[DEBUG] fetch_one success: (103, 'video', 92, 'Concerto Test', None, None, 'https://youtu.be/concert', 400, None, None, '[{"song_title": "Song1", "start_time": 0, "end_time": 200, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]}, {"song_title": "Song2", "start_time": 200, "end_time": 400, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}]', None, datetime.datetime(2025, 9, 11, 3, 14, 8, 295521), False, True, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 103, 'type': 'video', 'user_id': 92, 'title': 'Concerto Test', 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 8, 295521), 'is_author': False, 'is_performer': True, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=video, year=None, user_id=92, kwargs={'id': 103, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=103
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=103, title=Concerto Test>
[DEBUG][Media.fetch] Built object=<Video id=103, title=Concerto Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=103, title=Concerto Test>
[DEBUG][Media.to_dict] <Video id=103, title=Concerto Test> -> {'media_id': 103, 'type': 'video', 'title': 'Concerto Test', 'user_id': 92, 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:08.295521', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][get_video] STATUS=OK, TIME=0.6334s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_video, args=[103], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=103
[DEBUG][Media.fetch] Called cls=Video, media_id=103
[DEBUG] fetch_one success: (103, 'video', 92, 'Concerto Test', None, None, 'https://youtu.be/concert', 400, None, None, '[{"song_title": "Song1", "start_time": 0, "end_time": 200, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]}, {"song_title": "Song2", "start_time": 200, "end_time": 400, "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}]', None, datetime.datetime(2025, 9, 11, 3, 14, 8, 295521), False, True, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 103, 'type': 'video', 'user_id': 92, 'title': 'Concerto Test', 'year': None, 'description': None, 'link': 'https://youtu.be/concert', 'duration': 400, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 8, 295521), 'is_author': False, 'is_performer': True, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Concerto Test, type=video, year=None, user_id=92, kwargs={'id': 103, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=103
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=103, title=Concerto Test>
[DEBUG][Media.fetch] Built object=<Video id=103, title=Concerto Test>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=103, title=Concerto Test>
[DEBUG][delete_object] Deleting object <Video id=103, title=Concerto Test>
[DEBUG][Media.delete] Called on <Video id=103, title=Concerto Test>
[DEBUG] fetch_one success: (103,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (103,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (103,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (103,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (103,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (103,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (103,)
[DEBUG][Media.delete] Deleted media_id=103
[DEBUG][delete_object] Deleted object <Video id=None, title=Concerto Test>
[DEBUG][delete_video] STATUS=OK, TIME=4.2236s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_6

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano Autore', 'authors': [{'id': 92, 'type': 'user'}], 'is_author': True}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Autore', 'authors': [{'id': 92, 'type': 'user'}], 'is_author': True}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano Autore', 'authors': [{'id': 92, 'type': 'user'}], 'is_author': True}
[DEBUG][Media.__init__] Called with title=Brano Autore, type=None, year=None, user_id=None, kwargs={}
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano Autore>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano Autore>
[DEBUG][Media.save] Called on <Song id=None, title=Brano Autore>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Autore> -> {'media_id': None, 'type': 'song', 'title': 'Brano Autore', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:13.202979', 'genres': [], 'authors': [{'id': 92, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano Autore', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:13.202979', 'genres': [], 'authors': [{'id': 92, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=104
[DEBUG] Added author_id=6 to media_id=104
[DEBUG][Media.save] Result from create_media_db={'id': 104}
[DEBUG][Media.save] Assigned new media_id=104
[DEBUG][Media.save] Syncing relations for <Song id=104, title=Brano Autore>
[DEBUG][Media.save] END for <Song id=104, title=Brano Autore>
[DEBUG][Media.to_dict] <Song id=104, title=Brano Autore> -> {'media_id': 104, 'type': 'song', 'title': 'Brano Autore', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:13.202979', 'genres': [], 'authors': [{'id': 92, 'type': 'user'}], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][create_song] STATUS=OK, TIME=0.1046s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_song, args=[104], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=104
[DEBUG][get_object] cls=Song, object_id=104
[DEBUG][Media.fetch] Called cls=Song, media_id=104
[DEBUG] fetch_one success: (104, 'song', 92, 'Brano Autore', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), True, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 104, 'type': 'song', 'user_id': 92, 'title': 'Brano Autore', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano Autore', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': [], 'media_id': 104}
[DEBUG][Media.__init__] Called with title=Brano Autore, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=104, title=Brano Autore>
[DEBUG][Media.from_dict] Built object=<Song id=104, title=Brano Autore>
[DEBUG][Media.fetch] Built object=<Song id=104, title=Brano Autore>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(104, 6)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=104, title=Brano Autore>
[DEBUG][Media.to_dict] <Song id=104, title=Brano Autore> -> {'media_id': 104, 'type': 'song', 'title': 'Brano Autore', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:13.277175', 'genres': [], 'authors': [6], 'performers': [], 'references': [], 'is_author': True, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=0.2994s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_song, args=[104], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=104
[DEBUG][get_object] cls=Song, object_id=104
[DEBUG][Media.fetch] Called cls=Song, media_id=104
[DEBUG] fetch_one success: (104, 'song', 92, 'Brano Autore', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), True, False, None, None)
[DEBUG][Media.fetch] Data from DB={'id': 104, 'type': 'song', 'user_id': 92, 'title': 'Brano Autore', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano Autore', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 13, 277175), 'is_author': True, 'is_performer': False, 'performer_id': None, 'performers': [], 'media_id': 104}
[DEBUG][Media.__init__] Called with title=Brano Autore, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=104, title=Brano Autore>
[DEBUG][Media.from_dict] Built object=<Song id=104, title=Brano Autore>
[DEBUG][Media.fetch] Built object=<Song id=104, title=Brano Autore>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(104, 6)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=104, title=Brano Autore>
[DEBUG][delete_object] Deleting object <Song id=104, title=Brano Autore>
[DEBUG][Media.delete] Called on <Song id=104, title=Brano Autore>
[DEBUG] fetch_one success: (104,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (104,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (104,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (104,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (104,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (104,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (104,)
[DEBUG][Media.delete] Deleted media_id=104
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano Autore>
[DEBUG][delete_song] STATUS=OK, TIME=4.5362s, TAG=OK, ERROR=None


_________________________________________________________________



MEDIA CASE_7

[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'Brano Performer', 'performers': [{'id': 92, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][create_song_services] user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}, data={'title': 'Brano Performer', 'performers': [{'id': 92, 'type': 'user'}], 'instruments': ['Violin'], 'is_performer': True}
[DEBUG][Media.from_dict] cls=Song, data={'title': 'Brano Performer', 'performers': [{'type': 'user', 'id': 92}], 'instruments': ['Violin'], 'is_performer': True}
[DEBUG][Media.__init__] Called with title=Brano Performer, type=None, year=None, user_id=None, kwargs={'instruments': ['Violin']}
[DEBUG][Media.__init__] Extra attr: instruments=['Violin']
[DEBUG][Media.__init__] Finished -> <Song id=None, title=Brano Performer>
[DEBUG][Media.from_dict] Built object=<Song id=None, title=Brano Performer>
[DEBUG][Media.save] Called on <Song id=None, title=Brano Performer>
[DEBUG][Media.to_dict] <Song id=None, title=Brano Performer> -> {'media_id': None, 'type': 'song', 'title': 'Brano Performer', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:18.156434', 'genres': [], 'authors': [], 'performers': [{'type': 'user', 'id': 92}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][Media.save] Payload to create_media_db={'media_id': None, 'type': 'song', 'title': 'Brano Performer', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:18.156434', 'genres': [], 'authors': [], 'performers': [{'type': 'user', 'id': 92}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][Media.save] No media_id -> creating new record
[DEBUG] Inserted into media id=105
[DEBUG][Media.save] Result from create_media_db={'id': 105}
[DEBUG][Media.save] Assigned new media_id=105
[DEBUG][Media.save] Syncing relations for <Song id=105, title=Brano Performer>
[DEBUG][Media.save] END for <Song id=105, title=Brano Performer>
[DEBUG][Media.to_dict] <Song id=105, title=Brano Performer> -> {'media_id': 105, 'type': 'song', 'title': 'Brano Performer', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:18.156434', 'genres': [], 'authors': [], 'performers': [{'type': 'user', 'id': 92}], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][create_song] STATUS=OK, TIME=0.2107s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=get_song, args=[105], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=105
[DEBUG][get_object] cls=Song, object_id=105
[DEBUG][Media.fetch] Called cls=Song, media_id=105
[DEBUG] fetch_one success: (105, 'song', 92, 'Brano Performer', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), False, True, 7, None)
[DEBUG][Media.fetch] Data from DB={'id': 105, 'type': 'song', 'user_id': 92, 'title': 'Brano Performer', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), 'is_author': False, 'is_performer': True, 'performer_id': 7, 'performers': [{'id': 7, 'type': 'user'}]}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano Performer', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), 'is_author': False, 'is_performer': True, 'performer_id': 7, 'performers': [{'id': 7, 'type': 'user'}], 'media_id': 105}
[DEBUG][Media.__init__] Called with title=Brano Performer, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': 7}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=7
[DEBUG][Media.__init__] Finished -> <Song id=105, title=Brano Performer>
[DEBUG][Media.from_dict] Built object=<Song id=105, title=Brano Performer>
[DEBUG][Media.fetch] Built object=<Song id=105, title=Brano Performer>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(35, 105, 7, None)]
[DEBUG][get_object] Retrieved object=<Song id=105, title=Brano Performer>
[DEBUG][Media.to_dict] <Song id=105, title=Brano Performer> -> {'media_id': 105, 'type': 'song', 'title': 'Brano Performer', 'user_id': 92, 'year': None, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-11T03:14:18.336829', 'genres': [], 'authors': [], 'performers': [7], 'references': [], 'is_author': False, 'is_performer': True}
[DEBUG][get_song] STATUS=OK, TIME=0.7169s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=delete_song, args=[105], user_obj={'id': 92, 'username': 'quackerina9374', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=105
[DEBUG][get_object] cls=Song, object_id=105
[DEBUG][Media.fetch] Called cls=Song, media_id=105
[DEBUG] fetch_one success: (105, 'song', 92, 'Brano Performer', None, None, None, None, None, None, None, None, datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), False, True, 7, None)
[DEBUG][Media.fetch] Data from DB={'id': 105, 'type': 'song', 'user_id': 92, 'title': 'Brano Performer', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), 'is_author': False, 'is_performer': True, 'performer_id': 7, 'performers': [{'id': 7, 'type': 'user'}]}
[DEBUG][Media.from_dict] cls=Song, data={'type': 'song', 'user_id': 92, 'title': 'Brano Performer', 'year': None, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 11, 3, 14, 18, 336829), 'is_author': False, 'is_performer': True, 'performer_id': 7, 'performers': [{'id': 7, 'type': 'user'}], 'media_id': 105}
[DEBUG][Media.__init__] Called with title=Brano Performer, type=song, year=None, user_id=92, kwargs={'recording_date': None, 'performer_id': 7}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=7
[DEBUG][Media.__init__] Finished -> <Song id=105, title=Brano Performer>
[DEBUG][Media.from_dict] Built object=<Song id=105, title=Brano Performer>
[DEBUG][Media.fetch] Built object=<Song id=105, title=Brano Performer>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(35, 105, 7, None)]
[DEBUG][get_object] Retrieved object=<Song id=105, title=Brano Performer>
[DEBUG][delete_object] Deleting object <Song id=105, title=Brano Performer>
[DEBUG][Media.delete] Called on <Song id=105, title=Brano Performer>
[DEBUG] fetch_one success: (105,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (105,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (105,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (105,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (105,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (105,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (105,)
[DEBUG][Media.delete] Deleted media_id=105
[DEBUG][delete_object] Deleted object <Song id=None, title=Brano Performer>
[DEBUG][delete_song] STATUS=OK, TIME=4.1370s, TAG=OK, ERROR=None


_________________________________________________________________



=== ACCESS WITHOUT LOGIN ===
[DEBUG][dispatch_command] START - command=get_followers, args=[], user_obj=None
[DEBUG][dispatch_command] ERROR - User is not logged in, access denied for command get_followers
[DEBUG][get_followers] STATUS=ERROR, TIME=0.0021s, TAG=EXPECTED, ERROR={"error_msg": "User is not logged in. Please log in to proceed."}
[DEBUG][dispatch_command] START - command=create_song, args=[{'title': 'X', 'year': 0}], user_obj=None
[DEBUG][dispatch_command] ERROR - User is not logged in, access denied for command create_song
[DEBUG][create_song] STATUS=ERROR, TIME=0.0022s, TAG=EXPECTED, ERROR={"error_msg": "User is not logged in. Please log in to proceed."}

=== CONCURRENCY LOGIN (5 parallel) ===
[DEBUG][dispatch_command] START - command=register_user, args=['user03242@example.com', 'user03242', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user13244@example.com', 'user13244', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user23246@example.com', 'user23246', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user33248@example.com', 'user33248', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG][dispatch_command] START - command=register_user, args=['user43250@example.com', 'user43250', 'pass1234', '2000-01-01'], user_obj=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
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
[DEBUG] db_get_following result: [(95, 'user13244@example.com', 'user13244', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(97, 'user43250@example.com', 'user43250', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(96, 'user23246@example.com', 'user23246', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(94, 'user03242@example.com', 'user03242', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(97, 'user43250@example.com', 'user43250', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.5628s, TAG=OK, ERROR=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=login_user, args=['user43250', 'pass1234'], user_obj=None
[DEBUG] db_get_following result: [(96, 'user23246@example.com', 'user23246', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.5736s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['user23246', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(98, 'user33248@example.com', 'user33248', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(95, 'user13244@example.com', 'user13244', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.6501s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['user13244', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(97, 'user43250@example.com', 'user43250', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG][login_user] STATUS=OK, TIME=0.1163s, TAG=OK, ERROR=None
[DEBUG] db_get_following result: [(96, 'user23246@example.com', 'user23246', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1167s, TAG=OK, ERROR=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(98, 'user33248@example.com', 'user33248', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.7036s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['user33248', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(94, 'user03242@example.com', 'user03242', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][register_user] STATUS=OK, TIME=0.7495s, TAG=OK, ERROR=None
[DEBUG][dispatch_command] START - command=login_user, args=['user03242', 'pass1234'], user_obj=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(95, 'user13244@example.com', 'user13244', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.1049s, TAG=OK, ERROR=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(98, 'user33248@example.com', 'user33248', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.0884s, TAG=OK, ERROR=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(94, 'user03242@example.com', 'user03242', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][login_user] STATUS=OK, TIME=0.0805s, TAG=OK, ERROR=None
Got 5 tokens out of 5

=== TEST SUMMARY ===
Total commands: 43
Avg time per command: 1.1034s
Expected errors: 3 (ok)
Real errors: 0 (0.00%)
Total time: 47.45s

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>