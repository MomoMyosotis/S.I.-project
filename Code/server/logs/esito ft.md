[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1202, title=Media_7744>
[DEBUG][Media.from_dict] Built object=<Song id=1202, title=Media_7744>
[DEBUG][Media.fetch] Built object=<Song id=1202, title=Media_7744>
[DEBUG][Media.fetch] Data from DB={'id': 1248, 'type': 'song', 'user_id': 359, 'title': 'Media_5286', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 297012), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1248, 'type': 'song', 'user_id': 359, 'title': 'Media_5286', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 297012), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5286, type=song, year=2013, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: [(2051, 362, 1286, None, None, 'Commento 351', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2051, 'user_id': 362, 'media_id': 1286, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 351', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_one success: RealDictRow({'id': 353})
[DEBUG delete_comment] fetched comment: [{'id': 2037, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 314', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1200,)
[DEBUG][Media.from_dict] cls=Song, data={'id': 1193, 'type': 'song', 'user_id': 362, 'title': 'Media_5844', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 42, 884754), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(550, 358, 1206, 'regular', Decimal('3.69'), Decimal('7.90'), None, None, None, None, None, 'Nota aggiornata 534', None)]
[DEBUG][update_note] STATUS=OK, TIME=15.0800s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[558], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=361, note_id=558
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_5844, type=song, year=2023, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1248, title=Media_5286>
[DEBUG][Media.__init__] Finished -> <Song id=1193, title=Media_5844>
[DEBUG][Media.from_dict] Built object=<Song id=1248, title=Media_5286>
[DEBUG][Media.from_dict] Built object=<Song id=1193, title=Media_5844>
[DEBUG][Media.fetch] Built object=<Song id=1248, title=Media_5286>
[DEBUG][Media.fetch] Built object=<Song id=1193, title=Media_5844>
[DEBUG] fetch_one success: RealDictRow({'id': 1257, 'type': 'document', 'user_id': 355, 'title': 'Media_2596', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 48, 132347), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1257, 'type': 'document', 'user_id': 355, 'title': 'Media_2596', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 48, 132347), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2596, type=document, year=2006, user_id=355, kwargs={'id': 1257, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1257
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1257, title=Media_2596>
[DEBUG][Media.fetch] Built object=<Document id=1257, title=Media_2596>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(567, 361, 1272, 'regular', Decimal('1.28'), Decimal('9.25'), None, None, None, None, None, 'Nota 841', None)]
[DEBUG][get_object] Retrieved object=<Song id=1187, title=Media_3804>
[DEBUG][Media.to_dict] <Song id=1187, title=Media_3804> -> {'media_id': 1187, 'type': 'song', 'title': 'Media_3804', 'user_id': 353, 'year': 2023, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:33.183624', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][create_note] STATUS=OK, TIME=20.3879s, TAG=OK
[DEBUG][get_song] STATUS=OK, TIME=16.0514s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[567, 'Nota aggiornata 78'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][dispatch_command] START - command=delete_song, args=[1187], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=361, note_id=567
[DEBUG][delete_song_services] song_id=1187
[DEBUG][get_object] cls=Song, object_id=1187
[DEBUG][Media.fetch] Called cls=Song, media_id=1187
[DEBUG] fetch_one success: RealDictRow({'id': 1208, 'type': 'video', 'user_id': 358, 'title': 'Media_1239', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 51, 77282), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1208, 'type': 'video', 'user_id': 358, 'title': 'Media_1239', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 51, 77282), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1239, type=video, year=2007, user_id=358, kwargs={'id': 1208, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1208
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1208, title=Media_1239>
[DEBUG][Media.fetch] Built object=<Video id=1208, title=Media_1239>
[DEBUG][Media.delete] Deleted media_id=1145
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2050, 354, 1282, None, None, 'Aggiornato 425', datetime.date(2025, 9, 14))]
[DEBUG] fetch_one success: RealDictRow({'id': 1196, 'type': 'song', 'user_id': 357, 'title': 'Media_6446', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 45, 238709), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1196, 'type': 'song', 'user_id': 357, 'title': 'Media_6446', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 45, 238709), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1175, 'type': 'video', 'user_id': 356, 'title': 'Media_7778', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 23, 197101), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4946>
[DEBUG][delete_video] STATUS=OK, TIME=56.7435s, TAG=OK
[DEBUG][get_object] Retrieved object=<Document id=1184, title=Media_6376>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1159,)
[DEBUG][update_comment] STATUS=OK, TIME=17.5874s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2044], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 1247, 'type': 'document', 'user_id': 353, 'title': 'Media_8829', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 153020), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1224,)
[DEBUG delete_comment] fetched comment: [{'id': 2050, 'user_id': 354, 'media_id': 1282, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 425', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.from_dict] cls=Song, data={'id': 1196, 'type': 'song', 'user_id': 357, 'title': 'Media_6446', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 45, 238709), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1222, title=Media_4306>
[DEBUG][Media.to_dict] <Document id=1222, title=Media_4306> -> {'media_id': 1222, 'type': 'document', 'title': 'Media_4306', 'user_id': 353, 'year': 2004, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:05.055925', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][update_note] STATUS=OK, TIME=18.4768s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[557], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=358, note_id=557
[DEBUG][delete_object] Deleting object <Document id=1184, title=Media_6376>
[DEBUG][Media.delete] Called on <Document id=1184, title=Media_6376>
[DEBUG][Media.fetch] Data from DB={'id': 1247, 'type': 'document', 'user_id': 353, 'title': 'Media_8829', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 153020), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_document] STATUS=OK, TIME=8.1715s, TAG=OK
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 774', 2048)
[DEBUG][Media.__init__] Called with title=Media_8829, type=document, year=2015, user_id=353, kwargs={'id': 1247, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 1 rows
[DEBUG fetch_by_id] comment_id=2044
[DEBUG][Media.fetch] Data from DB={'id': 1175, 'type': 'video', 'user_id': 356, 'title': 'Media_7778', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 23, 197101), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][dispatch_command] START - command=delete_document, args=[1222], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2040,)
[DEBUG][update_note] STATUS=OK, TIME=14.9409s, TAG=OK
[DEBUG][Media.__init__] Called with title=Media_7778, type=video, year=2017, user_id=356, kwargs={'id': 1175, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(355, 'user242821@example.com', 'user242821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1283
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_6446, type=song, year=2013, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_object] cls=Document, object_id=1222
[DEBUG][Media.__init__] Extra attr: id=1175
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Commento 999', datetime.date(2025, 9, 14))]
[DEBUG] db_get_following result: []
[DEBUG][delete_comment] STATUS=OK, TIME=16.7118s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1273, 'regular', 2.4341281544119653, 4.627551979453271, None, None, None, None, 'Nota 495'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] Retrieved object=<Song id=1245, title=Media_1229>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1188,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1201,)
[DEBUG] fetch_one success: RealDictRow({'id': 1161})
[DEBUG][dispatch_command] START - command=delete_note, args=[559], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Called cls=Document, media_id=1222
[DEBUG] fetch_one success: RealDictRow({'id': 1250})
[DEBUG][Media.to_dict] <Song id=1245, title=Media_1229> -> {'media_id': 1245, 'type': 'song', 'title': 'Media_1229', 'user_id': 358, 'year': 2000, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:31.146355', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1218,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Extra attr: id=1247
[DEBUG][Media.delete] Deleted media_id=1200
[DEBUG] fetch_one success: RealDictRow({'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_song] STATUS=OK, TIME=15.1623s, TAG=OK
[DEBUG delete_note] START - user_id=360, note_id=559
[DEBUG][Media.__init__] Finished -> <Song id=1196, title=Media_6446>
[DEBUG] db_get_following result: [(562, 354, 1235, 'regular', Decimal('5.90'), Decimal('7.47'), None, None, None, None, None, 'Nota 797', None)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1214,)
[DEBUG] fetch_one success: RealDictRow({'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] Built object=<Song id=1196, title=Media_6446>
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_9035>
[DEBUG][Media.fetch] Data from DB={'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG __init__] Created Comment object: {'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999'}
[DEBUG] db_get_following result: [(2045, 356, 1285, None, None, 'Aggiornato 490', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2045, 'user_id': 356, 'media_id': 1285, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 490', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][delete_document] STATUS=OK, TIME=40.7286s, TAG=OK
[DEBUG][Media.from_dict] cls=Media, data={'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1230,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][dispatch_command] START - command=delete_song, args=[1245], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Called with title=Media_4856, type=video, year=2017, user_id=356, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1268, title=Media_4856>
[DEBUG][Media.from_dict] Built object=<Video id=1268, title=Media_4856>
[DEBUG][Media.fetch] Built object=<Song id=1196, title=Media_6446>
[DEBUG][Media.fetch] Built object=<Video id=1268, title=Media_4856>
ERROR:services.interventions_services:Invalid time range: start_time=6.737945194080259, end_time=0.4571736667862003
[DEBUG add_comment] Created Comment object from DB: {'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999'}
[DEBUG fetch_by_id] comment_id=2058
[DEBUG][Media.from_dict] cls=Media, data={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1272, type=song, year=2012, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][create_note] STATUS=OK, TIME=7.5455s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1175, title=Media_7778>
[DEBUG][Media.fetch] Built object=<Video id=1175, title=Media_7778>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][dispatch_command] START - command=get_video, args=[1268], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Finished -> <Document id=1247, title=Media_8829>
[DEBUG][Media.fetch] Built object=<Document id=1247, title=Media_8829>
[DEBUG] fetch_one success: RealDictRow({'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_song_services] song_id=1245
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2055, 354, 1290, None, None, 'Commento 867', datetime.date(2025, 9, 14))]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2054, 360, 1291, None, None, 'Commento 299', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1190,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1221, 'type': 'video', 'user_id': 359, 'title': 'Media_8477', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 4, 101006), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][get_object] cls=Song, object_id=1245
[DEBUG][Media.fetch] Data from DB={'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1197,)
[DEBUG] fetch_all returned 1 rows
[DEBUG from_dict] data={'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299'}
[DEBUG][Media.fetch] Called cls=Song, media_id=1245
[DEBUG][Media.from_dict] cls=Song, data={'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Song id=1269, title=Media_1272>
[DEBUG] db_get_following result: [(563, 354, 1236, 'regular', Decimal('7.08'), Decimal('8.53'), None, None, None, None, None, 'Nota 66', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG update_comment] update_comment_db result: True
[DEBUG][update_comment] STATUS=OK, TIME=12.3029s, TAG=OK
[DEBUG][get_object] cls=Video, object_id=1268
[DEBUG][Media.fetch] Called cls=Video, media_id=1268
[DEBUG] fetch_one success: RealDictRow({'id': 1295})
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1176,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2046, 361, 1299, None, None, 'Aggiornato 379', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Data from DB={'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5674, type=song, year=2001, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1210,)
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2046, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 379', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG __init__] Created Comment object: {'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867'}
[DEBUG][dispatch_command] START - command=delete_comment, args=[2048], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1221, 'type': 'video', 'user_id': 359, 'title': 'Media_8477', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 4, 101006), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(553, 358, 1234, 'regular', Decimal('2.51'), Decimal('7.83'), None, None, None, None, None, 'Nota aggiornata 243', None)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1140,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1165,)
[DEBUG][Media.from_dict] Built object=<Song id=1269, title=Media_1272>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1212, 'type': 'video', 'user_id': 361, 'title': 'Media_1601', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 551965), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG from_dict] data={'id': 2046, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 379', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.__init__] Called with title=Media_7196, type=song, year=2008, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_comment] STATUS=OK, TIME=15.2779s, TAG=OK
[DEBUG add_comment] new_id returned from DB: 2059
[DEBUG][create_comment] STATUS=OK, TIME=25.4473s, TAG=OK
[DEBUG __init__] Created Comment object: {'id': 2046, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 379'}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Data from DB={'id': 1212, 'type': 'video', 'user_id': 361, 'title': 'Media_1601', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 551965), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(2052, 359, 1287, None, None, 'Commento 743', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Video id=1254, title=Media_4949>
[DEBUG] fetch_one success: RealDictRow({'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Song id=1269, title=Media_1272>
[DEBUG][dispatch_command] START - command=create_comment, args=[1298, 'Commento 765'], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
ERROR:services.interventions_services:Invalid time range: start_time=1.3593225859021763, end_time=0.10799157755926325
[DEBUG][create_comment] STATUS=OK, TIME=28.9548s, TAG=OK
[DEBUG fetch_by_id] comment_id=2048
[DEBUG][Media.__init__] Called with title=Media_8477, type=video, year=2002, user_id=359, kwargs={'id': 1221, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1189, title=Media_7196>
[DEBUG update_comment] fetched comment: [{'id': 2052, 'user_id': 359, 'media_id': 1287, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 743', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1220,)
[DEBUG][Media.fetch] Data from DB={'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Media, media_id=1298
[DEBUG][create_note] STATUS=OK, TIME=6.1626s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1163,)
[DEBUG delete_comment] user_id=361, comment_id=2046
[DEBUG][Media.__init__] Finished -> <Song id=1239, title=Media_5674>
[DEBUG][Media.__init__] Called with title=Media_1601, type=video, year=2014, user_id=361, kwargs={'id': 1212, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1216,)
[DEBUG][Media.to_dict] <Video id=1254, title=Media_4949> -> {'media_id': 1254, 'type': 'video', 'title': 'Media_4949', 'user_id': 361, 'year': 2005, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:38.620565', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][dispatch_command] START - command=update_comment, args=[2054, 'Aggiornato 540'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2054
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: id=1221
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1170,)
[DEBUG][Media.from_dict] Built object=<Song id=1189, title=Media_7196>
[DEBUG][get_video] STATUS=OK, TIME=20.5371s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1254], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1254
[DEBUG] fetch_one success: RealDictRow({'id': 1275, 'type': 'video', 'user_id': 356, 'title': 'Media_4617', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 6, 153114), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] Built object=<Song id=1239, title=Media_5674>
[DEBUG][Media.__init__] Extra attr: id=1212
[DEBUG][Media.fetch] Built object=<Song id=1189, title=Media_7196>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(554, 357, 1225, 'regular', Decimal('4.29'), Decimal('4.44'), None, None, None, None, None, 'Nota aggiornata 665', None)]
[DEBUG][Media.fetch] Called cls=Video, media_id=1254
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1275, 'type': 'video', 'user_id': 356, 'title': 'Media_4617', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 6, 153114), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][dispatch_command] START - command=get_song, args=[1269], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(2047, 360, 1279, None, None, 'Aggiornato 15', datetime.date(2025, 9, 14))]
[DEBUG] fetch_one success: RealDictRow({'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Song id=1239, title=Media_5674>
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] cls=Song, data={'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6052, type=song, year=2004, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Data from DB={'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2047, 'user_id': 360, 'media_id': 1279, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 15', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Data from DB={'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(548, 357, 1231, 'regular', Decimal('1.87'), Decimal('9.99'), None, None, None, None, None, 'Nota aggiornata 335', None)]
[DEBUG] db_get_following result: [(555, 362, 1217, 'regular', Decimal('1.23'), Decimal('4.61'), None, None, None, None, None, 'Nota aggiornata 811', None)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][dispatch_command] START - command=update_comment, args=[2055, 'Aggiornato 434'], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1262, 'type': 'document', 'user_id': 356, 'title': 'Media_1728', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 53, 518516), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] cls=Media, data={'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1339, type=document, year=2018, user_id=356, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1187, 'type': 'song', 'user_id': 353, 'title': 'Media_3804', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 183624), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2056, 360, 1293, None, None, 'Commento 137', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Document id=1215, title=Media_7685>
[DEBUG][Media.to_dict] <Document id=1215, title=Media_7685> -> {'media_id': 1215, 'type': 'document', 'title': 'Media_7685', 'user_id': 353, 'year': 2002, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:57.639054', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=11.2733s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1215], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1215
[DEBUG][Media.fetch] Called cls=Document, media_id=1215
[DEBUG][Media.__init__] Finished -> <Video id=1212, title=Media_1601>
[DEBUG][Media.fetch] Built object=<Video id=1212, title=Media_1601>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Data from DB={'id': 1187, 'type': 'song', 'user_id': 353, 'title': 'Media_3804', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 183624), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1187, 'type': 'song', 'user_id': 353, 'title': 'Media_3804', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 183624), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1207, title=Media_6052>
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Data from DB={'id': 1262, 'type': 'document', 'user_id': 356, 'title': 'Media_1728', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 53, 518516), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Media, media_id=1270
[DEBUG][Media.__init__] Called with title=Media_3804, type=song, year=2023, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Called cls=Media, media_id=1277
[DEBUG][Media.from_dict] cls=Media, data={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3540, type=song, year=2008, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1152,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_1728, type=document, year=2023, user_id=356, kwargs={'id': 1262, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1221, title=Media_8477>
[DEBUG] fetch_one success: RealDictRow({'id': 1255, 'type': 'video', 'user_id': 356, 'title': 'Media_8372', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 39, 710774), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1187, title=Media_3804>
[DEBUG][Media.from_dict] Built object=<Song id=1187, title=Media_3804>
[DEBUG][Media.fetch] Built object=<Song id=1187, title=Media_3804>
[DEBUG fetch_by_id] comment_id=2055
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_7642, type=document, year=2006, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Video id=1221, title=Media_8477>
[DEBUG] fetch_one success: RealDictRow({'id': 1266})
[DEBUG][Media.fetch] Data from DB={'id': 1255, 'type': 'video', 'user_id': 356, 'title': 'Media_8372', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 39, 710774), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG from_dict] data={'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG from_dict] data={'id': 2047, 'user_id': 360, 'media_id': 1279, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 15', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.__init__] Called with title=Media_4617, type=video, year=2007, user_id=356, kwargs={'id': 1275, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_song_services] song_id=1269
[DEBUG][get_object] Retrieved object=<Document id=1243, title=Media_2864>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1158,)
[DEBUG][Media.delete] Deleted media_id=1197
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1205,)
[DEBUG][Media.from_dict] Built object=<Song id=1207, title=Media_6052>
[DEBUG] fetch_one success: RealDictRow({'id': 1249, 'type': 'video', 'user_id': 359, 'title': 'Media_4002', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 434745), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 858', 2051)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2043, 357, 1278, None, None, 'Aggiornato 776', datetime.date(2025, 9, 14))]
[DEBUG __init__] Created Comment object: {'id': 2047, 'user_id': 360, 'media_id': 1279, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 15'}
[DEBUG][Media.__init__] Extra attr: id=1275
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_object] cls=Song, object_id=1269
[DEBUG][delete_object] Deleting object <Document id=1243, title=Media_2864>
[DEBUG][Media.__init__] Called with title=Media_8372, type=video, year=2012, user_id=356, kwargs={'id': 1255, 'recording_date': None, 'performer_id': None}
[DEBUG __init__] Created Comment object: {'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137'}
[DEBUG][Media.fetch] Built object=<Song id=1207, title=Media_6052>
[DEBUG] fetch_one success: RealDictRow({'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(2049, 360, 1280, None, None, 'Aggiornato 268', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Data from DB={'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6866, type=song, year=2000, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1274, title=Media_6866>
[DEBUG][Media.from_dict] Built object=<Song id=1274, title=Media_6866>
[DEBUG][Media.fetch] Data from DB={'id': 1249, 'type': 'video', 'user_id': 359, 'title': 'Media_4002', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 434745), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4002, type=video, year=2022, user_id=359, kwargs={'id': 1249, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(562, 354, 1235, 'regular', Decimal('5.90'), Decimal('7.47'), None, None, None, None, None, 'Nota 797', None)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1174,)
[DEBUG delete_comment] fetched comment: [{'id': 2049, 'user_id': 360, 'media_id': 1280, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 268', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Extra attr: id=1262
[DEBUG delete_comment] user_id=360, comment_id=2047
[DEBUG][Media.__init__] Finished -> <Document id=1258, title=Media_1339>
[DEBUG][Media.from_dict] Built object=<Document id=1258, title=Media_1339>
[DEBUG] fetch_one success: RealDictRow({'id': 1289})
[DEBUG][Media.fetch] Data from DB={'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: id=1249
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][create_comment] STATUS=OK, TIME=21.5214s, TAG=OK
[DEBUG][dispatch_command] START - command=update_comment, args=[2056, 'Aggiornato 737'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG delete_comment] fetched comment: [{'id': 2043, 'user_id': 357, 'media_id': 1278, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 776', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(568, 359, 1238, 'regular', Decimal('2.14'), Decimal('2.56'), None, None, None, None, None, 'Nota 262', None)]
[DEBUG][create_note] STATUS=OK, TIME=29.5089s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Built object=<Document id=1258, title=Media_1339>
ERROR:services.interventions_services:Invalid time range: start_time=7.534318381915506, end_time=5.609885899540968
[DEBUG][Media.delete] Called on <Document id=1243, title=Media_2864>
[DEBUG][Media.__init__] Extra attr: id=1255
[DEBUG] fetch_one success: RealDictRow({'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG add_comment] new_id returned from DB: 2060
[DEBUG][get_object] Retrieved object=<Video id=1154, title=Media_7050>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1226, 'type': 'document', 'user_id': 361, 'title': 'Media_6653', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 794387), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Built object=<Song id=1274, title=Media_6866>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1166,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1176,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][dispatch_command] START - command=update_note, args=[568, 'Nota aggiornata 218'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5121>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleting object <Video id=1154, title=Media_7050>
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Video id=1249, title=Media_4002>
[DEBUG][Media.fetch] Built object=<Video id=1249, title=Media_4002>
[DEBUG fetch_by_id] comment_id=2056
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 359})
[DEBUG] fetch_one success: RealDictRow({'id': 1185, 'type': 'song', 'user_id': 355, 'title': 'Media_4277', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 32, 934546), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1185, 'type': 'song', 'user_id': 355, 'title': 'Media_4277', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 32, 934546), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1185, 'type': 'song', 'user_id': 355, 'title': 'Media_4277', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 32, 934546), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4277, type=song, year=2004, user_id=355, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Data from DB={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG update_comment] update_comment_db result: True
[DEBUG][update_comment] STATUS=OK, TIME=9.4917s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Song id=1260, title=Media_3540>
[DEBUG] fetch_one success: RealDictRow({'id': 1184})
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1204,)
[DEBUG][Media.__init__] Finished -> <Document id=1271, title=Media_7642>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (552,)
[DEBUG][Media.__init__] Finished -> <Video id=1275, title=Media_4617>
[DEBUG] fetch_one success: RealDictRow({'id': 1261, 'type': 'song', 'user_id': 357, 'title': 'Media_1015', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 405931), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Called cls=Song, media_id=1269
[DEBUG][Media.fetch] Data from DB={'id': 1261, 'type': 'song', 'user_id': 357, 'title': 'Media_1015', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 405931), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.from_dict] Built object=<Song id=1260, title=Media_3540>
[DEBUG][Media.fetch] Built object=<Song id=1260, title=Media_3540>
ERROR:services.interventions_services:Invalid time range: start_time=7.008490260477248, end_time=4.6386447055903375
[DEBUG][Media.from_dict] Built object=<Document id=1271, title=Media_7642>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1245, 'type': 'song', 'user_id': 358, 'title': 'Media_1229', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 146355), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Video id=1275, title=Media_4617>
[DEBUG][create_note] STATUS=OK, TIME=9.7722s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1258], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_1505, type=video, year=2011, user_id=355, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 304', 560)
[DEBUG][dispatch_command] START - command=delete_comment, args=[2051], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (548,)
[DEBUG] db_get_following result: [(2053, 359, 1292, None, None, 'Commento 314', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 314', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 314', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_object] Retrieved object=<Song id=1191, title=Media_9555>
[DEBUG][Media.from_dict] cls=Media, data={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.delete] Called on <Video id=1154, title=Media_7050>
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(565, 356, 1246, 'regular', Decimal('0.22'), Decimal('7.12'), None, None, None, None, None, 'Nota 580', None)]
[DEBUG][Media.fetch] Data from DB={'id': 1226, 'type': 'document', 'user_id': 361, 'title': 'Media_6653', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 794387), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6653, type=document, year=2009, user_id=361, kwargs={'id': 1226, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1230,)
[DEBUG __init__] Created Comment object: {'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 314'}
[DEBUG update_note] START - user_id=359, note_id=568
[DEBUG][Media.from_dict] cls=Song, data={'id': 1261, 'type': 'song', 'user_id': 357, 'title': 'Media_1015', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 405931), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][delete_object] Deleting object <Song id=1191, title=Media_9555>
[DEBUG][Media.__init__] Called with title=Media_5342, type=document, year=2004, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Finished -> <Video id=1267, title=Media_1505>
[DEBUG fetch_by_id] comment_id=2051
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1219,)
[DEBUG delete_comment] fetched media: {'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1172,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Built object=<Document id=1271, title=Media_7642>
[DEBUG] db_get_following result: [(564, 361, 1233, 'regular', Decimal('5.40'), Decimal('9.43'), None, None, None, None, None, 'Nota 439', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1163,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Video id=1255, title=Media_8372>
[DEBUG][Media.fetch] Built object=<Video id=1255, title=Media_8372>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(561, 358, 1256, 'regular', Decimal('1.79'), Decimal('6.30'), None, None, None, None, None, 'Nota 381', None)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1209,)
[DEBUG][create_note] STATUS=OK, TIME=7.6875s, TAG=OK
[DEBUG][delete_note] STATUS=OK, TIME=14.1600s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1227,)
[DEBUG][Media.__init__] Extra attr: id=1226
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG update_comment] user_id=359, comment_id=2053, new_text=Aggiornato 998
[DEBUG][Media.__init__] Finished -> <Song id=1185, title=Media_4277>
[DEBUG][get_object] cls=Document, object_id=1258
[DEBUG][get_object] Retrieved object=<Document id=1199, title=Media_7671>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1142,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1190,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1151,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1214,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 319', 563)
[DEBUG][Media.from_dict] Built object=<Song id=1185, title=Media_4277>
[DEBUG][update_note] STATUS=OK, TIME=15.6751s, TAG=OK
[DEBUG][Media.fetch] Called cls=Document, media_id=1258
[DEBUG][Media.from_dict] Built object=<Video id=1267, title=Media_1505>
[DEBUG][delete_note] STATUS=OK, TIME=12.3271s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Commento 262', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1179,)
[DEBUG][dispatch_command] START - command=get_video, args=[1223], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1245, 'type': 'song', 'user_id': 358, 'title': 'Media_1229', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 146355), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_document] STATUS=OK, TIME=46.2934s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1161,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Song id=1185, title=Media_4277>
[DEBUG][dispatch_command] START - command=delete_note, args=[560], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1201,)
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2041,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Document id=1296, title=Media_5342>
[DEBUG] db_get_following result: [(570, 359, 1266, 'regular', Decimal('5.06'), Decimal('5.38'), None, None, None, None, None, 'Nota 466', None)]
[DEBUG][get_object] cls=Video, object_id=1223
[DEBUG][Media.from_dict] cls=Song, data={'id': 1245, 'type': 'song', 'user_id': 358, 'title': 'Media_1229', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 146355), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1229, type=song, year=2000, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_one success: RealDictRow({'id': 1222, 'type': 'document', 'user_id': 353, 'title': 'Media_4306', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 5, 55925), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.delete] Called on <Song id=1191, title=Media_9555>
[DEBUG][Media.fetch] Data from DB={'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4856, type=video, year=2017, user_id=356, kwargs={'id': 1268, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG delete_note] START - user_id=356, note_id=560
[DEBUG][dispatch_command] START - command=get_video, args=[1231], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.from_dict] Built object=<Document id=1296, title=Media_5342>
[DEBUG][Media.fetch] Built object=<Document id=1296, title=Media_5342>
[DEBUG][Media.fetch] Called cls=Video, media_id=1223
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Song id=1245, title=Media_1229>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1222, 'type': 'document', 'user_id': 353, 'title': 'Media_4306', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 5, 55925), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: id=1268
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1254, 'type': 'video', 'user_id': 361, 'title': 'Media_4949', 'year': 2005, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 38, 620565), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Video id=1267, title=Media_1505>
ERROR:services.interventions_services:Invalid time range: start_time=6.295506379769976, end_time=4.734426499780552
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 353})
[DEBUG][get_object] cls=Video, object_id=1231
[DEBUG][Media.fetch] Called cls=Video, media_id=1231
[DEBUG][create_note] STATUS=OK, TIME=15.2048s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1224,)
[DEBUG add_comment] START - user_id=361, text=Commento 18, media_id=1296, note_id=None, parent_comment_id=None
[DEBUG][Media.__init__] Called with title=Media_1015, type=song, year=2024, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Data from DB={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1140,)
[DEBUG][Media.delete] Deleted media_id=1209
[DEBUG] db_get_following result: [(550, 358, 1206, 'regular', Decimal('3.69'), Decimal('7.90'), None, None, None, None, None, 'Nota aggiornata 534', None)]
[DEBUG][Media.__init__] Called with title=Media_4306, type=document, year=2004, user_id=353, kwargs={'id': 1222, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1268, title=Media_4856>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1158,)
[DEBUG][Media.delete] Deleted media_id=1214
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4849>
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1159,)
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=get_song, args=[1260], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][dispatch_command] START - command=update_note, args=[570, 'Nota aggiornata 142'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1170,)
[DEBUG] db_get_following result: [(569, 360, 1250, 'regular', Decimal('1.81'), Decimal('5.26'), None, None, None, None, None, 'Nota 860', None)]
[DEBUG] db_get_following result: [(554, 357, 1225, 'regular', Decimal('4.29'), Decimal('4.44'), None, None, None, None, None, 'Nota aggiornata 665', None)]
[DEBUG] db_get_following result: [(2057, 358, 1294, None, None, 'Commento 380', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched media: {'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(2054, 360, 1291, None, None, 'Commento 299', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1218,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1254, 'type': 'video', 'user_id': 361, 'title': 'Media_4949', 'year': 2005, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 38, 620565), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_video] STATUS=OK, TIME=44.2761s, TAG=OK
[DEBUG] db_get_following result: [(557, 358, 1242, 'regular', Decimal('0.71'), Decimal('3.51'), None, None, None, None, None, 'Nota aggiornata 666', None)]
[DEBUG] db_get_following result: []
[DEBUG][get_song_services] song_id=1260
[DEBUG __init__] Created Comment object: {'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262'}
[DEBUG update_note] START - user_id=359, note_id=570
[DEBUG][Media.__init__] Finished -> <Document id=1226, title=Media_6653>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][create_note] STATUS=OK, TIME=27.3348s, TAG=OK
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1216,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1152,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1220,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.delete] Deleted media_id=1190
[DEBUG][get_object] Retrieved object=<Song id=1195, title=Media_5890>
[DEBUG][Media.__init__] Called with title=Media_4949, type=video, year=2005, user_id=361, kwargs={'id': 1254, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (553,)
[DEBUG][Media.__init__] Finished -> <Document id=1262, title=Media_1728>
[DEBUG] fetch_all returned 1 rows
[DEBUG][update_note] STATUS=OK, TIME=12.3847s, TAG=OK
[DEBUG][Media.fetch] Built object=<Document id=1226, title=Media_6653>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6956>
[DEBUG][Media.__init__] Extra attr: id=1222
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.to_dict] <Document id=1199, title=Media_7671> -> {'media_id': 1199, 'type': 'document', 'title': 'Media_7671', 'user_id': 355, 'year': 2010, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:45.870444', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_one success: RealDictRow({'id': 356})
[DEBUG][Media.fetch] Built object=<Video id=1268, title=Media_4856>
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: [(2044, 359, 1281, None, None, 'Aggiornato 273', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2044, 'user_id': 359, 'media_id': 1281, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 273', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][delete_object] Deleting object <Song id=1195, title=Media_5890>
[DEBUG][Media.__init__] Extra attr: id=1254
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG add_comment] Created Comment object from DB: {'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262'}
[DEBUG] fetch_one success: RealDictRow({'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] cls=Media, data={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Finished -> <Song id=1261, title=Media_1015>
[DEBUG][delete_document] STATUS=OK, TIME=47.5795s, TAG=OK
[DEBUG from_dict] data={'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_document] STATUS=OK, TIME=15.1893s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299'}
[DEBUG update_comment] user_id=360, comment_id=2054, new_text=Aggiornato 540
[DEBUG from_dict] data={'id': 2044, 'user_id': 359, 'media_id': 1281, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 273', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2044, 'user_id': 359, 'media_id': 1281, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 273'}
[DEBUG delete_comment] user_id=359, comment_id=2044
[DEBUG] fetch_one success: RealDictRow({'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][dispatch_command] START - command=delete_note, args=[563], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_5839, type=song, year=2021, user_id=355, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.from_dict] Built object=<Song id=1261, title=Media_1015>
[DEBUG delete_comment] fetched media: {'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG __init__] Created Comment object: {'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380'}
[DEBUG][Media.__init__] Finished -> <Document id=1222, title=Media_4306>
[DEBUG][dispatch_command] START - command=delete_document, args=[1199], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_2104>
[DEBUG][create_note] STATUS=OK, TIME=8.9067s, TAG=OK
[DEBUG][Media.delete] Called on <Song id=1195, title=Media_5890>
[DEBUG][Media.fetch] Built object=<Document id=1262, title=Media_1728>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1230,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Video id=1254, title=Media_4949>
[DEBUG delete_comment] fetched media: {'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_comment] STATUS=OK, TIME=16.0264s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[569, 'Nota aggiornata 304'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(566, 354, 1253, 'regular', Decimal('0.26'), Decimal('5.16'), None, None, None, None, None, 'Nota 489', None)]
[DEBUG][create_comment] STATUS=OK, TIME=21.6059s, TAG=OK
[DEBUG][Media.fetch] Built object=<Document id=1222, title=Media_4306>
[DEBUG][get_object] cls=Document, object_id=1199
[DEBUG] db_get_following result: []
[DEBUG][delete_video] STATUS=OK, TIME=44.4262s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1267], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG fetch_by_id] comment_id=2059
[DEBUG][Media.from_dict] Built object=<Song id=1245, title=Media_1229>
[DEBUG delete_note] START - user_id=354, note_id=563
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Built object=<Song id=1261, title=Media_1015>
[DEBUG update_note] START - user_id=360, note_id=569
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Document, media_id=1199
[DEBUG][get_object] Retrieved object=<Document id=1213, title=Media_9014>
[DEBUG][Media.to_dict] <Document id=1213, title=Media_9014> -> {'media_id': 1213, 'type': 'document', 'title': 'Media_9014', 'user_id': 360, 'year': 2014, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:56.649200', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=13.3171s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1213], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1213
[DEBUG][Media.fetch] Called cls=Document, media_id=1213
[DEBUG] fetch_one success: RealDictRow({'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][get_object] Retrieved object=<Document id=1259, title=Media_8102>
[DEBUG][get_object] cls=Song, object_id=1260
[DEBUG] fetch_one success: RealDictRow({'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1215, 'type': 'document', 'user_id': 353, 'title': 'Media_7685', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 57, 639054), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Built object=<Song id=1245, title=Media_1229>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Commento 101', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Document id=1252, title=Media_4944>
[DEBUG][Media.__init__] Called with title=Media_3487, type=video, year=2003, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] cls=Video, object_id=1267
[DEBUG][Media.fetch] Called cls=Video, media_id=1267
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2048, 358, 1284, None, None, 'Aggiornato 774', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2048, 'user_id': 358, 'media_id': 1284, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 774', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1210,)
[DEBUG] db_get_following result: [(2053, 359, 1292, None, None, 'Commento 314', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1165,)
[DEBUG][dispatch_command] START - command=create_note, args=[1276, 'regular', 0.264438583413904, 5.657164062597042, None, None, None, None, 'Nota 690'], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.to_dict] <Document id=1252, title=Media_4944> -> {'media_id': 1252, 'type': 'document', 'title': 'Media_4944', 'user_id': 354, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:33.755124', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: [(2047, 360, 1279, None, None, 'Aggiornato 15', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Called cls=Song, media_id=1260
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Built object=<Video id=1254, title=Media_4949>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1154})
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_note] STATUS=OK, TIME=14.3675s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1234], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1234
[DEBUG][Media.fetch] Called cls=Video, media_id=1234
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.to_dict] <Document id=1259, title=Media_8102> -> {'media_id': 1259, 'type': 'document', 'title': 'Media_8102', 'user_id': 354, 'year': 2006, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:50.222384', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.fetch] Called cls=Media, media_id=1273
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1229, title=Media_5660>
[DEBUG][Media.fetch] Data from DB={'id': 1215, 'type': 'document', 'user_id': 353, 'title': 'Media_7685', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 57, 639054), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7685, type=document, year=2002, user_id=353, kwargs={'id': 1215, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1168,)
[DEBUG] db_get_following result: []
[DEBUG update_comment] fetched comment: [{'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 314', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_document] STATUS=OK, TIME=10.2836s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1252], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1252
[DEBUG][Media.fetch] Data from DB={'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(565, 356, 1246, 'regular', Decimal('0.22'), Decimal('7.12'), None, None, None, None, None, 'Nota 580', None)]
[DEBUG][delete_object] Deleting object <Video id=1229, title=Media_5660>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Commento 999', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Document id=1257, title=Media_2596>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(2046, 361, 1299, None, None, 'Aggiornato 379', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1298, title=Media_3487>
[DEBUG][Media.fetch] Called cls=Document, media_id=1252
[DEBUG][Media.__init__] Called with title=Media_1339, type=document, year=2018, user_id=356, kwargs={'id': 1258, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1219,)
[DEBUG][Media.__init__] Extra attr: id=1215
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG __init__] Created Comment object: {'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101'}
[DEBUG add_comment] Created Comment object from DB: {'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101'}
[DEBUG fetch_by_id] comment_id=2060
[DEBUG][get_document] STATUS=OK, TIME=11.3319s, TAG=OK
[DEBUG][Media.from_dict] Built object=<Video id=1298, title=Media_3487>
[DEBUG from_dict] data={'id': 2048, 'user_id': 358, 'media_id': 1284, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 774', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.delete] Called on <Video id=1229, title=Media_5660>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(556, 353, 1237, 'regular', Decimal('0.46'), Decimal('6.27'), None, None, None, None, None, 'Nota aggiornata 424', None)]
[DEBUG][Media.to_dict] <Document id=1257, title=Media_2596> -> {'media_id': 1257, 'type': 'document', 'title': 'Media_2596', 'user_id': 355, 'year': 2006, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:48.132347', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG delete_comment] fetched comment: [{'id': 2046, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 379', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG delete_comment] fetched comment: [{'id': 2047, 'user_id': 360, 'media_id': 1279, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 15', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Built object=<Video id=1298, title=Media_3487>
[DEBUG add_comment] START - user_id=357, text=Commento 765, media_id=1298, note_id=None, parent_comment_id=None
[DEBUG][dispatch_command] START - command=update_comment, args=[2057, 'Aggiornato 868'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1163,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1241, title=Media_3285>
[DEBUG][delete_object] Deleting object <Song id=1241, title=Media_3285>
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 235', 561)
[DEBUG][get_document] STATUS=OK, TIME=9.6199s, TAG=OK
[DEBUG __init__] Created Comment object: {'id': 2048, 'user_id': 358, 'media_id': 1284, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 774'}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(2051, 362, 1286, None, None, 'Aggiornato 858', datetime.date(2025, 9, 14))]
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_document, args=[1259], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1259
[DEBUG][Media.fetch] Called cls=Document, media_id=1259
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_document, args=[1257], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1257
[DEBUG][Media.__init__] Finished -> <Document id=1215, title=Media_7685>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1244})
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2051, 'user_id': 362, 'media_id': 1286, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 858', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 647', 2052)
[DEBUG][get_object] Retrieved object=<Document id=1263, title=Media_1895>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1251, title=Media_8570>
[DEBUG][delete_object] Deleting object <Video id=1251, title=Media_8570>
[DEBUG][Media.delete] Called on <Video id=1251, title=Media_8570>
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 670', 564)
[DEBUG][Media.delete] Called on <Song id=1241, title=Media_3285>
[DEBUG][Media.delete] Deleted media_id=1165
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: id=1258
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1179,)
[DEBUG fetch_by_id] comment_id=2057
[DEBUG delete_comment] user_id=358, comment_id=2048
[DEBUG] fetch_one success: RealDictRow({'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Document id=1215, title=Media_7685>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1166,)
[DEBUG] fetch_one success: RealDictRow({'id': 1223, 'type': 'video', 'user_id': 360, 'title': 'Media_4797', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 6, 720637), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG from_dict] data={'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999'}
[DEBUG] db_get_following result: [(2055, 354, 1290, None, None, 'Commento 867', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1227,)
[DEBUG] fetch_one success: RealDictRow({'id': 1264})
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Data from DB={'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1184,)
[DEBUG from_dict] data={'id': 2051, 'user_id': 362, 'media_id': 1286, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 858', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_2304>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1224,)
[DEBUG][update_note] STATUS=OK, TIME=16.9120s, TAG=OK
[DEBUG][create_comment] STATUS=OK, TIME=31.5627s, TAG=OK
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1188,)
[DEBUG][Media.fetch] Called cls=Document, media_id=1257
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2037,)
[DEBUG] fetch_one success: RealDictRow({'id': 1191})
[DEBUG][get_object] Retrieved object=<Song id=1186, title=Media_1608>
[DEBUG][delete_song] STATUS=OK, TIME=53.7178s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1265})
[DEBUG][Media.to_dict] <Document id=1263, title=Media_1895> -> {'media_id': 1263, 'type': 'document', 'title': 'Media_1895', 'user_id': 356, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:56.255845', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1174,)
[DEBUG][Media.fetch] Data from DB={'id': 1223, 'type': 'video', 'user_id': 360, 'title': 'Media_4797', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 6, 720637), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Finished -> <Song id=1283, title=Media_5839>
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=update_comment, args=[2058, 'Aggiornato 77'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG from_dict] data={'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1205,)
[DEBUG][Media.from_dict] cls=Media, data={'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4797, type=video, year=2023, user_id=360, kwargs={'id': 1223, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.from_dict] Built object=<Song id=1283, title=Media_5839>
[DEBUG] db_get_following result: []
[DEBUG fetch_by_id] comment_id=2058
[DEBUG __init__] Created Comment object: {'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867'}
[DEBUG __init__] Created Comment object: {'id': 2051, 'user_id': 362, 'media_id': 1286, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 858'}
[DEBUG][Media.to_dict] <Song id=1186, title=Media_1608> -> {'media_id': 1186, 'type': 'song', 'title': 'Media_1608', 'user_id': 354, 'year': 2000, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:33.171382', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][dispatch_command] START - command=delete_note, args=[561], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_document] STATUS=OK, TIME=10.6709s, TAG=OK
[DEBUG][Media.__init__] Finished -> <Document id=1258, title=Media_1339>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_8066, type=document, year=2015, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1223
[DEBUG][Media.fetch] Built object=<Song id=1283, title=Media_5839>
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG update_comment] user_id=354, comment_id=2055, new_text=Aggiornato 434
[DEBUG][get_song] STATUS=OK, TIME=19.3334s, TAG=OK
[DEBUG delete_note] START - user_id=358, note_id=561
[DEBUG][Media.fetch] Built object=<Document id=1258, title=Media_1339>
[DEBUG delete_comment] user_id=362, comment_id=2051
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][dispatch_command] START - command=delete_song, args=[1186], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2056, 360, 1293, None, None, 'Commento 137', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][get_object] Retrieved object=<Song id=1193, title=Media_5844>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][delete_song_services] song_id=1186
[DEBUG][get_object] cls=Song, object_id=1186
[DEBUG][Media.fetch] Called cls=Song, media_id=1186
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.to_dict] <Song id=1193, title=Media_5844> -> {'media_id': 1193, 'type': 'song', 'title': 'Media_5844', 'user_id': 362, 'year': 2023, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:42.884754', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=8.5596s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1193], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][dispatch_command] START - command=delete_document, args=[1263], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (554,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG from_dict] data={'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_all returned 1 rows
[DEBUG][update_note] STATUS=OK, TIME=14.7907s, TAG=OK
[DEBUG][Media.__init__] Finished -> <Video id=1223, title=Media_4797>
[DEBUG update_comment] update_comment_db result: True
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG __init__] Created Comment object: {'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137'}
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Commento 101', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Built object=<Video id=1223, title=Media_4797>
[DEBUG][update_comment] STATUS=OK, TIME=11.7194s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1172,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (555,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1151,)
[DEBUG] fetch_one success: RealDictRow({'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] cls=Document, object_id=1263
[DEBUG] fetch_one success: RealDictRow({'id': 1243})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1277, title=Media_8066>
[DEBUG][Media.from_dict] Built object=<Document id=1277, title=Media_8066>
[DEBUG][Media.fetch] Built object=<Document id=1277, title=Media_8066>
[DEBUG][Media.from_dict] cls=Media, data={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Document, media_id=1263
[DEBUG] fetch_one success: RealDictRow({'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG update_comment] user_id=360, comment_id=2056, new_text=Aggiornato 737
[DEBUG][dispatch_command] START - command=delete_note, args=[564], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=361, note_id=564
[DEBUG from_dict] data={'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101'}
[DEBUG][create_comment] STATUS=OK, TIME=25.0501s, TAG=OK
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=24.0672s, TAG=OK
[DEBUG][dispatch_command] START - command=create_comment, args=[1297, 'Commento 389'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(559, 360, 1228, 'regular', Decimal('1.82'), Decimal('7.09'), None, None, None, None, None, 'Nota aggiornata 163', None)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1297
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_song_services] song_id=1193
[DEBUG][get_object] cls=Song, object_id=1193
[DEBUG] fetch_one success: RealDictRow({'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Called with title=Media_4773, type=song, year=2007, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=update_comment, args=[2060, 'Aggiornato 950'], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1201,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (550,)
[DEBUG][dispatch_command] START - command=delete_comment, args=[2052], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_note] STATUS=OK, TIME=11.4081s, TAG=OK
[DEBUG fetch_by_id] comment_id=2060
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1152,)
[DEBUG][Media.fetch] Called cls=Song, media_id=1193
[DEBUG fetch_by_id] comment_id=2052
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1273, title=Media_4773>
[DEBUG][Media.from_dict] cls=Media, data={'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_note] STATUS=OK, TIME=15.7187s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1217], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_one success: RealDictRow({'id': 1234, 'type': 'video', 'user_id': 358, 'title': 'Media_8514', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 16, 214780), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Called with title=Media_6007, type=document, year=2016, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_object] cls=Video, object_id=1217
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=get_song, args=[1225], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1234, 'type': 'video', 'user_id': 358, 'title': 'Media_8514', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 16, 214780), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Video, media_id=1217
[DEBUG] db_get_following result: []
[DEBUG][get_song_services] song_id=1225
[DEBUG][Media.__init__] Called with title=Media_8514, type=video, year=2021, user_id=358, kwargs={'id': 1234, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Called with title=Media_3540, type=song, year=2008, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Called with title=Media_1505, type=video, year=2011, user_id=355, kwargs={'id': 1267, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1158,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.from_dict] Built object=<Song id=1273, title=Media_4773>
[DEBUG] fetch_one success: RealDictRow({'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: id=1267
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1219,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Document id=1270, title=Media_6007>
[DEBUG][Media.fetch] Built object=<Song id=1273, title=Media_4773>
[DEBUG][Media.__init__] Extra attr: id=1234
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1142,)
[DEBUG] db_get_following result: [(2044, 359, 1281, None, None, 'Aggiornato 273', datetime.date(2025, 9, 14))]
[DEBUG][Media.from_dict] Built object=<Document id=1270, title=Media_6007>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 729', 562)
[DEBUG delete_comment] fetched comment: [{'id': 2044, 'user_id': 359, 'media_id': 1281, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 273', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Built object=<Document id=1270, title=Media_6007>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.from_dict] cls=Song, data={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(567, 361, 1272, 'regular', Decimal('1.28'), Decimal('9.25'), None, None, None, None, None, 'Nota 841', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1195})
[DEBUG][Media.__init__] Finished -> <Video id=1267, title=Media_1505>
[DEBUG][Media.__init__] Called with title=Media_1272, type=song, year=2012, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] cls=Song, object_id=1225
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Built object=<Video id=1267, title=Media_1505>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Finished -> <Video id=1234, title=Media_8514>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 998', 2053)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Built object=<Video id=1234, title=Media_8514>
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Song, media_id=1225
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1140,)
[DEBUG][Media.__init__] Finished -> <Song id=1260, title=Media_3540>
[DEBUG] fetch_one success: RealDictRow({'id': 1231, 'type': 'video', 'user_id': 357, 'title': 'Media_1305', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 12, 513887), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1231, 'type': 'video', 'user_id': 357, 'title': 'Media_1305', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 12, 513887), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1305, type=video, year=2022, user_id=357, kwargs={'id': 1231, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1213, 'type': 'document', 'user_id': 360, 'title': 'Media_9014', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 649200), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: id=1231
[DEBUG][Media.fetch] Data from DB={'id': 1213, 'type': 'document', 'user_id': 360, 'title': 'Media_9014', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 649200), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9014, type=document, year=2014, user_id=360, kwargs={'id': 1213, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1213
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1213, title=Media_9014>
[DEBUG][Media.fetch] Built object=<Document id=1213, title=Media_9014>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1231, title=Media_1305>
[DEBUG][Media.fetch] Built object=<Video id=1231, title=Media_1305>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2049,)
[DEBUG][Media.__init__] Finished -> <Song id=1269, title=Media_1272>
[DEBUG][Media.from_dict] Built object=<Song id=1269, title=Media_1272>
[DEBUG][Media.fetch] Built object=<Song id=1269, title=Media_1272>
[DEBUG][Media.from_dict] Built object=<Song id=1260, title=Media_3540>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1216,)
[DEBUG][delete_note] STATUS=OK, TIME=16.8459s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1176,)
[DEBUG][Media.fetch] Built object=<Song id=1260, title=Media_3540>
[DEBUG][dispatch_command] START - command=get_video, args=[1206], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1206
[DEBUG][Media.fetch] Called cls=Video, media_id=1206
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1204,)
[DEBUG][Media.delete] Deleted media_id=1201
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8627>
[DEBUG][delete_document] STATUS=OK, TIME=44.6654s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2045,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(557, 358, 1242, 'regular', Decimal('0.71'), Decimal('3.51'), None, None, None, None, None, 'Nota aggiornata 666', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2054, 360, 1291, None, None, 'Commento 299', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 299', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.delete] Deleted media_id=1142
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_9476>
[DEBUG][delete_video] STATUS=OK, TIME=55.8283s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1154,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][update_note] STATUS=OK, TIME=15.9140s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=delete_note, args=[562], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG delete_note] START - user_id=354, note_id=562
[DEBUG] fetch_one success: RealDictRow({'id': 361})
[DEBUG][get_object] Retrieved object=<Song id=1189, title=Media_7196>
[DEBUG][Media.to_dict] <Song id=1189, title=Media_7196> -> {'media_id': 1189, 'type': 'song', 'title': 'Media_7196', 'user_id': 362, 'year': 2008, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:40.228975', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=10.3731s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1189], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1189
[DEBUG][get_object] cls=Song, object_id=1189
[DEBUG][Media.fetch] Called cls=Song, media_id=1189
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_object] Retrieved object=<Document id=1247, title=Media_8829>
[DEBUG] db_get_following result: []
[DEBUG][Media.to_dict] <Document id=1247, title=Media_8829> -> {'media_id': 1247, 'type': 'document', 'title': 'Media_8829', 'user_id': 353, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:32.153020', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=12.4734s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1247], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1247
[DEBUG][Media.fetch] Called cls=Document, media_id=1247
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][update_comment] STATUS=OK, TIME=8.7124s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1218,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1161,)
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1239, title=Media_5674>
[DEBUG][Media.to_dict] <Song id=1239, title=Media_5674> -> {'media_id': 1239, 'type': 'song', 'title': 'Media_5674', 'user_id': 362, 'year': 2001, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:21.373567', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=10.7252s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_song, args=[1239], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] Retrieved object=<Song id=1196, title=Media_6446>
[DEBUG][delete_object] Deleting object <Song id=1196, title=Media_6446>
[DEBUG][Media.delete] Called on <Song id=1196, title=Media_6446>
[DEBUG][delete_song_services] song_id=1239
[DEBUG][get_object] cls=Song, object_id=1239
[DEBUG][Media.fetch] Called cls=Song, media_id=1239
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=delete_comment, args=[2053], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Commento 999', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] comment_id=2053
[DEBUG] db_get_following result: []
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG from_dict] data={'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.delete] Deleted media_id=1216
[DEBUG][delete_comment] STATUS=OK, TIME=13.6746s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1140
[DEBUG __init__] Created Comment object: {'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999'}
[DEBUG][dispatch_command] START - command=create_note, args=[1280, 'regular', 6.3008481050643015, 7.4261903842505115, None, None, None, None, 'Nota 84'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3029>
[DEBUG update_comment] user_id=360, comment_id=2058, new_text=Aggiornato 77
[DEBUG][Media.delete] Deleted media_id=1204
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_8759>
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7838>
[DEBUG][delete_song] STATUS=OK, TIME=43.7248s, TAG=OK
[DEBUG][delete_song] STATUS=OK, TIME=44.6646s, TAG=OK
[DEBUG][delete_document] STATUS=OK, TIME=47.8454s, TAG=OK
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_comment] STATUS=OK, TIME=15.4798s, TAG=OK
[DEBUG delete_comment] fetched media: {'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][dispatch_command] START - command=create_note, args=[1285, 'regular', 0.06005502601377444, 3.4987562824428284, None, None, None, None, 'Nota 65'], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1220,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_one success: RealDictRow({'id': 1199, 'type': 'document', 'user_id': 355, 'title': 'Media_7671', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 45, 870444), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1199, 'type': 'document', 'user_id': 355, 'title': 'Media_7671', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 45, 870444), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7671, type=document, year=2010, user_id=355, kwargs={'id': 1199, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1199
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1199, title=Media_7671>
[DEBUG][Media.fetch] Built object=<Document id=1199, title=Media_7671>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1263, 'type': 'document', 'user_id': 356, 'title': 'Media_1895', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 56, 255845), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1263, 'type': 'document', 'user_id': 356, 'title': 'Media_1895', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 56, 255845), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1895, type=document, year=2015, user_id=356, kwargs={'id': 1263, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1263
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1263, title=Media_1895>
[DEBUG][Media.fetch] Built object=<Document id=1263, title=Media_1895>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1159,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(559, 360, 1228, 'regular', Decimal('1.82'), Decimal('7.09'), None, None, None, None, None, 'Nota aggiornata 163', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1184,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1257, 'type': 'document', 'user_id': 355, 'title': 'Media_2596', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 48, 132347), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1257, 'type': 'document', 'user_id': 355, 'title': 'Media_2596', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 48, 132347), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2596, type=document, year=2006, user_id=355, kwargs={'id': 1257, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1257
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1257, title=Media_2596>
[DEBUG][Media.fetch] Built object=<Document id=1257, title=Media_2596>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1174,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1205,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(568, 359, 1238, 'regular', Decimal('2.14'), Decimal('2.56'), None, None, None, None, None, 'Nota 262', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1229})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1166,)
[DEBUG] fetch_one success: RealDictRow({'id': 1259, 'type': 'document', 'user_id': 354, 'title': 'Media_8102', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 222384), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1259, 'type': 'document', 'user_id': 354, 'title': 'Media_8102', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 222384), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8102, type=document, year=2006, user_id=354, kwargs={'id': 1259, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1259
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1259, title=Media_8102>
[DEBUG][Media.fetch] Built object=<Document id=1259, title=Media_8102>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(558, 361, 1240, 'regular', Decimal('0.81'), Decimal('7.74'), None, None, None, None, None, 'Nota aggiornata 181', None)]
[DEBUG][Media.delete] Deleted media_id=1159
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_9827>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1191,)
[DEBUG][delete_document] STATUS=OK, TIME=46.6145s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1276
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2057, 358, 1294, None, None, 'Commento 380', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380'}
[DEBUG update_comment] user_id=358, comment_id=2057, new_text=Aggiornato 868
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1170,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1224,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(566, 354, 1253, 'regular', Decimal('0.26'), Decimal('5.16'), None, None, None, None, None, 'Nota 489', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(570, 359, 1266, 'regular', Decimal('5.06'), Decimal('5.38'), None, None, None, None, None, 'Nota 466', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1251})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(560, 356, 1232, 'regular', Decimal('4.90'), Decimal('6.88'), None, None, None, None, None, 'Nota aggiornata 304', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1176,)
[DEBUG] db_get_following result: [(2051, 362, 1286, None, None, 'Aggiornato 858', datetime.date(2025, 9, 14))]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2052, 359, 1287, None, None, 'Aggiornato 647', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2052, 'user_id': 359, 'media_id': 1287, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 647', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2052, 'user_id': 359, 'media_id': 1287, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 647', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2052, 'user_id': 359, 'media_id': 1287, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 647'}
[DEBUG delete_comment] user_id=359, comment_id=2052
[DEBUG delete_comment] fetched comment: [{'id': 2051, 'user_id': 362, 'media_id': 1286, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 858', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_one success: RealDictRow({'id': 1241})
[DEBUG] fetch_one success: RealDictRow({'id': 1186, 'type': 'song', 'user_id': 354, 'title': 'Media_1608', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 171382), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1186, 'type': 'song', 'user_id': 354, 'title': 'Media_1608', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 171382), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.delete] Deleted media_id=1205
[DEBUG][Media.from_dict] cls=Song, data={'id': 1186, 'type': 'song', 'user_id': 354, 'title': 'Media_1608', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 33, 171382), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5651>
[DEBUG][Media.__init__] Called with title=Media_1608, type=song, year=2000, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] Retrieved object=<Song id=1202, title=Media_7744>
[DEBUG][Media.__init__] Finished -> <Song id=1186, title=Media_1608>
[DEBUG][Media.to_dict] <Song id=1202, title=Media_7744> -> {'media_id': 1202, 'type': 'song', 'title': 'Media_7744', 'user_id': 361, 'year': 2006, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:47.051676', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] Built object=<Song id=1186, title=Media_1608>
[DEBUG][get_song] STATUS=OK, TIME=15.6258s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1193, 'type': 'song', 'user_id': 362, 'title': 'Media_5844', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 42, 884754), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_document] STATUS=OK, TIME=42.8950s, TAG=OK
[DEBUG][Media.fetch] Built object=<Song id=1186, title=Media_1608>
[DEBUG][Media.fetch] Data from DB={'id': 1193, 'type': 'song', 'user_id': 362, 'title': 'Media_5844', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 42, 884754), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1227,)
[DEBUG] fetch_one success: RealDictRow({'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] cls=Song, data={'id': 1193, 'type': 'song', 'user_id': 362, 'title': 'Media_5844', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 42, 884754), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=delete_song, args=[1202], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_comment] fetched media: {'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][delete_song_services] song_id=1202
[DEBUG][get_object] cls=Song, object_id=1202
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1229,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1168,)
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Song, media_id=1202
[DEBUG][get_object] Retrieved object=<Video id=1249, title=Media_4002>
[DEBUG][Media.__init__] Called with title=Media_5844, type=song, year=2023, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(571, 353, 1244, 'regular', Decimal('1.39'), Decimal('9.14'), None, None, None, None, None, 'Nota 419', None)]
[DEBUG][delete_object] Deleting object <Video id=1249, title=Media_4002>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Song id=1193, title=Media_5844>
[DEBUG][Media.delete] Called on <Video id=1249, title=Media_4002>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1152,)
[DEBUG][create_note] STATUS=OK, TIME=15.3783s, TAG=OK
[DEBUG][Media.from_dict] Built object=<Song id=1193, title=Media_5844>
[DEBUG][Media.fetch] Built object=<Song id=1193, title=Media_5844>
[DEBUG][dispatch_command] START - command=update_note, args=[571, 'Nota aggiornata 485'], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=353, note_id=571
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2046,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1212, title=Media_1601>
[DEBUG][Media.to_dict] <Video id=1212, title=Media_1601> -> {'media_id': 1212, 'type': 'video', 'title': 'Media_1601', 'user_id': 361, 'year': 2014, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:56.551965', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2050,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1230,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG][get_video] STATUS=OK, TIME=13.1009s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_video, args=[1212], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(558, 361, 1240, 'regular', Decimal('0.81'), Decimal('7.74'), None, None, None, None, None, 'Nota aggiornata 181', None)]
[DEBUG][get_object] cls=Video, object_id=1212
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Video, media_id=1212
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1226, title=Media_6653>
[DEBUG][Media.to_dict] <Document id=1226, title=Media_6653> -> {'media_id': 1226, 'type': 'document', 'title': 'Media_6653', 'user_id': 361, 'year': 2009, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:08.794387', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=11.0004s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1226], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1226
[DEBUG][Media.fetch] Called cls=Document, media_id=1226
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1222, title=Media_4306>
[DEBUG][delete_object] Deleting object <Document id=1222, title=Media_4306>
[DEBUG][Media.delete] Called on <Document id=1222, title=Media_4306>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(573, 359, 1265, 'regular', Decimal('3.99'), Decimal('4.25'), None, None, None, None, None, 'Nota 674', None)]
[DEBUG][create_note] STATUS=OK, TIME=19.1079s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[573, 'Nota aggiornata 905'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=359, note_id=573
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1195,)
[DEBUG] fetch_one success: RealDictRow({'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1217, 'type': 'video', 'user_id': 362, 'title': 'Media_6854', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 58, 571395), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Data from DB={'id': 1217, 'type': 'video', 'user_id': 362, 'title': 'Media_6854', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 58, 571395), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1189, 'type': 'song', 'user_id': 362, 'title': 'Media_7196', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 40, 228975), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6854, type=video, year=2016, user_id=362, kwargs={'id': 1217, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1217
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1217, title=Media_6854>
[DEBUG][Media.__init__] Called with title=Media_7196, type=song, year=2008, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Built object=<Video id=1217, title=Media_6854>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1189, title=Media_7196>
[DEBUG][Media.from_dict] Built object=<Song id=1189, title=Media_7196>
[DEBUG][Media.fetch] Built object=<Song id=1189, title=Media_7196>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2048, 358, 1284, None, None, 'Aggiornato 774', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2048, 'user_id': 358, 'media_id': 1284, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 774', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(572, 356, 1264, 'regular', Decimal('1.88'), Decimal('6.13'), None, None, None, None, None, 'Nota 677', None)]
[DEBUG][create_note] STATUS=OK, TIME=23.2874s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[572, 'Nota aggiornata 711'], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=356, note_id=572
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1151,)
[DEBUG][Media.delete] Deleted media_id=1227
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8260>
[DEBUG] db_get_following result: []
[DEBUG][delete_document] STATUS=OK, TIME=43.5775s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(567, 361, 1272, 'regular', Decimal('1.28'), Decimal('9.25'), None, None, None, None, None, 'Nota 841', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1175, title=Media_7778>
[DEBUG][delete_object] Deleting object <Video id=1175, title=Media_7778>
[DEBUG][Media.delete] Called on <Video id=1175, title=Media_7778>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1210,)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=15.6924s, TAG=OK
[DEBUG][dispatch_command] START - command=create_comment, args=[1299, 'Commento 918'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Called cls=Media, media_id=1299
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1163,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1179,)
[DEBUG][get_object] Retrieved object=<Song id=1187, title=Media_3804>
[DEBUG][delete_object] Deleting object <Song id=1187, title=Media_3804>
[DEBUG][Media.delete] Called on <Song id=1187, title=Media_3804>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1285
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2055, 354, 1290, None, None, 'Commento 867', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 867', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=17.2558s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1282, 'regular', 6.30644478465819, 8.548872539137463, None, None, None, None, 'Nota 351'], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1172,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1207, title=Media_6052>
[DEBUG][Media.to_dict] <Song id=1207, title=Media_6052> -> {'media_id': 1207, 'type': 'song', 'title': 'Media_6052', 'user_id': 361, 'year': 2004, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:50.498131', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=16.2508s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1207], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1207
[DEBUG][get_object] cls=Song, object_id=1207
[DEBUG][Media.fetch] Called cls=Song, media_id=1207
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1161,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(556, 353, 1237, 'regular', Decimal('0.46'), Decimal('6.27'), None, None, None, None, None, 'Nota aggiornata 424', None)]
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1251,)
[DEBUG] fetch_one success: RealDictRow({'id': 1196})
[DEBUG] fetch_one success: RealDictRow({'id': 1252, 'type': 'document', 'user_id': 354, 'title': 'Media_4944', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 755124), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1252, 'type': 'document', 'user_id': 354, 'title': 'Media_4944', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 755124), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4944, type=document, year=2015, user_id=354, kwargs={'id': 1252, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: id=1252
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1252, title=Media_4944>
[DEBUG][Media.fetch] Built object=<Document id=1252, title=Media_4944>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1158,)
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1154,)
[DEBUG][get_object] Retrieved object=<Video id=1221, title=Media_8477>
[DEBUG][delete_object] Deleting object <Video id=1221, title=Media_8477>
[DEBUG][Media.delete] Called on <Video id=1221, title=Media_8477>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Commento 999', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2044,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1296})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1243,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Commento 101', datetime.date(2025, 9, 14))]
[DEBUG] fetch_all returned 1 rows
[DEBUG update_comment] fetched comment: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 999', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG add_comment] new_id returned from DB: 2061
[DEBUG] fetch_one success: RealDictRow({'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1262, title=Media_1728>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1191,)
[DEBUG] fetch_one success: RealDictRow({'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1188,)
[DEBUG] db_get_following result: [(2052, 359, 1287, None, None, 'Aggiornato 647', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (557,)
[DEBUG delete_comment] fetched comment: [{'id': 2052, 'user_id': 359, 'media_id': 1287, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 647', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 78', 567)
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101'}
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Commento 262', datetime.date(2025, 9, 14))]
[DEBUG][Media.from_dict] cls=Song, data={'id': 1239, 'type': 'song', 'user_id': 362, 'title': 'Media_5674', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 21, 373567), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 490', 565)
[DEBUG][Media.to_dict] <Document id=1262, title=Media_1728> -> {'media_id': 1262, 'type': 'document', 'title': 'Media_1728', 'user_id': 356, 'year': 2023, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:53.518516', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1168,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1241,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_5674, type=song, year=2001, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (559,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_document] STATUS=OK, TIME=12.6509s, TAG=OK
[DEBUG] db_get_following result: [(564, 361, 1233, 'regular', Decimal('5.40'), Decimal('9.43'), None, None, None, None, None, 'Nota aggiornata 670', None)]
[DEBUG update_comment] user_id=353, comment_id=2060, new_text=Aggiornato 950
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(561, 358, 1256, 'regular', Decimal('1.79'), Decimal('6.30'), None, None, None, None, None, 'Nota aggiornata 235', None)]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1220,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1206, 'type': 'video', 'user_id': 358, 'title': 'Media_2820', 'year': 2025, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 48, 986938), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_one success: RealDictRow({'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1202, 'type': 'song', 'user_id': 361, 'title': 'Media_7744', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 47, 51676), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] Retrieved object=<Song id=1248, title=Media_5286>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(562, 354, 1235, 'regular', Decimal('5.90'), Decimal('7.47'), None, None, None, None, None, 'Nota aggiornata 729', None)]
[DEBUG][dispatch_command] START - command=delete_document, args=[1262], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 360})
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1268, title=Media_4856>
[DEBUG][Media.to_dict] <Video id=1268, title=Media_4856> -> {'media_id': 1268, 'type': 'video', 'title': 'Media_4856', 'user_id': 356, 'year': 2017, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:01.401850', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=11.5940s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1268], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1268
[DEBUG][Media.fetch] Called cls=Video, media_id=1268
[DEBUG] fetch_one success: RealDictRow({'id': 361})
[DEBUG] fetch_one success: RealDictRow({'id': 1212, 'type': 'video', 'user_id': 361, 'title': 'Media_1601', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 551965), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1202, 'type': 'song', 'user_id': 361, 'title': 'Media_7744', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 47, 51676), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Data from DB={'id': 1206, 'type': 'video', 'user_id': 358, 'title': 'Media_2820', 'year': 2025, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 48, 986938), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_comment] STATUS=OK, TIME=11.9170s, TAG=OK
[DEBUG][Media.fetch] Data from DB={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5271, type=song, year=2024, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][update_note] STATUS=OK, TIME=12.3163s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 358})
[DEBUG][Media.delete] Deleted media_id=1188
[DEBUG] db_get_following result: [(2053, 359, 1292, None, None, 'Aggiornato 998', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 998', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][get_object] cls=Document, object_id=1262
[DEBUG][Media.fetch] Called cls=Document, media_id=1262
[DEBUG][Media.__init__] Finished -> <Song id=1239, title=Media_5674>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] cls=Song, data={'id': 1202, 'type': 'song', 'user_id': 361, 'title': 'Media_7744', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 47, 51676), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7744, type=song, year=2006, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1202, title=Media_7744>
[DEBUG][Media.from_dict] Built object=<Song id=1202, title=Media_7744>
[DEBUG][Media.fetch] Built object=<Song id=1202, title=Media_7744>
[DEBUG][Media.__init__] Called with title=Media_2820, type=video, year=2025, user_id=358, kwargs={'id': 1206, 'recording_date': None, 'performer_id': None}
[DEBUG][delete_object] Deleting object <Song id=1248, title=Media_5286>
[DEBUG][delete_note] STATUS=OK, TIME=12.1893s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1219,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (558,)
[DEBUG][Media.fetch] Data from DB={'id': 1212, 'type': 'video', 'user_id': 361, 'title': 'Media_1601', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 56, 551965), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG from_dict] data={'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 998', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] Built object=<Song id=1239, title=Media_5674>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][update_note] STATUS=OK, TIME=15.6347s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[565], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1152,)
[DEBUG][Media.fetch] Data from DB={'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1243,)
[DEBUG][Media.__init__] Extra attr: id=1206
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=get_document, args=[1228], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(569, 360, 1250, 'regular', Decimal('1.81'), Decimal('5.26'), None, None, None, None, None, 'Nota 860', None)]
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 357})
[DEBUG][dispatch_command] START - command=delete_note, args=[567], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2047,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1130>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.delete] Deleted media_id=1220
[DEBUG] fetch_one success: RealDictRow({'id': 1187})
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 998'}
[DEBUG delete_comment] user_id=359, comment_id=2053
[DEBUG] db_get_following result: [(568, 359, 1238, 'regular', Decimal('2.14'), Decimal('2.56'), None, None, None, None, None, 'Nota 262', None)]
[DEBUG] db_get_following result: [(570, 359, 1266, 'regular', Decimal('5.06'), Decimal('5.38'), None, None, None, None, None, 'Nota 466', None)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1218,)
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1230,)
[DEBUG delete_note] START - user_id=356, note_id=565
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1184,)
[DEBUG delete_comment] fetched media: {'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.delete] Called on <Song id=1248, title=Media_5286>
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 540', 2054)
[DEBUG][get_object] cls=Document, object_id=1228
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 434', 2055)
[DEBUG][Media.__init__] Finished -> <Song id=1297, title=Media_5271>
[DEBUG delete_note] START - user_id=361, note_id=567
[DEBUG] fetch_one success: RealDictRow({'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][delete_video] STATUS=OK, TIME=51.4200s, TAG=OK
[DEBUG] db_get_following result: [(560, 356, 1232, 'regular', Decimal('4.90'), Decimal('6.88'), None, None, None, None, None, 'Nota aggiornata 304', None)]
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8558>
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Built object=<Song id=1239, title=Media_5674>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1249})
[DEBUG] fetch_one success: RealDictRow({'id': 355})
[DEBUG from_dict] data={'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][dispatch_command] START - command=create_note, args=[1281, 'regular', 7.778700388331723, 1.3135283527030805, None, None, None, None, 'Nota 806'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6439, type=video, year=2021, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1222})
[DEBUG][Media.__init__] Called with title=Media_2695, type=song, year=2020, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Document, media_id=1228
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1229,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1251,)
[DEBUG delete_comment] fetched media: {'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Media, media_id=1280
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1170,)
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1174,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Video id=1208, title=Media_1239>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1176,)
[DEBUG] fetch_one success: RealDictRow({'id': 362})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2057, 358, 1294, None, None, 'Commento 380', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] Retrieved object=<Document id=1215, title=Media_7685>
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1175})
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2043,)
[DEBUG] fetch_one success: RealDictRow({'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][get_object] Retrieved object=<Song id=1274, title=Media_6866>
[DEBUG][delete_object] Deleting object <Video id=1208, title=Media_1239>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1241,)
[DEBUG] fetch_one success: RealDictRow({'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG update_comment] fetched comment: [{'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 380', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1261, title=Media_1015>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][delete_note] STATUS=OK, TIME=11.9725s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.from_dict] cls=Media, data={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_object] Deleting object <Document id=1215, title=Media_7685>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.delete] Deleted media_id=1218
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1213, title=Media_9014>
[DEBUG][delete_object] Deleting object <Document id=1213, title=Media_9014>
[DEBUG][Media.delete] Called on <Document id=1213, title=Media_9014>
[DEBUG][Media.to_dict] <Song id=1274, title=Media_6866> -> {'media_id': 1274, 'type': 'song', 'title': 'Media_6866', 'user_id': 353, 'year': 2000, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:04.943230', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.delete] Called on <Video id=1208, title=Media_1239>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1196,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG update_comment] update_comment_db result: True
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1210,)
[DEBUG][Media.__init__] Finished -> <Video id=1276, title=Media_6439>
[DEBUG] db_get_following result: [(561, 358, 1256, 'regular', Decimal('1.79'), Decimal('6.30'), None, None, None, None, None, 'Nota aggiornata 235', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.from_dict] Built object=<Song id=1297, title=Media_5271>
[DEBUG][get_object] Retrieved object=<Document id=1259, title=Media_8102>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Called with title=Media_1601, type=video, year=2014, user_id=361, kwargs={'id': 1212, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1163,)
[DEBUG][delete_document] STATUS=OK, TIME=42.2744s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1154,)
[DEBUG][delete_comment] STATUS=OK, TIME=15.0910s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1279, 'regular', 7.469078227295993, 0.8729842595383297, None, None, None, None, 'Nota 408'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1187,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Commento 18', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Document id=1199, title=Media_7671>
[DEBUG][delete_object] Deleting object <Document id=1199, title=Media_7671>
[DEBUG][Media.delete] Called on <Document id=1199, title=Media_7671>
[DEBUG] db_get_following result: []
[DEBUG][update_comment] STATUS=OK, TIME=12.5960s, TAG=OK
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1172,)
[DEBUG][Media.__init__] Called with title=Media_9639, type=document, year=2013, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.delete] Called on <Document id=1215, title=Media_7685>
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4612>
[DEBUG][delete_document] STATUS=OK, TIME=39.2662s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1247, 'type': 'document', 'user_id': 353, 'title': 'Media_8829', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 153020), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262'}
[DEBUG][create_comment] STATUS=OK, TIME=26.7629s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1191,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (556,)
[DEBUG][Media.fetch] Data from DB={'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG update_comment] update_comment_db result: True
[DEBUG][update_comment] STATUS=OK, TIME=13.1862s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1151,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleting object <Song id=1261, title=Media_1015>
[DEBUG][Media.delete] Called on <Song id=1261, title=Media_1015>
[DEBUG][dispatch_command] START - command=get_video, args=[1242], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1242
[DEBUG][Media.__init__] Finished -> <Video id=1206, title=Media_2820>
[DEBUG][Media.fetch] Built object=<Song id=1297, title=Media_5271>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Commento 101', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Video id=1203, title=Media_9235>
[DEBUG][get_object] Retrieved object=<Video id=1255, title=Media_8372>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1224,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1158,)
[DEBUG] db_get_following result: [(2056, 360, 1293, None, None, 'Commento 137', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 137', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=update_comment, args=[2059, 'Aggiornato 677'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.delete] Deleted media_id=1176
[DEBUG][Media.from_dict] cls=Media, data={'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_note] STATUS=OK, TIME=13.3385s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1277})
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][dispatch_command] START - command=delete_comment, args=[2055], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2055
[DEBUG][Media.delete] Deleted media_id=1210
[DEBUG][Media.__init__] Finished -> <Song id=1225, title=Media_2695>
[DEBUG][Media.fetch] Called cls=Video, media_id=1242
[DEBUG][Media.fetch] Built object=<Video id=1206, title=Media_2820>
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleting object <Document id=1259, title=Media_8102>
[DEBUG][Media.__init__] Extra attr: id=1212
[DEBUG][Media.to_dict] <Video id=1203, title=Media_9235> -> {'media_id': 1203, 'type': 'video', 'title': 'Media_9235', 'user_id': 360, 'year': 2013, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:47.052832', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG update_comment] fetched comment: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 101', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][delete_object] Deleting object <Video id=1255, title=Media_8372>
[DEBUG][Media.fetch] Data from DB={'id': 1247, 'type': 'document', 'user_id': 353, 'title': 'Media_8829', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 153020), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_song] STATUS=OK, TIME=14.1214s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 55', 566)
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] db_get_following result: [(564, 361, 1233, 'regular', Decimal('5.40'), Decimal('9.43'), None, None, None, None, None, 'Nota aggiornata 670', None)]
[DEBUG][dispatch_command] START - command=delete_comment, args=[2054], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1226, 'type': 'document', 'user_id': 361, 'title': 'Media_6653', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 794387), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1226, 'type': 'document', 'user_id': 361, 'title': 'Media_6653', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 794387), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] Built object=<Video id=1276, title=Media_6439>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Called cls=Media, media_id=1282
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(563, 354, 1236, 'regular', Decimal('7.08'), Decimal('8.53'), None, None, None, None, None, 'Nota aggiornata 319', None)]
[DEBUG add_comment] START - user_id=361, text=Commento 389, media_id=1297, note_id=None, parent_comment_id=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1166,)
[DEBUG][Media.fetch] Data from DB={'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1195,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1175,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1248})
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(562, 354, 1235, 'regular', Decimal('5.90'), Decimal('7.47'), None, None, None, None, None, 'Nota aggiornata 729', None)]
[DEBUG fetch_by_id] comment_id=2059
[DEBUG __init__] Created Comment object: {'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18'}
[DEBUG][dispatch_command] START - command=get_video, args=[1240], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1240
[DEBUG][get_object] Retrieved object=<Song id=1185, title=Media_4277>
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 142', 570)
[DEBUG] fetch_one success: RealDictRow({'id': 1221})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Document id=1299, title=Media_9639>
[DEBUG][get_video] STATUS=OK, TIME=18.7549s, TAG=OK
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][Media.delete] Called on <Video id=1255, title=Media_8372>
[DEBUG delete_comment] fetched media: {'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1273})
[DEBUG][get_object] Retrieved object=<Document id=1258, title=Media_1339>
[DEBUG][Media.__init__] Called with title=Media_3931, type=video, year=2008, user_id=356, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1249,)
[DEBUG][delete_object] Deleting object <Song id=1185, title=Media_4277>
[DEBUG][Media.delete] Called on <Song id=1185, title=Media_4277>
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7780>
[DEBUG][Media.delete] Called on <Document id=1259, title=Media_8102>
[DEBUG] fetch_one success: RealDictRow({'id': 1228, 'type': 'document', 'user_id': 360, 'title': 'Media_5208', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 9, 603593), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] Built object=<Document id=1299, title=Media_9639>
[DEBUG][dispatch_command] START - command=delete_video, args=[1203], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1203
[DEBUG][dispatch_command] START - command=delete_song, args=[1274], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1274
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1161,)
[DEBUG add_comment] Created Comment object from DB: {'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18'}
[DEBUG fetch_by_id] comment_id=2061
[DEBUG][Media.delete] Deleted media_id=1151
[DEBUG] fetch_one success: RealDictRow({'id': 1271})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1285, title=Media_3931>
[DEBUG][Media.fetch] Built object=<Video id=1276, title=Media_6439>
[DEBUG][Media.delete] Deleted media_id=1158
[DEBUG][Media.delete] Deleted media_id=1224
[DEBUG][delete_document] STATUS=OK, TIME=42.0584s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Called cls=Video, media_id=1203
[DEBUG][delete_comment] STATUS=OK, TIME=24.3414s, TAG=OK
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 77', 2058)
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.to_dict] <Document id=1258, title=Media_1339> -> {'media_id': 1258, 'type': 'document', 'title': 'Media_1339', 'user_id': 356, 'year': 2018, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:49.178209', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG fetch_by_id] comment_id=2054
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6261>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2051,)
[DEBUG][delete_note] STATUS=OK, TIME=17.9604s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1243,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1219,)
[DEBUG][Media.from_dict] Built object=<Video id=1285, title=Media_3931>
[DEBUG] fetch_one success: RealDictRow({'id': 1262, 'type': 'document', 'user_id': 356, 'title': 'Media_1728', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 53, 518516), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1262, 'type': 'document', 'user_id': 356, 'title': 'Media_1728', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 53, 518516), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1728, type=document, year=2023, user_id=356, kwargs={'id': 1262, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1262
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1262, title=Media_1728>
[DEBUG][Media.fetch] Built object=<Document id=1262, title=Media_1728>
[DEBUG][get_object] cls=Song, object_id=1274
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6810>
[DEBUG][delete_document] STATUS=OK, TIME=36.6074s, TAG=OK
[DEBUG][Media.from_dict] Built object=<Song id=1225, title=Media_2695>
[DEBUG][delete_song] STATUS=OK, TIME=41.2086s, TAG=OK
[DEBUG][update_note] STATUS=OK, TIME=16.6652s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1199})
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3239>
[DEBUG][Media.fetch] Data from DB={'id': 1268, 'type': 'video', 'user_id': 356, 'title': 'Media_4856', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 401850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Song, media_id=1274
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_5962>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Built object=<Document id=1299, title=Media_9639>
[DEBUG][Media.__init__] Finished -> <Video id=1212, title=Media_1601>
[DEBUG][Media.__init__] Called with title=Media_8829, type=document, year=2015, user_id=353, kwargs={'id': 1247, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1247
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (560,)
[DEBUG][Media.fetch] Built object=<Song id=1225, title=Media_2695>
[DEBUG][dispatch_command] START - command=get_video, args=[1237], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][dispatch_command] START - command=delete_note, args=[566], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1222,)
[DEBUG][get_object] Retrieved object=<Video id=1231, title=Media_1305>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1223, title=Media_4797>
[DEBUG][Media.to_dict] <Video id=1223, title=Media_4797> -> {'media_id': 1223, 'type': 'video', 'title': 'Media_4797', 'user_id': 360, 'year': 2023, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:06.720637', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=12.0089s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1223], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG add_comment] START - user_id=361, text=Commento 918, media_id=1299, note_id=None, parent_comment_id=None
[DEBUG][Media.fetch] Built object=<Video id=1212, title=Media_1601>
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1163,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1168,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1247, title=Media_8829>
[DEBUG][Media.__init__] Called with title=Media_6653, type=document, year=2009, user_id=361, kwargs={'id': 1226, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1261})
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1179,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1298})
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][delete_song] STATUS=OK, TIME=41.3355s, TAG=OK
[DEBUG][Media.to_dict] <Video id=1231, title=Media_1305> -> {'media_id': 1231, 'type': 'video', 'title': 'Media_1305', 'user_id': 357, 'year': 2022, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:12.513887', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(569, 360, 1250, 'regular', Decimal('1.81'), Decimal('5.26'), None, None, None, None, None, 'Nota 860', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(573, 359, 1265, 'regular', Decimal('3.99'), Decimal('4.25'), None, None, None, None, None, 'Nota 674', None)]
[DEBUG] db_get_following result: []
[DEBUG][get_object] cls=Video, object_id=1223
[DEBUG][Media.fetch] Data from DB={'id': 1228, 'type': 'document', 'user_id': 360, 'title': 'Media_5208', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 9, 603593), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1184,)
[DEBUG][update_note] STATUS=OK, TIME=10.9429s, TAG=OK
[DEBUG][get_object] Retrieved object=<Video id=1275, title=Media_4617>
[DEBUG] fetch_one success: RealDictRow({'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Document id=1247, title=Media_8829>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1170,)
[DEBUG delete_note] START - user_id=354, note_id=566
[DEBUG] db_get_following result: [(567, 361, 1272, 'regular', Decimal('1.28'), Decimal('9.25'), None, None, None, None, None, 'Nota aggiornata 78', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_video] STATUS=OK, TIME=11.8836s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_video] STATUS=OK, TIME=41.1911s, TAG=OK
[DEBUG][get_object] Retrieved object=<Document id=1263, title=Media_1895>
[DEBUG][dispatch_command] START - command=create_note, args=[1278, 'regular', 6.009211908105195, 3.725733264214268, None, None, None, None, 'Nota 262'], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_5208, type=document, year=2010, user_id=360, kwargs={'id': 1228, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1283})
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 218', 568)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=12.9306s, TAG=OK
[DEBUG][Media.fetch] Data from DB={'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Built object=<Video id=1285, title=Media_3931>
[DEBUG][Media.fetch] Called cls=Media, media_id=1281
[DEBUG add_comment] new_id returned from DB: 2062
[DEBUG] fetch_one success: RealDictRow({'id': 1242, 'type': 'video', 'user_id': 358, 'title': 'Media_8574', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 98429), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (561,)
[DEBUG][Media.fetch] Called cls=Video, media_id=1240
[DEBUG][dispatch_command] START - command=delete_video, args=[1231], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1231
[DEBUG][delete_object] Deleting object <Document id=1263, title=Media_1895>
[DEBUG][Media.delete] Called on <Document id=1263, title=Media_1895>
[DEBUG][dispatch_command] START - command=delete_note, args=[570], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.to_dict] <Video id=1275, title=Media_4617> -> {'media_id': 1275, 'type': 'video', 'title': 'Media_4617', 'user_id': 356, 'year': 2007, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:06.153114', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=17.6692s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1286, 'regular', 8.6242752763922, 8.971666750735507, None, None, None, None, 'Nota 973'], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: id=1226
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.from_dict] cls=Media, data={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Video, media_id=1223
[DEBUG][get_document] STATUS=OK, TIME=12.1554s, TAG=OK
[DEBUG][get_object] Retrieved object=<Document id=1257, title=Media_2596>
[DEBUG] fetch_one success: RealDictRow({'id': 1259})
[DEBUG update_comment] update_comment_db result: True
[DEBUG][update_comment] STATUS=OK, TIME=9.6181s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2058], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_4856, type=video, year=2017, user_id=356, kwargs={'id': 1268, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1268
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Finished -> <Document id=1226, title=Media_6653>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1215})
[DEBUG][Media.__init__] Called with title=Media_4067, type=song, year=2024, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: id=1228
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1248,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.from_dict] cls=Media, data={'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(576, 360, 1271, 'regular', Decimal('1.02'), Decimal('4.36'), None, None, None, None, None, 'Nota 843', None)]
[DEBUG][Media.fetch] Data from DB={'id': 1242, 'type': 'video', 'user_id': 358, 'title': 'Media_8574', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 98429), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1267, title=Media_1505>
[DEBUG][Media.to_dict] <Video id=1267, title=Media_1505> -> {'media_id': 1267, 'type': 'video', 'title': 'Media_1505', 'user_id': 355, 'year': 2011, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:00.099471', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=11.2414s, TAG=OK
[DEBUG][Media.fetch] Called cls=Video, media_id=1231
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleting object <Document id=1257, title=Media_2596>
[DEBUG][Media.delete] Called on <Document id=1257, title=Media_2596>
[DEBUG][get_object] cls=Video, object_id=1237
[DEBUG][Media.__init__] Called with title=Media_5817, type=document, year=2022, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Called with title=Media_8574, type=video, year=2019, user_id=358, kwargs={'id': 1242, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.delete] Deleted media_id=1168
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1196,)
[DEBUG] db_get_following result: [(574, 361, 1277, 'regular', Decimal('4.07'), Decimal('5.13'), None, None, None, None, None, 'Nota 358', None)]
[DEBUG][create_note] STATUS=OK, TIME=18.7830s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=delete_document, args=[1258], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG delete_note] START - user_id=359, note_id=570
[DEBUG] db_get_following result: [(2053, 359, 1292, None, None, 'Aggiornato 998', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1230,)
[DEBUG delete_comment] fetched comment: [{'id': 2053, 'user_id': 359, 'media_id': 1292, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 998', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Called cls=Video, media_id=1237
[DEBUG fetch_by_id] comment_id=2058
[DEBUG][Media.__init__] Finished -> <Document id=1282, title=Media_5817>
[DEBUG][Media.fetch] Built object=<Document id=1226, title=Media_6653>
[DEBUG][Media.delete] Deleted media_id=1163
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_9517>
[DEBUG][delete_video] STATUS=OK, TIME=38.9531s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=update_note, args=[574, 'Nota aggiornata 226'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=361, note_id=574
[DEBUG][get_object] cls=Document, object_id=1258
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1280, title=Media_4067>
[DEBUG][Media.delete] Deleted media_id=1170
[DEBUG] db_get_following result: [(571, 353, 1244, 'regular', Decimal('1.39'), Decimal('9.14'), None, None, None, None, None, 'Nota 419', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1208})
[DEBUG][create_note] STATUS=OK, TIME=22.9714s, TAG=OK
[DEBUG][Media.from_dict] Built object=<Document id=1282, title=Media_5817>
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_9059>
[DEBUG][Media.from_dict] cls=Song, data={'id': 1207, 'type': 'song', 'user_id': 361, 'title': 'Media_6052', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 50, 498131), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_note] STATUS=OK, TIME=12.2075s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1213})
[DEBUG] fetch_one success: RealDictRow({'id': 1270})
[DEBUG][dispatch_command] START - command=delete_video, args=[1267], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(572, 356, 1264, 'regular', Decimal('1.88'), Decimal('6.13'), None, None, None, None, None, 'Nota 677', None)]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1241,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1174,)
[DEBUG][Media.__init__] Extra attr: id=1242
[DEBUG][Media.__init__] Finished -> <Video id=1268, title=Media_4856>
[DEBUG][Media.fetch] Built object=<Video id=1268, title=Media_4856>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1245, title=Media_1229>
[DEBUG][Media.delete] Deleted media_id=1179
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6063>
[DEBUG] db_get_following result: [(563, 354, 1236, 'regular', Decimal('7.08'), Decimal('8.53'), None, None, None, None, None, 'Nota aggiornata 319', None)]
[DEBUG][update_note] STATUS=OK, TIME=13.6956s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1172,)
[DEBUG][delete_note] STATUS=OK, TIME=9.9861s, TAG=OK
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4867>
[DEBUG][dispatch_command] START - command=update_note, args=[576, 'Nota aggiornata 500'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Built object=<Document id=1282, title=Media_5817>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1251,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2048,)
[DEBUG][dispatch_command] START - command=get_document, args=[1232], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(565, 356, 1246, 'regular', Decimal('0.22'), Decimal('7.12'), None, None, None, None, None, 'Nota aggiornata 490', None)]
[DEBUG][delete_document] STATUS=OK, TIME=40.9227s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1269, title=Media_1272>
[DEBUG][dispatch_command] START - command=get_document, args=[1256], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1256
[DEBUG][Media.fetch] Called cls=Document, media_id=1256
[DEBUG][Media.__init__] Called with title=Media_6052, type=song, year=2004, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][delete_object] Deleting object <Song id=1245, title=Media_1229>
[DEBUG][get_object] Retrieved object=<Song id=1186, title=Media_1608>
[DEBUG][Media.fetch] Called cls=Document, media_id=1258
[DEBUG][get_object] cls=Video, object_id=1267
[DEBUG][Media.fetch] Called cls=Video, media_id=1267
[DEBUG][Media.to_dict] <Song id=1269, title=Media_1272> -> {'media_id': 1269, 'type': 'song', 'title': 'Media_1272', 'user_id': 357, 'year': 2012, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:01.471890', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][delete_document] STATUS=OK, TIME=38.4014s, TAG=OK
[DEBUG update_note] START - user_id=360, note_id=576
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1152,)
[DEBUG] fetch_one success: RealDictRow({'id': 1203, 'type': 'video', 'user_id': 360, 'title': 'Media_9235', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 47, 52832), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Called cls=Media, media_id=1279
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (564,)
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 868', 2057)
[DEBUG][Media.from_dict] Built object=<Song id=1280, title=Media_4067>
[DEBUG][dispatch_command] START - command=delete_video, args=[1275], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1203, 'type': 'video', 'user_id': 360, 'title': 'Media_9235', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 47, 52832), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9235, type=video, year=2013, user_id=360, kwargs={'id': 1203, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.fetch] Built object=<Song id=1280, title=Media_4067>
[DEBUG][delete_song] STATUS=OK, TIME=45.5427s, TAG=OK
[DEBUG][get_object] cls=Document, object_id=1232
[DEBUG][Media.delete] Called on <Song id=1245, title=Media_1229>
[DEBUG][delete_object] Deleting object <Song id=1186, title=Media_1608>
[DEBUG][get_song] STATUS=OK, TIME=15.2570s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1269], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1221,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1207, title=Media_6052>
[DEBUG][Media.delete] Called on <Song id=1186, title=Media_1608>
[DEBUG][Media.__init__] Extra attr: id=1203
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_song_services] song_id=1269
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1229,)
[DEBUG][Media.fetch] Called cls=Document, media_id=1232
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1154,)
[DEBUG][Media.__init__] Finished -> <Document id=1228, title=Media_5208>
[DEBUG][get_object] cls=Video, object_id=1275
[DEBUG][Media.delete] Deleted media_id=1230
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7334>
[DEBUG][dispatch_command] START - command=delete_note, args=[568], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1203, title=Media_9235>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2052,)
[DEBUG][get_object] Retrieved object=<Video id=1254, title=Media_4949>
[DEBUG][delete_document] STATUS=OK, TIME=31.5698s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1242, title=Media_8574>
[DEBUG][Media.fetch] Built object=<Video id=1203, title=Media_9235>
[DEBUG][Media.fetch] Built object=<Video id=1242, title=Media_8574>
[DEBUG][delete_object] Deleting object <Video id=1254, title=Media_4949>
[DEBUG][Media.delete] Called on <Video id=1254, title=Media_4949>
[DEBUG][Media.fetch] Built object=<Document id=1228, title=Media_5208>
[DEBUG] db_get_following result: [(2055, 354, 1290, None, None, 'Aggiornato 434', datetime.date(2025, 9, 14))]
[DEBUG delete_note] START - user_id=359, note_id=568
[DEBUG][get_object] cls=Song, object_id=1269
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (562,)
[DEBUG][Media.from_dict] Built object=<Song id=1207, title=Media_6052>
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 434', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.delete] Deleted media_id=1174
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 950', 2060)
[DEBUG][Media.fetch] Built object=<Song id=1207, title=Media_6052>
[DEBUG][Media.fetch] Called cls=Video, media_id=1275
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1260, title=Media_3540>
[DEBUG from_dict] data={'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 434', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.fetch] Called cls=Song, media_id=1269
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.to_dict] <Song id=1260, title=Media_3540> -> {'media_id': 1260, 'type': 'song', 'title': 'Media_3540', 'user_id': 353, 'year': 2008, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:50.224839', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_song] STATUS=OK, TIME=13.3762s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1991>
[DEBUG][delete_document] STATUS=OK, TIME=36.1193s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1260], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1260
[DEBUG][get_object] Retrieved object=<Video id=1217, title=Media_6854>
[DEBUG][Media.to_dict] <Video id=1217, title=Media_6854> -> {'media_id': 1217, 'type': 'video', 'title': 'Media_6854', 'user_id': 362, 'year': 2016, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:58.571395', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG __init__] Created Comment object: {'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 434'}
[DEBUG][Media.delete] Deleted media_id=1172
[DEBUG][get_object] cls=Song, object_id=1260
[DEBUG][get_video] STATUS=OK, TIME=9.6630s, TAG=OK
[DEBUG delete_comment] user_id=354, comment_id=2055
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4767>
[DEBUG][Media.fetch] Called cls=Song, media_id=1260
[DEBUG][delete_document] STATUS=OK, TIME=33.9860s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1217], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1217
[DEBUG][Media.fetch] Called cls=Video, media_id=1217
[DEBUG] fetch_one success: RealDictRow({'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8330, type=document, year=2014, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1281, title=Media_8330>
[DEBUG][Media.from_dict] Built object=<Document id=1281, title=Media_8330>
[DEBUG][Media.fetch] Built object=<Document id=1281, title=Media_8330>
ERROR:services.interventions_services:Invalid time range: start_time=7.778700388331723, end_time=1.3135283527030805
[DEBUG][create_note] STATUS=OK, TIME=4.4171s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1281], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1281
[DEBUG][Media.fetch] Called cls=Document, media_id=1281
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1261,)
[DEBUG][delete_comment] STATUS=OK, TIME=16.0958s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1284, 'regular', 8.21789452231451, 6.062705357979735, None, None, None, None, 'Nota 151'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1219,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1152
[DEBUG][delete_note] STATUS=OK, TIME=10.4554s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 361})
[DEBUG update_comment] update_comment_db result: True
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6069>
[DEBUG][update_comment] STATUS=OK, TIME=12.2010s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2057], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2057
[DEBUG][delete_song] STATUS=OK, TIME=32.0795s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1233], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1233
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Called cls=Document, media_id=1233
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1252, title=Media_4944>
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1213,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleting object <Document id=1252, title=Media_4944>
[DEBUG] db_get_following result: [(572, 356, 1264, 'regular', Decimal('1.88'), Decimal('6.13'), None, None, None, None, None, 'Nota 677', None)]
[DEBUG][Media.delete] Called on <Document id=1252, title=Media_4944>
[DEBUG][delete_comment] STATUS=OK, TIME=10.1666s, TAG=OK
[DEBUG][delete_note] STATUS=OK, TIME=9.1365s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1287, 'regular', 8.998312193728916, 2.8117849429441364, None, None, None, None, 'Nota 263'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][dispatch_command] START - command=get_document, args=[1235], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 1255})
[DEBUG][get_object] cls=Document, object_id=1235
[DEBUG][Media.fetch] Called cls=Document, media_id=1235
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_all returned 0 rows
[DEBUG][update_comment] STATUS=OK, TIME=10.4999s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_comment, args=[2060], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2060
[DEBUG][get_object] Retrieved object=<Song id=1193, title=Media_5844>
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 737', 2056)
[DEBUG][delete_object] Deleting object <Song id=1193, title=Media_5844>
[DEBUG][Media.delete] Called on <Song id=1193, title=Media_5844>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1199,)
[DEBUG][Media.delete] Deleted media_id=1219
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1187,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1166,)
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1289>
[DEBUG] db_get_following result: [(578, 362, 1270, 'regular', Decimal('7.15'), Decimal('9.10'), None, None, None, None, None, 'Nota 46', None)]
[DEBUG][delete_document] STATUS=OK, TIME=31.5289s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(575, 358, 1273, 'regular', Decimal('2.43'), Decimal('4.63'), None, None, None, None, None, 'Nota 495', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1185})
[DEBUG][create_note] STATUS=OK, TIME=17.1880s, TAG=OK
[DEBUG][create_note] STATUS=OK, TIME=21.2608s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[575, 'Nota aggiornata 937'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=update_note, args=[578, 'Nota aggiornata 168'], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=362, note_id=578
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Commento 18', datetime.date(2025, 9, 14))]
[DEBUG update_note] START - user_id=358, note_id=575
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG from_dict] data={'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18'}
[DEBUG][create_comment] STATUS=OK, TIME=18.2316s, TAG=OK
[DEBUG][dispatch_command] START - command=update_comment, args=[2061, 'Aggiornato 791'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1248,)
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Commento 765', datetime.date(2025, 9, 14))]
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG __init__] Created Comment object: {'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765'}
[DEBUG fetch_by_id] comment_id=2061
[DEBUG add_comment] Created Comment object from DB: {'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765'}
[DEBUG fetch_by_id] comment_id=2062
[DEBUG] fetch_one success: RealDictRow({'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8330, type=document, year=2014, user_id=359, kwargs={'id': 1281, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1281
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1281, title=Media_8330>
[DEBUG][Media.fetch] Built object=<Document id=1281, title=Media_8330>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1215,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Commento 262', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262'}
[DEBUG] fetch_all returned 0 rows
[DEBUG update_comment] user_id=359, comment_id=2059, new_text=Aggiornato 677
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1189, title=Media_7196>
[DEBUG][delete_object] Deleting object <Song id=1189, title=Media_7196>
[DEBUG][Media.delete] Called on <Song id=1189, title=Media_7196>
[DEBUG update_comment] update_comment_db result: True
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1195,)
[DEBUG][update_comment] STATUS=OK, TIME=15.6235s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][dispatch_command] START - command=delete_comment, args=[2056], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2056
[DEBUG delete_comment] fetched media: {'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.delete] Deleted media_id=1166
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6907>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][delete_document] STATUS=OK, TIME=39.5117s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1274, 'type': 'song', 'user_id': 353, 'title': 'Media_6866', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 943230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6866, type=song, year=2000, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1274, title=Media_6866>
[DEBUG][Media.from_dict] Built object=<Song id=1274, title=Media_6866>
[DEBUG][Media.fetch] Built object=<Song id=1274, title=Media_6866>
[DEBUG] fetch_one success: RealDictRow({'id': 1223, 'type': 'video', 'user_id': 360, 'title': 'Media_4797', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 6, 720637), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1223, 'type': 'video', 'user_id': 360, 'title': 'Media_4797', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 6, 720637), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4797, type=video, year=2023, user_id=360, kwargs={'id': 1223, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1223
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1223, title=Media_4797>
[DEBUG][Media.fetch] Built object=<Video id=1223, title=Media_4797>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(565, 356, 1246, 'regular', Decimal('0.22'), Decimal('7.12'), None, None, None, None, None, 'Nota aggiornata 490', None)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1191,)
[DEBUG] fetch_one success: RealDictRow({'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1260, 'type': 'song', 'user_id': 353, 'title': 'Media_3540', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 50, 224839), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3540, type=song, year=2008, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1260, title=Media_3540>
[DEBUG][Media.from_dict] Built object=<Song id=1260, title=Media_3540>
[DEBUG][Media.fetch] Built object=<Song id=1260, title=Media_3540>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Aggiornato 77', datetime.date(2025, 9, 14))]
[DEBUG] fetch_one success: RealDictRow({'id': 1263})
[DEBUG] fetch_all returned 1 rows
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 77', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG from_dict] data={'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 77', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_one success: RealDictRow({'id': 1231, 'type': 'video', 'user_id': 357, 'title': 'Media_1305', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 12, 513887), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG __init__] Created Comment object: {'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 77'}
[DEBUG delete_comment] user_id=360, comment_id=2058
[DEBUG][Media.fetch] Data from DB={'id': 1231, 'type': 'video', 'user_id': 357, 'title': 'Media_1305', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 12, 513887), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1249,)
[DEBUG] fetch_one success: RealDictRow({'id': 1232, 'type': 'document', 'user_id': 356, 'title': 'Media_1193', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 445800), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Called with title=Media_1305, type=video, year=2022, user_id=357, kwargs={'id': 1231, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2054, 360, 1291, None, None, 'Aggiornato 540', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Data from DB={'id': 1232, 'type': 'document', 'user_id': 356, 'title': 'Media_1193', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 445800), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1184,)
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 540', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Called with title=Media_1193, type=document, year=2006, user_id=356, kwargs={'id': 1232, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1237, 'type': 'video', 'user_id': 353, 'title': 'Media_7336', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 369200), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 361})
[DEBUG from_dict] data={'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 540', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.__init__] Extra attr: id=1232
[DEBUG][Media.fetch] Data from DB={'id': 1237, 'type': 'video', 'user_id': 353, 'title': 'Media_7336', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 369200), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: id=1231
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1245})
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 304', 569)
[DEBUG] fetch_all returned 0 rows
[DEBUG __init__] Created Comment object: {'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 540'}
[DEBUG] db_get_following result: [(577, 355, 1283, 'regular', Decimal('1.76'), Decimal('3.28'), None, None, None, None, None, 'Nota 4', None)]
[DEBUG][create_note] STATUS=OK, TIME=19.4903s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=update_note, args=[577, 'Nota aggiornata 877'], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_7336, type=video, year=2023, user_id=353, kwargs={'id': 1237, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1237
[DEBUG update_note] START - user_id=355, note_id=577
[DEBUG delete_comment] user_id=360, comment_id=2054
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1231, title=Media_1305>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1175,)
[DEBUG][Media.fetch] Built object=<Video id=1231, title=Media_1305>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1237, title=Media_7336>
[DEBUG][Media.__init__] Finished -> <Document id=1232, title=Media_1193>
[DEBUG][Media.fetch] Built object=<Video id=1237, title=Media_7336>
[DEBUG][Media.fetch] Built object=<Document id=1232, title=Media_1193>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(357, 'user443793@example.com', 'user443793', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1278
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1286
[DEBUG] fetch_one success: RealDictRow({'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1269, 'type': 'song', 'user_id': 357, 'title': 'Media_1272', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 471890), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1272, type=song, year=2012, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1269, title=Media_1272>
[DEBUG][Media.from_dict] Built object=<Song id=1269, title=Media_1272>
[DEBUG][Media.fetch] Built object=<Song id=1269, title=Media_1272>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1193})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1222,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(573, 359, 1265, 'regular', Decimal('3.99'), Decimal('4.25'), None, None, None, None, None, 'Nota 674', None)]
[DEBUG][update_note] STATUS=OK, TIME=14.5833s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=delete_note, args=[569], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(567, 361, 1272, 'regular', Decimal('1.28'), Decimal('9.25'), None, None, None, None, None, 'Nota aggiornata 78', None)]
[DEBUG delete_note] START - user_id=360, note_id=569
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1161,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1261,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1251,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2056, 360, 1293, None, None, 'Aggiornato 737', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 737', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 737', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 737'}
[DEBUG delete_comment] user_id=360, comment_id=2056
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 711', 572)
[DEBUG] fetch_one success: RealDictRow({'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1258, 'type': 'document', 'user_id': 356, 'title': 'Media_1339', 'year': 2018, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 49, 178209), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1339, type=document, year=2018, user_id=356, kwargs={'id': 1258, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1258
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1258, title=Media_1339>
[DEBUG][Media.fetch] Built object=<Document id=1258, title=Media_1339>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Commento 18', datetime.date(2025, 9, 14))]
[DEBUG] fetch_one success: RealDictRow({'id': 1186})
[DEBUG] fetch_one success: RealDictRow({'id': 1257})
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (563,)
[DEBUG from_dict] data={'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18'}
[DEBUG update_comment] user_id=361, comment_id=2061, new_text=Aggiornato 791
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2057, 358, 1294, None, None, 'Aggiornato 868', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 868', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG from_dict] data={'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 868', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Commento 262', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 262', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG __init__] Created Comment object: {'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 868'}
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1229,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG delete_comment] user_id=358, comment_id=2057
[DEBUG] fetch_one success: RealDictRow({'id': 1189})
[DEBUG] fetch_one success: RealDictRow({'id': 1235, 'type': 'document', 'user_id': 354, 'title': 'Media_5882', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 19, 3653), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1235, 'type': 'document', 'user_id': 354, 'title': 'Media_5882', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 19, 3653), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5882, type=document, year=2024, user_id=354, kwargs={'id': 1235, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1235
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1235, title=Media_5882>
[DEBUG][Media.fetch] Built object=<Document id=1235, title=Media_5882>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][update_note] STATUS=OK, TIME=9.2407s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1185,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(571, 353, 1244, 'regular', Decimal('1.39'), Decimal('9.14'), None, None, None, None, None, 'Nota 419', None)]
[DEBUG][dispatch_command] START - command=delete_note, args=[572], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG delete_note] START - user_id=356, note_id=572
[DEBUG][get_object] Retrieved object=<Document id=1281, title=Media_8330>
[DEBUG][Media.to_dict] <Document id=1281, title=Media_8330> -> {'media_id': 1281, 'type': 'document', 'title': 'Media_8330', 'user_id': 359, 'year': 2014, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:24.043093', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=3.0408s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1281], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1281
[DEBUG][Media.fetch] Called cls=Document, media_id=1281
[DEBUG] fetch_one success: RealDictRow({'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1435, type=video, year=2002, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1278, title=Media_1435>
[DEBUG][Media.from_dict] Built object=<Video id=1278, title=Media_1435>
[DEBUG][Media.fetch] Built object=<Video id=1278, title=Media_1435>
ERROR:services.interventions_services:Invalid time range: start_time=6.009211908105195, end_time=3.725733264214268
[DEBUG][create_note] STATUS=OK, TIME=4.9070s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1278], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1278
[DEBUG][Media.fetch] Called cls=Video, media_id=1278
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1221,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1191,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1193,)
[DEBUG][delete_note] STATUS=OK, TIME=15.3781s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1248,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1215,)
[DEBUG][dispatch_command] START - command=get_document, args=[1236], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][get_object] cls=Document, object_id=1236
[DEBUG][Media.fetch] Called cls=Document, media_id=1236
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2058, 360, 1288, None, None, 'Aggiornato 77', datetime.date(2025, 9, 14))]
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(355, 'user242821@example.com', 'user242821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG delete_comment] fetched comment: [{'id': 2058, 'user_id': 360, 'media_id': 1288, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 77', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Data from DB={'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1770, type=document, year=2019, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1279, title=Media_1770>
[DEBUG][Media.from_dict] Built object=<Document id=1279, title=Media_1770>
[DEBUG][Media.fetch] Built object=<Document id=1279, title=Media_1770>
ERROR:services.interventions_services:Invalid time range: start_time=7.469078227295993, end_time=0.8729842595383297
[DEBUG][create_note] STATUS=OK, TIME=6.2556s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1279], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1279
[DEBUG][Media.fetch] Called cls=Document, media_id=1279
[DEBUG] fetch_one success: RealDictRow({'id': 1252})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1249,)
[DEBUG] fetch_one success: RealDictRow({'id': 1254})
[DEBUG] fetch_one success: RealDictRow({'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1196,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1213,)
[DEBUG][Media.__init__] Called with title=Media_4810, type=video, year=2001, user_id=362, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1208,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: [(566, 354, 1253, 'regular', Decimal('0.26'), Decimal('5.16'), None, None, None, None, None, 'Nota aggiornata 55', None)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1286, title=Media_4810>
[DEBUG] fetch_one success: RealDictRow({'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] Built object=<Video id=1286, title=Media_4810>
[DEBUG][Media.fetch] Data from DB={'id': 1267, 'type': 'video', 'user_id': 355, 'title': 'Media_1505', 'year': 2011, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 99471), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1505, type=video, year=2011, user_id=355, kwargs={'id': 1267, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Built object=<Video id=1286, title=Media_4810>
[DEBUG][Media.__init__] Extra attr: id=1267
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1267, title=Media_1505>
[DEBUG][Media.fetch] Built object=<Video id=1267, title=Media_1505>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1187,)
[DEBUG] fetch_one success: RealDictRow({'id': 1233, 'type': 'document', 'user_id': 361, 'title': 'Media_6787', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 893063), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1233, 'type': 'document', 'user_id': 361, 'title': 'Media_6787', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 893063), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1239, title=Media_5674>
[DEBUG][delete_object] Deleting object <Song id=1239, title=Media_5674>
[DEBUG][Media.delete] Called on <Song id=1239, title=Media_5674>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_6787, type=document, year=2014, user_id=361, kwargs={'id': 1233, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1233
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1241,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 362})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1255,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1154,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1202, title=Media_7744>
[DEBUG][delete_object] Deleting object <Song id=1202, title=Media_7744>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1247, title=Media_8829>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1243,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1275, 'type': 'video', 'user_id': 356, 'title': 'Media_4617', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 6, 153114), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1259,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_object] Deleting object <Document id=1247, title=Media_8829>
[DEBUG][Media.delete] Called on <Song id=1202, title=Media_7744>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1217, 'type': 'video', 'user_id': 362, 'title': 'Media_6854', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 58, 571395), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1275, 'type': 'video', 'user_id': 356, 'title': 'Media_4617', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 6, 153114), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4617, type=video, year=2007, user_id=356, kwargs={'id': 1275, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1275
[DEBUG][Media.delete] Called on <Document id=1247, title=Media_8829>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1217, 'type': 'video', 'user_id': 362, 'title': 'Media_6854', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 58, 571395), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Aggiornato 950', datetime.date(2025, 9, 14))]
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_one success: RealDictRow({'id': 1299})
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: [(2055, 354, 1290, None, None, 'Aggiornato 434', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Called with title=Media_6854, type=video, year=2016, user_id=362, kwargs={'id': 1217, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1245,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] Retrieved object=<Video id=1206, title=Media_2820>
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 950', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] Retrieved object=<Video id=1234, title=Media_8514>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1257,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(576, 360, 1271, 'regular', Decimal('1.02'), Decimal('4.36'), None, None, None, None, None, 'Nota 843', None)]
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: id=1217
[DEBUG] fetch_one success: RealDictRow({'id': 1297})
[DEBUG][Media.to_dict] <Video id=1206, title=Media_2820> -> {'media_id': 1206, 'type': 'video', 'title': 'Media_2820', 'user_id': 358, 'year': 2025, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:39:48.986938', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG from_dict] data={'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 950', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: [(2054, 360, 1291, None, None, 'Aggiornato 540', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Finished -> <Video id=1275, title=Media_4617>
[DEBUG][Media.to_dict] <Video id=1234, title=Media_8514> -> {'media_id': 1234, 'type': 'video', 'title': 'Media_8514', 'user_id': 358, 'year': 2021, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:16.214780', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1252,)
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 950'}
[DEBUG delete_comment] user_id=353, comment_id=2060
[DEBUG][Media.fetch] Called cls=Media, media_id=1284
[DEBUG][get_video] STATUS=OK, TIME=15.6707s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Commento 765', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][get_video] STATUS=OK, TIME=13.2217s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1206], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 356})
[DEBUG delete_comment] fetched comment: [{'id': 2054, 'user_id': 360, 'media_id': 1291, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 540', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][dispatch_command] START - command=delete_video, args=[1234], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Called with title=Media_1770, type=document, year=2019, user_id=360, kwargs={'id': 1279, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1279
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1240, 'type': 'video', 'user_id': 361, 'title': 'Media_1916', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 22, 699230), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched comment: [{'id': 2055, 'user_id': 354, 'media_id': 1290, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 434', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765'}
[DEBUG][get_object] Retrieved object=<Document id=1228, title=Media_5208>
[DEBUG] fetch_one success: RealDictRow({'id': 1256, 'type': 'document', 'user_id': 358, 'title': 'Media_9797', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 41, 666466), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] cls=Video, object_id=1234
[DEBUG] db_get_following result: []
[DEBUG][create_comment] STATUS=OK, TIME=20.1870s, TAG=OK
[DEBUG][Media.to_dict] <Document id=1228, title=Media_5208> -> {'media_id': 1228, 'type': 'document', 'title': 'Media_5208', 'user_id': 360, 'year': 2010, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:09.603593', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Document id=1279, title=Media_1770>
[DEBUG][Media.fetch] Called cls=Video, media_id=1234
[DEBUG][Media.fetch] Built object=<Video id=1275, title=Media_4617>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(568, 359, 1238, 'regular', Decimal('2.14'), Decimal('2.56'), None, None, None, None, None, 'Nota aggiornata 218', None)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1229,)
[DEBUG][dispatch_command] START - command=update_comment, args=[2062, 'Aggiornato 359'], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1184,)
[DEBUG][Media.fetch] Data from DB={'id': 1256, 'type': 'document', 'user_id': 358, 'title': 'Media_9797', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 41, 666466), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9797, type=document, year=2012, user_id=358, kwargs={'id': 1256, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1256
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_one success: RealDictRow({'id': 1239})
[DEBUG][Media.__init__] Finished -> <Document id=1233, title=Media_6787>
[DEBUG][Media.fetch] Built object=<Document id=1233, title=Media_6787>
[DEBUG] fetch_one success: RealDictRow({'id': 354})
[DEBUG][Media.fetch] Called cls=Media, media_id=1287
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1217, title=Media_6854>
[DEBUG][Media.fetch] Built object=<Video id=1217, title=Media_6854>
[DEBUG][Media.fetch] Built object=<Document id=1279, title=Media_1770>
[DEBUG fetch_by_id] comment_id=2062
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1263,)
[DEBUG add_comment] new_id returned from DB: 2063
[DEBUG][Media.fetch] Data from DB={'id': 1240, 'type': 'video', 'user_id': 361, 'title': 'Media_1916', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 22, 699230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1916, type=video, year=2013, user_id=361, kwargs={'id': 1240, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1240
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1222,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Document id=1256, title=Media_9797>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_document] STATUS=OK, TIME=8.7351s, TAG=OK
[DEBUG][Media.fetch] Built object=<Document id=1256, title=Media_9797>
[DEBUG] fetch_one success: RealDictRow({'id': 360})
[DEBUG add_comment] new_id returned from DB: 2064
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 485', 571)
[DEBUG] db_get_following result: [(570, 359, 1266, 'regular', Decimal('5.06'), Decimal('5.38'), None, None, None, None, None, 'Nota aggiornata 142', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] cls=Video, object_id=1206
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1236, 'type': 'document', 'user_id': 354, 'title': 'Media_4531', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 10161), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Video id=1240, title=Media_1916>
[DEBUG][Media.fetch] Built object=<Video id=1240, title=Media_1916>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Called cls=Video, media_id=1206
[DEBUG] db_get_following result: [(566, 354, 1253, 'regular', Decimal('0.26'), Decimal('5.16'), None, None, None, None, None, 'Nota aggiornata 55', None)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1195,)
[DEBUG] db_get_following result: [(2057, 358, 1294, None, None, 'Aggiornato 868', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Data from DB={'id': 1236, 'type': 'document', 'user_id': 354, 'title': 'Media_4531', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 10161), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 905', 573)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2053,)
[DEBUG][dispatch_command] START - command=delete_document, args=[1228], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1228
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Data from DB={'id': 1281, 'type': 'document', 'user_id': 359, 'title': 'Media_8330', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 24, 43093), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: [(577, 355, 1283, 'regular', Decimal('1.76'), Decimal('3.28'), None, None, None, None, None, 'Nota 4', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1215,)
[DEBUG][Media.fetch] Called cls=Document, media_id=1228
[DEBUG] db_get_following result: [(2056, 360, 1293, None, None, 'Aggiornato 737', datetime.date(2025, 9, 14))]
[DEBUG][Media.__init__] Called with title=Media_8330, type=document, year=2014, user_id=359, kwargs={'id': 1281, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1281
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1251,)
[DEBUG][get_object] Retrieved object=<Video id=1203, title=Media_9235>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1196,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1184
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6376>
[DEBUG][delete_document] STATUS=OK, TIME=34.3238s, TAG=OK
[DEBUG][Media.__init__] Called with title=Media_4531, type=document, year=2016, user_id=354, kwargs={'id': 1236, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleting object <Video id=1203, title=Media_9235>
[DEBUG] fetch_one success: RealDictRow({'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1189,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1191,)
[DEBUG delete_comment] fetched comment: [{'id': 2056, 'user_id': 360, 'media_id': 1293, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 737', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1193,)
[DEBUG][Media.__init__] Extra attr: id=1236
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Called on <Video id=1203, title=Media_9235>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1254,)
[DEBUG][Media.fetch] Data from DB={'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1435, type=video, year=2002, user_id=357, kwargs={'id': 1278, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1278
[DEBUG] fetch_one success: RealDictRow({'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1249,)
[DEBUG] fetch_one success: RealDictRow({'id': 1282})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1221,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1175,)
[DEBUG][update_note] STATUS=OK, TIME=12.0192s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[571], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=353, note_id=571
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 677', 2059)
[DEBUG][get_object] Retrieved object=<Document id=1262, title=Media_1728>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1199,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (567,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1278, title=Media_1435>
[DEBUG][Media.fetch] Built object=<Video id=1278, title=Media_1435>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1226, title=Media_6653>
[DEBUG] db_get_following result: [(575, 358, 1273, 'regular', Decimal('2.43'), Decimal('4.63'), None, None, None, None, None, 'Nota 495', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Commento 18', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1161,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_9951, type=video, year=2012, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][delete_object] Deleting object <Document id=1226, title=Media_6653>
[DEBUG][Media.delete] Called on <Document id=1226, title=Media_6653>
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (565,)
[DEBUG] fetch_one success: RealDictRow({'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1186,)
[DEBUG][Media.__init__] Finished -> <Document id=1281, title=Media_8330>
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1259,)
[DEBUG delete_comment] fetched media: {'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG update_comment] fetched comment: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 18', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][delete_object] Deleting object <Document id=1262, title=Media_1728>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2060, 353, 1289, None, None, 'Aggiornato 950', datetime.date(2025, 9, 14))]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(576, 360, 1271, 'regular', Decimal('1.02'), Decimal('4.36'), None, None, None, None, None, 'Nota 843', None)]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1236, title=Media_4531>
[DEBUG][Media.fetch] Built object=<Document id=1236, title=Media_4531>
[DEBUG] fetch_one success: RealDictRow({'id': 1202})
[DEBUG][Media.delete] Deleted media_id=1191
[DEBUG][update_note] STATUS=OK, TIME=12.0361s, TAG=OK
[DEBUG delete_comment] fetched comment: [{'id': 2057, 'user_id': 358, 'media_id': 1294, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 868', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1284, title=Media_9951>
[DEBUG] fetch_one success: RealDictRow({'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1261,)
[DEBUG][Media.delete] Called on <Document id=1262, title=Media_1728>
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_9555>
[DEBUG][get_object] Retrieved object=<Document id=1232, title=Media_1193>
[DEBUG][Media.to_dict] <Document id=1232, title=Media_1193> -> {'media_id': 1232, 'type': 'document', 'title': 'Media_1193', 'user_id': 356, 'year': 2006, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:14.445800', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1243,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1225, title=Media_2695>
[DEBUG] fetch_one success: RealDictRow({'id': 1234, 'type': 'video', 'user_id': 358, 'title': 'Media_8514', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 16, 214780), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Commento 918', datetime.date(2025, 9, 14))]
[DEBUG][delete_song] STATUS=OK, TIME=34.9774s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_document] STATUS=OK, TIME=6.7285s, TAG=OK
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=14.7511s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1187,)
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1234, 'type': 'video', 'user_id': 358, 'title': 'Media_8514', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 16, 214780), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8514, type=video, year=2021, user_id=358, kwargs={'id': 1234, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1234
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_note] STATUS=OK, TIME=10.4738s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1239,)
[DEBUG][dispatch_command] START - command=delete_document, args=[1232], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.from_dict] Built object=<Video id=1284, title=Media_9951>
[DEBUG] fetch_all returned 0 rows
[DEBUG update_comment] update_comment_db result: True
[DEBUG][Media.to_dict] <Song id=1225, title=Media_2695> -> {'media_id': 1225, 'type': 'song', 'title': 'Media_2695', 'user_id': 357, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:08.361069', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.fetch] Built object=<Document id=1281, title=Media_8330>
[DEBUG delete_comment] fetched comment: [{'id': 2060, 'user_id': 353, 'media_id': 1289, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 950', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1208,)
[DEBUG] fetch_one success: RealDictRow({'id': 1280})
[DEBUG] db_get_following result: []
[DEBUG][get_object] cls=Document, object_id=1232
[DEBUG][Media.fetch] Built object=<Video id=1284, title=Media_9951>
ERROR:services.interventions_services:Invalid time range: start_time=8.21789452231451, end_time=6.062705357979735
[DEBUG] db_get_following result: []
[DEBUG][update_comment] STATUS=OK, TIME=8.8365s, TAG=OK
[DEBUG][get_song] STATUS=OK, TIME=15.8523s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[573], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG __init__] Created Comment object: {'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918'}
[DEBUG][dispatch_command] START - command=get_document, args=[1272], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=create_note, args=[1292, 'regular', 7.999827781899439, 4.9809676878151095, None, None, None, None, 'Nota 481'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.delete] Deleted media_id=1161
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_9278>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG add_comment] Created Comment object from DB: {'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918'}
[DEBUG][get_object] Retrieved object=<Video id=1212, title=Media_1601>
[DEBUG][delete_object] Deleting object <Video id=1212, title=Media_1601>
[DEBUG][Media.delete] Called on <Video id=1212, title=Media_1601>
[DEBUG] db_get_following result: [(578, 362, 1270, 'regular', Decimal('7.15'), Decimal('9.10'), None, None, None, None, None, 'Nota 46', None)]
[DEBUG][create_note] STATUS=OK, TIME=6.2006s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2059], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=359, note_id=573
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_object] cls=Document, object_id=1272
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(570, 359, 1266, 'regular', Decimal('5.06'), Decimal('5.38'), None, None, None, None, None, 'Nota aggiornata 142', None)]
[DEBUG][delete_note] STATUS=OK, TIME=10.4609s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1246], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1246
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1248,)
[DEBUG] fetch_one success: RealDictRow({'id': 1276})
[DEBUG][dispatch_command] START - command=get_video, args=[1284], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1154,)
[DEBUG fetch_by_id] comment_id=2059
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1213,)
[DEBUG fetch_by_id] comment_id=2063
[DEBUG][Media.fetch] Called cls=Document, media_id=1232
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Called cls=Video, media_id=1246
[DEBUG delete_comment] fetched media: {'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] cls=Video, object_id=1284
[DEBUG] db_get_following result: [(574, 361, 1277, 'regular', Decimal('4.07'), Decimal('5.13'), None, None, None, None, None, 'Nota 358', None)]
[DEBUG][Media.__init__] Finished -> <Video id=1234, title=Media_8514>
[DEBUG][Media.fetch] Built object=<Video id=1234, title=Media_8514>
[DEBUG] fetch_one success: RealDictRow({'id': 1285})
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_song, args=[1225], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1225
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1257,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(568, 359, 1238, 'regular', Decimal('2.14'), Decimal('2.56'), None, None, None, None, None, 'Nota aggiornata 218', None)]
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Commento 765', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Called cls=Video, media_id=1284
[DEBUG][get_object] cls=Song, object_id=1225
[DEBUG] fetch_one success: RealDictRow({'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Document, media_id=1272
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG from_dict] data={'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1268, title=Media_4856>
[DEBUG][delete_object] Deleting object <Video id=1268, title=Media_4856>
[DEBUG][Media.delete] Called on <Video id=1268, title=Media_4856>
[DEBUG delete_comment] fetched media: {'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Song, media_id=1225
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Commento 389', datetime.date(2025, 9, 14))]
[DEBUG add_comment] fetch_comment_db returned: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG __init__] Created Comment object: {'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389'}
[DEBUG] fetch_all returned 0 rows
[DEBUG __init__] Created Comment object: {'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765'}
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1247})
[DEBUG][delete_song] STATUS=OK, TIME=46.5686s, TAG=OK
[DEBUG add_comment] Created Comment object from DB: {'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389'}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(579, 354, 1282, 'regular', Decimal('6.31'), Decimal('8.55'), None, None, None, None, None, 'Nota 351', None)]
[DEBUG update_comment] user_id=357, comment_id=2062, new_text=Aggiornato 359
[DEBUG][create_note] STATUS=OK, TIME=13.0306s, TAG=OK
[DEBUG fetch_by_id] comment_id=2064
[DEBUG][dispatch_command] START - command=update_note, args=[579, 'Nota aggiornata 852'], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=354, note_id=579
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1226})
[DEBUG][Media.delete] Deleted media_id=1154
[DEBUG] fetch_one success: RealDictRow({'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(577, 355, 1283, 'regular', Decimal('1.76'), Decimal('3.28'), None, None, None, None, None, 'Nota 4', None)]
[DEBUG delete_comment] fetched media: {'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1252,)
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_7050>
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_video] STATUS=OK, TIME=37.8174s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1195,)
[DEBUG][get_object] Retrieved object=<Document id=1235, title=Media_5882>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.to_dict] <Document id=1235, title=Media_5882> -> {'media_id': 1235, 'type': 'document', 'title': 'Media_5882', 'user_id': 354, 'year': 2024, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:19.003653', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(569, 360, 1250, 'regular', Decimal('1.81'), Decimal('5.26'), None, None, None, None, None, 'Nota aggiornata 304', None)]
[DEBUG][get_document] STATUS=OK, TIME=6.9288s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1235], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1235
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1185,)
[DEBUG][Media.fetch] Called cls=Document, media_id=1235
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 791', 2061)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(580, 360, 1280, 'regular', Decimal('6.30'), Decimal('7.43'), None, None, None, None, None, 'Nota 84', None)]
[DEBUG][create_note] STATUS=OK, TIME=15.9826s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[580, 'Nota aggiornata 170'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=360, note_id=580
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1207, title=Media_6052>
[DEBUG][delete_object] Deleting object <Song id=1207, title=Media_6052>
[DEBUG][Media.delete] Called on <Song id=1207, title=Media_6052>
[DEBUG] fetch_one success: RealDictRow({'id': 1206, 'type': 'video', 'user_id': 358, 'title': 'Media_2820', 'year': 2025, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 48, 986938), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1206, 'type': 'video', 'user_id': 358, 'title': 'Media_2820', 'year': 2025, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 39, 48, 986938), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2820, type=video, year=2025, user_id=358, kwargs={'id': 1206, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1206
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1206, title=Media_2820>
[DEBUG][Media.fetch] Built object=<Video id=1206, title=Media_2820>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1241,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1222,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1258, title=Media_1339>
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleting object <Document id=1258, title=Media_1339>
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Called on <Document id=1258, title=Media_1339>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1247,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1215,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1251,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(575, 358, 1273, 'regular', Decimal('2.43'), Decimal('4.63'), None, None, None, None, None, 'Nota 495', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1212})
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (568,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(572, 356, 1264, 'regular', Decimal('1.88'), Decimal('6.13'), None, None, None, None, None, 'Nota aggiornata 711', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2055,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (566,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1255,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1186,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG update_comment] update_comment_db result: True
[DEBUG][update_comment] STATUS=OK, TIME=7.1508s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2061], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2061
[DEBUG] fetch_one success: RealDictRow({'id': 362})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1260, title=Media_3540>
[DEBUG][delete_object] Deleting object <Song id=1260, title=Media_3540>
[DEBUG][Media.delete] Called on <Song id=1260, title=Media_3540>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1292
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1228, 'type': 'document', 'user_id': 360, 'title': 'Media_5208', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 9, 603593), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1228, 'type': 'document', 'user_id': 360, 'title': 'Media_5208', 'year': 2010, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 9, 603593), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1196,)
[DEBUG][Media.__init__] Called with title=Media_5208, type=document, year=2010, user_id=360, kwargs={'id': 1228, 'recording_date': None, 'performer_id': None}
[DEBUG][get_object] Retrieved object=<Video id=1223, title=Media_4797>
[DEBUG][Media.__init__] Extra attr: id=1228
[DEBUG][delete_object] Deleting object <Video id=1223, title=Media_4797>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.delete] Called on <Video id=1223, title=Media_4797>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1228, title=Media_5208>
[DEBUG][Media.fetch] Built object=<Document id=1228, title=Media_5208>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(578, 362, 1270, 'regular', Decimal('7.15'), Decimal('9.10'), None, None, None, None, None, 'Nota 46', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1251
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_8570>
[DEBUG][delete_video] STATUS=OK, TIME=32.8619s, TAG=OK
[DEBUG][delete_note] STATUS=OK, TIME=8.8165s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][dispatch_command] START - command=get_document, args=[1238], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1248,)
[DEBUG][Media.from_dict] cls=Media, data={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5096, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1259,)
[DEBUG] fetch_all returned 1 rows
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1199,)
[DEBUG] fetch_one success: RealDictRow({'id': 1203})
[DEBUG][get_object] cls=Document, object_id=1238
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Commento 918', datetime.date(2025, 9, 14))]
[DEBUG][delete_comment] STATUS=OK, TIME=11.3602s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1290, 'regular', 3.616712696907589, 4.422710467538269, None, None, None, None, 'Nota 559'], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Called cls=Document, media_id=1238
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG delete_comment] fetched media: {'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_note] STATUS=OK, TIME=10.1435s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Song id=1287, title=Media_5096>
[DEBUG][Media.from_dict] Built object=<Song id=1287, title=Media_5096>
[DEBUG][Media.fetch] Built object=<Song id=1287, title=Media_5096>
ERROR:services.interventions_services:Invalid time range: start_time=8.998312193728916, end_time=2.8117849429441364
[DEBUG from_dict] data={'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG][create_note] STATUS=OK, TIME=8.2004s, TAG=OK
[DEBUG __init__] Created Comment object: {'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918'}
[DEBUG][get_object] Retrieved object=<Video id=1231, title=Media_1305>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1254,)
[DEBUG] fetch_one success: RealDictRow({'id': 1232, 'type': 'document', 'user_id': 356, 'title': 'Media_1193', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 445800), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][dispatch_command] START - command=get_song, args=[1287], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][create_comment] STATUS=OK, TIME=14.8061s, TAG=OK
[DEBUG][delete_object] Deleting object <Video id=1231, title=Media_1305>
[DEBUG][get_object] Retrieved object=<Song id=1274, title=Media_6866>
[DEBUG][get_song_services] song_id=1287
[DEBUG][dispatch_command] START - command=update_comment, args=[2063, 'Aggiornato 688'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] comment_id=2063
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1229,)
[DEBUG][delete_object] Deleting object <Song id=1274, title=Media_6866>
[DEBUG][get_object] cls=Song, object_id=1287
[DEBUG][dispatch_command] START - command=get_song, args=[1253], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_object] Retrieved object=<Song id=1269, title=Media_1272>
[DEBUG][Media.fetch] Data from DB={'id': 1232, 'type': 'document', 'user_id': 356, 'title': 'Media_1193', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 445800), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.delete] Called on <Video id=1231, title=Media_1305>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.delete] Called on <Song id=1274, title=Media_6866>
[DEBUG][Media.fetch] Called cls=Song, media_id=1287
[DEBUG][get_song_services] song_id=1253
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_1193, type=document, year=2006, user_id=356, kwargs={'id': 1232, 'recording_date': None, 'performer_id': None}
[DEBUG][get_object] cls=Song, object_id=1253
[DEBUG][Media.fetch] Called cls=Song, media_id=1253
[DEBUG][Media.__init__] Extra attr: id=1232
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][delete_object] Deleting object <Song id=1269, title=Media_1272>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.delete] Called on <Song id=1269, title=Media_1272>
[DEBUG][Media.__init__] Finished -> <Document id=1232, title=Media_1193>
[DEBUG][Media.fetch] Built object=<Document id=1232, title=Media_1193>
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 500', 576)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(572, 356, 1264, 'regular', Decimal('1.88'), Decimal('6.13'), None, None, None, None, None, 'Nota aggiornata 711', None)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1245,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1249,)
[DEBUG] fetch_one success: RealDictRow({'id': 1272, 'type': 'document', 'user_id': 361, 'title': 'Media_1395', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 99887), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1272, 'type': 'document', 'user_id': 361, 'title': 'Media_1395', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 99887), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1395, type=document, year=2014, user_id=361, kwargs={'id': 1272, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1272
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1272, title=Media_1395>
[DEBUG][Media.fetch] Built object=<Document id=1272, title=Media_1395>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1193,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1263,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1236, title=Media_4531>
[DEBUG][Media.to_dict] <Document id=1236, title=Media_4531> -> {'media_id': 1236, 'type': 'document', 'title': 'Media_4531', 'user_id': 354, 'year': 2016, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:20.010161', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=6.0118s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1236], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1236
[DEBUG][Media.fetch] Called cls=Document, media_id=1236
[DEBUG] fetch_one success: RealDictRow({'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1252,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1208,)
[DEBUG] fetch_one success: RealDictRow({'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9951, type=video, year=2012, user_id=358, kwargs={'id': 1284, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1284
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1213,)
[DEBUG][Media.delete] Deleted media_id=1229
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2058,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_5660>
[DEBUG] db_get_following result: []
[DEBUG][delete_video] STATUS=OK, TIME=39.0003s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][update_note] STATUS=OK, TIME=10.0457s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1268})
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 877', 577)
[DEBUG][Media.__init__] Finished -> <Video id=1284, title=Media_9951>
[DEBUG][dispatch_command] START - command=delete_note, args=[576], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Built object=<Video id=1284, title=Media_9951>
[DEBUG delete_note] START - user_id=360, note_id=576
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1202,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1242, title=Media_8574>
[DEBUG][Media.to_dict] <Video id=1242, title=Media_8574> -> {'media_id': 1242, 'type': 'video', 'title': 'Media_8574', 'user_id': 358, 'year': 2019, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:30.098429', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=12.6831s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1242], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1242
[DEBUG][Media.fetch] Called cls=Video, media_id=1242
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1189,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1239,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1267, title=Media_1505>
[DEBUG][delete_object] Deleting object <Video id=1267, title=Media_1505>
[DEBUG][Media.delete] Called on <Video id=1267, title=Media_1505>
[DEBUG] fetch_one success: RealDictRow({'id': 1246, 'type': 'video', 'user_id': 356, 'title': 'Media_9534', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 524013), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1246, 'type': 'video', 'user_id': 356, 'title': 'Media_9534', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 524013), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9534, type=video, year=2000, user_id=356, kwargs={'id': 1246, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1246
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1259,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1226,)
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Commento 389', datetime.date(2025, 9, 14))]
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 168', 578)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Video id=1246, title=Media_9534>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1257,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1243,)
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Built object=<Video id=1246, title=Media_9534>
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1286})
[DEBUG from_dict] data={'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] db_get_following result: []
[DEBUG __init__] Created Comment object: {'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389'}
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Document id=1233, title=Media_6787>
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][create_comment] STATUS=OK, TIME=19.8413s, TAG=OK
[DEBUG][Media.to_dict] <Document id=1233, title=Media_6787> -> {'media_id': 1233, 'type': 'document', 'title': 'Media_6787', 'user_id': 361, 'year': 2014, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:14.893063', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][delete_comment] STATUS=OK, TIME=10.9467s, TAG=OK
[DEBUG][dispatch_command] START - command=update_comment, args=[2064, 'Aggiornato 814'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_document] STATUS=OK, TIME=9.7269s, TAG=OK
[DEBUG][update_note] STATUS=OK, TIME=8.2243s, TAG=OK
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 937', 575)
[DEBUG] db_get_following result: [(579, 354, 1282, 'regular', Decimal('6.31'), Decimal('8.55'), None, None, None, None, None, 'Nota 351', None)]
[DEBUG fetch_by_id] comment_id=2064
[DEBUG][dispatch_command] START - command=delete_document, args=[1233], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1233
[DEBUG][dispatch_command] START - command=create_note, args=[1288, 'regular', 1.0648272595214059, 3.9398269631073113, None, None, None, None, 'Nota 411'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1203,)
[DEBUG] fetch_one success: RealDictRow({'id': 1207})
[DEBUG][Media.fetch] Called cls=Document, media_id=1233
[DEBUG][dispatch_command] START - command=delete_note, args=[577], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 1260})
[DEBUG delete_note] START - user_id=355, note_id=577
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Document id=1279, title=Media_1770>
[DEBUG][Media.to_dict] <Document id=1279, title=Media_1770> -> {'media_id': 1279, 'type': 'document', 'title': 'Media_1770', 'user_id': 360, 'year': 2019, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:20.171555', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_one success: RealDictRow({'id': 1223})
[DEBUG][get_document] STATUS=OK, TIME=6.8374s, TAG=OK
[DEBUG][Media.fetch] Called cls=Media, media_id=1290
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=delete_document, args=[1279], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(574, 361, 1277, 'regular', Decimal('4.07'), Decimal('5.13'), None, None, None, None, None, 'Nota 358', None)]
[DEBUG][get_object] cls=Document, object_id=1279
[DEBUG][Media.fetch] Called cls=Document, media_id=1279
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Aggiornato 677', datetime.date(2025, 9, 14))]
[DEBUG][update_note] STATUS=OK, TIME=9.4930s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1231})
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1247,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1268,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1187,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1241,)
[DEBUG][dispatch_command] START - command=delete_note, args=[578], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1185,)
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1243
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_2864>
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 677', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 677', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 677'}
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2054,)
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2060,)
[DEBUG delete_note] START - user_id=362, note_id=578
[DEBUG][delete_document] STATUS=OK, TIME=38.3946s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1175,)
[DEBUG][get_object] Retrieved object=<Document id=1256, title=Media_9797>
[DEBUG] fetch_one success: RealDictRow({'id': 1262})
[DEBUG] fetch_one success: RealDictRow({'id': 1258})
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1199,)
[DEBUG] fetch_all returned 1 rows
[DEBUG delete_comment] user_id=359, comment_id=2059
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.to_dict] <Document id=1256, title=Media_9797> -> {'media_id': 1256, 'type': 'document', 'title': 'Media_9797', 'user_id': 358, 'year': 2012, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:41.666466', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1221,)
[DEBUG] db_get_following result: [(569, 360, 1250, 'regular', Decimal('1.81'), Decimal('5.26'), None, None, None, None, None, 'Nota aggiornata 304', None)]
[DEBUG][get_document] STATUS=OK, TIME=11.0760s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1256], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG][update_note] STATUS=OK, TIME=9.8200s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[575], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=358, note_id=575
[DEBUG] fetch_one success: RealDictRow({'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] cls=Document, object_id=1256
[DEBUG][Media.fetch] Called cls=Document, media_id=1256
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1252,)
[DEBUG] db_get_following result: [(582, 356, 1285, 'regular', Decimal('0.06'), Decimal('3.50'), None, None, None, None, None, 'Nota 65', None)]
[DEBUG] db_get_following result: [(571, 353, 1244, 'regular', Decimal('1.39'), Decimal('9.14'), None, None, None, None, None, 'Nota aggiornata 485', None)]
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Commento 765', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1186,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (572,)
[DEBUG][create_note] STATUS=OK, TIME=18.9999s, TAG=OK
[DEBUG update_comment] fetched comment: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 765', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.fetch] Data from DB={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1235, 'type': 'document', 'user_id': 354, 'title': 'Media_5882', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 19, 3653), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][dispatch_command] START - command=update_note, args=[582, 'Nota aggiornata 367'], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=356, note_id=582
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1261,)
[DEBUG][Media.fetch] Data from DB={'id': 1235, 'type': 'document', 'user_id': 354, 'title': 'Media_5882', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 19, 3653), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5882, type=document, year=2024, user_id=354, kwargs={'id': 1235, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1235
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1235, title=Media_5882>
[DEBUG][Media.fetch] Built object=<Document id=1235, title=Media_5882>
[DEBUG][Media.from_dict] cls=Media, data={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Called with title=Media_3787, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1274})
[DEBUG][Media.__init__] Finished -> <Song id=1292, title=Media_3787>
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Data from DB={'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1225, 'type': 'song', 'user_id': 357, 'title': 'Media_2695', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 8, 361069), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] Built object=<Song id=1292, title=Media_3787>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2056,)
[DEBUG][Media.delete] Deleted media_id=1241
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1275, title=Media_4617>
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3285>
[DEBUG][Media.__init__] Called with title=Media_2695, type=song, year=2020, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Built object=<Song id=1292, title=Media_3787>
ERROR:services.interventions_services:Invalid time range: start_time=7.999827781899439, end_time=4.9809676878151095
[DEBUG][delete_object] Deleting object <Video id=1275, title=Media_4617>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_one success: RealDictRow({'id': 1236, 'type': 'document', 'user_id': 354, 'title': 'Media_4531', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 10161), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 1269})
[DEBUG][Media.delete] Called on <Video id=1275, title=Media_4617>
[DEBUG][create_note] STATUS=OK, TIME=4.7422s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1238, 'type': 'document', 'user_id': 359, 'title': 'Media_1978', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 762671), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=10.6249s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1257,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1263,)
[DEBUG][delete_song] STATUS=OK, TIME=37.5255s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Song id=1225, title=Media_2695>
[DEBUG][Media.fetch] Data from DB={'id': 1238, 'type': 'document', 'user_id': 359, 'title': 'Media_1978', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 762671), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_one success: RealDictRow({'id': 1267})
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1195,)
[DEBUG][dispatch_command] START - command=get_song, args=[1292], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1292
[DEBUG][Media.from_dict] Built object=<Song id=1225, title=Media_2695>
[DEBUG][Media.__init__] Called with title=Media_1978, type=document, year=2012, user_id=359, kwargs={'id': 1238, 'recording_date': None, 'performer_id': None}
[DEBUG][dispatch_command] START - command=create_note, args=[1289, 'regular', 0.007508990003984861, 6.496296368950551, None, None, None, None, 'Nota 672'], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1236, 'type': 'document', 'user_id': 354, 'title': 'Media_4531', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 10161), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1254,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1189,)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_one success: RealDictRow({'id': 1242, 'type': 'video', 'user_id': 358, 'title': 'Media_8574', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 98429), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(579, 354, 1282, 'regular', Decimal('6.31'), Decimal('8.55'), None, None, None, None, None, 'Nota 351', None)]
[DEBUG][Media.__init__] Called with title=Media_4531, type=document, year=2016, user_id=354, kwargs={'id': 1236, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1236
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Commento 918', datetime.date(2025, 9, 14))]
[DEBUG][Media.fetch] Data from DB={'id': 1242, 'type': 'video', 'user_id': 358, 'title': 'Media_8574', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 98429), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Built object=<Song id=1225, title=Media_2695>
[DEBUG][Media.__init__] Extra attr: id=1238
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.__init__] Called with title=Media_8574, type=video, year=2019, user_id=358, kwargs={'id': 1242, 'recording_date': None, 'performer_id': None}
[DEBUG][delete_note] STATUS=OK, TIME=8.2041s, TAG=OK
[DEBUG][dispatch_command] START - command=get_song, args=[1264], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1264
[DEBUG][delete_comment] STATUS=OK, TIME=13.8306s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (570,)
[DEBUG][Media.__init__] Finished -> <Document id=1236, title=Media_4531>
[DEBUG][Media.fetch] Built object=<Document id=1236, title=Media_4531>
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] cls=Song, object_id=1264
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: id=1242
[DEBUG from_dict] data={'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][dispatch_command] START - command=create_note, args=[1291, 'regular', 1.1919800607783848, 0.5317515108515569, None, None, None, None, 'Nota 716'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1239,)
[DEBUG][get_object] cls=Song, object_id=1292
[DEBUG][Media.fetch] Called cls=Song, media_id=1292
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG __init__] Created Comment object: {'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918'}
[DEBUG update_comment] user_id=361, comment_id=2063, new_text=Aggiornato 688
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1193,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1238, title=Media_1978>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1226,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1212,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1215,)
[DEBUG][Media.fetch] Called cls=Song, media_id=1264
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1245,)
[DEBUG][Media.fetch] Built object=<Document id=1238, title=Media_1978>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1222,)
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Finished -> <Video id=1242, title=Media_8574>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(583, 362, 1286, 'regular', Decimal('8.62'), Decimal('8.97'), None, None, None, None, None, 'Nota 973', None)]
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1248,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1202,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(581, 362, 1276, 'regular', Decimal('0.26'), Decimal('5.66'), None, None, None, None, None, 'Nota 690', None)]
[DEBUG][Media.fetch] Built object=<Video id=1242, title=Media_8574>
[DEBUG][delete_comment] STATUS=OK, TIME=10.4344s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1217, title=Media_6854>
[DEBUG][delete_object] Deleting object <Video id=1217, title=Media_6854>
[DEBUG] fetch_one success: RealDictRow({'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][create_note] STATUS=OK, TIME=23.5889s, TAG=OK
[DEBUG][create_note] STATUS=OK, TIME=12.7843s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1293, 'regular', 4.730023921646588, 0.3704189196940755, None, None, None, None, 'Nota 791'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] Retrieved object=<Video id=1278, title=Media_1435>
[DEBUG][Media.delete] Called on <Video id=1217, title=Media_6854>
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Commento 389', datetime.date(2025, 9, 14))]
[DEBUG][Media.delete] Deleted media_id=1195
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5890>
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.to_dict] <Video id=1278, title=Media_1435> -> {'media_id': 1278, 'type': 'video', 'title': 'Media_1435', 'user_id': 357, 'year': 2002, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:15.970868', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1196,)
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2057,)
[DEBUG][dispatch_command] START - command=update_note, args=[581, 'Nota aggiornata 379'], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][get_video] STATUS=OK, TIME=8.7834s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (569,)
[DEBUG][dispatch_command] START - command=update_note, args=[583, 'Nota aggiornata 979'], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=362, note_id=583
[DEBUG][delete_note] STATUS=OK, TIME=13.1486s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1269,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1249,)
[DEBUG][delete_song] STATUS=OK, TIME=39.3699s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=get_song, args=[1266], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG __init__] Created Comment object: {'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389'}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1267,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_5096, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][dispatch_command] START - command=delete_video, args=[1278], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=362, note_id=581
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_song_services] song_id=1266
[DEBUG][get_object] cls=Video, object_id=1278
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1252,)
[DEBUG] fetch_one success: RealDictRow({'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Finished -> <Song id=1287, title=Media_5096>
[DEBUG][Media.from_dict] Built object=<Song id=1287, title=Media_5096>
[DEBUG][Media.fetch] Built object=<Song id=1287, title=Media_5096>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1208,)
[DEBUG update_comment] user_id=361, comment_id=2064, new_text=Aggiornato 814
[DEBUG][Media.fetch] Data from DB={'id': 1279, 'type': 'document', 'user_id': 360, 'title': 'Media_1770', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 20, 171555), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1260,)
[DEBUG][Media.fetch] Called cls=Video, media_id=1278
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1255,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1274,)
[DEBUG][get_object] cls=Song, object_id=1266
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1288
[DEBUG][Media.__init__] Called with title=Media_1770, type=document, year=2019, user_id=360, kwargs={'id': 1279, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Called cls=Song, media_id=1266
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1231,)
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1248
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(355, 'user242821@example.com', 'user242821', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1262,)
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Aggiornato 791', datetime.date(2025, 9, 14))]
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5286>
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 791', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][delete_song] STATUS=OK, TIME=32.7533s, TAG=OK
[DEBUG from_dict] data={'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 791', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG][Media.__init__] Extra attr: id=1279
[DEBUG __init__] Created Comment object: {'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 791'}
[DEBUG delete_comment] user_id=361, comment_id=2061
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: [(573, 359, 1265, 'regular', Decimal('3.99'), Decimal('4.25'), None, None, None, None, None, 'Nota aggiornata 905', None)]
[DEBUG][Media.__init__] Finished -> <Document id=1279, title=Media_1770>
[DEBUG] fetch_one success: RealDictRow({'id': 1256, 'type': 'document', 'user_id': 358, 'title': 'Media_9797', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 41, 666466), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Built object=<Document id=1279, title=Media_1770>
[DEBUG][Media.fetch] Data from DB={'id': 1256, 'type': 'document', 'user_id': 358, 'title': 'Media_9797', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 41, 666466), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1223,)
[DEBUG][Media.__init__] Called with title=Media_9797, type=document, year=2012, user_id=358, kwargs={'id': 1256, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1256
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1256, title=Media_9797>
[DEBUG][Media.fetch] Built object=<Document id=1256, title=Media_9797>
[DEBUG] fetch_one success: RealDictRow({'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6657, type=song, year=2000, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1253, title=Media_6657>
[DEBUG][Media.from_dict] Built object=<Song id=1253, title=Media_6657>
[DEBUG][Media.fetch] Built object=<Song id=1253, title=Media_6657>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(576, 360, 1271, 'regular', Decimal('1.02'), Decimal('4.36'), None, None, None, None, None, 'Nota aggiornata 500', None)]
[DEBUG][Media.delete] Deleted media_id=1196
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6446>
[DEBUG][delete_song] STATUS=OK, TIME=32.6279s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1259,)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=12.2253s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=create_note, args=[1294, 'regular', 4.4368582039775255, 8.281527470073913, None, None, None, None, 'Nota 204'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.delete] Deleted media_id=1249
[DEBUG][get_object] Retrieved object=<Video id=1206, title=Media_2820>
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4002>
[DEBUG][delete_object] Deleting object <Video id=1206, title=Media_2820>
[DEBUG][delete_video] STATUS=OK, TIME=32.4068s, TAG=OK
[DEBUG][Media.delete] Called on <Video id=1206, title=Media_2820>
[DEBUG][delete_note] STATUS=OK, TIME=10.1431s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1250], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1250
[DEBUG][Media.fetch] Called cls=Video, media_id=1250
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1268,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Video id=1237, title=Media_7336>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1207,)
[DEBUG] db_get_following result: [(2059, 359, 1295, None, None, 'Aggiornato 677', datetime.date(2025, 9, 14))]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1213,)
[DEBUG delete_comment] fetched comment: [{'id': 2059, 'user_id': 359, 'media_id': 1295, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 677', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.to_dict] <Video id=1237, title=Media_7336> -> {'media_id': 1237, 'type': 'video', 'title': 'Media_7336', 'user_id': 353, 'year': 2023, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:20.369200', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=14.4391s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1257,)
[DEBUG][dispatch_command] START - command=delete_video, args=[1237], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1237
[DEBUG][Media.fetch] Called cls=Video, media_id=1237
[DEBUG] fetch_one success: RealDictRow({'id': 1233, 'type': 'document', 'user_id': 361, 'title': 'Media_6787', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 893063), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1233, 'type': 'document', 'user_id': 361, 'title': 'Media_6787', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 14, 893063), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6787, type=document, year=2014, user_id=361, kwargs={'id': 1233, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.__init__] Extra attr: id=1233
[DEBUG][Media.fetch] Data from DB={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.from_dict] cls=Song, data={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1233, title=Media_6787>
[DEBUG][Media.__init__] Called with title=Media_3787, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Built object=<Document id=1233, title=Media_6787>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1199,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1292, title=Media_3787>
[DEBUG][Media.from_dict] Built object=<Song id=1292, title=Media_3787>
[DEBUG][Media.fetch] Built object=<Song id=1292, title=Media_3787>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1187,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1261,)
[DEBUG] fetch_one success: RealDictRow({'id': 1275})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1281, title=Media_8330>
[DEBUG][delete_object] Deleting object <Document id=1281, title=Media_8330>
[DEBUG][Media.delete] Called on <Document id=1281, title=Media_8330>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1278, 'type': 'video', 'user_id': 357, 'title': 'Media_1435', 'year': 2002, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 15, 970868), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1435, type=video, year=2002, user_id=357, kwargs={'id': 1278, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1278
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1278, title=Media_1435>
[DEBUG][Media.fetch] Built object=<Video id=1278, title=Media_1435>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1208,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1228, title=Media_5208>
[DEBUG][delete_object] Deleting object <Document id=1228, title=Media_5208>
[DEBUG][Media.delete] Called on <Document id=1228, title=Media_5208>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1263,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1226,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1221,)
[DEBUG][Media.delete] Deleted media_id=1187
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3804>
[DEBUG][delete_song] STATUS=OK, TIME=30.2349s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1217})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Commento 918', datetime.date(2025, 9, 14))]
[DEBUG][get_object] Retrieved object=<Video id=1240, title=Media_1916>
[DEBUG update_comment] fetched comment: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 918', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][Media.to_dict] <Video id=1240, title=Media_1916> -> {'media_id': 1240, 'type': 'video', 'title': 'Media_1916', 'user_id': 361, 'year': 2013, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:22.699230', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=15.9943s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1240], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1240
[DEBUG][Media.fetch] Called cls=Video, media_id=1240
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 359', 2062)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1247,)
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 226', 574)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1203,)
[DEBUG] fetch_one success: RealDictRow({'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8544, type=song, year=2003, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1288, title=Media_8544>
[DEBUG][Media.from_dict] Built object=<Song id=1288, title=Media_8544>
[DEBUG][Media.fetch] Built object=<Song id=1288, title=Media_8544>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1175,)
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 852', 579)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1234, title=Media_8514>
[DEBUG][delete_object] Deleting object <Video id=1234, title=Media_8514>
[DEBUG][Media.delete] Called on <Video id=1234, title=Media_8514>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1294
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(580, 360, 1280, 'regular', Decimal('6.30'), Decimal('7.43'), None, None, None, None, None, 'Nota 84', None)]
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1291
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1258,)
[DEBUG] fetch_one success: RealDictRow({'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Commento 389', datetime.date(2025, 9, 14))]
[DEBUG update_comment] fetched comment: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Commento 389', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG][update_comment] STATUS=OK, TIME=9.5501s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=delete_comment, args=[2062], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG fetch_by_id] comment_id=2062
[DEBUG][Media.from_dict] cls=Media, data={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5097, type=song, year=2015, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1290, title=Media_5097>
[DEBUG][Media.from_dict] Built object=<Song id=1290, title=Media_5097>
[DEBUG][Media.fetch] Built object=<Song id=1290, title=Media_5097>
[DEBUG] fetch_one success: RealDictRow({'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9052, type=song, year=2009, user_id=356, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1264, title=Media_9052>
[DEBUG][Media.from_dict] Built object=<Song id=1264, title=Media_9052>
[DEBUG][Media.fetch] Built object=<Song id=1264, title=Media_9052>
[DEBUG][update_note] STATUS=OK, TIME=14.7861s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1185,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1186,)
[DEBUG][dispatch_command] START - command=delete_note, args=[574], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=361, note_id=574
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1272, title=Media_1395>
[DEBUG][Media.to_dict] <Document id=1272, title=Media_1395> -> {'media_id': 1272, 'type': 'document', 'title': 'Media_1395', 'user_id': 361, 'year': 2014, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:04.099887', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=7.9702s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1272], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1272
[DEBUG][Media.fetch] Called cls=Document, media_id=1272
[DEBUG][update_note] STATUS=OK, TIME=7.0975s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[579], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=354, note_id=579
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1215,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1212,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1255,)
[DEBUG][Media.fetch] Called cls=Media, media_id=1293
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1202,)
[DEBUG] fetch_one success: RealDictRow({'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6457, type=song, year=2007, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1266, title=Media_6457>
[DEBUG][Media.from_dict] Built object=<Song id=1266, title=Media_6457>
[DEBUG][Media.fetch] Built object=<Song id=1266, title=Media_6457>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_one success: RealDictRow({'id': 1240, 'type': 'video', 'user_id': 361, 'title': 'Media_1916', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 22, 699230), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Called cls=Media, media_id=1289
[DEBUG][Media.fetch] Data from DB={'id': 1240, 'type': 'video', 'user_id': 361, 'title': 'Media_1916', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 22, 699230), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1916, type=video, year=2013, user_id=361, kwargs={'id': 1240, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1240
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1240, title=Media_1916>
[DEBUG][Media.fetch] Built object=<Video id=1240, title=Media_1916>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1207,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(571, 353, 1244, 'regular', Decimal('1.39'), Decimal('9.14'), None, None, None, None, None, 'Nota aggiornata 485', None)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1222,)
[DEBUG] fetch_one success: RealDictRow({'id': 1250, 'type': 'video', 'user_id': 360, 'title': 'Media_5372', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 755122), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1250, 'type': 'video', 'user_id': 360, 'title': 'Media_5372', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 755122), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5372, type=video, year=2016, user_id=360, kwargs={'id': 1250, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1250
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1250, title=Media_5372>
[DEBUG][Media.fetch] Built object=<Video id=1250, title=Media_5372>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1189,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1257,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1215
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7685>
[DEBUG][delete_document] STATUS=OK, TIME=29.9113s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(577, 355, 1283, 'regular', Decimal('1.76'), Decimal('3.28'), None, None, None, None, None, 'Nota aggiornata 877', None)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1231,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1260,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1267,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1268,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1217,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1269,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1245,)
[DEBUG][Media.delete] Deleted media_id=1222
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4306>
[DEBUG][delete_document] STATUS=OK, TIME=31.6044s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(576, 360, 1271, 'regular', Decimal('1.02'), Decimal('4.36'), None, None, None, None, None, 'Nota aggiornata 500', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1256, title=Media_9797>
[DEBUG][delete_object] Deleting object <Document id=1256, title=Media_9797>
[DEBUG][Media.delete] Called on <Document id=1256, title=Media_9797>
[DEBUG] fetch_one success: RealDictRow({'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1853, type=song, year=2017, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1291, title=Media_1853>
[DEBUG][Media.from_dict] Built object=<Song id=1291, title=Media_1853>
[DEBUG][Media.fetch] Built object=<Song id=1291, title=Media_1853>
ERROR:services.interventions_services:Invalid time range: start_time=1.1919800607783848, end_time=0.5317515108515569
[DEBUG][create_note] STATUS=OK, TIME=3.7242s, TAG=OK
[DEBUG][dispatch_command] START - command=get_song, args=[1291], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1291
[DEBUG][get_object] cls=Song, object_id=1291
[DEBUG][Media.fetch] Called cls=Song, media_id=1291
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1239,)
[DEBUG][Media.delete] Deleted media_id=1257
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(582, 356, 1285, 'regular', Decimal('0.06'), Decimal('3.50'), None, None, None, None, None, 'Nota 65', None)]
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_2596>
[DEBUG][delete_document] STATUS=OK, TIME=26.3260s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(573, 359, 1265, 'regular', Decimal('3.99'), Decimal('4.25'), None, None, None, None, None, 'Nota aggiornata 905', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1262,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1235, title=Media_5882>
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 688', 2063)
[DEBUG][delete_object] Deleting object <Document id=1235, title=Media_5882>
[DEBUG][Media.delete] Called on <Document id=1235, title=Media_5882>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1254,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1223,)
[DEBUG] fetch_one success: RealDictRow({'id': 1272, 'type': 'document', 'user_id': 361, 'title': 'Media_1395', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 99887), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1272, 'type': 'document', 'user_id': 361, 'title': 'Media_1395', 'year': 2014, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 99887), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1395, type=document, year=2014, user_id=361, kwargs={'id': 1272, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1272
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1272, title=Media_1395>
[DEBUG][Media.fetch] Built object=<Document id=1272, title=Media_1395>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1193,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1228})
[DEBUG] execute success: UPDATE comments SET text=%s WHERE id=%s ('Aggiornato 814', 2064)
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1212,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1263,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1247,)
[DEBUG] db_get_following result: [(2061, 361, 1296, None, None, 'Aggiornato 791', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2061, 'user_id': 361, 'media_id': 1296, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 791', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1232, title=Media_1193>
[DEBUG][delete_object] Deleting object <Document id=1232, title=Media_1193>
[DEBUG][Media.delete] Called on <Document id=1232, title=Media_1193>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1189,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1246, title=Media_9534>
[DEBUG][Media.to_dict] <Video id=1246, title=Media_9534> -> {'media_id': 1246, 'type': 'video', 'title': 'Media_9534', 'user_id': 356, 'year': 2000, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:31.524013', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=9.0858s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1246], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1246
[DEBUG][Media.fetch] Called cls=Video, media_id=1246
[DEBUG] fetch_one success: RealDictRow({'id': 1237, 'type': 'video', 'user_id': 353, 'title': 'Media_7336', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 369200), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1237, 'type': 'video', 'user_id': 353, 'title': 'Media_7336', 'year': 2023, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 369200), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7336, type=video, year=2023, user_id=353, kwargs={'id': 1237, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Extra attr: id=1237
[DEBUG] db_get_following result: [(578, 362, 1270, 'regular', Decimal('7.15'), Decimal('9.10'), None, None, None, None, None, 'Nota aggiornata 168', None)]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_one success: RealDictRow({'id': 1281})
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_one success: RealDictRow({'id': 1234})
[DEBUG][Media.__init__] Finished -> <Video id=1237, title=Media_7336>
[DEBUG][Media.fetch] Built object=<Video id=1237, title=Media_7336>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1274,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1238, title=Media_1978>
[DEBUG][Media.to_dict] <Document id=1238, title=Media_1978> -> {'media_id': 1238, 'type': 'document', 'title': 'Media_1978', 'user_id': 359, 'year': 2012, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:20.762671', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=7.4475s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1238], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1238
[DEBUG][Media.fetch] Called cls=Document, media_id=1238
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Aggiornato 359', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 359', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 359', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 359'}
[DEBUG delete_comment] user_id=357, comment_id=2062
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1259,)
[DEBUG] fetch_one success: RealDictRow({'id': 1206})
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][update_comment] STATUS=OK, TIME=7.1662s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_comment, args=[2063], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1275,)
[DEBUG fetch_by_id] comment_id=2063
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1208,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1252,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1199,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(575, 358, 1273, 'regular', Decimal('2.43'), Decimal('4.63'), None, None, None, None, None, 'Nota aggiornata 937', None)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1221,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1217,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(580, 360, 1280, 'regular', Decimal('6.30'), Decimal('7.43'), None, None, None, None, None, 'Nota 84', None)]
[DEBUG update_comment] update_comment_db result: True
[DEBUG] fetch_one success: RealDictRow({'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][update_comment] STATUS=OK, TIME=6.2022s, TAG=OK
[DEBUG][Media.fetch] Data from DB={'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][dispatch_command] START - command=delete_comment, args=[2064], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Called with title=Media_3850, type=document, year=2004, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG fetch_by_id] comment_id=2064
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1294, title=Media_3850>
[DEBUG][Media.from_dict] Built object=<Document id=1294, title=Media_3850>
[DEBUG][Media.fetch] Built object=<Document id=1294, title=Media_3850>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1175,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1203,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1269,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1186,)
[DEBUG][Media.delete] Deleted media_id=1259
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8102>
[DEBUG][delete_document] STATUS=OK, TIME=27.5731s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1231,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1213,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1255,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1185,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1284, title=Media_9951>
[DEBUG][Media.to_dict] <Video id=1284, title=Media_9951> -> {'media_id': 1284, 'type': 'video', 'title': 'Media_9951', 'user_id': 358, 'year': 2012, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:25.803102', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=9.9242s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1284], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1261,)
[DEBUG][Media.delete] Deleted media_id=1252
[DEBUG][get_object] cls=Video, object_id=1284
[DEBUG][Media.fetch] Called cls=Video, media_id=1284
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4944>
[DEBUG][delete_document] STATUS=OK, TIME=27.9768s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1208
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1239>
[DEBUG][delete_video] STATUS=OK, TIME=36.3502s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(582, 356, 1285, 'regular', Decimal('0.06'), Decimal('3.50'), None, None, None, None, None, 'Nota 65', None)]
[DEBUG][Media.delete] Deleted media_id=1199
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7671>
[DEBUG][delete_document] STATUS=OK, TIME=28.6984s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1221
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_8477>
[DEBUG][delete_video] STATUS=OK, TIME=35.4654s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(583, 362, 1286, 'regular', Decimal('8.62'), Decimal('8.97'), None, None, None, None, None, 'Nota 973', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1175
[DEBUG] fetch_one success: RealDictRow({'id': 1235})
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1236, title=Media_4531>
[DEBUG][delete_object] Deleting object <Document id=1236, title=Media_4531>
[DEBUG][Media.delete] Called on <Document id=1236, title=Media_4531>
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_7778>
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_video] STATUS=OK, TIME=37.9445s, TAG=OK
[DEBUG] db_get_following result: [(577, 355, 1283, 'regular', Decimal('1.76'), Decimal('3.28'), None, None, None, None, None, 'Nota aggiornata 877', None)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1202,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1258,)
[DEBUG] fetch_one success: RealDictRow({'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2076, type=video, year=2019, user_id=353, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1289, title=Media_2076>
[DEBUG][Media.from_dict] Built object=<Video id=1289, title=Media_2076>
[DEBUG][Media.fetch] Built object=<Video id=1289, title=Media_2076>
[DEBUG][Media.delete] Deleted media_id=1213
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_9014>
[DEBUG][delete_document] STATUS=OK, TIME=28.7778s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6146, type=video, year=2015, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_one success: RealDictRow({'id': 1256})
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1293, title=Media_6146>
[DEBUG][Media.from_dict] Built object=<Video id=1293, title=Media_6146>
[DEBUG][Media.fetch] Built object=<Video id=1293, title=Media_6146>
[DEBUG][Media.delete] Deleted media_id=1261
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_1015>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1226,)
[DEBUG][delete_song] STATUS=OK, TIME=37.3090s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (571,)
[DEBUG] fetch_one success: RealDictRow({'id': 1232})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1238, 'type': 'document', 'user_id': 359, 'title': 'Media_1978', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 762671), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1238, 'type': 'document', 'user_id': 359, 'title': 'Media_1978', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 20, 762671), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_1978, type=document, year=2012, user_id=359, kwargs={'id': 1238, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1238
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1238, title=Media_1978>
[DEBUG][Media.fetch] Built object=<Document id=1238, title=Media_1978>
ERROR:services.interventions_services:Invalid time range: start_time=4.730023921646588, end_time=0.3704189196940755
[DEBUG][create_note] STATUS=OK, TIME=5.5629s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(575, 358, 1273, 'regular', Decimal('2.43'), Decimal('4.63'), None, None, None, None, None, 'Nota aggiornata 937', None)]
[DEBUG delete_comment] fetched media: {'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (573,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=get_video, args=[1293], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1293
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Video, media_id=1293
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Song id=1253, title=Media_6657>
[DEBUG] db_get_following result: [(578, 362, 1270, 'regular', Decimal('7.15'), Decimal('9.10'), None, None, None, None, None, 'Nota aggiornata 168', None)]
[DEBUG][Media.to_dict] <Song id=1253, title=Media_6657> -> {'media_id': 1253, 'type': 'song', 'title': 'Media_6657', 'user_id': 354, 'year': 2000, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:33.840966', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=8.5345s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1253], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1253
[DEBUG][get_object] cls=Song, object_id=1253
[DEBUG][Media.fetch] Called cls=Song, media_id=1253
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1225, title=Media_2695>
[DEBUG][delete_object] Deleting object <Song id=1225, title=Media_2695>
[DEBUG][Media.delete] Called on <Song id=1225, title=Media_2695>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Aggiornato 814', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 814', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 814', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG] fetch_one success: RealDictRow({'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_one success: RealDictRow({'id': 360})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1260,)
[DEBUG delete_comment] fetched media: {'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG __init__] Created Comment object: {'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 814'}
[DEBUG delete_comment] user_id=361, comment_id=2064
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1245,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1239,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2062, 357, 1298, None, None, 'Aggiornato 359', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2062, 'user_id': 357, 'media_id': 1298, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 359', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (576,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][delete_note] STATUS=OK, TIME=12.0419s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG][dispatch_command] START - command=get_document, args=[1244], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: [(579, 354, 1282, 'regular', Decimal('6.31'), Decimal('8.55'), None, None, None, None, None, 'Nota aggiornata 852', None)]
[DEBUG][get_object] cls=Document, object_id=1244
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Document, media_id=1244
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1234,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1186,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1189,)
[DEBUG][delete_note] STATUS=OK, TIME=11.7845s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1228,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1235,)
[DEBUG] fetch_one success: RealDictRow({'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][dispatch_command] START - command=get_song, args=[1265], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 170', 580)
[DEBUG][get_song_services] song_id=1265
[DEBUG][Media.fetch] Data from DB={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] cls=Song, object_id=1265
[DEBUG][Media.from_dict] cls=Song, data={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Song, media_id=1265
[DEBUG][Media.__init__] Called with title=Media_1853, type=song, year=2017, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1291, title=Media_1853>
[DEBUG][Media.from_dict] Built object=<Song id=1291, title=Media_1853>
[DEBUG][Media.fetch] Built object=<Song id=1291, title=Media_1853>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1279, title=Media_1770>
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleting object <Document id=1279, title=Media_1770>
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Called on <Document id=1279, title=Media_1770>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1262,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1275,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1207,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Aggiornato 688', datetime.date(2025, 9, 14))]
[DEBUG fetch_by_id] fetch_comment_db returned: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 688', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG from_dict] data={'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 688', 'created_at': datetime.date(2025, 9, 14)}
[DEBUG __init__] Created Comment object: {'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 688'}
[DEBUG] fetch_all returned 0 rows
[DEBUG delete_comment] user_id=361, comment_id=2063
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1268,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1233, title=Media_6787>
[DEBUG][delete_object] Deleting object <Document id=1233, title=Media_6787>
[DEBUG][Media.delete] Called on <Document id=1233, title=Media_6787>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2061,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1267,)
[DEBUG][delete_note] STATUS=OK, TIME=8.7012s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1271], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1271
[DEBUG][Media.fetch] Called cls=Document, media_id=1271
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1232,)
[DEBUG] fetch_one success: RealDictRow({'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6146, type=video, year=2015, user_id=360, kwargs={'id': 1293, 'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1193,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1256,)
[DEBUG][Media.__init__] Extra attr: id=1293
[DEBUG] fetch_one success: RealDictRow({'id': 1246, 'type': 'video', 'user_id': 356, 'title': 'Media_9534', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 524013), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1269,)
[DEBUG][Media.fetch] Data from DB={'id': 1246, 'type': 'video', 'user_id': 356, 'title': 'Media_9534', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 31, 524013), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9534, type=video, year=2000, user_id=356, kwargs={'id': 1246, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1246
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1203,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.delete] Deleted media_id=1186
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_1608>
[DEBUG][Media.__init__] Finished -> <Video id=1293, title=Media_6146>
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1206,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1281,)
[DEBUG][delete_song] STATUS=OK, TIME=28.8330s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1255,)
[DEBUG][update_note] STATUS=OK, TIME=10.8218s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[580], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (577,)
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 367', 582)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1212,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1274,)
[DEBUG delete_note] START - user_id=360, note_id=580
[DEBUG][Media.__init__] Finished -> <Video id=1246, title=Media_9534>
[DEBUG][Media.fetch] Built object=<Video id=1293, title=Media_6146>
[DEBUG][Media.fetch] Built object=<Video id=1246, title=Media_9534>
[DEBUG][Media.delete] Deleted media_id=1189
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_7196>
[DEBUG][delete_song] STATUS=OK, TIME=27.2041s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1258,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(579, 354, 1282, 'regular', Decimal('6.31'), Decimal('8.55'), None, None, None, None, None, 'Nota aggiornata 852', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1225})
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][delete_comment] STATUS=OK, TIME=10.5995s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1296, 'regular', 8.06329187320947, 9.320196088853029, None, None, None, None, 'Nota 158'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2064, 361, 1297, None, None, 'Aggiornato 814', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2064, 'user_id': 361, 'media_id': 1297, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 814', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1185,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1287, title=Media_5096>
[DEBUG][Media.to_dict] <Song id=1287, title=Media_5096> -> {'media_id': 1287, 'type': 'song', 'title': 'Media_5096', 'user_id': 359, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:30.424217', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=10.0031s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1287], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1287
[DEBUG][get_object] cls=Song, object_id=1287
[DEBUG][Media.fetch] Called cls=Song, media_id=1287
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(581, 362, 1276, 'regular', Decimal('0.26'), Decimal('5.66'), None, None, None, None, None, 'Nota 690', None)]
[DEBUG][Media.delete] Deleted media_id=1193
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5844>
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (578,)
[DEBUG][delete_song] STATUS=OK, TIME=29.1671s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1223,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1217,)
[DEBUG][Media.delete] Deleted media_id=1255
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_8372>
[DEBUG][update_note] STATUS=OK, TIME=8.2577s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_video] STATUS=OK, TIME=39.4213s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_note] STATUS=OK, TIME=8.9519s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[582], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1231,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.from_dict] cls=Song, data={'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_2577, type=song, year=2008, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] Retrieved object=<Document id=1238, title=Media_1978>
[DEBUG delete_note] START - user_id=356, note_id=582
[DEBUG][Media.__init__] Finished -> <Song id=1265, title=Media_2577>
[DEBUG][dispatch_command] START - command=get_song, args=[1283], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1283
[DEBUG][get_object] cls=Song, object_id=1283
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1239,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1288})
[DEBUG][Media.fetch] Called cls=Song, media_id=1283
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1226,)
[DEBUG][delete_object] Deleting object <Document id=1238, title=Media_1978>
[DEBUG][Media.delete] Deleted media_id=1185
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1247,)
[DEBUG][Media.from_dict] Built object=<Song id=1265, title=Media_2577>
[DEBUG][get_object] Retrieved object=<Song id=1264, title=Media_9052>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1262,)
[DEBUG][Media.fetch] Built object=<Song id=1265, title=Media_2577>
[DEBUG][Media.to_dict] <Song id=1264, title=Media_9052> -> {'media_id': 1264, 'type': 'song', 'title': 'Media_9052', 'user_id': 356, 'year': 2009, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:57.977654', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (579,)
[DEBUG][Media.delete] Called on <Document id=1238, title=Media_1978>
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_4277>
[DEBUG][delete_song] STATUS=OK, TIME=36.5795s, TAG=OK
[DEBUG][get_object] Retrieved object=<Document id=1272, title=Media_1395>
[DEBUG][delete_object] Deleting object <Document id=1272, title=Media_1395>
[DEBUG][Media.delete] Called on <Document id=1272, title=Media_1395>
[DEBUG][get_song] STATUS=OK, TIME=7.9499s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1233})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_song, args=[1264], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1260,)
[DEBUG][delete_song_services] song_id=1264
[DEBUG][get_object] cls=Song, object_id=1264
[DEBUG][Media.fetch] Called cls=Song, media_id=1264
[DEBUG] fetch_one success: RealDictRow({'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1284, 'type': 'video', 'user_id': 358, 'title': 'Media_9951', 'year': 2012, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 803102), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9951, type=video, year=2012, user_id=358, kwargs={'id': 1284, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1284
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1284, title=Media_9951>
[DEBUG][Media.fetch] Built object=<Video id=1284, title=Media_9951>
[DEBUG][delete_note] STATUS=OK, TIME=9.0980s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1270], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1263,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(2063, 361, 1299, None, None, 'Aggiornato 688', datetime.date(2025, 9, 14))]
[DEBUG delete_comment] fetched comment: [{'id': 2063, 'user_id': 361, 'media_id': 1299, 'note_id': None, 'parent_comment_id': None, 'text': 'Aggiornato 688', 'created_at': datetime.date(2025, 9, 14)}]
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2059,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1228,)
[DEBUG][get_object] cls=Document, object_id=1270
[DEBUG] fetch_one success: RealDictRow({'id': 354})
[DEBUG] fetch_one success: RealDictRow({'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] Retrieved object=<Song id=1292, title=Media_3787>
[DEBUG][Media.fetch] Called cls=Document, media_id=1270
[DEBUG] fetch_one success: RealDictRow({'id': 1244, 'type': 'document', 'user_id': 353, 'title': 'Media_6364', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 500098), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.to_dict] <Song id=1292, title=Media_3787> -> {'media_id': 1292, 'type': 'song', 'title': 'Media_3787', 'user_id': 359, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:49.562642', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Data from DB={'id': 1244, 'type': 'document', 'user_id': 353, 'title': 'Media_6364', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 500098), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Data from DB={'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6364, type=document, year=2001, user_id=353, kwargs={'id': 1244, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1253, 'type': 'song', 'user_id': 354, 'title': 'Media_6657', 'year': 2000, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 33, 840966), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Extra attr: id=1244
[DEBUG][Media.__init__] Called with title=Media_6657, type=song, year=2000, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] db_get_following result: []
[DEBUG][get_song] STATUS=OK, TIME=8.4370s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_object] Retrieved object=<Song id=1266, title=Media_6457>
[DEBUG][Media.__init__] Finished -> <Song id=1253, title=Media_6657>
[DEBUG][dispatch_command] START - command=delete_song, args=[1292], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Finished -> <Document id=1244, title=Media_6364>
[DEBUG][Media.to_dict] <Song id=1266, title=Media_6457> -> {'media_id': 1266, 'type': 'song', 'title': 'Media_6457', 'user_id': 359, 'year': 2007, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:00.056902', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.from_dict] Built object=<Song id=1253, title=Media_6657>
[DEBUG][delete_song_services] song_id=1292
[DEBUG][Media.fetch] Built object=<Document id=1244, title=Media_6364>
[DEBUG][get_song] STATUS=OK, TIME=7.6232s, TAG=OK
[DEBUG][get_object] cls=Song, object_id=1292
[DEBUG][dispatch_command] START - command=delete_song, args=[1266], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Called cls=Song, media_id=1292
[DEBUG][delete_song_services] song_id=1266
[DEBUG][Media.fetch] Built object=<Song id=1253, title=Media_6657>
[DEBUG][get_object] cls=Song, object_id=1266
[DEBUG][Media.fetch] Called cls=Song, media_id=1266
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1235,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1242, title=Media_8574>
[DEBUG][delete_object] Deleting object <Video id=1242, title=Media_8574>
[DEBUG][Media.delete] Called on <Video id=1242, title=Media_8574>
[DEBUG][Media.delete] Deleted media_id=1239
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5674>
[DEBUG][delete_song] STATUS=OK, TIME=28.2654s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1281,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1225,)
[DEBUG] fetch_one success: RealDictRow({'id': 1236})
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (575,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1254,)
[DEBUG] db_get_following result: []
[DEBUG][delete_note] STATUS=OK, TIME=5.5635s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1282], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1282
[DEBUG][Media.fetch] Called cls=Document, media_id=1282
[DEBUG] fetch_one success: RealDictRow({'id': 358})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1274,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1232,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1240, title=Media_1916>
[DEBUG][delete_object] Deleting object <Video id=1240, title=Media_1916>
[DEBUG][Media.delete] Called on <Video id=1240, title=Media_1916>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1269,)
[DEBUG] fetch_one success: RealDictRow({'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7642, type=document, year=2006, user_id=360, kwargs={'id': 1271, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1271
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1271, title=Media_7642>
[DEBUG][Media.fetch] Built object=<Document id=1271, title=Media_7642>
[DEBUG][Media.delete] Deleted media_id=1263
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1279})
[DEBUG][delete_comment] STATUS=OK, TIME=13.7654s, TAG=OK
[DEBUG] db_get_following result: [(574, 361, 1277, 'regular', Decimal('4.07'), Decimal('5.13'), None, None, None, None, None, 'Nota aggiornata 226', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1234,)
[DEBUG][Media.fetch] Data from DB={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5839, type=song, year=2021, user_id=355, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1283, title=Media_5839>
[DEBUG][get_object] Retrieved object=<Video id=1278, title=Media_1435>
[DEBUG][delete_object] Deleting object <Video id=1278, title=Media_1435>
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1895>
[DEBUG][dispatch_command] START - command=create_note, args=[1295, 'regular', 2.2201370106927296, 3.8346984251226015, None, None, None, None, 'Nota 953'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.delete] Called on <Video id=1278, title=Media_1435>
[DEBUG][delete_document] STATUS=OK, TIME=30.6784s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1202,)
[DEBUG][Media.from_dict] Built object=<Song id=1283, title=Media_5839>
[DEBUG][Media.fetch] Built object=<Song id=1283, title=Media_5839>
[DEBUG] db_get_following result: [(583, 362, 1286, 'regular', Decimal('8.62'), Decimal('8.97'), None, None, None, None, None, 'Nota 973', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1206,)
[DEBUG][Media.from_dict] cls=Song, data={'id': 1287, 'type': 'song', 'user_id': 359, 'title': 'Media_5096', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 30, 424217), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5096, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][delete_note] STATUS=OK, TIME=9.6633s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][dispatch_command] START - command=get_song, args=[1273], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Finished -> <Song id=1287, title=Media_5096>
[DEBUG][get_song_services] song_id=1273
[DEBUG][Media.from_dict] Built object=<Song id=1287, title=Media_5096>
[DEBUG][get_object] cls=Song, object_id=1273
[DEBUG][Media.fetch] Called cls=Song, media_id=1273
[DEBUG][Media.fetch] Built object=<Song id=1287, title=Media_5096>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1212,)
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2062,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1267,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1296
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1207,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(581, 362, 1276, 'regular', Decimal('0.26'), Decimal('5.66'), None, None, None, None, None, 'Nota 690', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1203,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1231,)
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG delete_comment] fetched media: {'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1268,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1245,)
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1256,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(356, 'user343306@example.com', 'user343306', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_one success: RealDictRow({'id': 353})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(584, 360, 1288, 'regular', Decimal('1.06'), Decimal('3.94'), None, None, None, None, None, 'Nota 411', None)]
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1275,)
[DEBUG][create_note] STATUS=OK, TIME=10.6829s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[584, 'Nota aggiornata 195'], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=360, note_id=584
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1260,)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_comment] STATUS=OK, TIME=6.8396s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=create_note, args=[1298, 'regular', 5.831381616727058, 6.100861707606343, None, None, None, None, 'Nota 503'], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_one success: RealDictRow({'id': 1242})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1247,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1225,)
[DEBUG] fetch_one success: RealDictRow({'id': 1290})
[DEBUG][Media.delete] Deleted media_id=1245
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2064,)
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_1229>
[DEBUG] fetch_one success: RealDictRow({'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_song] STATUS=OK, TIME=37.5358s, TAG=OK
[DEBUG][Media.fetch] Data from DB={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5342, type=document, year=2004, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1296, title=Media_5342>
[DEBUG][Media.from_dict] Built object=<Document id=1296, title=Media_5342>
[DEBUG][Media.fetch] Built object=<Document id=1296, title=Media_5342>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1258,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1269,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1223,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1238})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1217,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1228,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1262,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(574, 361, 1277, 'regular', Decimal('4.07'), Decimal('5.13'), None, None, None, None, None, 'Nota aggiornata 226', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1292, 'type': 'song', 'user_id': 359, 'title': 'Media_3787', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 49, 562642), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3787, type=song, year=2015, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1292, title=Media_3787>
[DEBUG][Media.from_dict] Built object=<Song id=1292, title=Media_3787>
[DEBUG][Media.fetch] Built object=<Song id=1292, title=Media_3787>
[DEBUG][Media.delete] Deleted media_id=1247
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8829>
[DEBUG] fetch_one success: RealDictRow({'id': 1294})
[DEBUG][delete_document] STATUS=OK, TIME=30.1680s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1266, 'type': 'song', 'user_id': 359, 'title': 'Media_6457', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 0, 56902), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6457, type=song, year=2007, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1266, title=Media_6457>
[DEBUG][Media.from_dict] Built object=<Song id=1266, title=Media_6457>
[DEBUG][Media.fetch] Built object=<Song id=1266, title=Media_6457>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1281,)
[DEBUG] fetch_one success: RealDictRow({'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1264, 'type': 'song', 'user_id': 356, 'title': 'Media_9052', 'year': 2009, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 57, 977654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9052, type=song, year=2009, user_id=356, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1264, title=Media_9052>
[DEBUG][Media.from_dict] Built object=<Song id=1264, title=Media_9052>
[DEBUG][Media.fetch] Built object=<Song id=1264, title=Media_9052>
[DEBUG] fetch_one success: RealDictRow({'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5817, type=document, year=2022, user_id=354, kwargs={'id': 1282, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1282
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1282, title=Media_5817>
[DEBUG][Media.fetch] Built object=<Document id=1282, title=Media_5817>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1235,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1236,)
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG][Media.delete] Deleted media_id=1269
[DEBUG][delete_comment] STATUS=OK, TIME=5.5233s, TAG=OK
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_1272>
[DEBUG][dispatch_command] START - command=create_note, args=[1297, 'regular', 2.325725687660981, 0.2852360422020783, None, None, None, None, 'Nota 618'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song] STATUS=OK, TIME=21.9546s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6007, type=document, year=2016, user_id=362, kwargs={'id': 1270, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1270
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1270, title=Media_6007>
[DEBUG][Media.fetch] Built object=<Document id=1270, title=Media_6007>
[DEBUG] execute success: DELETE FROM comments WHERE id=%s (2063,)
[DEBUG] fetch_one success: RealDictRow({'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1242,)
[DEBUG][Media.fetch] Data from DB={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_one success: RealDictRow({'id': 1278})
[DEBUG][Media.from_dict] cls=Song, data={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_4773, type=song, year=2007, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Video id=1246, title=Media_9534>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(582, 356, 1285, 'regular', Decimal('0.06'), Decimal('3.50'), None, None, None, None, None, 'Nota aggiornata 367', None)]
[DEBUG][Media.__init__] Finished -> <Song id=1273, title=Media_4773>
[DEBUG][Media.from_dict] Built object=<Song id=1273, title=Media_4773>
[DEBUG][delete_object] Deleting object <Video id=1246, title=Media_9534>
[DEBUG][Media.delete] Called on <Video id=1246, title=Media_9534>
[DEBUG][Media.fetch] Built object=<Song id=1273, title=Media_4773>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1250, title=Media_5372>
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1207,)
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.to_dict] <Video id=1250, title=Media_5372> -> {'media_id': 1250, 'type': 'video', 'title': 'Media_5372', 'user_id': 360, 'year': 2016, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:32.755122', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=9.4981s, TAG=OK
[DEBUG][Media.fetch] Called cls=Media, media_id=1295
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(580, 360, 1280, 'regular', Decimal('6.30'), Decimal('7.43'), None, None, None, None, None, 'Nota aggiornata 170', None)]
[DEBUG][dispatch_command] START - command=delete_video, args=[1250], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1250
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Called cls=Video, media_id=1250
[DEBUG] db_get_following result: [(357, 'user443793@example.com', 'user443793', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1298
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1225,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1291, title=Media_1853>
[DEBUG][Media.to_dict] <Song id=1291, title=Media_1853> -> {'media_id': 1291, 'type': 'song', 'title': 'Media_1853', 'user_id': 360, 'year': 2017, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:42.119304', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=7.1599s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1291], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1291
[DEBUG][get_object] cls=Song, object_id=1291
[DEBUG][Media.fetch] Called cls=Song, media_id=1291
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1237, title=Media_7336>
[DEBUG][delete_object] Deleting object <Video id=1237, title=Media_7336>
[DEBUG][Media.delete] Called on <Video id=1237, title=Media_7336>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1254,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1226,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1233,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG delete_comment] delete_comment_db result: True
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1212,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1274,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1206,)
[DEBUG][delete_comment] STATUS=OK, TIME=6.4358s, TAG=OK
[DEBUG][dispatch_command] START - command=create_note, args=[1299, 'regular', 8.086917960818763, 3.9425456955782243, None, None, None, None, 'Nota 831'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1281,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1234,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1260,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1279,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1268,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1202,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1293, title=Media_6146>
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1250, 'type': 'video', 'user_id': 360, 'title': 'Media_5372', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 755122), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1250, 'type': 'video', 'user_id': 360, 'title': 'Media_5372', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 32, 755122), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1231,)
[DEBUG] db_get_following result: [(585, 354, 1290, 'regular', Decimal('3.62'), Decimal('4.42'), None, None, None, None, None, 'Nota 559', None)]
[DEBUG][Media.__init__] Called with title=Media_5372, type=video, year=2016, user_id=360, kwargs={'id': 1250, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1250
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1232,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1275,)
[DEBUG][create_note] STATUS=OK, TIME=14.3182s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[585, 'Nota aggiornata 249'], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1267,)
[DEBUG] fetch_one success: RealDictRow({'id': 1240})
[DEBUG][Media.delete] Deleted media_id=1254
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1256,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(580, 360, 1280, 'regular', Decimal('6.30'), Decimal('7.43'), None, None, None, None, None, 'Nota aggiornata 170', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1289})
[DEBUG][Media.delete] Deleted media_id=1226
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6653>
[DEBUG][delete_document] STATUS=OK, TIME=29.2559s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG update_note] START - user_id=354, note_id=585
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4949>
[DEBUG][Media.to_dict] <Video id=1293, title=Media_6146> -> {'media_id': 1293, 'type': 'video', 'title': 'Media_6146', 'user_id': 360, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:56.718126', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] db_get_following result: []
[DEBUG][delete_video] STATUS=OK, TIME=38.5027s, TAG=OK
[DEBUG][get_video] STATUS=OK, TIME=5.6838s, TAG=OK
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] fetch_one success: RealDictRow({'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 379', 581)
[DEBUG][Media.fetch] Data from DB={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1291, 'type': 'song', 'user_id': 360, 'title': 'Media_1853', 'year': 2017, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 42, 119304), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1244, title=Media_6364>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.__init__] Called with title=Media_1853, type=song, year=2017, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.to_dict] <Document id=1244, title=Media_6364> -> {'media_id': 1244, 'type': 'document', 'title': 'Media_6364', 'user_id': 353, 'year': 2001, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:30.500098', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][dispatch_command] START - command=delete_video, args=[1293], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.delete] Deleted media_id=1212
[DEBUG] db_get_following result: [(586, 358, 1294, 'regular', Decimal('4.44'), Decimal('8.28'), None, None, None, None, None, 'Nota 204', None)]
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][get_document] STATUS=OK, TIME=5.3478s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1260
[DEBUG][Media.__init__] Finished -> <Video id=1250, title=Media_5372>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1258,)
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Song id=1291, title=Media_1853>
[DEBUG][dispatch_command] START - command=delete_document, args=[1244], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1244
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 979', 583)
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] Built object=<Song id=1291, title=Media_1853>
[DEBUG][Media.fetch] Built object=<Song id=1291, title=Media_1853>
[DEBUG][Media.fetch] Called cls=Document, media_id=1244
[DEBUG][create_note] STATUS=OK, TIME=10.5575s, TAG=OK
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1601>
[DEBUG][get_object] cls=Video, object_id=1293
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.fetch] Called cls=Media, media_id=1299
[DEBUG][Media.delete] Deleted media_id=1268
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1203,)
[DEBUG][Media.fetch] Built object=<Video id=1250, title=Media_5372>
[DEBUG][delete_video] STATUS=OK, TIME=29.5648s, TAG=OK
[DEBUG][Media.fetch] Called cls=Video, media_id=1293
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1262,)
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4856>
[DEBUG] fetch_one success: RealDictRow({'id': 1246})
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (574,)
[DEBUG][dispatch_command] START - command=update_note, args=[586, 'Nota aggiornata 903'], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3540>
[DEBUG][delete_video] STATUS=OK, TIME=27.7872s, TAG=OK
[DEBUG update_note] START - user_id=358, note_id=586
[DEBUG][delete_song] STATUS=OK, TIME=23.2667s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1225,)
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1202
[DEBUG][Media.fetch] Data from DB={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] Retrieved object=<Document id=1271, title=Media_7642>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1236,)
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_7744>
[DEBUG][Media.from_dict] cls=Media, data={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_song] STATUS=OK, TIME=30.1201s, TAG=OK
[DEBUG][Media.__init__] Called with title=Media_8153, type=song, year=2020, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.to_dict] <Document id=1271, title=Media_7642> -> {'media_id': 1271, 'type': 'document', 'title': 'Media_7642', 'user_id': 360, 'year': 2006, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:01.926052', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][get_document] STATUS=OK, TIME=5.1279s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][dispatch_command] START - command=delete_document, args=[1271], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.__init__] Finished -> <Song id=1295, title=Media_8153>
[DEBUG][get_object] cls=Document, object_id=1271
[DEBUG][Media.from_dict] Built object=<Song id=1295, title=Media_8153>
[DEBUG][Media.fetch] Built object=<Song id=1295, title=Media_8153>
[DEBUG][Media.fetch] Called cls=Document, media_id=1271
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(582, 356, 1285, 'regular', Decimal('0.06'), Decimal('3.50'), None, None, None, None, None, 'Nota aggiornata 367', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.delete] Deleted media_id=1231
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1272})
[DEBUG] fetch_one success: RealDictRow({'id': 1237})
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1233,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1242,)
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1305>
[DEBUG][delete_video] STATUS=OK, TIME=24.7214s, TAG=OK
[DEBUG][Media.fetch] Called cls=Media, media_id=1297
[DEBUG][update_note] STATUS=OK, TIME=11.7375s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(584, 360, 1288, 'regular', Decimal('1.06'), Decimal('3.94'), None, None, None, None, None, 'Nota 411', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=delete_note, args=[581], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1235,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG delete_note] START - user_id=362, note_id=581
[DEBUG][update_note] STATUS=OK, TIME=11.8823s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[583], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=362, note_id=583
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1262
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1728>
[DEBUG][Media.delete] Deleted media_id=1203
[DEBUG] fetch_one success: RealDictRow({'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_note] STATUS=OK, TIME=9.5944s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1277], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] cls=Document, object_id=1277
[DEBUG][Media.fetch] Called cls=Document, media_id=1277
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_9235>
[DEBUG][delete_document] STATUS=OK, TIME=28.6276s, TAG=OK
[DEBUG][delete_video] STATUS=OK, TIME=25.9949s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1238,)
[DEBUG][Media.__init__] Called with title=Media_3487, type=video, year=2003, user_id=357, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1298, title=Media_3487>
[DEBUG][Media.from_dict] Built object=<Video id=1298, title=Media_3487>
[DEBUG][Media.fetch] Built object=<Video id=1298, title=Media_3487>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1284, title=Media_9951>
[DEBUG][delete_object] Deleting object <Video id=1284, title=Media_9951>
[DEBUG][Media.delete] Called on <Video id=1284, title=Media_9951>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1278,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1281,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1258,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1279,)
[DEBUG] fetch_one success: RealDictRow({'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1293, 'type': 'video', 'user_id': 360, 'title': 'Media_6146', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 56, 718126), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6146, type=video, year=2015, user_id=360, kwargs={'id': 1293, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1293
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1293, title=Media_6146>
[DEBUG][Media.fetch] Built object=<Video id=1293, title=Media_6146>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1234,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1217,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1223,)
[DEBUG] fetch_one success: RealDictRow({'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1271, 'type': 'document', 'user_id': 360, 'title': 'Media_7642', 'year': 2006, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 926052), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_7642, type=document, year=2006, user_id=360, kwargs={'id': 1271, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1271
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1271, title=Media_7642>
[DEBUG][Media.fetch] Built object=<Document id=1271, title=Media_7642>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1207,)
[DEBUG] fetch_one success: RealDictRow({'id': 1244, 'type': 'document', 'user_id': 353, 'title': 'Media_6364', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 500098), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1244, 'type': 'document', 'user_id': 353, 'title': 'Media_6364', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 30, 500098), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6364, type=document, year=2001, user_id=353, kwargs={'id': 1244, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1244
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1228,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Data from DB={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Media, data={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5271, type=song, year=2024, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1297, title=Media_5271>
[DEBUG][Media.from_dict] Built object=<Song id=1297, title=Media_5271>
[DEBUG][Media.fetch] Built object=<Song id=1297, title=Media_5271>
ERROR:services.interventions_services:Invalid time range: start_time=2.325725687660981, end_time=0.2852360422020783
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][create_note] STATUS=OK, TIME=2.7112s, TAG=OK
[DEBUG][Media.__init__] Finished -> <Document id=1244, title=Media_6364>
[DEBUG][dispatch_command] START - command=get_song, args=[1297], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Built object=<Document id=1244, title=Media_6364>
[DEBUG][get_song_services] song_id=1297
[DEBUG][get_object] cls=Song, object_id=1297
[DEBUG][Media.fetch] Called cls=Song, media_id=1297
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1264, title=Media_9052>
[DEBUG][delete_object] Deleting object <Song id=1264, title=Media_9052>
[DEBUG][Media.delete] Called on <Song id=1264, title=Media_9052>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1274,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1270, title=Media_6007>
[DEBUG][Media.to_dict] <Document id=1270, title=Media_6007> -> {'media_id': 1270, 'type': 'document', 'title': 'Media_6007', 'user_id': 362, 'year': 2016, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:01.872901', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=5.1992s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1270], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1270
[DEBUG][Media.fetch] Called cls=Document, media_id=1270
[DEBUG][Media.delete] Deleted media_id=1258
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1339>
[DEBUG][delete_document] STATUS=OK, TIME=25.6891s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (580,)
[DEBUG][Media.delete] Deleted media_id=1207
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1233,)
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6052>
[DEBUG][delete_song] STATUS=OK, TIME=30.7172s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1256,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (582,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(587, 353, 1289, 'regular', Decimal('0.01'), Decimal('6.50'), None, None, None, None, None, 'Nota 672', None)]
[DEBUG][create_note] STATUS=OK, TIME=13.7847s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[587, 'Nota aggiornata 146'], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=353, note_id=587
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1282, title=Media_5817>
[DEBUG][Media.to_dict] <Document id=1282, title=Media_5817> -> {'media_id': 1282, 'type': 'document', 'title': 'Media_5817', 'user_id': 354, 'year': 2022, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:25.116450', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=5.2410s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1282], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1282
[DEBUG][Media.fetch] Called cls=Document, media_id=1282
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1275,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 361})
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1242,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1236,)
[DEBUG] fetch_one success: RealDictRow({'id': 1284})
[DEBUG][Media.delete] Deleted media_id=1274
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6866>
[DEBUG][delete_song] STATUS=OK, TIME=27.5085s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1246,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1250, title=Media_5372>
[DEBUG][delete_object] Deleting object <Video id=1250, title=Media_5372>
[DEBUG][Media.delete] Called on <Video id=1250, title=Media_5372>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1240,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1272,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1267,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1237,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1235,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(362, 'user946384@example.com', 'user946384', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1206,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1223,)
[DEBUG][delete_note] STATUS=OK, TIME=6.8660s, TAG=OK
[DEBUG][dispatch_command] START - command=get_song, args=[1280], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1280
[DEBUG][get_object] cls=Song, object_id=1280
[DEBUG][Media.fetch] Called cls=Song, media_id=1280
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(585, 354, 1290, 'regular', Decimal('3.62'), Decimal('4.42'), None, None, None, None, None, 'Nota 559', None)]
[DEBUG][get_object] Retrieved object=<Song id=1287, title=Media_5096>
[DEBUG][delete_object] Deleting object <Song id=1287, title=Media_5096>
[DEBUG][Media.delete] Called on <Song id=1287, title=Media_5096>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 357})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1234,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1225,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(584, 360, 1288, 'regular', Decimal('1.06'), Decimal('3.94'), None, None, None, None, None, 'Nota 411', None)]
[DEBUG][get_object] Retrieved object=<Song id=1273, title=Media_4773>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1238,)
[DEBUG][Media.to_dict] <Song id=1273, title=Media_4773> -> {'media_id': 1273, 'type': 'song', 'title': 'Media_4773', 'user_id': 358, 'year': 2007, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:04.858318', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=5.1770s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1273], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1273
[DEBUG][get_object] cls=Song, object_id=1273
[DEBUG][Media.fetch] Called cls=Song, media_id=1273
[DEBUG][delete_note] STATUS=OK, TIME=6.3986s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1285], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1285
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1217,)
[DEBUG][Media.fetch] Called cls=Video, media_id=1285
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1281,)
[DEBUG][get_object] Retrieved object=<Song id=1283, title=Media_5839>
[DEBUG] fetch_one success: RealDictRow({'id': 359})
[DEBUG][Media.to_dict] <Song id=1283, title=Media_5839> -> {'media_id': 1283, 'type': 'song', 'title': 'Media_5839', 'user_id': 355, 'year': 2021, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:25.374765', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=6.4901s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1283], user_obj={'id': 355, 'username': 'user242821', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1278,)
[DEBUG][delete_song_services] song_id=1283
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][get_object] cls=Song, object_id=1283
[DEBUG][Media.fetch] Called cls=Song, media_id=1283
[DEBUG][Media.fetch] Data from DB={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5271, type=song, year=2024, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1297, title=Media_5271>
[DEBUG][Media.from_dict] Built object=<Song id=1297, title=Media_5271>
[DEBUG][Media.fetch] Built object=<Song id=1297, title=Media_5271>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1253, title=Media_6657>
[DEBUG][delete_object] Deleting object <Song id=1253, title=Media_6657>
[DEBUG][Media.delete] Called on <Song id=1253, title=Media_6657>
[DEBUG] fetch_one success: RealDictRow({'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1282, 'type': 'document', 'user_id': 354, 'title': 'Media_5817', 'year': 2022, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 116450), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5817, type=document, year=2022, user_id=354, kwargs={'id': 1282, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1282
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1282, title=Media_5817>
[DEBUG][Media.fetch] Built object=<Document id=1282, title=Media_5817>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(586, 358, 1294, 'regular', Decimal('4.44'), Decimal('8.28'), None, None, None, None, None, 'Nota 204', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8066, type=document, year=2015, user_id=361, kwargs={'id': 1277, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1277
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1277, title=Media_8066>
[DEBUG][Media.fetch] Built object=<Document id=1277, title=Media_8066>
[DEBUG] fetch_one success: RealDictRow({'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1270, 'type': 'document', 'user_id': 362, 'title': 'Media_6007', 'year': 2016, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 1, 872901), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6007, type=document, year=2016, user_id=362, kwargs={'id': 1270, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1270
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1270, title=Media_6007>
[DEBUG][Media.fetch] Built object=<Document id=1270, title=Media_6007>
[DEBUG][Media.delete] Deleted media_id=1267
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1505>
[DEBUG][delete_video] STATUS=OK, TIME=26.4117s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(581, 362, 1276, 'regular', Decimal('0.26'), Decimal('5.66'), None, None, None, None, None, 'Nota aggiornata 379', None)]
[DEBUG][Media.delete] Deleted media_id=1223
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4797>
[DEBUG][delete_video] STATUS=OK, TIME=27.1684s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1232,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(583, 362, 1286, 'regular', Decimal('8.62'), Decimal('8.97'), None, None, None, None, None, 'Nota aggiornata 979', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1250})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1279,)
[DEBUG] fetch_one success: RealDictRow({'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1273, 'type': 'song', 'user_id': 358, 'title': 'Media_4773', 'year': 2007, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 4, 858318), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4773, type=song, year=2007, user_id=358, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1273, title=Media_4773>
[DEBUG][Media.from_dict] Built object=<Song id=1273, title=Media_4773>
[DEBUG][Media.fetch] Built object=<Song id=1273, title=Media_4773>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1271, title=Media_7642>
[DEBUG][delete_object] Deleting object <Document id=1271, title=Media_7642>
[DEBUG][Media.delete] Called on <Document id=1271, title=Media_7642>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1228,)
[DEBUG][Media.delete] Deleted media_id=1217
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_6854>
[DEBUG][delete_video] STATUS=OK, TIME=25.9915s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1281
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8330>
[DEBUG] fetch_all returned 1 rows
[DEBUG][delete_document] STATUS=OK, TIME=23.0113s, TAG=OK
[DEBUG] db_get_following result: [(586, 358, 1294, 'regular', Decimal('4.44'), Decimal('8.28'), None, None, None, None, None, 'Nota 204', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1265, title=Media_2577>
[DEBUG][Media.to_dict] <Song id=1265, title=Media_2577> -> {'media_id': 1265, 'type': 'song', 'title': 'Media_2577', 'user_id': 359, 'year': 2008, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:40:59.643951', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=8.2461s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1265], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: []
[DEBUG][delete_song_services] song_id=1265
[DEBUG][Media.fetch] Data from DB={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][get_object] cls=Song, object_id=1265
[DEBUG][Media.from_dict] cls=Media, data={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9639, type=document, year=2013, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.fetch] Called cls=Song, media_id=1265
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1299, title=Media_9639>
[DEBUG][Media.from_dict] Built object=<Document id=1299, title=Media_9639>
[DEBUG][Media.fetch] Built object=<Document id=1299, title=Media_9639>
ERROR:services.interventions_services:Invalid time range: start_time=8.086917960818763, end_time=3.9425456955782243
[DEBUG][create_note] STATUS=OK, TIME=3.8075s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1299], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1299
[DEBUG][Media.fetch] Called cls=Document, media_id=1299
[DEBUG] fetch_one success: RealDictRow({'id': 1287})
[DEBUG] fetch_one success: RealDictRow({'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4067, type=song, year=2024, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1280, title=Media_4067>
[DEBUG][Media.from_dict] Built object=<Song id=1280, title=Media_4067>
[DEBUG][Media.fetch] Built object=<Song id=1280, title=Media_4067>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1284,)
[DEBUG] fetch_one success: RealDictRow({'id': 1264})
[DEBUG] fetch_one success: RealDictRow({'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1283, 'type': 'song', 'user_id': 355, 'title': 'Media_5839', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 25, 374765), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5839, type=song, year=2021, user_id=355, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1283, title=Media_5839>
[DEBUG][Media.from_dict] Built object=<Song id=1283, title=Media_5839>
[DEBUG][Media.fetch] Built object=<Song id=1283, title=Media_5839>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1233,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1256,)
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(585, 354, 1290, 'regular', Decimal('3.62'), Decimal('4.42'), None, None, None, None, None, 'Nota 559', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1253})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1242,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1206,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(581, 362, 1276, 'regular', Decimal('0.26'), Decimal('5.66'), None, None, None, None, None, 'Nota aggiornata 379', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1271})
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1235,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1240,)
[DEBUG] fetch_one success: RealDictRow({'id': 1295})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1287,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1236,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1292, title=Media_3787>
[DEBUG][delete_object] Deleting object <Song id=1292, title=Media_3787>
[DEBUG][Media.delete] Called on <Song id=1292, title=Media_3787>
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1278,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1266, title=Media_6457>
[DEBUG][delete_object] Deleting object <Song id=1266, title=Media_6457>
[DEBUG][Media.delete] Called on <Song id=1266, title=Media_6457>
[DEBUG] fetch_one success: RealDictRow({'id': 1298})
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1237,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1244, title=Media_6364>
[DEBUG][delete_object] Deleting object <Document id=1244, title=Media_6364>
[DEBUG][Media.delete] Called on <Document id=1244, title=Media_6364>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1279,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1246,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 195', 584)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1225,)
[DEBUG][Media.fetch] Data from DB={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_9639, type=document, year=2013, user_id=361, kwargs={'id': 1299, 'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: id=1299
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1299, title=Media_9639>
[DEBUG][Media.fetch] Built object=<Document id=1299, title=Media_9639>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1275,)
[DEBUG] fetch_one success: RealDictRow({'id': 1296})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1264,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1272,)
[DEBUG] fetch_one success: RealDictRow({'id': 1292})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1277, title=Media_8066>
[DEBUG][Media.to_dict] <Document id=1277, title=Media_8066> -> {'media_id': 1277, 'type': 'document', 'title': 'Media_8066', 'user_id': 361, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:11.578852', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1253,)
[DEBUG][get_document] STATUS=OK, TIME=3.6139s, TAG=OK
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 903', 586)
[DEBUG][dispatch_command] START - command=delete_document, args=[1277], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1277
[DEBUG][Media.fetch] Called cls=Document, media_id=1277
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 249', 585)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1228,)
[DEBUG][Media.delete] Deleted media_id=1235
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5882>
[DEBUG] db_get_following result: []
[DEBUG][delete_document] STATUS=OK, TIME=20.1191s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1238,)
[DEBUG][get_object] Retrieved object=<Song id=1291, title=Media_1853>
[DEBUG][delete_object] Deleting object <Song id=1291, title=Media_1853>
[DEBUG][Media.delete] Called on <Song id=1291, title=Media_1853>
[DEBUG] fetch_one success: RealDictRow({'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.from_dict] cls=Song, data={'id': 1265, 'type': 'song', 'user_id': 359, 'title': 'Media_2577', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 40, 59, 643951), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_2577, type=song, year=2008, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_object] Retrieved object=<Document id=1282, title=Media_5817>
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleting object <Document id=1282, title=Media_5817>
[DEBUG][Media.delete] Called on <Document id=1282, title=Media_5817>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1265, title=Media_2577>
[DEBUG][Media.from_dict] Built object=<Song id=1265, title=Media_2577>
[DEBUG] fetch_all returned 1 rows
[DEBUG][Media.fetch] Built object=<Song id=1265, title=Media_2577>
[DEBUG] db_get_following result: [(587, 353, 1289, 'regular', Decimal('0.01'), Decimal('6.50'), None, None, None, None, None, 'Nota 672', None)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1233,)
[DEBUG][update_note] STATUS=OK, TIME=6.9769s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[584], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=360, note_id=584
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1225
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.delete] Deleted media_id=1275
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4617>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_2695>
[DEBUG][delete_song] STATUS=OK, TIME=21.4121s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1297, title=Media_5271>
[DEBUG][delete_video] STATUS=OK, TIME=28.4914s, TAG=OK
[DEBUG][Media.to_dict] <Song id=1297, title=Media_5271> -> {'media_id': 1297, 'type': 'song', 'title': 'Media_5271', 'user_id': 361, 'year': 2024, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:19.113850', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(583, 362, 1286, 'regular', Decimal('8.62'), Decimal('8.97'), None, None, None, None, None, 'Nota aggiornata 979', None)]
[DEBUG][get_song] STATUS=OK, TIME=3.3152s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1297], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1297
[DEBUG][get_object] cls=Song, object_id=1297
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (581,)
[DEBUG][Media.fetch] Called cls=Song, media_id=1297
[DEBUG][update_note] STATUS=OK, TIME=4.7317s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[586], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=358, note_id=586
[DEBUG][Media.delete] Deleted media_id=1228
[DEBUG][update_note] STATUS=OK, TIME=5.0124s, TAG=OK
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5208>
[DEBUG][dispatch_command] START - command=delete_note, args=[585], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=354, note_id=585
[DEBUG][delete_document] STATUS=OK, TIME=23.1980s, TAG=OK
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(588, 359, 1295, 'regular', Decimal('2.22'), Decimal('3.83'), None, None, None, None, None, 'Nota 953', None)]
[DEBUG][create_note] STATUS=OK, TIME=7.8565s, TAG=OK
[DEBUG][dispatch_command] START - command=update_note, args=[588, 'Nota aggiornata 607'], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG update_note] START - user_id=359, note_id=588
[DEBUG] fetch_one success: RealDictRow({'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3931, type=video, year=2008, user_id=356, kwargs={'id': 1285, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1285
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1285, title=Media_3931>
[DEBUG][Media.fetch] Built object=<Video id=1285, title=Media_3931>
[DEBUG] fetch_one success: RealDictRow({'id': 1266})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1234,)
[DEBUG] fetch_one success: RealDictRow({'id': 1244})
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1236,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1271,)
[DEBUG] fetch_one success: RealDictRow({'id': 1291})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1292,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1256,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1284,)
[DEBUG] fetch_one success: RealDictRow({'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1277, 'type': 'document', 'user_id': 361, 'title': 'Media_8066', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 11, 578852), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8066, type=document, year=2015, user_id=361, kwargs={'id': 1277, 'recording_date': None, 'performer_id': None}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: id=1277
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (583,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: [(590, 361, 1296, 'regular', Decimal('8.06'), Decimal('9.32'), None, None, None, None, None, 'Nota 158', None)]
[DEBUG] db_get_following result: []
[DEBUG][create_note] STATUS=OK, TIME=9.7751s, TAG=OK
[DEBUG][get_object] Retrieved object=<Document id=1270, title=Media_6007>
[DEBUG][dispatch_command] START - command=update_note, args=[590, 'Nota aggiornata 661'], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_object] Deleting object <Document id=1270, title=Media_6007>
[DEBUG update_note] START - user_id=361, note_id=590
[DEBUG][Media.delete] Called on <Document id=1270, title=Media_6007>
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][delete_note] STATUS=OK, TIME=4.8367s, TAG=OK
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1277, title=Media_8066>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1240,)
[DEBUG][Media.fetch] Built object=<Document id=1277, title=Media_8066>
[DEBUG][dispatch_command] START - command=get_video, args=[1276], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1242,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1279,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1246,)
[DEBUG][get_object] cls=Video, object_id=1276
[DEBUG][Media.fetch] Called cls=Video, media_id=1276
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1250,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1237,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(589, 357, 1298, 'regular', Decimal('5.83'), Decimal('6.10'), None, None, None, None, None, 'Nota 503', None)]
[DEBUG][create_note] STATUS=OK, TIME=7.6536s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=update_note, args=[589, 'Nota aggiornata 514'], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1278,)
[DEBUG][get_object] Retrieved object=<Video id=1293, title=Media_6146>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG update_note] START - user_id=357, note_id=589
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleting object <Video id=1293, title=Media_6146>
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Called on <Video id=1293, title=Media_6146>
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1244,)
[DEBUG] db_get_following result: [(587, 353, 1289, 'regular', Decimal('0.01'), Decimal('6.50'), None, None, None, None, None, 'Nota 672', None)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1232,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1234
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_8514>
[DEBUG][delete_video] STATUS=OK, TIME=24.3536s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1253,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1287,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1273, title=Media_4773>
[DEBUG][delete_object] Deleting object <Song id=1273, title=Media_4773>
[DEBUG][Media.delete] Called on <Song id=1273, title=Media_4773>
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: [(360, 'user745397@example.com', 'user745397', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.delete] Deleted media_id=1256
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_9797>
[DEBUG][delete_document] STATUS=OK, TIME=18.1989s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1299, title=Media_9639>
[DEBUG][Media.to_dict] <Document id=1299, title=Media_9639> -> {'media_id': 1299, 'type': 'document', 'title': 'Media_9639', 'user_id': 361, 'year': 2013, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:36.677066', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=2.5690s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1206,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][dispatch_command] START - command=delete_document, args=[1299], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1299
[DEBUG][Media.fetch] Called cls=Document, media_id=1299
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1283, title=Media_5839>
[DEBUG][delete_note] STATUS=OK, TIME=5.2058s, TAG=OK
[DEBUG][delete_object] Deleting object <Song id=1283, title=Media_5839>
[DEBUG][dispatch_command] START - command=get_video, args=[1286], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.delete] Called on <Song id=1283, title=Media_5839>
[DEBUG][get_object] cls=Video, object_id=1286
[DEBUG][Media.fetch] Called cls=Video, media_id=1286
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1238,)
[DEBUG] fetch_one success: RealDictRow({'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1297, 'type': 'song', 'user_id': 361, 'title': 'Media_5271', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 19, 113850), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5271, type=song, year=2024, user_id=361, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1264,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1291,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1272,)
[DEBUG][Media.__init__] Finished -> <Song id=1297, title=Media_5271>
[DEBUG][Media.from_dict] Built object=<Song id=1297, title=Media_5271>
[DEBUG][Media.fetch] Built object=<Song id=1297, title=Media_5271>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(358, 'user544294@example.com', 'user544294', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1270})
[DEBUG] fetch_one success: RealDictRow({'id': 1273})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1280, title=Media_4067>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1233,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1236,)
[DEBUG][Media.to_dict] <Song id=1280, title=Media_4067> -> {'media_id': 1280, 'type': 'song', 'title': 'Media_4067', 'user_id': 360, 'year': 2024, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:21.827816', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_one success: RealDictRow({'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1266,)
[DEBUG][get_song] STATUS=OK, TIME=3.8617s, TAG=OK
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 146', 587)
[DEBUG][dispatch_command] START - command=delete_song, args=[1280], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][Media.fetch] Data from DB={'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][delete_song_services] song_id=1280
[DEBUG][Media.__init__] Called with title=Media_6439, type=video, year=2021, user_id=362, kwargs={'id': 1276, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1276
[DEBUG][get_object] cls=Song, object_id=1280
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.fetch] Called cls=Song, media_id=1280
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1276, title=Media_6439>
[DEBUG][Media.fetch] Built object=<Video id=1276, title=Media_6439>
[DEBUG] fetch_one success: RealDictRow({'id': 1282})
[DEBUG] fetch_one success: RealDictRow({'id': 1293})
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(354, 'user142450@example.com', 'user142450', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.delete] Deleted media_id=1206
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Data from DB={'id': 1299, 'type': 'document', 'user_id': 361, 'title': 'Media_9639', 'year': 2013, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 36, 677066), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_9639, type=document, year=2013, user_id=361, kwargs={'id': 1299, 'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: [(357, 'user443793@example.com', 'user443793', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_2820>
[DEBUG][get_object] Retrieved object=<Document id=1277, title=Media_8066>
[DEBUG][delete_object] Deleting object <Document id=1277, title=Media_8066>
[DEBUG][Media.delete] Called on <Document id=1277, title=Media_8066>
[DEBUG][delete_video] STATUS=OK, TIME=25.1394s, TAG=OK
[DEBUG][Media.__init__] Extra attr: id=1299
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1299, title=Media_9639>
[DEBUG][Media.fetch] Built object=<Document id=1299, title=Media_9639>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1292,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(588, 359, 1295, 'regular', Decimal('2.22'), Decimal('3.83'), None, None, None, None, None, 'Nota 953', None)]
[DEBUG][Media.delete] Deleted media_id=1236
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_4531>
[DEBUG][delete_document] STATUS=OK, TIME=20.4068s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1233
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6787>
[DEBUG][delete_document] STATUS=OK, TIME=19.6322s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1240,)
[DEBUG][update_note] STATUS=OK, TIME=4.7182s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[587], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1284,)
[DEBUG delete_note] START - user_id=353, note_id=587
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1273,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(585, 354, 1290, 'regular', Decimal('3.62'), Decimal('4.42'), None, None, None, None, None, 'Nota aggiornata 249', None)]
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1270,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1242,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(584, 360, 1288, 'regular', Decimal('1.06'), Decimal('3.94'), None, None, None, None, None, 'Nota aggiornata 195', None)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1271,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1244,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1264,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1253,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1250,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1287,)
[DEBUG] fetch_one success: RealDictRow({'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4810, type=video, year=2001, user_id=362, kwargs={'id': 1286, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1286
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1286, title=Media_4810>
[DEBUG][Media.fetch] Built object=<Video id=1286, title=Media_4810>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1246,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(353, 'user041987@example.com', 'user041987', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1266,)
[DEBUG] fetch_one success: RealDictRow({'id': 1277})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1279,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1237,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(590, 361, 1296, 'regular', Decimal('8.06'), Decimal('9.32'), None, None, None, None, None, 'Nota 158', None)]
[DEBUG] fetch_one success: RealDictRow({'id': 1283})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1232,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1291,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1293,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1282,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG][get_object] Retrieved object=<Video id=1285, title=Media_3931>
[DEBUG] db_get_following result: [(589, 357, 1298, 'regular', Decimal('5.83'), Decimal('6.10'), None, None, None, None, None, 'Nota 503', None)]
[DEBUG][Media.to_dict] <Video id=1285, title=Media_3931> -> {'media_id': 1285, 'type': 'video', 'title': 'Media_3931', 'user_id': 356, 'year': 2008, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:26.332135', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][Media.delete] Deleted media_id=1242
[DEBUG][get_video] STATUS=OK, TIME=4.8576s, TAG=OK
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_8574>
[DEBUG][dispatch_command] START - command=delete_video, args=[1285], user_obj={'id': 356, 'username': 'user343306', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_video] STATUS=OK, TIME=20.7965s, TAG=OK
[DEBUG][get_object] cls=Video, object_id=1285
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(586, 358, 1294, 'regular', Decimal('4.44'), Decimal('8.28'), None, None, None, None, None, 'Nota aggiornata 903', None)]
[DEBUG][Media.fetch] Called cls=Video, media_id=1285
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_one success: RealDictRow({'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] db_get_following result: [(588, 359, 1295, 'regular', Decimal('2.22'), Decimal('3.83'), None, None, None, None, None, 'Nota 953', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(585, 354, 1290, 'regular', Decimal('3.62'), Decimal('4.42'), None, None, None, None, None, 'Nota aggiornata 249', None)]
[DEBUG][Media.fetch] Data from DB={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1280, 'type': 'song', 'user_id': 360, 'title': 'Media_4067', 'year': 2024, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 21, 827816), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_4067, type=song, year=2024, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1280, title=Media_4067>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1238,)
[DEBUG][Media.from_dict] Built object=<Song id=1280, title=Media_4067>
[DEBUG][Media.fetch] Built object=<Song id=1280, title=Media_4067>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1278,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(584, 360, 1288, 'regular', Decimal('1.06'), Decimal('3.94'), None, None, None, None, None, 'Nota aggiornata 195', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1265, title=Media_2577>
[DEBUG][delete_object] Deleting object <Song id=1265, title=Media_2577>
[DEBUG][Media.delete] Called on <Song id=1265, title=Media_2577>
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1272,)
[DEBUG][Media.delete] Deleted media_id=1279
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1770>
[DEBUG] db_get_following result: []
[DEBUG][delete_document] STATUS=OK, TIME=20.5205s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1292,)
[DEBUG][Media.delete] Deleted media_id=1232
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1193>
[DEBUG][delete_document] STATUS=OK, TIME=24.5732s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 607', 588)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(587, 353, 1289, 'regular', Decimal('0.01'), Decimal('6.50'), None, None, None, None, None, 'Nota aggiornata 146', None)]
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1283,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1240,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (585,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1250,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1277,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(590, 361, 1296, 'regular', Decimal('8.06'), Decimal('9.32'), None, None, None, None, None, 'Nota 158', None)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1253,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1271,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1244,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (584,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1293,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(586, 358, 1294, 'regular', Decimal('4.44'), Decimal('8.28'), None, None, None, None, None, 'Nota aggiornata 903', None)]
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1266,)
[DEBUG] fetch_one success: RealDictRow({'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1285, 'type': 'video', 'user_id': 356, 'title': 'Media_3931', 'year': 2008, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 26, 332135), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3931, type=video, year=2008, user_id=356, kwargs={'id': 1285, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1285
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1285, title=Media_3931>
[DEBUG][Media.fetch] Built object=<Video id=1285, title=Media_3931>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1238,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(589, 357, 1298, 'regular', Decimal('5.83'), Decimal('6.10'), None, None, None, None, None, 'Nota 503', None)]
[DEBUG] db_get_following result: [(587, 353, 1289, 'regular', Decimal('0.01'), Decimal('6.50'), None, None, None, None, None, 'Nota aggiornata 146', None)]
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 661', 590)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1299, title=Media_9639>
[DEBUG][delete_object] Deleting object <Document id=1299, title=Media_9639>
[DEBUG][Media.delete] Called on <Document id=1299, title=Media_9639>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1246,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1278,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1282,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1270,)
[DEBUG][update_note] STATUS=OK, TIME=3.4572s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[588], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1264,)
[DEBUG delete_note] START - user_id=359, note_id=588
[DEBUG] fetch_one success: RealDictRow({'id': 1265})
[DEBUG][delete_note] STATUS=OK, TIME=3.5269s, TAG=OK
[DEBUG][dispatch_command] START - command=get_song, args=[1290], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1287,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1291,)
[DEBUG][get_song_services] song_id=1290
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1276, title=Media_6439>
[DEBUG][Media.to_dict] <Video id=1276, title=Media_6439> -> {'media_id': 1276, 'type': 'video', 'title': 'Media_6439', 'user_id': 362, 'year': 2021, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:08.855315', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=3.1627s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1276], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1276
[DEBUG][Media.fetch] Called cls=Video, media_id=1276
[DEBUG][get_object] cls=Song, object_id=1290
[DEBUG][Media.fetch] Called cls=Song, media_id=1290
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1284,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1273,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1272,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1297, title=Media_5271>
[DEBUG][delete_object] Deleting object <Song id=1297, title=Media_5271>
[DEBUG][Media.delete] Called on <Song id=1297, title=Media_5271>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1237,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (586,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (587,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1292,)
[DEBUG][delete_note] STATUS=OK, TIME=4.0903s, TAG=OK
[DEBUG][dispatch_command] START - command=get_song, args=[1288], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_song_services] song_id=1288
[DEBUG] fetch_one success: RealDictRow({'id': 1299})
[DEBUG][get_object] cls=Song, object_id=1288
[DEBUG] execute success: UPDATE notes SET content=%s WHERE id=%s ('Nota aggiornata 514', 589)
[DEBUG][Media.fetch] Called cls=Song, media_id=1288
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1283,)
[DEBUG][Media.delete] Deleted media_id=1238
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1978>
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1286, title=Media_4810>
[DEBUG][delete_document] STATUS=OK, TIME=16.1279s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1278
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1435>
[DEBUG][update_note] STATUS=OK, TIME=3.5652s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[590], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=361, note_id=590
[DEBUG][delete_video] STATUS=OK, TIME=19.9775s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1271,)
[DEBUG][Media.to_dict] <Video id=1286, title=Media_4810> -> {'media_id': 1286, 'type': 'video', 'title': 'Media_4810', 'user_id': 362, 'year': 2001, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:29.389185', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=3.0719s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][dispatch_command] START - command=delete_video, args=[1286], user_obj={'id': 362, 'username': 'user946384', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1286
[DEBUG][Media.fetch] Data from DB={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.fetch] Called cls=Video, media_id=1286
[DEBUG][Media.__init__] Called with title=Media_5097, type=song, year=2015, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1277,)
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1253,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Finished -> <Song id=1290, title=Media_5097>
[DEBUG] db_get_following result: []
[DEBUG][Media.from_dict] Built object=<Song id=1290, title=Media_5097>
[DEBUG][Media.fetch] Built object=<Song id=1290, title=Media_5097>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1265,)
[DEBUG] fetch_one success: RealDictRow({'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1276, 'type': 'video', 'user_id': 362, 'title': 'Media_6439', 'year': 2021, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 8, 855315), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_6439, type=video, year=2021, user_id=362, kwargs={'id': 1276, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1276
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1276, title=Media_6439>
[DEBUG][Media.fetch] Built object=<Video id=1276, title=Media_6439>
[DEBUG][delete_note] STATUS=OK, TIME=4.2701s, TAG=OK
[DEBUG][dispatch_command] START - command=get_document, args=[1294], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_object] cls=Document, object_id=1294
[DEBUG] db_get_following result: []
[DEBUG][Media.fetch] Called cls=Document, media_id=1294
[DEBUG][get_object] Retrieved object=<Song id=1280, title=Media_4067>
[DEBUG][delete_object] Deleting object <Song id=1280, title=Media_4067>
[DEBUG][Media.delete] Called on <Song id=1280, title=Media_4067>
[DEBUG][delete_note] STATUS=OK, TIME=2.4851s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1289], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1289
[DEBUG][Media.fetch] Called cls=Video, media_id=1289
[DEBUG] fetch_one success: RealDictRow({'id': 1297})
[DEBUG][update_note] STATUS=OK, TIME=3.7800s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_note, args=[589], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG delete_note] START - user_id=357, note_id=589
[DEBUG] fetch_one success: RealDictRow({'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8544, type=song, year=2003, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1288, title=Media_8544>
[DEBUG][Media.from_dict] Built object=<Song id=1288, title=Media_8544>
[DEBUG][Media.fetch] Built object=<Song id=1288, title=Media_8544>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1240,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1246,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1244,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1264,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1250,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1299,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1293,)
[DEBUG] fetch_one success: RealDictRow({'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.fetch] Data from DB={'id': 1286, 'type': 'video', 'user_id': 362, 'title': 'Media_4810', 'year': 2001, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 29, 389185), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Called with title=Media_4810, type=video, year=2001, user_id=362, kwargs={'id': 1286, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1286
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1286, title=Media_4810>
[DEBUG][Media.fetch] Built object=<Video id=1286, title=Media_4810>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1287,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(361, 'user845882@example.com', 'user845882', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1291,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1266,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1283,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1273,)
[DEBUG] db_get_following result: [(359, 'user644811@example.com', 'user644811', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1271,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1237,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(357, 'user443793@example.com', 'user443793', 'bd94dcda26fccb4e68d6a31f9b5aac0b571ae266d822620e901ef7ebe3a11d4f', datetime.date(2000, 1, 1), '', '', 4)]
[DEBUG][Media.delete] Deleted media_id=1240
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_1916>
[DEBUG][delete_video] STATUS=OK, TIME=19.3980s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1270,)
[DEBUG][Media.delete] Deleted media_id=1246
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1297,)
[DEBUG] fetch_one success: RealDictRow({'id': 1280})
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1282,)
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_9534>
[DEBUG][delete_video] STATUS=OK, TIME=17.2402s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1292,)
[DEBUG] fetch_one success: RealDictRow({'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3850, type=document, year=2004, user_id=358, kwargs={'id': 1294, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1294
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1294, title=Media_3850>
[DEBUG][Media.fetch] Built object=<Document id=1294, title=Media_3850>
[DEBUG] fetch_one success: RealDictRow({'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2076, type=video, year=2019, user_id=353, kwargs={'id': 1289, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1289
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1289, title=Media_2076>
[DEBUG][Media.fetch] Built object=<Video id=1289, title=Media_2076>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1284,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1272,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1277,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1253,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1285, title=Media_3931>
[DEBUG][delete_object] Deleting object <Video id=1285, title=Media_3931>
[DEBUG][Media.delete] Called on <Video id=1285, title=Media_3931>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1265,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(589, 357, 1298, 'regular', Decimal('5.83'), Decimal('6.10'), None, None, None, None, None, 'Nota aggiornata 514', None)]
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(590, 361, 1296, 'regular', Decimal('8.06'), Decimal('9.32'), None, None, None, None, None, 'Nota aggiornata 661', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(588, 359, 1295, 'regular', Decimal('2.22'), Decimal('3.83'), None, None, None, None, None, 'Nota aggiornata 607', None)]
[DEBUG][Media.delete] Deleted media_id=1237
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_7336>
[DEBUG][delete_video] STATUS=OK, TIME=20.7940s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1264,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1244,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1299,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1280,)
[DEBUG][Media.delete] Deleted media_id=1272
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_1395>
[DEBUG][delete_document] STATUS=OK, TIME=19.3848s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1293,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1253
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6657>
[DEBUG][delete_song] STATUS=OK, TIME=16.4289s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1250,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1276, title=Media_6439>
[DEBUG][delete_object] Deleting object <Video id=1276, title=Media_6439>
[DEBUG][Media.delete] Called on <Video id=1276, title=Media_6439>
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(588, 359, 1295, 'regular', Decimal('2.22'), Decimal('3.83'), None, None, None, None, None, 'Nota aggiornata 607', None)]
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1266,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1287,)
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(590, 361, 1296, 'regular', Decimal('8.06'), Decimal('9.32'), None, None, None, None, None, 'Nota aggiornata 661', None)]
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1292,)
[DEBUG] fetch_one success: RealDictRow({'id': 1285})
[DEBUG][Media.delete] Deleted media_id=1264
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_9052>
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_song] STATUS=OK, TIME=14.6986s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1283,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1277,)
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1294, title=Media_3850>
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1297,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1273,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1270,)
[DEBUG] fetch_one success: RealDictRow({'id': 1276})
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1284,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1282,)
[DEBUG][Media.to_dict] <Document id=1294, title=Media_3850> -> {'media_id': 1294, 'type': 'document', 'title': 'Media_3850', 'user_id': 358, 'year': 2004, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:04.401085', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG] fetch_all returned 0 rows
[DEBUG][get_document] STATUS=OK, TIME=1.9485s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1290, title=Media_5097>
[DEBUG][dispatch_command] START - command=delete_document, args=[1294], user_obj={'id': 358, 'username': 'user544294', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1294
[DEBUG][Media.fetch] Called cls=Document, media_id=1294
[DEBUG][Media.to_dict] <Song id=1290, title=Media_5097> -> {'media_id': 1290, 'type': 'song', 'title': 'Media_5097', 'user_id': 354, 'year': 2015, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:40.288364', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=2.6018s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1290], user_obj={'id': 354, 'username': 'user142450', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1290
[DEBUG][get_object] cls=Song, object_id=1290
[DEBUG][Media.fetch] Called cls=Song, media_id=1290
[DEBUG] fetch_all returned 1 rows
[DEBUG] db_get_following result: [(589, 357, 1298, 'regular', Decimal('5.83'), Decimal('6.10'), None, None, None, None, None, 'Nota aggiornata 514', None)]
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1291,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1265,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1286, title=Media_4810>
[DEBUG][delete_object] Deleting object <Video id=1286, title=Media_4810>
[DEBUG][Media.delete] Called on <Video id=1286, title=Media_4810>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1271,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1244,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1288, title=Media_8544>
[DEBUG][Media.to_dict] <Song id=1288, title=Media_8544> -> {'media_id': 1288, 'type': 'song', 'title': 'Media_8544', 'user_id': 360, 'year': 2003, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:38.765654', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=2.5759s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1288], user_obj={'id': 360, 'username': 'user745397', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1288
[DEBUG][get_object] cls=Song, object_id=1288
[DEBUG][Media.fetch] Called cls=Song, media_id=1288
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1299,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (590,)
[DEBUG][Media.delete] Deleted media_id=1292
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_3787>
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (588,)
[DEBUG][Media.delete] Deleted media_id=1287
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5096>
[DEBUG][delete_song] STATUS=OK, TIME=15.6768s, TAG=OK
[DEBUG][delete_song] STATUS=OK, TIME=14.8421s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1294, 'type': 'document', 'user_id': 358, 'title': 'Media_3850', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 4, 401085), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3850, type=document, year=2004, user_id=358, kwargs={'id': 1294, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1294
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1280,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1276,)
[DEBUG][Media.__init__] Finished -> <Document id=1294, title=Media_3850>
[DEBUG][Media.fetch] Built object=<Document id=1294, title=Media_3850>
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1293,)
[DEBUG] execute success: DELETE FROM notes WHERE id=%s (589,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1289, title=Media_2076>
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1285,)
[DEBUG][Media.to_dict] <Video id=1289, title=Media_2076> -> {'media_id': 1289, 'type': 'video', 'title': 'Media_2076', 'user_id': 353, 'year': 2019, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:41:40.025037', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=2.2644s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1289], user_obj={'id': 353, 'username': 'user041987', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1289
[DEBUG][Media.fetch] Called cls=Video, media_id=1289
[DEBUG] fetch_one success: RealDictRow({'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1290, 'type': 'song', 'user_id': 354, 'title': 'Media_5097', 'year': 2015, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 288364), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5097, type=song, year=2015, user_id=354, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1290, title=Media_5097>
[DEBUG][Media.from_dict] Built object=<Song id=1290, title=Media_5097>
[DEBUG][Media.fetch] Built object=<Song id=1290, title=Media_5097>
[DEBUG] fetch_one success: RealDictRow({'id': 1286})
[DEBUG] fetch_one success: RealDictRow({'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1288, 'type': 'song', 'user_id': 360, 'title': 'Media_8544', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 38, 765654), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8544, type=song, year=2003, user_id=360, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1250,)
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1288, title=Media_8544>
[DEBUG][Media.from_dict] Built object=<Song id=1288, title=Media_8544>
[DEBUG][Media.fetch] Built object=<Song id=1288, title=Media_8544>
[DEBUG][Media.delete] Deleted media_id=1284
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_9951>
[DEBUG][delete_video] STATUS=OK, TIME=18.1484s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1289, 'type': 'video', 'user_id': 353, 'title': 'Media_2076', 'year': 2019, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 41, 40, 25037), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_2076, type=video, year=2019, user_id=353, kwargs={'id': 1289, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1289
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1289, title=Media_2076>
[DEBUG][Media.fetch] Built object=<Video id=1289, title=Media_2076>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1266,)
[DEBUG][Media.delete] Deleted media_id=1271
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_7642>
[DEBUG][delete_document] STATUS=OK, TIME=11.5226s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1244
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6364>
[DEBUG][delete_document] STATUS=OK, TIME=11.7145s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1283,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1277,)
[DEBUG][delete_note] STATUS=OK, TIME=2.9706s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG][dispatch_command] START - command=get_document, args=[1296], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG] db_get_following result: []
[DEBUG][get_object] cls=Document, object_id=1296
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1282,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1270,)
[DEBUG][delete_note] STATUS=OK, TIME=3.4538s, TAG=OK
[DEBUG] db_get_following result: []
[DEBUG][dispatch_command] START - command=get_song, args=[1295], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] Retrieved object=<Document id=1294, title=Media_3850>
[DEBUG][delete_object] Deleting object <Document id=1294, title=Media_3850>
[DEBUG][Media.delete] Called on <Document id=1294, title=Media_3850>
[DEBUG][get_song_services] song_id=1295
[DEBUG][Media.fetch] Called cls=Document, media_id=1296
[DEBUG][get_object] cls=Song, object_id=1295
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1273,)
[DEBUG][Media.fetch] Called cls=Song, media_id=1295
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1286,)
[DEBUG][delete_note] STATUS=OK, TIME=2.6628s, TAG=OK
[DEBUG][dispatch_command] START - command=get_video, args=[1298], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1298
[DEBUG][Media.fetch] Called cls=Video, media_id=1298
[DEBUG][Media.delete] Deleted media_id=1250
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_5372>
[DEBUG][delete_video] STATUS=OK, TIME=12.9771s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1297,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1291,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1265,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][Media.delete] Deleted media_id=1266
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_6457>
[DEBUG][delete_song] STATUS=OK, TIME=15.6936s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1294})
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1299,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1293,)
[DEBUG] fetch_one success: RealDictRow({'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1276,)
[DEBUG][Media.__init__] Called with title=Media_8153, type=song, year=2020, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1280,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1285,)
[DEBUG][Media.__init__] Finished -> <Song id=1295, title=Media_8153>
[DEBUG] fetch_one success: RealDictRow({'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.from_dict] Built object=<Song id=1295, title=Media_8153>
[DEBUG][Media.fetch] Built object=<Song id=1295, title=Media_8153>
[DEBUG][Media.fetch] Data from DB={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG] fetch_all returned 0 rows
[DEBUG][Media.__init__] Called with title=Media_3487, type=video, year=2003, user_id=357, kwargs={'id': 1298, 'recording_date': None, 'performer_id': None}
[DEBUG] db_get_following result: []
[DEBUG][Media.__init__] Extra attr: id=1298
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1298, title=Media_3487>
[DEBUG][Media.fetch] Built object=<Video id=1298, title=Media_3487>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1288, title=Media_8544>
[DEBUG] fetch_one success: RealDictRow({'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][delete_object] Deleting object <Song id=1288, title=Media_8544>
[DEBUG][Media.delete] Called on <Song id=1288, title=Media_8544>
[DEBUG][Media.fetch] Data from DB={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5342, type=document, year=2004, user_id=361, kwargs={'id': 1296, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1296
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1296, title=Media_5342>
[DEBUG][Media.fetch] Built object=<Document id=1296, title=Media_5342>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1290, title=Media_5097>
[DEBUG][delete_object] Deleting object <Song id=1290, title=Media_5097>
[DEBUG][Media.delete] Called on <Song id=1290, title=Media_5097>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1277,)
[DEBUG][Media.delete] Deleted media_id=1291
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1283,)
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_1853>
[DEBUG][delete_song] STATUS=OK, TIME=13.4648s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1294,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1286,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1273,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1290})
[DEBUG][get_object] Retrieved object=<Video id=1289, title=Media_2076>
[DEBUG][delete_object] Deleting object <Video id=1289, title=Media_2076>
[DEBUG][Media.delete] Called on <Video id=1289, title=Media_2076>
[DEBUG][Media.delete] Deleted media_id=1293
[DEBUG] fetch_one success: RealDictRow({'id': 1288})
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_6146>
[DEBUG][delete_video] STATUS=OK, TIME=12.8750s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1282,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1265,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1297,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1270,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_one success: RealDictRow({'id': 1289})
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1299,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1280,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1290,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1285,)
[DEBUG][Media.delete] Deleted media_id=1277
[DEBUG] fetch_all returned 0 rows
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_8066>
[DEBUG] db_get_following result: []
[DEBUG][delete_document] STATUS=OK, TIME=8.7986s, TAG=OK
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1276,)
[DEBUG][get_object] Retrieved object=<Document id=1296, title=Media_5342>
[DEBUG][Media.to_dict] <Document id=1296, title=Media_5342> -> {'media_id': 1296, 'type': 'document', 'title': 'Media_5342', 'user_id': 361, 'year': 2004, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:18.580678', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_document] STATUS=OK, TIME=1.2691s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_document, args=[1296], user_obj={'id': 361, 'username': 'user845882', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Document, object_id=1296
[DEBUG][Media.fetch] Called cls=Document, media_id=1296
[DEBUG][Media.delete] Deleted media_id=1283
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5839>
[DEBUG][delete_song] STATUS=OK, TIME=10.6450s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1288,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1298, title=Media_3487>
[DEBUG][Media.to_dict] <Video id=1298, title=Media_3487> -> {'media_id': 1298, 'type': 'video', 'title': 'Media_3487', 'user_id': 357, 'year': 2003, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:24.883481', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_video] STATUS=OK, TIME=1.2675s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_video, args=[1298], user_obj={'id': 357, 'username': 'user443793', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][get_object] cls=Video, object_id=1298
[DEBUG][Media.fetch] Called cls=Video, media_id=1298
[DEBUG][Media.delete] Deleted media_id=1273
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_4773>
[DEBUG][delete_song] STATUS=OK, TIME=10.8318s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1289,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1295, title=Media_8153>
[DEBUG][Media.to_dict] <Song id=1295, title=Media_8153> -> {'media_id': 1295, 'type': 'song', 'title': 'Media_8153', 'user_id': 359, 'year': 2020, 'description': None, 'link': None, 'duration': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': '2025-09-14T22:42:13.398115', 'genres': [], 'authors': [], 'performers': [], 'references': [], 'is_author': False, 'is_performer': False}
[DEBUG][get_song] STATUS=OK, TIME=1.4368s, TAG=OK
[DEBUG][dispatch_command] START - command=delete_song, args=[1295], user_obj={'id': 359, 'username': 'user644811', 'birthday': '2000-01-01', 'bio': '', 'profile_pic': '', 'followers_count': 0, 'followed_count': 0, 'lvl': 4}
[DEBUG][delete_song_services] song_id=1295
[DEBUG][get_object] cls=Song, object_id=1295
[DEBUG][Media.fetch] Called cls=Song, media_id=1295
[DEBUG] fetch_one success: RealDictRow({'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1296, 'type': 'document', 'user_id': 361, 'title': 'Media_5342', 'year': 2004, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 18, 580678), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_5342, type=document, year=2004, user_id=361, kwargs={'id': 1296, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1296
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Document id=1296, title=Media_5342>
[DEBUG][Media.fetch] Built object=<Document id=1296, title=Media_5342>
[DEBUG][Media.delete] Deleted media_id=1282
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5817>
[DEBUG][delete_document] STATUS=OK, TIME=11.3726s, TAG=OK
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1294,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1286,)
[DEBUG] fetch_one success: RealDictRow({'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1298, 'type': 'video', 'user_id': 357, 'title': 'Media_3487', 'year': 2003, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 24, 883481), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_3487, type=video, year=2003, user_id=357, kwargs={'id': 1298, 'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: id=1298
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Video id=1298, title=Media_3487>
[DEBUG][Media.fetch] Built object=<Video id=1298, title=Media_3487>
[DEBUG][Media.delete] Deleted media_id=1270
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_6007>
[DEBUG][delete_document] STATUS=OK, TIME=11.8272s, TAG=OK
[DEBUG] fetch_one success: RealDictRow({'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None})
[DEBUG][Media.fetch] Data from DB={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.from_dict] cls=Song, data={'id': 1295, 'type': 'song', 'user_id': 359, 'title': 'Media_8153', 'year': 2020, 'description': None, 'link': None, 'duration': None, 'recording_date': None, 'location': None, 'additional_info': None, 'stored_at': None, 'created_at': datetime.datetime(2025, 9, 14, 22, 42, 13, 398115), 'is_author': False, 'is_performer': False, 'performer_id': None, 'performers': []}
[DEBUG][Media.__init__] Called with title=Media_8153, type=song, year=2020, user_id=359, kwargs={'recording_date': None, 'performer_id': None}
[DEBUG][Media.__init__] Extra attr: recording_date=None
[DEBUG][Media.__init__] Extra attr: performer_id=None
[DEBUG][Media.__init__] Finished -> <Song id=1295, title=Media_8153>
[DEBUG][Media.from_dict] Built object=<Song id=1295, title=Media_8153>
[DEBUG][Media.fetch] Built object=<Song id=1295, title=Media_8153>
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1297,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1265,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Document id=1296, title=Media_5342>
[DEBUG][delete_object] Deleting object <Document id=1296, title=Media_5342>
[DEBUG][Media.delete] Called on <Document id=1296, title=Media_5342>
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1299,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1285,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1290,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1276,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1280,)
[DEBUG] fetch_one success: RealDictRow({'id': 1296})
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1288,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1289,)
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Video id=1298, title=Media_3487>
[DEBUG][delete_object] Deleting object <Video id=1298, title=Media_3487>
[DEBUG][Media.delete] Called on <Video id=1298, title=Media_3487>
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1294,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1286,)
[DEBUG][Media.delete] Deleted media_id=1265
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_2577>
[DEBUG][delete_song] STATUS=OK, TIME=11.0179s, TAG=OK
[DEBUG] fetch_all returned 0 rows
[DEBUG] db_get_following result: []
[DEBUG][get_object] Retrieved object=<Song id=1295, title=Media_8153>
[DEBUG][delete_object] Deleting object <Song id=1295, title=Media_8153>
[DEBUG][Media.delete] Called on <Song id=1295, title=Media_8153>
[DEBUG] fetch_one success: RealDictRow({'id': 1298})
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1296,)
[DEBUG] fetch_one success: RealDictRow({'id': 1295})
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1297,)
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1298,)
[DEBUG][Media.delete] Deleted media_id=1299
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_9639>
[DEBUG][delete_document] STATUS=OK, TIME=8.5204s, TAG=OK
[DEBUG] execute success: DELETE FROM comments WHERE media_id=%s (1295,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1290,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1276,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1280,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1285,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1289,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1288,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1286,)
[DEBUG][Media.delete] Deleted media_id=1297
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5271>
[DEBUG][delete_song] STATUS=OK, TIME=9.9990s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1294,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1296,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1298,)
[DEBUG] execute success: DELETE FROM notes WHERE media_id=%s (1295,)
[DEBUG][Media.delete] Deleted media_id=1280
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_4067>
[DEBUG][delete_song] STATUS=OK, TIME=8.9227s, TAG=OK
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1290,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1276,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1285,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1288,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1289,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1294,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1286,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1296,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1298,)
[DEBUG] execute success: DELETE FROM media_genres WHERE media_id=%s (1295,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1290,)
[DEBUG][Media.delete] Deleted media_id=1276
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_6439>
[DEBUG][delete_video] STATUS=OK, TIME=7.1461s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1285
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_3931>
[DEBUG][delete_video] STATUS=OK, TIME=8.4300s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1289,)
[DEBUG][Media.delete] Deleted media_id=1286
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_4810>
[DEBUG][delete_video] STATUS=OK, TIME=6.9572s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1288,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1296,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1294,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1295,)
[DEBUG] execute success: DELETE FROM media_authors WHERE media_id=%s (1298,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1290,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1289,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1288,)
[DEBUG][Media.delete] Deleted media_id=1294
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_3850>
[DEBUG][delete_document] STATUS=OK, TIME=5.4872s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1296,)
[DEBUG][Media.delete] Deleted media_id=1290
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_5097>
[DEBUG][delete_song] STATUS=OK, TIME=5.6377s, TAG=OK
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1295,)
[DEBUG] execute success: DELETE FROM media_performances WHERE media_id=%s (1298,)
[DEBUG][Media.delete] Deleted media_id=1289
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_2076>
[DEBUG][delete_video] STATUS=OK, TIME=5.5574s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1288
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_8544>
[DEBUG][delete_song] STATUS=OK, TIME=5.7096s, TAG=OK
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1296,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1295,)
[DEBUG] execute success: DELETE FROM media WHERE id=%s (1298,)
[DEBUG][Media.delete] Deleted media_id=1296
[DEBUG][delete_object] Deleted object <Document id=None, title=Media_5342>
[DEBUG][delete_document] STATUS=OK, TIME=4.5913s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1295
[DEBUG][delete_object] Deleted object <Song id=None, title=Media_8153>
[DEBUG][delete_song] STATUS=OK, TIME=4.5160s, TAG=OK
[DEBUG][Media.delete] Deleted media_id=1298
[DEBUG][delete_object] Deleted object <Video id=None, title=Media_3487>
[DEBUG][delete_video] STATUS=OK, TIME=4.7657s, TAG=OK

=== CHAOS TEST SUMMARY ===
Total commands: 6341
Avg time per command: 23.8292s
Expected errors: 0
Real errors: 0
Total time: 151100.77s

--- REAL ERROR LOG (DETAILED) ---

C:\Users\LENOVO\Desktop\prj\I.S\Code\server>