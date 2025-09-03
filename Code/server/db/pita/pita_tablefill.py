# first line

import datetime
from db.db_crud import hash_pswd
# Nota: non usiamo create_user_db() perché la sua signature in questo progetto
# non coincideva con i dati che il populate passava. Facciamo INSERT/UPDATE diretti.

# =========================
# UTILITY
# =========================
def duration_to_seconds(dur):
    if not dur:
        return None
    # accetta sia "3:21" che "3" e anche valori già numerici
    if isinstance(dur, int):
        return dur
    parts = str(dur).split(":")
    try:
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 1:
            return int(parts[0])
    except Exception:
        return None
    return None
##############################


# USER LEVELS
user_levels = [
    (0, "ROOT", "Accesso totale al sistema"),
    (1, "ADMIN", "Amministratore, gestione utenti e contenuti"),
    (2, "MOD", "Moderatore, gestione commenti e segnalazioni"),
    (3, "PUBLISHER", "Può pubblicare contenuti"),
    (4, "REGULAR", "Utente registrato standard"),
    (5, "RESTRICTED", "Utente affetto da restrizioni"),
    (6, "BANNED", "Utente sospeso o bannato"),
]

def user_levels_tablefill(cnt, cur):
    try:
        for lvl_id, name, description in user_levels:
            cur.execute(
                "INSERT INTO user_levels (id, name, description) VALUES (%s, %s, %s) "
                "ON CONFLICT (id) DO UPDATE SET name=EXCLUDED.name, description=EXCLUDED.description;",
                (lvl_id, name, description)
            )
            print(f"[INFO] User level {name} ({lvl_id}) inserito/aggiornato")
        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Failed to insert user_levels: {e}")
        return False

# PERMISSIONS
permissions = [
    ("manage_users", "Gestire utenti e ruoli"),
    ("manage_content", "Gestire contenuti multimediali"),
    ("comment", "Lasciare commenti"),
    ("view_content", "Visualizzare contenuti"),
    ("publish", "Pubblicare contenuti"),
]

def permissions_tablefill(cnt, cur):
    try:
        for name, desc in permissions:
            # Prima cerco se esiste già (evita dipendere da UNIQUE/ON CONFLICT)
            cur.execute("SELECT id FROM permissions WHERE name=%s;", (name,))
            row = cur.fetchone()
            if row:
                cur.execute("UPDATE permissions SET description=%s WHERE id=%s;", (desc, row[0]))
                print(f"[INFO] Permission {name} aggiornata")
            else:
                cur.execute("INSERT INTO permissions (name, description) VALUES (%s, %s);", (name, desc))
                print(f"[INFO] Permission {name} inserita")
        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Failed to insert permissions: {e}")
        return False

# ROLE-PERMISSIONS
role_permissions = {
    0: ["manage_users", "manage_content", "comment", "view_content", "publish"],   # ROOT
    1: ["manage_users", "manage_content", "comment", "view_content", "publish"],   # ADMIN
    2: ["manage_content", "comment", "view_content"],                              # MOD
    3: ["publish", "comment", "view_content"],                                     # PUBLISHER
    4: ["comment", "view_content"],                                                # REGULAR
    5: ["view_content"],                                                           # RESTRICTED
    6: []                                                                          # BANNED
}

def role_permissions_tablefill(cnt, cur):
    try:
        for lvl_id, perms in role_permissions.items():
            for perm in perms:
                cur.execute("SELECT id FROM permissions WHERE name=%s;", (perm,))
                perm_row = cur.fetchone()
                if not perm_row:
                    print(f"[WARN] Permission {perm} non trovata, saltata.")
                    continue
                perm_id = perm_row[0]

                # Evitiamo ON CONFLICT: controlliamo se esiste già la coppia
                cur.execute(
                    "SELECT 1 FROM role_permissions WHERE lvl_id=%s AND permission_id=%s;",
                    (lvl_id, perm_id)
                )
                if cur.fetchone():
                    print(f"[INFO] Role {lvl_id} → Permission {perm} già esistente")
                    continue

                cur.execute(
                    "INSERT INTO role_permissions (lvl_id, permission_id) VALUES (%s, %s);",
                    (lvl_id, perm_id)
                )
                print(f"[INFO] Role {lvl_id} → Permission {perm} inserito")
        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Failed to insert role_permissions: {e}")
        return False

# USERS
users = [
    # (username, password_plain, email, profile_pic, birthday, bio, lvl)
    ("Myosotis", "molollo73", "molollo73@gmail.com", "pic_ID001", "2002-12-14", "find what you love and let it kill you", 0),
    ("temp user", "123456", "apocalypt73@gmail.com", "pic_ID002", "1999-04-23", "nel blup dipinto di blup", 1),
    ("Root", "160718", "a@b.c", "pic_ID003", "2005-02-04", "wonderlust", 0),
    ("Anna", "password1", "anna.cappelli@gmail.com", "pic_ID004", "1998-07-16", "sunshine on my mind", 4),
    ("Marco", "password123", "marco.rossi@domain.com", "pic_ID005", "2000-05-22", "chasing dreams", 4),
    ("Giulia", "letmein", "giulia@libero.it", "pic_ID006", "1995-11-11", "peace and love", 4),
    ("Luca", "qwertyuiop", "luca.martini@example.com", "pic_ID007", "2001-02-05", "just do it", 4),
    ("Francesca", "supersecret", "francesca.smith@yahoo.com", "pic_ID008", "1997-12-04", "living the dream", 4),
    ("Tommaso", "123456789", "tommyboy@outlook.com", "pic_ID009", "1996-09-30", "never stop learning", 3),
    ("Giovanni", "abcd1234", "giovanni.r@gmail.com", "pic_ID010", "1993-01-12", "always improving", 3),
    ("Elena", "qwertzuiop", "elena.andrea@mail.com", "pic_ID011", "2000-07-29", "seek the unknown", 3),
    ("Alessandra", "mypassword", "alessandra@domain.net", "pic_ID012", "1994-04-18", "one step at a time", 3),
    ("Francesco", "ilovemusic", "francesco.cano@live.it", "pic_ID013", "1999-03-09", "music is life", 3),
    ("Chiara", "summerdays", "chiara.martini@protonmail.com", "pic_ID014", "2003-05-22", "be happy", 4),
    ("Stefano", "securepass", "stefano.ferro@gmail.com", "pic_ID015", "1995-10-02", "work hard, play hard", 4),
    ("Federico", "password1234", "federico.scarpelli@me.com", "pic_ID016", "1992-06-15", "keep going", 4),
    ("Valentina", "1234abcd", "valentina.sardi@domain.it", "pic_ID017", "2001-11-09", "stay positive", 4),
    ("Alessio", "longpassword", "alessio.viviani@outlook.com", "pic_ID018", "1998-03-14", "embrace the challenge", 4),
    ("Cristina", "abc12345", "cristina.morandi@yahoo.it", "pic_ID019", "2000-08-30", "dream big", 4),
    ("Riccardo", "letmein123", "riccardo.zappa@gmail.com", "pic_ID020", "2002-02-17", "you only live once", 4)
]

def user_tablefill(cnt, cur):
    try:
        for username, password_plain, mail, foto, birthday, bio, lvl in users:
            # normalizzo valori
            birthday_date = None
            if birthday:
                try:
                    birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                except Exception:
                    birthday_date = None

            password_hash = hash_pswd(password_plain)

            # controlla se esiste per email (mail) o per username
            cur.execute("SELECT id FROM users WHERE mail=%s;", (mail,))
            row = cur.fetchone()
            if row:
                user_id = row[0]
                cur.execute(
                    "UPDATE users SET username=%s, password_hash=%s, birthday=%s, bio=%s, profile_pic=%s, lvl=%s WHERE id=%s;",
                    (username, password_hash, birthday_date, bio, foto, lvl, user_id)
                )
                print(f"[INFO] {username} ({mail}) già presente, aggiornato (id={user_id})")
            else:
                # Evitiamo di mandare errori se username già esiste: controllo preventivo
                cur.execute("SELECT id FROM users WHERE username=%s;", (username,))
                if cur.fetchone():
                    # se username preso ma mail libera, aggiungiamo un suffisso allo username
                    orig = username
                    i = 1
                    while True:
                        candidate = f"{orig}_{i}"
                        cur.execute("SELECT id FROM users WHERE username=%s;", (candidate,))
                        if not cur.fetchone():
                            username = candidate
                            break
                        i += 1
                    print(f"[WARN] Username duplicato, inserito come {username}")

                cur.execute(
                    "INSERT INTO users (mail, username, password_hash, birthday, bio, profile_pic, lvl) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;",
                    (mail, username, password_hash, birthday_date, bio, foto, lvl)
                )
                new_id = cur.fetchone()[0]
                print(f"[INFO] {username} ({mail}) inserito con id {new_id}")

        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Users population failed: {e}")
        return False
###########


# SONGS
# SONGS
songs = [
    {
        "title": "Moral Of The Story",
        "durata": "3:21",
        "year": "2019-02-14",
        "location": "music/ashe-moral-of-the-story-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "EP Moral of the Story: Chapter 1; Remix Niall Horan 2020",
        "performer": "Ashe"
    },
    {
        "title": "IDFC",
        "durata": "4:07",
        "year": "2014-10-16",
        "location": "music/blackbear-idfc-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo dall’album Deadroses",
        "performer": "blackbear"
    },
    {
        "title": "Hold On",
        "durata": "3:21",
        "year": "2017-02-03",
        "location": "music/chord-overstreet-hold-on-lyric-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo di debutto di Chord Overstreet",
        "performer": "Chord Overstreet"
    },
    {
        "title": "A Thousand Years",
        "durata": "4:45",
        "year": "2011-10-18",
        "location": "music/christina-perri-a-thousand-years-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo dalla colonna sonora di Twilight – Breaking Dawn Pt. 1",
        "performer": "Christina Perri"
    },
    {
        "title": "Numb Little Bug",
        "durata": "2:49",
        "year": "2022-01-28",
        "location": "music/em-beihold-numb-little-bug-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "single dall’EP Egg in the Backseat",
        "performer": "Em Beihold"
    },
    {
        "title": "It's Not So Bad",
        "durata": "2:20",
        "year": "2021-01-05",
        "location": "music/its-not-so-bad-dybbukk-sabrina-gomes-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "single – Dybbukk & Sabrina Gomes cover",
        "performer": "Dybbukk & Sabrina Gomes"
    },
    {
        "title": "Perfetti Sconosciuti",
        "durata": "2:56",
        "year": "2018-09-07",
        "location": "music/mose-perfetti-sconosciuti-official-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo Mose",
        "performer": "Mose"
    },
    {
        "title": "Reckless",
        "durata": "3:23",
        "year": "2021-06-04",
        "location": "music/madison-beer-reckless-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo dal secondo album Silence Between Songs",
        "performer": "Madison Beer"
    },
    {
        "title": "Sabato Sera",
        "durata": "4:20",
        "year": "2017-08-04",
        "location": "music/mostro-12-sabato-sera-128-ytshorts.savetube.me.mp3",
        "additional_info": "dall’album Ogni maledetto giorno (Deluxe Edition)",
        "performer": "Mostro"
    },
    {
        "title": "Die First",
        "durata": "2:57",
        "year": "2022-06-24",
        "location": "music/nessa-barrett-die-first-official-music-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "lead single dall’album Young Forever",
        "performer": "Nessa Barrett"
    },
        {
        "title": "What Was I Made For?",
        "durata": "3:42",
        "year": "2023-07-13",
        "location": "music/billie-eilish-what-was-i-made-for-official-music-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "colonna sonora film Barbie (2023)",
        "performer": "Billie Eilish"
    },
    {
        "title": "Off My Face",
        "durata": "2:36",
        "year": "2021-03-19",
        "location": "music/off-my-face-128-ytshorts.savetube.me.mp3",
        "additional_info": "dall’album Justice",
        "performer": "Justin Bieber"
    },
    {
        "title": "I Don't Want to Miss a Thing",
        "durata": "4:59",
        "year": "1998-08-18",
        "location": "music/aerosmith-i-dont-want-to-miss-a-thing-official-hd-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "colonna sonora Armageddon",
        "performer": "Aerosmith"
    },
    {
        "title": "The Perfect Girl (Nightcore)",
        "durata": "2:15",
        "year": "2020-01-01",
        "location": "music/nightcore-the-perfect-girl-128-ytshorts.savetube.me.mp3",
        "additional_info": "Nightcore version – original da Mareux (2015)",
        "performer": "Nightcore (Mareux cover)"
    },
    {
        "title": "Never Forget You",
        "durata": "3:33",
        "year": "2015-07-10",
        "location": "music/zaralarsson-never-forget-you-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. MNEK, singolo di Zara Larsson",
        "performer": "Zara Larsson & MNEK"
    },
    {
        "title": "Another Love",
        "durata": "4:10",
        "year": "2012-06-15",
        "location": "music/tom-odell-another-love-128-ytshorts.savetube.me.mp3",
        "additional_info": "dall’album Long Way Down",
        "performer": "Tom Odell"
    },
    {
        "title": "Love Me Like You Do",
        "durata": "4:12",
        "year": "2015-01-07",
        "location": "music/ellie-goulding-love-me-like-you-do-128-ytshorts.savetube.me.mp3",
        "additional_info": "colonna sonora 50 Sfumature di Grigio",
        "performer": "Ellie Goulding"
    },
    {
        "title": "Lovely",
        "durata": "3:21",
        "year": "2018-04-19",
        "location": "music/billie-eilish-khalid-lovely-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Khalid",
        "performer": "Billie Eilish & Khalid"
    },
    {
        "title": "Take Me to Church",
        "durata": "4:01",
        "year": "2013-09-13",
        "location": "music/hozier-take-me-to-church-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo d’esordio",
        "performer": "Hozier"
    },
    {
        "title": "Let Her Go",
        "durata": "4:12",
        "year": "2012-07-24",
        "location": "music/passenger-let-her-go-128-ytshorts.savetube.me.mp3",
        "additional_info": "album All the Little Lights",
        "performer": "Passenger"
    },
    {
        "title": "Unstoppable",
        "durata": "3:37",
        "year": "2016-01-21",
        "location": "music/sia-unstoppable-128-ytshorts.savetube.me.mp3",
        "additional_info": "album This Is Acting",
        "performer": "Sia"
    },
    {
        "title": "Arcade",
        "durata": "3:04",
        "year": "2019-03-16",
        "location": "music/duncan-laurence-arcade-128-ytshorts.savetube.me.mp3",
        "additional_info": "Eurovision 2019 winner",
        "performer": "Duncan Laurence"
    },
    {
        "title": "Dandelions",
        "durata": "3:54",
        "year": "2017-11-16",
        "location": "music/ruth-b-dandelions-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Safe Haven",
        "performer": "Ruth B."
    },
    {
        "title": "Say You Won’t Let Go",
        "durata": "3:31",
        "year": "2016-09-09",
        "location": "music/james-arthur-say-you-wont-let-go-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Back from the Edge",
        "performer": "James Arthur"
    },
    {
        "title": "Let Me Down Slowly",
        "durata": "2:49",
        "year": "2019-01-08",
        "location": "music/alec-benjamin-let-me-down-slowly-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo da Narrated for You",
        "performer": "Alec Benjamin"
    },
    {
        "title": "Heat Waves",
        "durata": "3:59",
        "year": "2020-06-29",
        "location": "music/glass-animals-heat-waves-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Dreamland",
        "performer": "Glass Animals"
    },
    {
        "title": "Dance Monkey",
        "durata": "3:29",
        "year": "2019-05-10",
        "location": "music/tones-and-i-dance-monkey-128-ytshorts.savetube.me.mp3",
        "additional_info": "singolo mondiale",
        "performer": "Tones and I"
    },
    {
        "title": "Shallow",
        "durata": "3:37",
        "year": "2018-09-27",
        "location": "music/lady-gaga-bradley-cooper-shallow-128-ytshorts.savetube.me.mp3",
        "additional_info": "colonna sonora A Star Is Born",
        "performer": "Lady Gaga & Bradley Cooper"
    },
    {
        "title": "Someone You Loved",
        "durata": "3:02",
        "year": "2018-11-08",
        "location": "music/lewis-capaldi-someone-you-loved-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Divinely Uninspired to a Hellish Extent",
        "performer": "Lewis Capaldi"
    },
    {
        "title": "Believer",
        "durata": "3:24",
        "year": "2017-02-01",
        "location": "music/imagine-dragons-believer-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Evolve",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Thunder",
        "durata": "3:07",
        "year": "2017-04-27",
        "location": "music/imagine-dragons-thunder-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Evolve",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Whatever It Takes",
        "durata": "3:21",
        "year": "2017-05-08",
        "location": "music/imagine-dragons-whatever-it-takes-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Evolve",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Natural",
        "durata": "3:09",
        "year": "2018-07-17",
        "location": "music/imagine-dragons-natural-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Origins",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Bones",
        "durata": "2:45",
        "year": "2022-03-11",
        "location": "music/imagine-dragons-bones-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Mercury – Act 2",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Enemy",
        "durata": "2:53",
        "year": "2021-10-28",
        "location": "music/imagine-dragons-enemy-128-ytshorts.savetube.me.mp3",
        "additional_info": "con JID – colonna sonora serie Arcane",
        "performer": "Imagine Dragons & JID"
    },
    {
        "title": "Demons",
        "durata": "2:57",
        "year": "2013-05-07",
        "location": "music/imagine-dragons-demons-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Night Visions",
        "performer": "Imagine Dragons"
    },
    {
        "title": "On Top of the World",
        "durata": "3:12",
        "year": "2012-03-13",
        "location": "music/imagine-dragons-on-top-of-the-world-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Night Visions",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Radioactive",
        "durata": "3:06",
        "year": "2012-04-02",
        "location": "music/imagine-dragons-radioactive-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Night Visions",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Warriors",
        "durata": "2:50",
        "year": "2014-09-17",
        "location": "music/imagine-dragons-warriors-128-ytshorts.savetube.me.mp3",
        "additional_info": "realizzata per League of Legends Worlds 2014",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Birds",
        "durata": "3:40",
        "year": "2019-07-03",
        "location": "music/imagine-dragons-birds-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Elisa – album Origins",
        "performer": "Imagine Dragons feat. Elisa"
    },
    {
        "title": "Sharks",
        "durata": "3:11",
        "year": "2022-06-24",
        "location": "music/imagine-dragons-sharks-128-ytshorts.savetube.me.mp3",
        "additional_info": "album Mercury – Act 2",
        "performer": "Imagine Dragons"
    },
    {
        "title": "Waves",
        "durata": "3:47",
        "year": "2014-04-11",
        "location": "music/mr-probz-waves-128-ytshorts.savetube.me.mp3",
        "additional_info": "hit remixata da Robin Schulz",
        "performer": "Mr. Probz"
    },
    {
        "title": "Let’s Love",
        "durata": "3:20",
        "year": "2020-09-11",
        "location": "music/david-guetta-sia-lets-love-128-ytshorts.savetube.me.mp3",
        "additional_info": "collaborazione David Guetta e Sia",
        "performer": "David Guetta & Sia"
    },
    {
        "title": "Flames",
        "durata": "3:15",
        "year": "2018-03-22",
        "location": "music/david-guetta-sia-flames-128-ytshorts.savetube.me.mp3",
        "additional_info": "collaborazione David Guetta e Sia",
        "performer": "David Guetta & Sia"
    },
    {
        "title": "Titanium",
        "durata": "4:05",
        "year": "2011-12-09",
        "location": "music/david-guetta-titanium-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sia – album Nothing but the Beat",
        "performer": "David Guetta feat. Sia"
    },
    {
        "title": "She Wolf (Falling to Pieces)",
        "durata": "3:41",
        "year": "2012-08-21",
        "location": "music/david-guetta-shewolf-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sia",
        "performer": "David Guetta feat. Sia"
    },
    {
        "title": "Say My Name",
        "durata": "3:12",
        "year": "2018-10-26",
        "location": "music/david-guetta-say-my-name-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Bebe Rexha & J Balvin",
        "performer": "David Guetta, Bebe Rexha & J Balvin"
    },
    {
        "title": "Dangerous",
        "durata": "3:23",
        "year": "2014-10-06",
        "location": "music/david-guetta-dangerous-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sam Martin",
        "performer": "David Guetta feat. Sam Martin"
    },
    {
        "title": "Play Hard",
        "durata": "3:28",
        "year": "2013-03-15",
        "location": "music/david-guetta-play-hard-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Ne-Yo & Akon",
        "performer": "David Guetta feat. Ne-Yo & Akon"
    },
    {
        "title": "Lovers on the Sun",
        "durata": "3:23",
        "year": "2014-06-30",
        "location": "music/david-guetta-lovers-on-the-sun-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sam Martin",
        "performer": "David Guetta feat. Sam Martin"
    },
        {
        "title": "From The Start",
        "durata": "3:12",
        "year": "2021-02-12",
        "location": "music/laufey-from-the-start-lyrics-yt.savetube.me.mp3",
        "additional_info": "album Everything I Know About Love",
        "performer": "Laufey"
    },
    {
        "title": "Il Filo Rosso",
        "durata": "3:34",
        "year": "2023-03-15",
        "location": "music/alfa-il-filo-rosso-yt.savetube.me.mp3",
        "additional_info": "",
        "performer": "ALFA"
    },
    {
        "title": "Obsidian / Monster",
        "durata": "4:05",
        "year": "2021-07-23",
        "location": "music/adventure-time-distant-lands-obsidian-monster-yt.savetube.me.mp3",
        "additional_info": "feat. Olivia Olson & Half Shy – colonna sonora",
        "performer": "Adventure Time"
    },
    {
        "title": "Ain't No Crying",
        "durata": "3:00",
        "year": "2021-01-15",
        "location": "music/derivakat-aint-no-crying-yt.savetube.me.mp3",
        "additional_info": "Dream SMP original song",
        "performer": "Derivakat"
    },
    {
        "title": "Always",
        "durata": "3:18",
        "year": "2020-09-04",
        "location": "music/ashe-always-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "I'm Fine",
        "durata": "3:25",
        "year": "2019-07-12",
        "location": "music/ashe-im-fine-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Love Is Not Enough",
        "durata": "3:12",
        "year": "2020-05-20",
        "location": "music/ashe-love-is-not-enough-yt.savetube.me.mp3",
        "additional_info": "Official Audio",
        "performer": "Ashe"
    },
    {
        "title": "Moral Of The Story",
        "durata": "2:48",
        "year": "2019-05-10",
        "location": "music/ashe-moral-of-the-story-lyric-video-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Save Myself",
        "durata": "3:15",
        "year": "2020-03-15",
        "location": "music/ashe-save-myself-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "We Get High",
        "durata": "3:10",
        "year": "2021-02-01",
        "location": "music/ashe-we-get-high-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Voilà",
        "durata": "2:47",
        "year": "2021-02-19",
        "location": "music/barbara-pravi-voila-paroles-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Barbara Pravi"
    },
    {
        "title": "When You Say My Name",
        "durata": "3:04",
        "year": "2020-11-23",
        "location": "music/chandler-leighton-when-you-say-my-name-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Chandler Leighton"
    },
    {
        "title": "Sofia",
        "durata": "2:58",
        "year": "2019-10-03",
        "location": "music/clairo-sofia-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Clairo"
    },
    {
        "title": "I Hear a Symphony",
        "durata": "3:30",
        "year": "2020-07-01",
        "location": "music/cody-fry-i-hear-a-symphony-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Cody Fry"
    },
    {
        "title": "Hate Me",
        "durata": "2:45",
        "year": "2019-11-08",
        "location": "music/ellie-goulding-juice-wrld-hate-me-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ellie Goulding & Juice WRLD"
    },
    {
        "title": "City of Angels",
        "durata": "3:19",
        "year": "2021-04-21",
        "location": "music/em-beihold-city-of-angels-official-audio-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Em Beihold"
    },
    {
        "title": "Cupid",
        "durata": "3:13",
        "year": "2022-02-14",
        "location": "music/fifty-fifty-cupid-official-mv-yt.savetube.me.mp3",
        "additional_info": "MV ufficiale",
        "performer": "FIFTY FIFTY"
    },
    {
        "title": "IDGAF",
        "durata": "3:38",
        "year": "2018-03-09",
        "location": "music/idgaf-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Dua Lipa"
    },
    {
        "title": "Die With A Smile",
        "durata": "3:05",
        "year": "2021-08-18",
        "location": "music/lady-gaga-bruno-mars-die-with-a-smile-lyrics-yt.savetube.me.mp3",
        "additional_info": "",
        "performer": "Lady Gaga & Bruno Mars"
    },
    {
        "title": "Diet Mountain Dew",
        "durata": "3:20",
        "year": "2012-12-12",
        "location": "music/lana-del-rey-diet-mountain-dew-lyrics-yt.savetube.me.mp3",
        "additional_info": "album Born to Die",
        "performer": "Lana Del Rey"
    },
    {
        "title": "happier than ever",
        "durata": "4:58",
        "year": "2021-07-30",
        "location": "music/loveless-happier-than-ever-cover-yt.savetube.me.mp3",
        "additional_info": "cover di Billie Eilish",
        "performer": "Loveless"
    },
    {
        "title": "the alternative",
        "durata": "3:10",
        "year": "2021-05-22",
        "location": "music/lyn-lapid-the-alternative-lyric-video-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Alex Sloan / Lyn Lapid"
    }
]

def songs_tablefill(cnt, cur):
    try:
        for s in songs:
            title = s.get("title")
            # year può essere YYYY-MM-DD o solo YYYY
            year_val = None
            if s.get("year"):
                try:
                    year_val = int(str(s.get("year"))[:4])
                except Exception:
                    year_val = None

            # Inserisco in media (senza author)
            cur.execute(
                "INSERT INTO media (type, title, year, description, link) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
                ('song', title, year_val, s.get("additional_info"), s.get("location"))
            )
            media_id = cur.fetchone()[0]

            # durata
            dur = s.get("duration") or s.get("durata")
            seconds = duration_to_seconds(dur)

            # Inserisco nella tabella songs (id = media.id)
            cur.execute(
                "INSERT INTO songs (id, duration, recording_date, location, additional_info) VALUES (%s, %s, %s, %s, %s);",
                (media_id, seconds, None, s.get("location"), s.get("additional_info"))
            )

            # Autore / performer: uso authors + song_authors
            performer = s.get("performer")
            if performer:
                # inserisco author se non esiste
                cur.execute("SELECT id FROM authors WHERE name=%s;", (performer,))
                arow = cur.fetchone()
                if arow:
                    author_id = arow[0]
                else:
                    cur.execute("INSERT INTO authors (name) VALUES (%s) RETURNING id;", (performer,))
                    author_id = cur.fetchone()[0]
                # collegamento song_authors
                cur.execute("SELECT 1 FROM song_authors WHERE song_id=%s AND author_id=%s;", (media_id, author_id))
                if not cur.fetchone():
                    cur.execute("INSERT INTO song_authors (song_id, author_id) VALUES (%s, %s);", (media_id, author_id))

            print(f"[INFO] Song '{title}' inserted with media ID {media_id}")

        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Failed to insert songs: {e}")
        return False
##############################

#############################
#############################
#############################

# DOCUMENTS
documents = [
    # (+) ho mantenuto la tua struttura originale; useremo doc[1] come title
    (1, "Moral Of The Story", "Ashe", "2019-02-14", "C:\\Users\\LENOVO\\Desktop\\prj\\I.S\\Code\\server\\db\\storage\\documents\\id_001.pdf", 1, "EP Moral of the Story: Chapter 1; Remix Niall Horan 2020"),
    # altri documenti...
]

def documents_tablefill(cnt, cur):
    try:
        for doc in documents:
            title = doc[1]
            author = doc[2]
            date = doc[3]
            filepath = doc[4]
            caption = doc[6] if len(doc) > 6 else None

            # Trova la canzone associata (media.title, type='song')
            cur.execute("SELECT id FROM media WHERE title=%s AND type='song';", (title,))
            song_media = cur.fetchone()
            if not song_media:
                print(f"[WARN] Document '{title}' skipped: song not found")
                continue
            song_id = song_media[0]

            # year
            year_val = None
            if date:
                try:
                    year_val = int(str(date)[:4])
                except Exception:
                    year_val = None

            # Inserisco media per il document (senza author in media)
            cur.execute(
                "INSERT INTO media (type, title, year, description, link) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
                ('document', title, year_val, caption, filepath)
            )
            media_id = cur.fetchone()[0]

            # Inserisco author se esiste e collego (authors + song_authors o una tabella apposita se vuoi)
            if author:
                cur.execute("SELECT id FROM authors WHERE name=%s;", (author,))
                arow = cur.fetchone()
                if arow:
                    author_id = arow[0]
                else:
                    cur.execute("INSERT INTO authors (name) VALUES (%s) RETURNING id;", (author,))
                    author_id = cur.fetchone()[0]
                # per i documenti non esiste song_authors — lascio gli autori nel DB ma non li relaziono
                # se vuoi una relazione specifica, la creiamo.

            # Inserisco nella tabella documents
            cur.execute(
                "INSERT INTO documents (id, format, pages, caption, song_id) VALUES (%s, %s, %s, %s, %s);",
                (media_id, None, None, caption, song_id)
            )

            print(f"[INFO] Document '{title}' inserted with media ID {media_id} linked to song ID {song_id}")

        cnt.commit()
        return True
    except Exception as e:
        cnt.rollback()
        print(f"[DB ERROR] Failed to insert documents: {e}")
        return False
##############################

# VIDEOS
def videos_tablefill(cnt, cur):
    print("[INFO] videos_tablefill not implemented yet")
    return True
##############################

# last line