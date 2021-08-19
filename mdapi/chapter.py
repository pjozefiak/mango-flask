from mdapi import connector, helpers

class Chapter():
    def __init__(self, **fields):
        self.fields = fields

    def get_chapters(self):
        chapters = connector.Connect('chapter', **self.fields).get_data()
        total_chapters = chapters['total']
        chapters_pagination = helpers.paginate_chapters(total_chapters)
        return chapters_pagination