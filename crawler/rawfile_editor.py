from os import startfile, chdir
from json import load, dump
chdir("crawler")

rawquestions = []
with open('tempfiles/result/raw_result.json', 'r') as rq:  # raw questions, not request
    rawquestions = load(rq)
print(rawquestions)
