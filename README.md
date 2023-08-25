# gpt-nv
Dependancies:

requries two additional Python libraries, OpenAI and BeautifulSoup. Install using the following console commands:

pip install openai
pip install bs4

Config:

must include your OpenAI API key

model - 'false' defaults to GPT-3.5-turbo model, 'true' switches modle to gpt-4

edit the prompt to suit your needs


Flaws and limitations:

on some stories throws up an exception, most often on "LIFE" section stories due to http request returning a 404 code

Input URLs:

paste URLs to UA versions of NV stories in the 'in.txt' file, one url per line, with no separators

output includes transaltion, url to source, and the original text, generated into a series of .txt files named '1-N.txt'
