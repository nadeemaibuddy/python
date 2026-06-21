word="python"
with open("log.txt") as f:
    content=f.read()
if word in content:
    print("this log file contain python")
else:
    print("this log file dont contain python")
