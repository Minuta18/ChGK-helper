from os import startfile, chdir
from json import dump
import bs4 as bs  # beautiful soup 4
chdir("crawler")

rawquestions = []
with open('tempfiles/result/raw_result.txt', 'br') as rq:  # raw questions, not request
    rawquestions = rq.read().decode().split("#elementend#")
#
questions = []
for i in rawquestions:
    question = {"question": "", "answer": [], "comment": "", "img": ""}
    PSi = bs.BeautifulSoup(i, 'html.parser')  # parsed i
    # searching for the question
    strongquestion = [str(s) for s in PSi.select("strong.Question")][0]
    question["question"] = i[
        (i.find(strongquestion) + len(strongquestion) + 1):
        i[i.find(strongquestion):].find("</p>") + i.find(strongquestion)]
    q_sp = 2
    while (' '*q_sp in question["question"]):
        question["question"] = question["question"].replace(' '*q_sp, '')
    # searching for the answer
    stronganswer = [str(s) for s in PSi.select("strong.Answer")][0]
    question["answer"] = i[
        (i.find(stronganswer) + len(stronganswer) + 1):
        i[i.find(stronganswer):].find("</p>") + i.find(stronganswer)].split(" или ")
    for j in range(len(question["answer"])):
        a_sp = 2
        while (' '*a_sp in question["answer"][j]):
            question["answer"][j] = question["answer"][j].replace(' '*a_sp, '')
    # searching for the comment
    if (len(PSi.select("strong.Comments")) > 0):
        strongcomment = [str(s) for s in PSi.select("strong.Comments")][0]
        question["comment"] = i[
            (i.find(strongcomment) + len(strongcomment) + 1):
            i[i.find(strongcomment):].find("</p>") + i.find(strongcomment)]
        c_sp = 2
        while (' '*c_sp in question["comment"]):
            question["comment"] = question["comment"].replace(' '*c_sp, '')
    else:
        question["comment"] == "#NoComment#"
    print(question)
    questions.append(question)
#
with open("tempfiles/result/result.json", 'w') as res:
    dump(questions, res)
#
startfile('filecleaner.py')
