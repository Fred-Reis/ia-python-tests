from openai import OpenAI


client = OpenAI(api_key="")

response = client.images.generate(
    model="dall-e-3",
    prompt="Um programador no seu laptop no estilo Simpsons fututrista.",
    n=1,
    size="1024x1024",
    quality="standard",
)

image_url = response.data[0].url

print(image_url)
# print(response.choices[0].message.content)
