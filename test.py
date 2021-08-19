from mdapi import chapter

manga_data = {
    'manga': 'c086153a-0162-412a-9914-a7b2633d0cd3',
    'translatedLanguage[]': ['en']
}

chapter = chapter.Chapter(**manga_data).get_chapters()

print(chapter)