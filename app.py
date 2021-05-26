from flask import Flask, render_template, request
import poc

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/manga', methods=['POST', 'GET'])
def manga_search():
    if request.method == 'POST':
        manga_query = request.form['manga']
        manga_data = poc.search_manga(manga_query)
        return render_template('manga_search.html', manga_data=manga_data)

@app.route('/manga/<manga_id>')
def get_chapters(manga_id):
    chapter_data = poc.get_chapters(manga_id)
    return render_template('chapter_list.html', chapter_data=chapter_data, manga_id=manga_id)

@app.route('/manga/<manga_id>/chapter/<chapter_id>')
def get_pages(manga_id, chapter_id):
    at_home_url = poc.get_athome_url(chapter_id)
    pages = poc.get_pages(chapter_id)
    return render_template('pages_list.html', pages=pages, at_home_url=at_home_url)


if __name__ == '__main__':
    app.run()
