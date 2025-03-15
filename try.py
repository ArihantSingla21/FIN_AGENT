from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai and a joke about ai"}
  ]
)

print(completion.choices[0].message);
