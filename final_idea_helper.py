import os
from openai import OpenAI
from dotenv import load_dotenv 
import time


summary_files = []
for summary_name in os.listdir("summaries"):
    summary = os.path.join("summaries", summary_name)
    if os.path.isfile(summary):  # Check if it's a file instead of a directory
        summary_files.append(summary)
#print(summary_files)



directory = "summaries"

summary_info = [{"role": "system", "content": 
                 "Review the summaries of my repositiories and provide a list of possible additions that can be made, and other project ideas using similar skillsets."
                 },]

choice = input("The current prompt is: | " + str(summary_info[0]['content']) + " |  Would you like to change it? (y/n): ")
choice = "n"
if choice == "y":
    new_prompt = input("Enter the new prompt: ")
    summary_info[0]['content'] = new_prompt


for file_name in os.listdir(directory):
        file = os.path.join(directory, file_name)
        if os.path.isfile(file):
            file_extension = os.path.splitext(file_name)[1]
            
                
                
            with open(file, 'r') as f:
                
                summary_info.append({"role": "user", "content": f"File Name: {file_name}, Contents: {f.read()}"})






load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    organization=os.getenv("ORGANIZATION"),
    project=os.getenv("PROJECT"),
)

response = client.chat.completions.create(
        model="gpt-4o",
        messages=summary_info,
    )
for _ in range(1000):
    print("\n")
print(response)
time.sleep(10)
print("\n\n\n\n")
print(response.choices[0].message.content)
print("\n\n\n\n")
prompt_tokens = response.usage.prompt_tokens
response_tokens = response.usage.completion_tokens
print("Price: ", (((prompt_tokens/1000)*0.005) + ((response_tokens/1000)*0.015)))