from openai import OpenAI
from dotenv import dotenv_values
import datetime

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

job = client.fine_tuning.jobs.retrieve("ftjob-qN643v6nNOd8cDoMWv8tya2X")
print(job.fine_tuned_model)
