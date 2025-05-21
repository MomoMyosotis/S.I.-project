-- first line

INSERT INTO Users(username, password, mail, foto_profilo, birthday, bio, lvl)
VALUES
    ("Myosotis", "tsuki", "molollo73@gmail.com", "" , "2002-12-14", "find what you love and let it kill you", 0),
    ('temp user', '123456', "apocalypt73@gmail.com", "", "1999-4-23", "nel blup dipinto di blup" 1)

ON CONFLICT (id) DO NOTHING


-- last line