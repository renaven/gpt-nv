from nv import nv_grab, gpt_query
from time import sleep
import json

with open('in.txt') as file:
    lines = [line.rstrip() for line in file]

with open('config.json') as config_file:
    config = json.load(config_file)
    prefix = config['prompt']
    oai_key = config['api_key']
    if config['gpt_4'] == 'true':
        model_key = 'gpt-4'
    else:
        model_key = 'gpt-3.5-turbo'

count = 1
for url in lines:
    print(url)
    article = nv_grab(url)
    query = article['head']

    for p in article['body']:
        query = query + '\n' + p

    result = gpt_query(prefix, query, oai_key, model_key)

    with open(str(count)+'.txt', 'w', encoding='utf-8') as f:
        for l in result:
            f.write(l)
        f.write('\n\n' + url + '\n\n')
        f.write(article['head'] + '\n')
        for p in article['body']:
            f.write(p + '\n')
    count = count + 1
    sleep(4)
