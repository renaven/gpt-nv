from nv import nv_grab, gpt_query
from time import sleep
import json

with open('in.txt') as file:
    lines = [line.rstrip() for line in file]

with open('config.json') as config_file:
    config = json.load(config_file)
    # loading ChatGPT prompt that is sent with every request
    prefix = config['prompt']
    oai_key = config['api_key']  # loading OpeanAI API key
    if config['gpt_4'] == 'true':
        model_key = 'gpt-4'  # switching from default GPT-3.5 to GPT-4
    else:
        model_key = 'gpt-3.5-turbo'

count = 1  # simply keeping track of translated articles to name the output files accordingly
for url in lines:
    print(url)
    # calling a function to get title aand body of a given article
    article = nv_grab(url)
    query = article['head']

    for p in article['body']:  # appending every paraagraph to our eventual translation query
        query = query + '\n' + p

    # calling a function to make the ChatGPT request and return the final result
    result = gpt_query(prefix, query, oai_key, model_key)

    with open(str(count)+'.txt', 'w', encoding='utf-8') as f:
        for l in result:
            f.write(l)
        f.write('\n\n' + url + '\n\n')
        f.write(article['head'] + '\n')
        for p in article['body']:
            f.write(p + '\n')
    count = count + 1
    sleep(4)  # to make sure we don't step over the rate limiting on the OpeanAI API
