import math

def paginate_chapters(total_chapters):
    pagination = math.floor(total_chapters / 100)
    pagination_last = total_chapters % 100
    return {
        'pagination': pagination,
        'pagination_last': pagination_last
    }

def chapter_array(chapters_list):
    for chapter_page in chapters_list['results']:
        chapter_data = {
            'id': chapter_page['data']['id'],
            'title': chapter_page['data']['attributes']['title'],
            'hash': chapter_page['data']['attributes']['hash'],
            'page_data': chapter_page['data']['attributes']['data'],
            'scanlation_group': chapter_page['relationships'][0]["id"]
        }
        try:
            if float(chapter_page['data']['attributes']['chapter']) % 1 == 0:
                chapter_data['chapter'] = int(chapter_page['data']['attributes']['chapter'])
            else:
                chapter_data['chapter'] = float(chapter_page['data']['attributes']['chapter'])
        except TypeError:
            chapter_data['chapter'] = 000
    return chapter_data