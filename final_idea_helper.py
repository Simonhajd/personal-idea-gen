import os
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
if choice == "y":
    new_prompt = input("Enter the new prompt: ")
    summary_info[0]['content'] = new_prompt


for file_name in os.listdir(directory):
        file = os.path.join(directory, file_name)
        if os.path.isfile(file):
            file_extension = os.path.splitext(file_name)[1]
            
                
                
            with open(file, 'r') as f:
                print("\n\n MESSAGE APPENDED \n\n")
                summary_info.append({"role": "user", "content": f"File Name: {file_name}, Contents: {f.read()}"})

print(summary_info)