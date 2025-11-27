from openai import OpenAI


client = OpenAI(api_key="")

audio_file = open("audio.mp3", "rb")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text",
    language="pt",
)

print(response)
