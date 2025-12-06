from openai import OpenAI


client = OpenAI(api_key="")

response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input="Olá, seja bem-vindo ao mundo da inteligência artificial com OpenAI!",
)

response.write_to_file("my_audio.mp3")
