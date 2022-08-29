
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import pandas as pd
import yake
from functools import reduce


def create_content():

    query = input("Type your search: ")

    urls = [j for j in search(query, tld="co.in", num=10, stop=10, pause=2)
            if not j.startswith(('https://towardsdatascience.com/', 'https://stackoverflow.com/'))]

    contents = []

    html_string = '''
    <html>
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <body>
    <h1> Search results for Linkedin Content Creation </h1>

        {table}
    </body>
    </html>.
    '''

    for url in urls:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for title in soup.find_all('h1'):
            chapters = ['* ' + chapter.get_text() +
                        '----' for chapter in soup.find_all('h2')]
            kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
            keywords = [['#' + h for h in kw.split(" ")] for kw, v in kw_extractor.extract_keywords(
                " ".join(chapters))]
            hashtags = reduce(lambda xs, ys: xs + ys, keywords)
            contents.append({
                'url': '<a target="_blank" href="{0}">{0}</a>'.format(url),
                'title': title.get_text(),
                'chapters': chapters,
                'hashtags': " ".join(hashtags)
            })

    df = pd.DataFrame(data=contents)
    # convert into html
    # OUTPUT AN HTML FILE
    with open('index.html', 'w') as f:
        f.write(html_string.format(table=df.to_html(
            render_links=True, escape=False, classes='mystyle')))
