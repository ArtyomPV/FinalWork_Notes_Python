class Note:
    # user_id = 1
    #
    # def __init__(self, title, message):
    #     self.time = 'time'
    #     self.uid = Note.user_id
    #     Note.user_id += 1
    #     Note.__init__(self, self.uid,  self.time, title, message)
    #     self.title = title
    #     self.message = message

    def __init__(self, uid, time, title, message):
        self.uid = uid
        self.time = time
        self.title = title
        self.message = message

    def __str__(self):
        return f'id: {self.uid}\ntime: {self.time}\ntitle: {self.title}\nmessage: {self.message}'

    def note_to_dict(self):
        dict_note = {'id': str(self.uid), 'time': str(self.time), 'title': self.title, 'message': self.message}
        return dict_note
