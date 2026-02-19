from openai import OpenAI

client = OpenAI(api_key="sk-your-api-key")

prompt = input("Prompt: ")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)