from openai import OpenAI
 
# pip install openai 

client = OpenAI(
  api_key="<Your Key Here>",
)
user_question =input("enter your question ,(ask me any thing )")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": user_question}
  ]
)

print(completion.choices[0].message.content)
