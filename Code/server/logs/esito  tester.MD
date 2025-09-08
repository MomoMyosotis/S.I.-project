
# =========================================================================
#                                  TESTER
# =========================================================================

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>python tester.py

==================== SERVER MEGA TESTER ====================

==================== REGISTER / LOGIN - Happy path ====================
>> {"command": "register_user", "args": ["quackerina5228@example.com", "quackerina5228", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 49, "user_obj": {"id": 49, "username": "quackerina5228", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "b5a1e846549acfe088cec282a8fce1b9"}, "token": "b5a1e846549acfe088cec282a8fce1b9"}
>> {"command": "register_user", "args": ["bassettina5228@example.com", "bassettina5228", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 50, "user_obj": {"id": 50, "username": "bassettina5228", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "fde1c630412fff0f277ea74655c9699d"}, "token": "fde1c630412fff0f277ea74655c9699d"}
>> {"command": "login_user", "args": ["quackerina5228", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 49, "username": "quackerina5228", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "3e12b0defe5d51f77c1db232520e2c67", "error_msg": null}, "token": "3e12b0defe5d51f77c1db232520e2c67"}
>> {"command": "login_user", "args": ["bassettina5228", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 50, "username": "bassettina5228", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "3557607613d498fd6bb2df6ed9d1a4f1", "error_msg": null}, "token": "3557607613d498fd6bb2df6ed9d1a4f1"}
>> {"command": "login_user", "args": ["quackerina5228", "wrongpassword"]}
<< {"status": "OK", "response": {"status": "wrong_password", "user_obj": null, "error_msg": "WRONG_PASSWORD"}, "token": null}
>> {"command": "login_user", "args": ["nonexistent", "pass1234"]}
<< {"status": "OK", "response": {"status": "error", "user_obj": null, "error_msg": "404"}, "token": null}

==================== FOLLOW / FOLLOWERS / FOLLOWED ====================
>> {"command": "follow_user", "args": ["bassettina5228"], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": "FOLLOWED", "token": null}
>> {"command": "get_followed", "args": [], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": [{"id": 50, "username": "bassettina5228", "mail": "bassettina5228@example.com"}], "token": null}
>> {"command": "get_followers", "args": [], "token": "3557607613d498fd6bb2df6ed9d1a4f1"}
<< {"status": "OK", "response": [{"id": 49, "username": "quackerina5228", "mail": "quackerina5228@example.com"}], "token": null}
>> {"command": "unfollow_user", "args": ["bassettina5228"], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": "UNFOLLOWED", "token": null}
>> {"command": "get_followed", "args": [], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": [], "token": null}
>> {"command": "get_followers", "args": [], "token": "3557607613d498fd6bb2df6ed9d1a4f1"}
<< {"status": "OK", "response": [], "token": null}

==================== MEDIA CRUD - SONG ====================
>> {"command": "create_song", "args": [{"type": "song", "title": "Imagine", "year": 1971, "description": "Un classico immortale", "link": "https://example.com/imagine.mp3", "duration": 183, "location": "London", "additional_info": "John Lennon"}], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": 89, "token": null}
>> {"command": "get_song", "args": [89], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"id": 89, "title": "Imagine", "user_id": null, "year": 1971, "description": "Un classico immortale", "link": "https://example.com/imagine.mp3", "media_type": "song", "created_at": "2025-09-04T16:19:58.138796", "type": "song", "duration": 183, "location": "London", "additional_info": "John Lennon"}, "token": null}
>> {"command": "update_song", "args": [89, {"title": "Imagine (Remastered)"}], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"success": true}, "token": null}
>> {"command": "delete_song", "args": [89], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"success": true}, "token": null}

==================== MEDIA CRUD - DOCUMENT ====================
>> {"command": "create_document", "args": [{"type": "document", "title": "Resistenza", "year": 1958, "description": "Memorie di Primo Levi", "link": "https://example.com/resistenza.pdf"}], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": 90, "token": null}
>> {"command": "get_document", "args": [90], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"id": 90, "title": "Resistenza", "user_id": null, "year": 1958, "description": "Memorie di Primo Levi", "link": "https://example.com/resistenza.pdf", "media_type": "document", "created_at": "2025-09-04T16:19:58.922022", "type": "document", "format": null, "pages": null, "caption": null, "song_id": null}, "token": null}
>> {"command": "delete_document", "args": [90], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"success": true}, "token": null}

==================== MEDIA CRUD - VIDEO ====================
>> {"command": "create_video", "args": [{"type": "video", "title": "Metropolis", "year": 1927, "description": "Capolavoro di Fritz Lang", "link": "https://example.com/metropolis.mp4"}], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": 91, "token": null}
>> {"command": "get_video", "args": [91], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"id": 91, "title": "Metropolis", "user_id": null, "year": 1927, "description": "Capolavoro di Fritz Lang", "link": "https://example.com/metropolis.mp4", "media_type": "video", "created_at": "2025-09-04T16:19:59.697024", "type": "video", "duration": null, "location": null, "additional_info": null, "director": null}, "token": null}
>> {"command": "delete_video", "args": [91], "token": "3e12b0defe5d51f77c1db232520e2c67"}
<< {"status": "OK", "response": {"success": true}, "token": null}

==================== ACCESS WITHOUT LOGIN ====================
>> {"command": "get_followers", "args": []}
<< {"status": "OK", "response": {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": null}, "token": null}
[Expected error]  Expected 'ERROR: NOT_LOGGED_IN' in response but got: {"status": "OK", "response": {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": null}, "token": null}

==================== CONCURRENCY - 8 parallel logins ====================
>> {"command": "register_user", "args": ["user1821@example.com", "user1821", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 51, "user_obj": {"id": 51, "username": "user1821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "761144203a05f1420c6e1d3845f83617"}, "token": "761144203a05f1420c6e1d3845f83617"}
>> {"command": "register_user", "args": ["user3821@example.com", "user3821", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 53, "user_obj": {"id": 53, "username": "user3821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "904458c082620bedce3e67b5a0bbf7c7"}, "token": "904458c082620bedce3e67b5a0bbf7c7"}
>> {"command": "register_user", "args": ["user0821@example.com", "user0821", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 52, "user_obj": {"id": 52, "username": "user0821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "3b3cf316d1924494d1de2112ae65c3a0"}, "token": "3b3cf316d1924494d1de2112ae65c3a0"}
>> {"command": "register_user", "args": ["user6822@example.com", "user6822", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 56, "user_obj": {"id": 56, "username": "user6822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "269d3927f6a74162d3cc2ed5ebe81253"}, "token": "269d3927f6a74162d3cc2ed5ebe81253"}
>> {"command": "login_user", "args": ["user3821", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 53, "username": "user3821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "9539ea2ab5520b43b2400b8465920d38", "error_msg": null}, "token": "9539ea2ab5520b43b2400b8465920d38"}
>> {"command": "login_user", "args": ["user1821", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 51, "username": "user1821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "5b7cd8da8d1fc67188025848e56309cc", "error_msg": null}, "token": "5b7cd8da8d1fc67188025848e56309cc"}
>> {"command": "register_user", "args": ["user7822@example.com", "user7822", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 54, "user_obj": {"id": 54, "username": "user7822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "c8066e6f8b7ae7d9944b0d11855c63df"}, "token": "c8066e6f8b7ae7d9944b0d11855c63df"}
>> {"command": "register_user", "args": ["user2821@example.com", "user2821", "pass1234", "2000-01-01"]}
<<
 {"status": "OK", "response": {"status": "OK", "user_id": 55, "user_obj": {"id": 55, "username": "user2821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "4d9413ff77a03e06570dd7d775c0f465"}, "token": "4d9413ff77a03e06570dd7d775c0f465"}
>> {"command": "register_user", "args": ["user5822@example.com", "user5822", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 57, "user_obj": {"id": 57, "username": "user5822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "7411d82900ebeaeeeb5e809df9b7a01d"}, "token": "7411d82900ebeaeeeb5e809df9b7a01d"}
>> {"command": "login_user", "args": ["user0821", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 52, "username": "user0821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "fd143a79c768b681529bb3b06ec66abc", "error_msg": null}, "token": "fd143a79c768b681529bb3b06ec66abc"}
>> {"command": "register_user", "args": ["user4821@example.com", "user4821", "pass1234", "2000-01-01"]}
<< {"status": "OK", "response": {"status": "OK", "user_id": 58, "user_obj": {"id": 58, "username": "user4821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "401de918863d766e917211dce71b2f1e"}, "token": "401de918863d766e917211dce71b2f1e"}
>> {"command": "login_user", "args": ["user6822", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 56, "username": "user6822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "d9920ab9fb2e4cc170d19474833d250c", "error_msg": null}, "token": "d9920ab9fb2e4cc170d19474833d250c"}
>> {"command": "login_user", "args": ["user7822", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 54, "username": "user7822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "a1fa31fe44e4a8c732e9fc4b5df94486", "error_msg": null}, "token": "a1fa31fe44e4a8c732e9fc4b5df94486"}
>> {"command": "login_user", "args": ["user2821", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 55, "username": "user2821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "4f3119f235251a85f623274f4a8474e2", "error_msg": null}, "token": "4f3119f235251a85f623274f4a8474e2"}
>> {"command": "login_user", "args": ["user5822", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 57, "username": "user5822", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "050281dbd8f6b03e016c546aeb549544", "error_msg": null}, "token": "050281dbd8f6b03e016c546aeb549544"}
>> {"command": "login_user", "args": ["user4821", "pass1234"]}
<< {"status": "OK", "response": {"status": "accepted", "user_obj": {"id": 58, "username": "user4821", "birthday": "2000-01-01", "bio": "", "profile_pic": "", "followers_count": 0, "followed_count": 0, "lvl": 4}, "token": "18d018f9b56bd7fa1c1c4b4acce4767e", "error_msg": null}, "token": "18d018f9b56bd7fa1c1c4b4acce4767e"}
Got 8 tokens.

==================== DONE ====================

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>












# =========================================================================
#                                  SERVER
# =========================================================================


















server:

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>python main.py
Loading [SERVER]...

>> Server listening on 0.0.0.0:8000
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s) (49, 50)
[DEBUG] user_id is: 49 (type=<class 'int'>)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228', 'bassettina5228@example.com')]
[DEBUG] raw followed: [{'id': 50, 'username': 'bassettina5228', 'mail': 'bassettina5228@example.com'}]
[DEBUG] user_id is: 50 (type=<class 'int'>)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228', 'quackerina5228@example.com')]
[DEBUG] raw followers: [{'id': 49, 'username': 'quackerina5228', 'mail': 'quackerina5228@example.com'}]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(49, 'quackerina5228@example.com', 'quackerina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(50, 'bassettina5228@example.com', 'bassettina5228', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM user_follow WHERE follower_id=%s AND followed_id=%s (49, 50)
[DEBUG] user_id is: 49 (type=<class 'int'>)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] raw followed: []
[DEBUG] user_id is: 50 (type=<class 'int'>)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] raw followers: []
[DEBUG] create_song_services | user_id=49 data={'type': 'song', 'title': 'Imagine', 'year': 1971, 'description': 'Un classico immortale', 'link': 'https://example.com/imagine.mp3', 'duration': 183, 'location': 'London', 'additional_info': 'John Lennon'}
[DEBUG] create_media | media_data={'type': 'song', 'title': 'Imagine', 'year': 1971, 'description': 'Un classico immortale', 'link': 'https://example.com/imagine.mp3', 'duration': 183, 'location': 'London', 'additional_info': 'John Lennon'} child_table=songs child_columns=('duration', 'location', 'additional_info') child_values=(183, 'London', 'John Lennon')
[DEBUG] validate_media_data | media_data={'type': 'song', 'title': 'Imagine', 'year': 1971, 'description': 'Un classico immortale', 'link': 'https://example.com/imagine.mp3', 'duration': 183, 'location': 'London', 'additional_info': 'John Lennon'}
[DEBUG] create_media prepared fields: ('song', 'Imagine', None, 1971, 'Un classico immortale', 'https://example.com/imagine.mp3', datetime.datetime(2025, 9, 4, 16, 19, 58, 138796))
[DEBUG] create_media_db returned media_id=89
[DEBUG] create_song_services created song_id=89
[DEBUG] fetch_media | media_id=89, child_table=songs, child_fields=['duration', 'location', 'additional_info']
[DEBUG] fetch_one success: (89, 'song', None, 'Imagine', 1971, 'Un classico immortale', 'https://example.com/imagine.mp3', datetime.datetime(2025, 9, 4, 16, 19, 58, 138796), 183, 'London', 'John Lennon')
[DEBUG] fetch_media_db returned: {'id': 89, 'type': 'song', 'user_id': None, 'title': 'Imagine', 'year': 1971, 'description': 'Un classico immortale', 'link': 'https://example.com/imagine.mp3', 'created_at': datetime.datetime(2025, 9, 4, 16, 19, 58, 138796), 'duration': 183, 'location': 'London', 'additional_info': 'John Lennon'}
[DEBUG] update_object | media_type=media object_id=89 updates={'title': 'Imagine (Remastered)'}
[DEBUG]
 update_media | media_id=89, updates={'title': 'Imagine (Remastered)'}, table=media
[DEBUG] execute success: UPDATE media SET title=%s WHERE id=%s ('Imagine (Remastered)', 89)
[DEBUG] update_media_db returned: True
[DEBUG] delete_song_services | user_id={'id': 49, 'username': 'quackerina5228', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4} song_id=89
[DEBUG] delete_object | media_type=songs object_id=89
[DEBUG] delete_media | media_id=89
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (89,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (89,)
[DEBUG] execute success: DELETE FROM song_genres WHERE song_id=%s (89,)
[DEBUG] execute success: DELETE FROM song_authors WHERE song_id=%s (89,)
[DEBUG] execute success: DELETE FROM song_performances WHERE song_id=%s (89,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (89,)
[DEBUG] delete_media_db returned: True
[DEBUG] create_document_services | data={'type': 'document', 'title': 'Resistenza', 'year': 1958, 'description': 'Memorie di Primo Levi', 'link': 'https://example.com/resistenza.pdf'}
[DEBUG] create_media | media_data={'type': 'document', 'title': 'Resistenza', 'year': 1958, 'description': 'Memorie di Primo Levi', 'link': 'https://example.com/resistenza.pdf'} child_table=documents child_columns=('format', 'pages', 'caption', 'song_id') child_values=(None, None, None, None)
[DEBUG] validate_media_data | media_data={'type': 'document', 'title': 'Resistenza', 'year': 1958, 'description': 'Memorie di Primo Levi', 'link': 'https://example.com/resistenza.pdf'}
[DEBUG] create_media prepared fields: ('document', 'Resistenza', None, 1958, 'Memorie di Primo Levi', 'https://example.com/resistenza.pdf', datetime.datetime(2025, 9, 4, 16, 19, 58, 922022))
[DEBUG] create_media_db returned media_id=90
[DEBUG] create_document_services created doc_id=90
[DEBUG] get_document_services | user_id={'id': 49, 'username': 'quackerina5228', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4} doc_id=90
[DEBUG] fetch_media | media_id=90, child_table=documents, child_fields=None
[DEBUG] fetch_one success: (90, 'document', None, 'Resistenza', 1958, 'Memorie di Primo Levi', 'https://example.com/resistenza.pdf', datetime.datetime(2025, 9, 4, 16, 19, 58, 922022))
[DEBUG] fetch_media_db returned: {'id': 90, 'type': 'document', 'user_id': None, 'title': 'Resistenza', 'year': 1958, 'description': 'Memorie di Primo Levi', 'link': 'https://example.com/resistenza.pdf', 'created_at': datetime.datetime(2025, 9, 4, 16, 19, 58, 922022)}
[DEBUG] delete_document_services | user_id={'id': 49, 'username': 'quackerina5228', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4} doc_id=90
[DEBUG] delete_object | media_type=documents object_id=90
[DEBUG] delete_media | media_id=90
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (90,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (90,)
[DEBUG] execute success: DELETE FROM song_genres WHERE song_id=%s (90,)
[DEBUG] execute success: DELETE FROM song_authors WHERE song_id=%s (90,)
[DEBUG] execute success: DELETE FROM song_performances WHERE song_id=%s (90,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (90,)
[DEBUG] delete_media_db returned: True
[DEBUG] create_video_services | user_id=49 data={'type': 'video', 'title': 'Metropolis', 'year': 1927, 'description': 'Capolavoro di Fritz Lang', 'link': 'https://example.com/metropolis.mp4'}
[DEBUG] create_media | media_data={'type': 'video', 'title': 'Metropolis', 'year': 1927, 'description': 'Capolavoro di Fritz Lang', 'link': 'https://example.com/metropolis.mp4'} child_table=videos child_columns=('duration', 'location', 'additional_info', 'director') child_values=(None, None, None, None)
[DEBUG] validate_media_data | media_data={'type': 'video', 'title': 'Metropolis', 'year': 1927, 'description': 'Capolavoro di Fritz Lang', 'link': 'https://example.com/metropolis.mp4'}
[DEBUG] create_media prepared fields: ('video', 'Metropolis', None, 1927, 'Capolavoro di Fritz Lang', 'https://example.com/metropolis.mp4', datetime.datetime(2025, 9, 4, 16, 19, 59, 697024))
[DEBUG] create_media_db returned media_id=91
[DEBUG] create_video_services created video_id=91
[DEBUG] fetch_media | media_id=91, child_table=videos, child_fields=['duration', 'location', 'additional_info', 'director']
[DEBUG] fetch_one success: (91, 'video', None, 'Metropolis', 1927, 'Capolavoro di Fritz Lang', 'https://example.com/metropolis.mp4', datetime.datetime(2025, 9, 4, 16, 19, 59, 697024), None, None, None, None)
[DEBUG] fetch_media_db returned: {'id': 91, 'type': 'video', 'user_id': None, 'title': 'Metropolis', 'year': 1927, 'description': 'Capolavoro di Fritz Lang', 'link': 'https://example.com/metropolis.mp4', 'created_at': datetime.datetime(2025, 9, 4, 16, 19, 59, 697024), 'duration': None, 'location': None, 'additional_info': None, 'director': None}
[DEBUG] delete_video_services | user_id={'id': 49, 'username': 'quackerina5228', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4} video_id=91
[DEBUG] delete_object | media_type=videos object_id=91
[DEBUG] delete_media | media_id=91
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (91,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (91,)
[DEBUG] execute success: DELETE FROM song_genres WHERE song_id=%s (91,)
[DEBUG] execute success: DELETE FROM song_authors WHERE song_id=%s (91,)
[DEBUG] execute success: DELETE FROM song_performances WHERE song_id=%s (91,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (91,)
[DEBUG] delete_media_db returned: True
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
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(51, 'user1821@example.com', 'user1821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(53, 'user3821@example.com', 'user3821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(52, 'user0821@example.com', 'user0821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(56, 'user6822@example.com', 'user6822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(54, 'user7822@example.com', 'user7822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(51, 'user1821@example.com', 'user1821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(53, 'user3821@example.com', 'user3821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(57, 'user5822@example.com', 'user5822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(55, 'user2821@example.com', 'user2821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(58, 'user4821@example.com', 'user4821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(52, 'user0821@example.com', 'user0821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(56, 'user6822@example.com', 'user6822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(53, 'user3821@example.com', 'user3821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(51, 'user1821@example.com', 'user1821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f',
 datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(54, 'user7822@example.com', 'user7822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(55, 'user2821@example.com', 'user2821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(57, 'user5822@example.com', 'user5822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(52, 'user0821@example.com', 'user0821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(58, 'user4821@example.com', 'user4821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(56, 'user6822@example.com', 'user6822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(54, 'user7822@example.com', 'user7822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(55, 'user2821@example.com', 'user2821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(57, 'user5822@example.com', 'user5822', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(58, 'user4821@example.com', 'user4821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
c
Server closing...


C:\Users\LENOVO\Desktop\prj\I.S\Code\server>