from bs4 import BeautifulSoup
import requests
import re
import unicodedata
import openai


def nv_grab(url):
    clean = re.compile('<.*?>')
    source_url = url
    r = requests.get(source_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for img in soup.find_all("p", {'class': 'article__content__head_img-info'}):
        img.decompose()
    t = soup.find(
        "div", {'class': 'article__content__head__text'}).find_all('h1')
    p = soup.find(
        "div", {'class': 'content_wrapper'}).find_all('p')
    body = []
    for i in p:
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


url = "https://nv.ua/ukr/ukraine/events/v-nasa-sprostuvali-padinnya-suputnika-v-kiyevi-novini-ukrajini-50318987.html"
article = nv_grab(url)

article_full = article['head']

for p in article['body']:
    article_full = article_full + '\n' + p

with open('out.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n' + url + '\n\n')
    f.write(article['head'] + '\n')
    for p in article['body']:
        f.write(p + '\n')
