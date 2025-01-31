import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint="https://multiagentsystem.openai.azure.com/"
)

# This will correspond to the custom name you chose for your deployment when you deployed a model.
# Use a gpt-35-turbo-instruct deployment.
deployment_name = "gpt35turbo"

# Send a completion call to generate an answer
prompt = ""
response = client.completions.create(
    model=deployment_name,
    prompt=prompt,
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(prompt + response.choices[0].text)
