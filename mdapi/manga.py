from mdapi import connector

class Manga():
    def __init__(self, language, **fields):
        self.language = language
        self.fields = fields

    def get_mango(self):
        mango = connector.Connect('manga', **self.fields).get_data()
        data = []
        for manga in mango['results']:
            mango_array = {
                "id": manga['data']['id'],
                "type": manga['data']['type'],
                "title": manga['data']['attributes']['title'][self.language],
                "altTitles": manga['data']['attributes']['altTitles'],
                "description": manga['data']['attributes']['description'][self.language],
                "originalLanguage": manga['data']['attributes']['originalLanguage'],
                "lastVolume": manga['data']['attributes']['lastVolume'],
                "lastChapter": manga['data']['attributes']['lastChapter'],
                "publicationDemographic": manga['data']['attributes']['publicationDemographic'],
                "status": manga['data']['attributes']['status'],
                "year": manga['data']['attributes']['year'],
                "contentRating": manga['data']['attributes']['contentRating']
            }
            data.append(mango_array)
        return data