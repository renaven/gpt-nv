from nv import nv_grab, gpt_query
from time import sleep

with open('in.txt') as file:
    lines = [line.rstrip() for line in file]

count = 1
for url in lines:
    print(url)
    article = nv_grab(url)
    query = article['head']

    for p in article['body']:
        query = query + '\n' + p

    prefix = "I need you to translate a news article from Ukrainian into English, and then edit it in accordance with the AP Style Guide, prioritizing clarity and readability. Here is the article, beginning with the title: "

    result = gpt_query(prefix, query)

    with open(str(count)+'.txt', 'w', encoding='utf-8') as f:
        for l in result:
            f.write(l)
        f.write('\n\n' + url + '\n\n')
        f.write(article['head'] + '\n')
        for p in article['body']:
            f.write(p + '\n')
    count = count + 1
    sleep(4)
