import os
import time
from openai import OpenAI
import tkinter
from tkinter import messagebox
import os
from dotenv import load_dotenv 
import time

load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    organization=os.getenv("ORGANIZATION"),
    project=os.getenv("PROJECT"),
)

extensions = [
    '.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.css', '.scss', '.sass', '.less',
    '.php', '.rb', '.go', '.java', '.class', '.jar', '.swift', '.m', '.mm', '.h', '.hpp',
    '.c', '.cpp', '.cs', '.fs', '.vb', '.pyd', '.pyo', '.pyc', '.lua', '.pl', '.pm', '.t',
    '.r', '.rs', '.dart', '.jl', '.hs', '.lhs', '.erl', '.ex', '.exs', '.sh', '.bat', '.cmd',
    '.ps1', '.vbs', '.sql', '.xml', '.json', '.yaml', '.yml', '.ini', '.cfg', '.toml', '.md',
    '.rmd', '.tex', '.clj', '.cljs', '.cljc', '.edn'
]

text_extensions = ['.txt', '.md', '.rtf', '.log', '.csv', '.tex', '.nfo', '.ini', '.cfg', '.yaml', '.yml', '.json', '.xml', '.html', '.css', '.js', '.py', '.java', '.c', '.cpp', '.h', '.hpp', '.sh', '.bat', '.cmd', '.ps1', '.vbs', '.sql']




folder_path = 'repos'
folders = []



def chatgpt_summary(i):
    messages = [{"role": "system", "content": "Interpret and summarize the files"},
            

    ]
    for file_name in os.listdir(i):
        file = os.path.join(i, file_name)
        if os.path.isfile(file):
            file_extension = os.path.splitext(file_name)[1]
            if file_extension in text_extensions or file_extension in extensions:
                
                
                with open(file, 'r') as f:
                    #print("\n\n MESSAGE APPENDED \n\n")
                    messages.append({"role": "user", "content": f"File Name: {file_name}, Contents: {f.read()}"})
    return messages
                
    
    
    

for folder_name in os.listdir(folder_path):
    folder = os.path.join(folder_path, folder_name)
    if os.path.isdir(folder):
        folders.append(folder)
#print(folders)

for i in folders:
    proj_name=(i.replace('repos/', ''))
    print(proj_name)
    project_message = chatgpt_summary(i)
    #print(project_message)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=project_message,
    )

    ai_response = response.choices[0].message.content
    
    print("AI: ", ai_response, "\n")
    summary_file_path = os.path.join('summaries', f'summary-{proj_name}.txt')
    with open(summary_file_path, 'w') as summary_file:
        summary_file.write(ai_response)


print("\n\n     -----finished-----      \n\n")