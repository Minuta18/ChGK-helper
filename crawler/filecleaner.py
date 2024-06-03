import os
os.chdir("crawler")
os.replace("tempfiles/result/result.json", "result.json")
os.remove("tempfiles")
