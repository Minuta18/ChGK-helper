import os
os.chdir("crawler")
os.replace("tempfiles/result/result.json", "result.json")
print("Текущая деректория:", os.getcwd())
os.remove("tempfiles")
