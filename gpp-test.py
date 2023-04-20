import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": "Can you edit a news article for clarity and readbility, confroming with AP style gyuide?"},
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
