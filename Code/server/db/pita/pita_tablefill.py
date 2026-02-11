# first line

import datetime
from server.db.db_crud import hash_pswd, debug

# =========================
# DATI DI BASE
# =========================

user_levels = [
    (0, "ROOT", "Accesso totale al sistema"),
    (1, "ADMIN", "Gestione utenti e contenuti"),
    (2, "MOD", "Moderazione commenti e segnalazioni"),
    (3, "PUBLISHER", "Può pubblicare contenuti"),
    (4, "REGULAR", "Utente registrato standard"),
    (5, "RESTRICTED", "Utente con restrizioni"),
    (6, "BANNED", "Utente sospeso o bannato"),
]

permissions = [
    ("manage_users", "Gestire utenti e ruoli"),
    ("manage_content", "Gestire contenuti multimediali"),
    ("comment", "Lasciare commenti"),
    ("view_content", "Visualizzare contenuti"),
    ("publish", "Pubblicare contenuti"),
]

role_permissions = {
    0: ["manage_users", "manage_content", "comment", "view_content", "publish"],  # ROOT
    1: ["manage_users", "manage_content", "comment", "view_content", "publish"],  # ADMIN
    2: ["manage_content", "comment", "view_content"],                             # MOD
    3: ["publish", "comment", "view_content"],                                    # PUBLISHER
    4: ["comment", "view_content"],                                               # REGULAR
    5: ["view_content"],                                                          # RESTRICTED
    6: []                                                                         # BANNED
}

users = [
    # (username, password_plain, email, profile_pic, birthday, bio, lvl_id)
    ("Myosotis", "Shoganai", "molollo73@gmail.com", "pic_ID001", "2002-12-14", "Nothing ever ends poetically. It ends and we turn it into poetry. All that blood was never once beautiful. It was just red.", 0),
    ("temp user", "123456", "apocalypt73@gmail.com", "pic_ID002", "1999-04-23", "nel blup dipinto di blup", 1),
    ("Root", "160718", "a@b.c", "pic_ID003", "2005-02-04", "wonderlust", 0),
    ("Anna", "password1", "anna.cappelli@gmail.com", "pic_ID004", "1998-07-16", "sunshine on my mind", 4),
    ("Marco", "password123", "marco.rossi@domain.com", "pic_ID005", "2000-05-22", "chasing dreams", 4),
]

songs = [
    {
        "title": "Moral Of The Story",
        "duration": "3:21",
        "year": "2019-02-14",
        "stored_at": "music/ashe-moral-of-the-story-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "EP Moral of the Story: Chapter 1; Remix Niall Horan 2020",
        "performer": "Ashe",
        "author": "Ashe",
        "user_id": 1
    },
    {
        "title": "IDFC",
        "duration": "4:07",
        "year": "2014-10-16",
        "stored_at": "music/blackbear-idfc-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo dall’album Deadroses",
        "performer": "blackbear",
        "author": "blackbear",
        "user_id": 1
    },
    {
        "title": "Hold On",
        "duration": "3:21",
        "year": "2017-02-03",
        "stored_at": "music/chord-overstreet-hold-on-lyric-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo di debutto di Chord Overstreet",
        "performer": "Chord Overstreet",
        "author": "Chord Overstreet",
        "user_id": 1
    },
    {
        "title": "A Thousand Years",
        "duration": "4:45",
        "year": "2011-10-18",
        "stored_at": "music/christina-perri-a-thousand-years-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo dalla colonna sonora di *Twilight – Breaking Dawn Pt. 1*",
        "performer": "Christina Perri",
        "author": "Christina Perri",
        "user_id": 1
    },
    {
        "title": "Numb Little Bug",
        "duration": "2:49",
        "year": "2022-01-28",
        "stored_at": "music/em-beihold-numb-little-bug-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo dall’EP *Egg in the Backseat*",
        "performer": "Em Beihold",
        "author": "Em Beihold",
        "user_id": 1
    },
    {
        "title": "It's Not So Bad",
        "duration": "2:20",
        "year": "2021-01-05",
        "stored_at": "music/its-not-so-bad-dybbukk-sabrina-gomes-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo – Dybbukk & Sabrina Gomes (cover)",
        "performer": "Dybbukk & Sabrina Gomes",
        "author": "Dybbukk & Sabrina Gomes",
        "user_id": 1
    },
    {
        "title": "Perfetti Sconosciuti",
        "duration": "2:56",
        "year": "2018-09-07",
        "stored_at": "music/mose-perfetti-sconosciuti-official-video-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo di Mose",
        "performer": "Mose",
        "author": "Mose",
        "user_id": 1
    },
    {
        "title": "Reckless",
        "duration": "3:23",
        "year": "2021-06-04",
        "stored_at": "music/madison-beer-reckless-lyrics-128-ytshorts.savetube.me.mp3",
        "additional_info": "Singolo dal secondo album *Silence Between Songs*",
        "performer": "Madison Beer",
        "author": "Madison Beer",
        "user_id": 1
    },
    {
        "title": "Sabato Sera",
        "duration": "4:20",
        "year": "2017-08-04",
        "stored_at": "music/mostro-12-sabato-sera.mp3",
        "additional_info": "dall’album Ogni maledetto giorno (Deluxe Edition)",
        "performer": "Mostro",
        "author": "Mostro",
        "user_id": 1
    },
    {
        "title": "Die First",
        "duration": "2:57",
        "year": "2022-06-24",
        "stored_at": "music/nessa-barrett-die-first.mp3",
        "additional_info": "lead single dall’album Young Forever",
        "performer": "Nessa Barrett",
        "author": "Nessa Barrett",
        "user_id": 1
    },
    {
        "title": "What Was I Made For?",
        "duration": "3:42",
        "year": "2023-07-13",
        "stored_at": "music/billie-eilish-what-was-i-made-for.mp3",
        "additional_info": "colonna sonora del film Barbie (2023)",
        "performer": "Billie Eilish",
        "author": "Billie Eilish",
        "user_id": 1
    },
    {
        "title": "Off My Face",
        "duration": "2:36",
        "year": "2021-03-19",
        "stored_at": "music/justin-bieber-off-my-face.mp3",
        "additional_info": "dall’album Justice",
        "performer": "Justin Bieber",
        "author": "Justin Bieber",
        "user_id": 1
    },
    {
        "title": "I Don't Want to Miss a Thing",
        "duration": "4:59",
        "year": "1998-08-18",
        "stored_at": "music/aerosmith-i-dont-want-to-miss-a-thing.mp3",
        "additional_info": "colonna sonora di Armageddon",
        "performer": "Aerosmith",
        "author": "Aerosmith",
        "user_id": 1
    },
    {
        "title": "The Perfect Girl (Nightcore)",
        "duration": "2:15",
        "year": "2020-01-01",
        "stored_at": "music/nightcore-the-perfect-girl.mp3",
        "additional_info": "versione Nightcore – originale di Mareux (2015)",
        "performer": "Nightcore (Mareux cover)",
        "author": "Mareux",
        "user_id": 1
    },
    {
        "title": "Never Forget You",
        "duration": "3:33",
        "year": "2015-07-10",
        "stored_at": "music/zara-larsson-never-forget-you.mp3",
        "additional_info": "feat. MNEK, singolo di Zara Larsson",
        "performer": "Zara Larsson & MNEK",
        "author": "Zara Larsson, MNEK",
        "user_id": 1
    },
    {
        "title": "Another Love",
        "duration": "4:10",
        "year": "2012-06-15",
        "stored_at": "music/tom-odell-another-love.mp3",
        "additional_info": "dall’album Long Way Down",
        "performer": "Tom Odell",
        "author": "Tom Odell",
        "user_id": 1
    },
    {
        "title": "Love Me Like You Do",
        "duration": "4:12",
        "year": "2015-01-07",
        "stored_at": "music/ellie-goulding-love-me-like-you-do.mp3",
        "additional_info": "colonna sonora di 50 Sfumature di Grigio",
        "performer": "Ellie Goulding",
        "author": "Ellie Goulding",
        "user_id": 1
    },
    {
        "title": "Lovely",
        "duration": "3:21",
        "year": "2018-04-19",
        "stored_at": "music/billie-eilish-khalid-lovely.mp3",
        "additional_info": "feat. Khalid",
        "performer": "Billie Eilish & Khalid",
        "author": "Billie Eilish, Khalid",
        "user_id": 1
    },
    {
        "title": "Take Me to Church",
        "duration": "4:01",
        "year": "2013-09-13",
        "stored_at": "music/hozier-take-me-to-church.mp3",
        "additional_info": "singolo d’esordio",
        "performer": "Hozier",
        "author": "Hozier",
        "user_id": 1
    },
    {
        "title": "Let Her Go",
        "duration": "4:12",
        "year": "2012-07-24",
        "stored_at": "music/passenger-let-her-go.mp3",
        "additional_info": "dall’album All the Little Lights",
        "performer": "Passenger",
        "author": "Passenger",
        "user_id": 1
    },
    {
        "title": "Unstoppable",
        "duration": "3:37",
        "year": "2016-01-21",
        "stored_at": "music/sia-unstoppable.mp3",
        "additional_info": "dall’album This Is Acting",
        "performer": "Sia",
        "author": "Sia",
        "user_id": 1
    },
    {
        "title": "Arcade",
        "duration": "3:04",
        "year": "2019-03-16",
        "stored_at": "music/duncan-laurence-arcade.mp3",
        "additional_info": "vincitore Eurovision 2019",
        "performer": "Duncan Laurence",
        "author": "Duncan Laurence",
        "user_id": 1
    },
    {
        "title": "Dandelions",
        "duration": "3:54",
        "year": "2017-11-16",
        "stored_at": "music/ruth-b-dandelions.mp3",
        "additional_info": "dall’album Safe Haven",
        "performer": "Ruth B.",
        "author": "Ruth B.",
        "user_id": 1
    },
    
    {
        "title": "Say You Won’t Let Go",
        "duration": "3:31",
        "year": "2016-09-09",
        "stored_at": "music/james-arthur-say-you-wont-let-go.mp3",
        "additional_info": "dall’album Back from the Edge",
        "performer": "James Arthur",
        "author": "James Arthur",
        "user_id": 1
    },
    {
        "title": "Let Me Down Slowly",
        "duration": "2:49",
        "year": "2019-01-08",
        "stored_at": "music/alec-benjamin-let-me-down-slowly.mp3",
        "additional_info": "singolo da Narrated for You",
        "performer": "Alec Benjamin",
        "author": "Alec Benjamin",
        "user_id": 1
    },
    {
        "title": "Heat Waves",
        "duration": "3:59",
        "year": "2020-06-29",
        "stored_at": "music/glass-animals-heat-waves.mp3",
        "additional_info": "dall’album Dreamland",
        "performer": "Glass Animals",
        "author": "Glass Animals",
        "user_id": 1
    },
    {
        "title": "Dance Monkey",
        "duration": "3:29",
        "year": "2019-05-10",
        "stored_at": "music/tones-and-i-dance-monkey.mp3",
        "additional_info": "singolo di successo mondiale",
        "performer": "Tones and I",
        "author": "Tones and I",
        "user_id": 1
    },
    {
        "title": "Shallow",
        "duration": "3:37",
        "year": "2018-09-27",
        "stored_at": "music/lady-gaga-bradley-cooper-shallow.mp3",
        "additional_info": "colonna sonora di A Star Is Born",
        "performer": "Lady Gaga & Bradley Cooper",
        "author": "Lady Gaga, Bradley Cooper",
        "user_id": 1
    },
    {
        "title": "Someone You Loved",
        "duration": "3:02",
        "year": "2018-11-08",
        "stored_at": "music/lewis-capaldi-someone-you-loved.mp3",
        "additional_info": "dall’album Divinely Uninspired to a Hellish Extent",
        "performer": "Lewis Capaldi",
        "author": "Lewis Capaldi",
        "user_id": 1
    },
    {
        "title": "Believer",
        "duration": "3:24",
        "year": "2017-02-01",
        "stored_at": "music/imagine-dragons-believer.mp3",
        "additional_info": "dall’album Evolve",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Thunder",
        "duration": "3:07",
        "year": "2017-04-27",
        "stored_at": "music/imagine-dragons-thunder.mp3",
        "additional_info": "dall’album Evolve",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Whatever It Takes",
        "duration": "3:21",
        "year": "2017-05-08",
        "stored_at": "music/imagine-dragons-whatever-it-takes.mp3",
        "additional_info": "dall’album Evolve",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Natural",
        "duration": "3:09",
        "year": "2018-07-17",
        "stored_at": "music/imagine-dragons-natural.mp3",
        "additional_info": "dall’album Origins",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Bones",
        "duration": "2:45",
        "year": "2022-03-11",
        "stored_at": "music/imagine-dragons-bones.mp3",
        "additional_info": "dall’album Mercury – Act 2",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Enemy",
        "duration": "2:53",
        "year": "2021-10-28",
        "stored_at": "music/imagine-dragons-enemy.mp3",
        "additional_info": "feat. JID – colonna sonora della serie Arcane",
        "performer": "Imagine Dragons & JID",
        "author": "Imagine Dragons, JID",
        "user_id": 1
    },
    {
        "title": "Demons",
        "duration": "2:57",
        "year": "2013-05-07",
        "stored_at": "music/imagine-dragons-demons.mp3",
        "additional_info": "dall’album Night Visions",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "On Top of the World",
        "duration": "3:12",
        "year": "2012-03-13",
        "stored_at": "music/imagine-dragons-on-top-of-the-world.mp3",
        "additional_info": "dall’album Night Visions",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Radioactive",
        "duration": "3:06",
        "year": "2012-04-02",
        "stored_at": "music/imagine-dragons-radioactive.mp3",
        "additional_info": "dall’album Night Visions",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Warriors",
        "duration": "2:50",
        "year": "2014-09-17",
        "stored_at": "music/imagine-dragons-warriors.mp3",
        "additional_info": "realizzata per League of Legends Worlds 2014",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Birds",
        "duration": "3:40",
        "year": "2019-07-03",
        "stored_at": "music/imagine-dragons-birds.mp3",
        "additional_info": "feat. Elisa – dall’album Origins",
        "performer": "Imagine Dragons feat. Elisa",
        "author": "Imagine Dragons, Elisa",
        "user_id": 1
    },
    {
        "title": "Sharks",
        "duration": "3:11",
        "year": "2022-06-24",
        "stored_at": "music/imagine-dragons-sharks.mp3",
        "additional_info": "dall’album Mercury – Act 2",
        "performer": "Imagine Dragons",
        "author": "Imagine Dragons",
        "user_id": 1
    },
    {
        "title": "Waves",
        "duration": "3:47",
        "year": "2014-04-11",
        "stored_at": "music/mr-probz-waves.mp3",
        "additional_info": "hit remixata da Robin Schulz",
        "performer": "Mr. Probz",
        "author": "Mr. Probz",
        "user_id": 1
    },
    {
        "title": "Let’s Love",
        "duration": "3:20",
        "year": "2020-09-11",
        "stored_at": "music/david-guetta-sia-lets-love.mp3",
        "additional_info": "collaborazione tra David Guetta e Sia",
        "performer": "David Guetta & Sia",
        "author": "David Guetta, Sia",
        "user_id": 1
    },
    
    {
        "title": "Flames",
        "duration": "3:15",
        "year": "2018-03-22",
        "location": "music/david-guetta-sia-flames-128-ytshorts.savetube.me.mp3",
        "additional_info": "collaborazione tra David Guetta e Sia",
        "performer": "David Guetta & Sia"
    },
    {
        "title": "Titanium",
        "duration": "4:05",
        "year": "2011-12-09",
        "location": "music/david-guetta-titanium-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sia – dall’album Nothing but the Beat",
        "performer": "David Guetta feat. Sia"
    },
    {
        "title": "She Wolf (Falling to Pieces)",
        "duration": "3:41",
        "year": "2012-08-21",
        "location": "music/david-guetta-shewolf-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sia",
        "performer": "David Guetta feat. Sia"
    },
    {
        "title": "Say My Name",
        "duration": "3:12",
        "year": "2018-10-26",
        "location": "music/david-guetta-say-my-name-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Bebe Rexha & J Balvin",
        "performer": "David Guetta, Bebe Rexha & J Balvin"
    },
    {
        "title": "Dangerous",
        "duration": "3:23",
        "year": "2014-10-06",
        "location": "music/david-guetta-dangerous-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sam Martin",
        "performer": "David Guetta feat. Sam Martin"
    },
    {
        "title": "Play Hard",
        "duration": "3:28",
        "year": "2013-03-15",
        "location": "music/david-guetta-play-hard-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Ne-Yo & Akon",
        "performer": "David Guetta feat. Ne-Yo & Akon"
    },
    {
        "title": "Lovers on the Sun",
        "duration": "3:23",
        "year": "2014-06-30",
        "location": "music/david-guetta-lovers-on-the-sun-128-ytshorts.savetube.me.mp3",
        "additional_info": "feat. Sam Martin",
        "performer": "David Guetta feat. Sam Martin"
    },
    {
        "title": "From The Start",
        "duration": "3:12",
        "year": "2021-02-12",
        "location": "music/laufey-from-the-start-lyrics-yt.savetube.me.mp3",
        "additional_info": "dall’album Everything I Know About Love",
        "performer": "Laufey"
    },
    {
        "title": "Il Filo Rosso",
        "duration": "3:34",
        "year": "2023-03-15",
        "location": "music/alfa-il-filo-rosso-yt.savetube.me.mp3",
        "additional_info": "",
        "performer": "ALFA"
    },
    {
        "title": "Obsidian / Monster",
        "duration": "4:05",
        "year": "2021-07-23",
        "location": "music/adventure-time-distant-lands-obsidian-monster-yt.savetube.me.mp3",
        "additional_info": "feat. Olivia Olson & Half Shy – colonna sonora di Adventure Time: Distant Lands",
        "performer": "Adventure Time"
    },
    {
        "title": "Ain't No Crying",
        "duration": "3:00",
        "year": "2021-01-15",
        "location": "music/derivakat-aint-no-crying-yt.savetube.me.mp3",
        "additional_info": "canzone originale Dream SMP",
        "performer": "Derivakat"
    },
    {
        "title": "Always",
        "duration": "3:18",
        "year": "2020-09-04",
        "location": "music/ashe-always-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "I'm Fine",
        "duration": "3:25",
        "year": "2019-07-12",
        "location": "music/ashe-im-fine-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Love Is Not Enough",
        "duration": "3:12",
        "year": "2020-05-20",
        "location": "music/ashe-love-is-not-enough-yt.savetube.me.mp3",
        "additional_info": "official audio",
        "performer": "Ashe"
    },
    {
        "title": "Moral Of The Story",
        "duration": "2:48",
        "year": "2019-05-10",
        "location": "music/ashe-moral-of-the-story-lyric-video-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Save Myself",
        "duration": "3:15",
        "year": "2020-03-15",
        "location": "music/ashe-save-myself-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "We Get High",
        "duration": "3:10",
        "year": "2021-02-01",
        "location": "music/ashe-we-get-high-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ashe"
    },
    {
        "title": "Voilà",
        "duration": "2:47",
        "year": "2021-02-19",
        "location": "music/barbara-pravi-voila-paroles-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Barbara Pravi"
    },
    {
        "title": "When You Say My Name",
        "duration": "3:04",
        "year": "2020-11-23",
        "location": "music/chandler-leighton-when-you-say-my-name-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Chandler Leighton"
    },
    {
        "title": "Sofia",
        "duration": "2:58",
        "year": "2019-10-03",
        "location": "music/clairo-sofia-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Clairo"
    },
    {
        "title": "I Hear a Symphony",
        "duration": "3:30",
        "year": "2020-07-01",
        "location": "music/cody-fry-i-hear-a-symphony-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Cody Fry"
    },
    {
        "title": "Hate Me",
        "duration": "2:45",
        "year": "2019-11-08",
        "location": "music/ellie-goulding-juice-wrld-hate-me-lyrics-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Ellie Goulding & Juice WRLD"
    },
    {
        "title": "City of Angels",
        "duration": "3:19",
        "year": "2021-04-21",
        "location": "music/em-beihold-city-of-angels-official-audio-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Em Beihold"
    },
    {
        "title": "Cupid",
        "duration": "3:13",
        "year": "2022-02-14",
        "location": "music/fifty-fifty-cupid-official-mv-yt.savetube.me.mp3",
        "additional_info": "video musicale ufficiale",
        "performer": "FIFTY FIFTY"
    },
    {
        "title": "IDGAF",
        "duration": "3:38",
        "year": "2018-03-09",
        "location": "music/idgaf-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Dua Lipa"
    },
    {
        "title": "Die With A Smile",
        "duration": "3:05",
        "year": "2021-08-18",
        "location": "music/lady-gaga-bruno-mars-die-with-a-smile-lyrics-yt.savetube.me.mp3",
        "additional_info": "duetto inedito",
        "performer": "Lady Gaga & Bruno Mars"
    },
    {
        "title": "Diet Mountain Dew",
        "duration": "3:20",
        "year": "2012-12-12",
        "location": "music/lana-del-rey-diet-mountain-dew-lyrics-yt.savetube.me.mp3",
        "additional_info": "dall’album Born to Die",
        "performer": "Lana Del Rey"
    },
    {
        "title": "Happier Than Ever",
        "duration": "4:58",
        "year": "2021-07-30",
        "location": "music/loveless-happier-than-ever-cover-yt.savetube.me.mp3",
        "additional_info": "cover di Billie Eilish",
        "performer": "Loveless"
    },
    {
        "title": "The Alternative",
        "duration": "3:10",
        "year": "2021-05-22",
        "location": "music/lyn-lapid-the-alternative-lyric-video-yt.savetube.me.mp3",
        "additional_info": "singolo",
        "performer": "Alex Sloan / Lyn Lapid"
    }
]

documents = [
    {
        "title": "Moral Of The Story",
        "author": "Ashe",
        "date": "2019-02-14",
        "stored_at": "C:\\Users\\LENOVO\\Desktop\\prj\\I.S\\Code\\server\\db\\storage\\documents\\id_001.pdf",
        "caption": "EP Moral of the Story: Chapter 1; Remix Niall Horan 2020",
        "linked_song": "Moral Of The Story",
    }
]

videos = []

# =========================
# UTILITY
# =========================

def duration_to_seconds(dur):
    if not dur:
        return None
    if isinstance(dur, int):
        return dur
    parts = str(dur).split(":")
    try:
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 1:
            return int(parts[0])
    except Exception:
        pass
    return None

# =========================
# POPULATE FUNCTIONS
# =========================

def fill_user_levels(cnt, cur):
    try:
        for lvl_id, code, desc in user_levels:
            cur.execute("""
                INSERT INTO user_levels (id, code, description)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET code=EXCLUDED.code, description=EXCLUDED.description;
            """, (lvl_id, code, desc))
            #print(f"[INFO] User level {code} inserito/aggiornato")
        cnt.commit()
    except Exception as e:
        cnt.rollback()
        #print(f"[DB ERROR] user_levels: {e}")

def fill_permissions(cnt, cur):
    try:
        for name, desc in permissions:
            cur.execute("""
                INSERT INTO permissions (name, description)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING;
            """, (name, desc))
            #print(f"[INFO] Permission {name} inserita/aggiornata")
        cnt.commit()
    except Exception as e:
        cnt.rollback()
        #print(f"[DB ERROR] permissions: {e}")

def fill_role_permissions(cnt, cur):
    try:
        for lvl_id, perms in role_permissions.items():
            for perm in perms:
                cur.execute("SELECT id FROM permissions WHERE name=%s;", (perm,))
                perm_row = cur.fetchone()
                if not perm_row:
                    #print(f"[WARN] Permission {perm} non trovata.")
                    continue
                perm_id = perm_row[0]

                cur.execute("""
                    INSERT INTO role_permissions (lvl_id, permission_id)
                    VALUES (%s, %s)
                    ON CONFLICT DO NOTHING;
                """, (lvl_id, perm_id))
        cnt.commit()
        #print("[INFO] Role-permissions inserite")
    except Exception as e:
        cnt.rollback()
        #print(f"[DB ERROR] role_permissions: {e}")

def fill_users(cnt, cur):
    try:
        for username, pwd, mail, pic, bday, bio, lvl_id in users:
            password_hash = hash_pswd(pwd)
            try:
                birthday = datetime.datetime.strptime(bday, "%Y-%m-%d").date()
            except Exception:
                birthday = None

            cur.execute("""
                INSERT INTO users (mail, username, password_hash, birthday, bio, profile_pic, lvl_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (mail) DO UPDATE SET
                    username=EXCLUDED.username,
                    password_hash=EXCLUDED.password_hash,
                    birthday=EXCLUDED.birthday,
                    bio=EXCLUDED.bio,
                    profile_pic=EXCLUDED.profile_pic,
                    lvl_id=EXCLUDED.lvl_id;
            """, (mail, username, password_hash, birthday, bio, pic, lvl_id))
            #print(f"[INFO] User {username} inserito/aggiornato")
        cnt.commit()
    except Exception as e:
        cnt.rollback()
        #print(f"[DB ERROR] users: {e}")

media_list = songs + videos + documents

def fill_media(cnt, cur):
    """
    Popola la tabella media e relative tabelle collegate.
    Ritorna la lista degli ID creati.
    """
    # Assicurati che le liste siano valide
    media_list = []
    for lst in [songs, videos, documents]:
        if lst:
            media_list.extend(lst)

    if not media_list:
        debug("[WARN] Nessun media da inserire")
        return []

    created_ids = []

    try:
        for s in media_list:
            title = s.get("title")
            year = int(str(s.get("year"))[:4]) if s.get("year") else None
            duration = duration_to_seconds(s.get("duration"))
            stored_at = s.get("stored_at")
            info = s.get("additional_info")
            user_id = s.get("user_id")
            media_type = s.get("type", "song")  # default 'song'

            # Inserisci media
            cur.execute("""
                INSERT INTO media (
                        type, user_id, title, year, duration,
                        stored_at, additional_info, is_author, is_performer)
                VALUES (%s, %s, %s, %s, %s, %s, %s, FALSE, FALSE)
                RETURNING id;
            """, (media_type, user_id, title, year, duration, stored_at, info))

            row = cur.fetchone()
            if row is None:
                debug(f"[ERROR] Media '{title}' non inserito!")
                continue

            media_id = row[0]
            created_ids.append(media_id)
            debug(f"[DB][CREATE] media_id={media_id}")

            # --- AUTHORS ---
            for author_id in s.get("authors", []):
                cur.execute("""
                    INSERT INTO media_authors (media_id, author_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, author_id))
                debug(f"[DB][AUTHOR] linked {author_id}")

            # --- PERFORMERS ---
            for performer_id in s.get("performers", []):
                cur.execute("""
                    INSERT INTO media_performances (media_id, performer_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, performer_id))
                debug(f"[DB][PERF] linked {performer_id}")

            # --- GENRES ---
            for genre_id in s.get("genres", []):
                cur.execute("""
                    INSERT INTO media_genres (media_id, genre_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, genre_id))
                debug(f"[DB][GENRE] linked {genre_id}")

            # --- REFERENCES ---
            for ref_id in s.get("references", []):
                cur.execute("""
                    INSERT INTO media_references (active_id, passive_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, ref_id))
                debug(f"[DB][REF] linked {ref_id}")

            # --- DOCUMENTI ---
            if media_type == "document":
                cur.execute("""
                    INSERT INTO documents (media_id, format, pages, caption)
                    VALUES (%s,%s,%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (
                    media_id,
                    s.get("format"),
                    s.get("pages"),
                    s.get("caption"),
                ))
                debug(f"[DB][DOC] document for media_id={media_id}")

        cnt.commit()
        debug(f"[INFO] Popolamento media completato, {len(created_ids)} record inseriti.")
        return created_ids

    except Exception as e:
        if cnt.closed == 0:
            cnt.rollback()
        debug(f"[ERROR][create_media_db] {e}")
        return []

# last line