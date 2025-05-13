# obj nota

import json as J
#note_details è "notes details.json"

class note:
    def __init__(self, id, user_data, file_data, note_data):
        self.id = id
        self.user_data = user_data
        self.file_data = file_data
        self.note_data = note_data