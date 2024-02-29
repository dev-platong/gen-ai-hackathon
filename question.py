import logging
from langchain_openai import ChatOpenAI
from dotenv import dotenv_values
from openai import OpenAI

logging.basicConfig(level=logging.DEBUG)

config = dotenv_values(".env")

model_name = "ft:gpt-3.5-turbo-0613:personal::8xVOcOuR"
client = OpenAI(api_key=config["OPENAI_API_KEY"])

message = "藤井聡太と羽生善治の大局の戦型予想をしてください。得意な戦型について考えた上で"

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message},
    ],
)

print(response)