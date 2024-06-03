import os
# os.mkdir("tempfiles")
print("Текущая деректория:", os.getcwd())
os.chdir("tempfiles")
print("Текущая деректория:", os.getcwd())
os.mkdir("result")
