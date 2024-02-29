import logging
from openai import OpenAI
import time

from dotenv import dotenv_values


config = dotenv_values(".env")

logging.basicConfig(level=logging.DEBUG)

client = OpenAI(api_key=config["OPENAI_API_KEY"])
file_obj = client.files.create(file=open("data.jsonl", "rb"), purpose="fine-tune")
client.fine_tuning.jobs.create(training_file=file_obj.id, model="gpt-3.5-turbo-0613", hyperparameters={"n_epochs": 2})
jobs = client.fine_tuning.jobs.list(limit=2)

training_file = client.files.create(file=open("data.jsonl", "rb"), purpose="fine-tune")

training_file = client.files.create(file=open("data.jsonl", "rb"), purpose="fine-tune")

# Wait while the file is processed
status = client.files.retrieve(training_file.id).status
start_time = time.time()
while status != "processed":
    print(f"Status=[{status}]... {time.time() - start_time:.2f}s", end="\r", flush=True)
    time.sleep(5)
    status = client.files.retrieve(training_file.id).status
print(f"File {training_file.id} ready after {time.time() - start_time:.2f} seconds.")

job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model="gpt-3.5-turbo",
)

# It may take 10-20+ minutes to complete training.
status = client.fine_tuning.jobs.retrieve(job.id).status
start_time = time.time()
while status != "succeeded":
    print(f"Status=[{status}]... {time.time() - start_time:.2f}s", end="\r", flush=True)
    time.sleep(5)
    job = client.fine_tuning.jobs.retrieve(job.id)
    status = job.status

print(job.fine_tuned_model)