import openai

openai.api_key_path = "openai_key"

prompt = "Write a one liner tagline for a tech-based company"


response = openai.Completion.create(
    engine = "text-davinci-002",
    prompt=prompt,
    temperature=0.4,
    max_tokens=64
)

print(response)