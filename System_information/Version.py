import re

print("Changing the version in text file")

filename = "../venv/version.txt"
with open (filename,"r+") as file:
    text = file.read()
with open(filename,"w")as file:
    text = re.sub("1.1","1.2",text)
    file.write(text)
