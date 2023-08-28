from bs4 import BeautifulSoup
import requests
import re
import unicodedata
import openai


def nv_grab(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    cookies = {'CONSENT': "YES+"}
    clean = re.compile('<.*?>')
    r = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')

    for read_also_li in soup.find_all(
            'ul', {'class': 'media__also__news_links__list'}):
        read_also_li.decompose()

    for img in soup.find_all("p", {'class': 'article__content__head_img-info'}):
        img.decompose()

    try:
        t = soup.find(
            "div", {'class': 'article__content__head__text'}).find_all('h1')
    except:
        t = soup.find(
            "div", {'class': 'article-content-body'}).find_all('h1')

    p = soup.find(
        "div", {'class': 'content_wrapper'}).find_all(['p', 'li'])
    body = []
    for i in p:  # I had no patience to properly filter out these two tags, so skipping them is just hardocded here
        if 'Відео дня' in str(i):
            continue
        if 'Теги' in str(i):
            continue
        raw_para = unicodedata.normalize('NFKD', str(i))
        body.append(re.sub(clean, '', raw_para))
    t2 = unicodedata.normalize('NFKD', str(t[0]))
    title = re.sub(clean, '', t2)
    content = {'head': title, 'body': body}
    return (content)


def gpt_query(prefix, query, oai_key, model_key):
    openai.api_key = oai_key
    response = openai.ChatCompletion.create(
        model=model_key,
        messages=[
            {"role": "system", "content": "You are a news editor's assistant"},
            {"role": "user", "content": prefix + query},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return (result)
