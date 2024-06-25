import subprocess

# Run main.py and wait for it to complete
subprocess.run(["python3", "main.py"])
subprocess.run(["python3", "chatgpt_project_summarizer.py"])
subprocess.run(["python3", "final_idea_helper.py"])

# This line will only execute after main.py has finished running
print("finished")