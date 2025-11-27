from openai import OpenAI


client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Me fale sobre as epistolas de Paulo na Bíblia."}
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# print(response.choices[0].message.content)
