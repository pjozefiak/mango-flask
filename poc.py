import requests, math

def search_manga(title):
    endpoint = 'https://api.mangadex.org/manga'
    manga_data = {
        'originalLanguage[]': ['ja'],
        'title': title
    }

    manga_list = requests.get(endpoint, params=manga_data)

    manga_array = []

    for manga in manga_list.json()['results']:
        result = {
            'id': manga['data']['id'],
            'title': manga['data']['attributes']['title']['en'],
            'status': manga['data']['attributes']['status']
        }
        manga_array.append(result)

    return manga_array

def get_chapters(manga_id):
    endpoint = 'https://api.mangadex.org/chapter'
    manga_data = {
        'manga': manga_id,
        'translatedLanguage[]': ['en'],
    }
    chapter_list = requests.get(endpoint, params=manga_data)
    total_chapters = chapter_list.json()['total']
    pagination = math.floor(total_chapters / 100)
    pagination_last = total_chapters % 100
    chapter_data = []
    page = 0
    while page < pagination:
        page_data = {
            'manga': manga_id,
            'translatedLanguage[]': ['en'],
            'offset': page * 100,
            'limit': 100
        }
        page_dump = requests.get(endpoint, params=page_data).json()
        for chapters_page in page_dump['results']:
            chapter_array = {
                'id': chapters_page['data']['id'],
                'title': chapters_page['data']['attributes']['title'],
                'hash': chapters_page['data']['attributes']['hash'],
                'page_data': chapters_page['data']['attributes']['data']
            }
            try:
                if float(chapters_page['data']['attributes']['chapter']) % 1 == 0:
                    chapter_array['chapter'] = int(chapters_page['data']['attributes']['chapter'])
                else:
                    chapter_array['chapter'] = float(chapters_page['data']['attributes']['chapter'])
            except TypeError:
                chapter_array['chapter'] = 000
            chapter_data.append(chapter_array)
        page += 1
    last_page_data = {
        'manga': manga_id,
        'translatedLanguage[]': ['en'],
        'offset': page * 100,
        'limit': pagination_last
    }

    #duplicated code to be refractored

    last_page_dump = requests.get(endpoint, params=last_page_data).json()
    for chapters_page in last_page_dump['results']:
        chapter_array = {
            'id': chapters_page['data']['id'],
            'title': chapters_page['data']['attributes']['title'],
            'hash': chapters_page['data']['attributes']['hash'],
            'page_data': chapters_page['data']['attributes']['data']
        }
        try:
            if float(chapters_page['data']['attributes']['chapter']) % 1 == 0:
                chapter_array['chapter'] = int(chapters_page['data']['attributes']['chapter'])
            else:
                chapter_array['chapter'] = float(chapters_page['data']['attributes']['chapter'])
        except TypeError:
            chapter_array['chapter'] = 000
        chapter_data.append(chapter_array)
    return sorted(chapter_data, key=lambda k: k['chapter'])

def get_athome_url(chapter):
    endpoint = 'https://api.mangadex.org/at-home/server/{}'.format(chapter)
    url_data = requests.get(endpoint)
    return url_data.json()['baseUrl']

def get_pages(chapter):
    endpoint = 'https://api.mangadex.org/chapter/{}'.format(chapter)
    chapter_data = requests.get(endpoint)
    chapter_array = {
        'hash': chapter_data.json()['data']['attributes']['hash'],
        'page_data': chapter_data.json()['data']['attributes']['data']
    }
    return chapter_array