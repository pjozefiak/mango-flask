from mdapi import connector 

class Chapter():
    def __init__(self, **fields):
        self.fields = fields

    def get_chapters(self):
        chapters = connector.Connect('chapter', **self.fields).get_data()
        return chapters