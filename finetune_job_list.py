from openai import OpenAI
from dotenv import dotenv_values
import datetime

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

jobs = client.fine_tuning.jobs.list(limit=10).data

for job in jobs:
    print(job.id)
    print(datetime.datetime.fromtimestamp(job.created_at))