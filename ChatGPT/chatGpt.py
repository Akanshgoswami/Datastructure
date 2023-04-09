import openai

openai.api_key = "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"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[

            {
                "role": "user",
                "content": "Why should DevOps engineer learn kubernetes?"
            },
        ]
)
result = ''
# print(response)
for choice in response.choices:
    result += choice.message.content

print(result)