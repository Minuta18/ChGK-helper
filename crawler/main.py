import requests
import bs4

def get_links_page(page: int = 1) -> str:
    response = requests.get(f'https://db.chgk.info/last?page={ page }')
    if response.status_code != 200:
        return ValueError('Invalid page')
    return response.text

def get_questions_page(page_uuid: str) -> str:
    response = requests.get(f'https://db.chgk.info/tour/{ page_uuid }')
    if response.status_code != 200:
        return ValueError('Invalid page')
    return response.text

class Question:
    text: str
    answer: str
    comment: str
    source: str
    author: str

def parse_page(page: str) -> list[str]:
    soup = bs4.BeautifulSoup(page, 'html.parser')
    links = soup.find('table', class_='last_packages')
    questions = list()
    for link in links.find_all('a', href=True):
        if '/tour/' in link['href']:
            questions.append(link['href'][6:])
    return questions

def search(where, what):
    try:
        return [i.text for i in where if 
            f'class="{ what }"' in i.__repr__()][0]
    except IndexError:
        return ''

def parse_questions_page(page: str) -> list[Question]:
    soup = bs4.BeautifulSoup(page, 'html.parser')
    questions = list()
    for question in soup.find_all('div', class_='question'):
        question_ = Question()
        question_.text = (
            ' '.join(question.find('p').text.split(':')[1:])
        ).removeprefix(' ')
        
        attrs = question.find(
            'div', class_='collapsible collapsed'
        ).find_all('p')
        
        question_.answer = search(attrs, 'Answer')
        question_.comment = search(attrs, 'Comments')
        question_.source = search(attrs, 'Sources')
        question_.author = search(attrs, 'Authors')

        print('[New question] Text: {}\n    Answer: {}\n    Comment: {}\n    Source: {}\n    Author: {}\n'.format(
            question_.text,
            question_.answer, 
            question_.comment,
            question_.source,
            question_.author,
        ))

        questions.append(question_)
    return questions

def send_question_to_db(q: Question):
    response = requests.post('http://127.0.0.1:5000/api/v1/questions/', 
        headers={
            'Content-Type': 'application/json',
            'Authorization': '5HanMEv0vIbnz9mSXpAnMlIxKlPnoGxYiAdr9UsAQNyc1yZFMpTt3QWsLGL8saX0nG--eRGxrBhnn5YLmJr9eY4Q526YjDx-RvMyqY1RMTnomRii-1y3WrJwruguNOYuBKAKAbVq1ZLaMq7F8LVx_FV-UYOSJwqnkIDhVpcYyjwYd9SGsLcctO_5wkew-Z_nqPbKqktB',
    }, json={
        'text': q.text,
        'comment': q.comment,
    })
    if response.status_code != 201:
        print(f'[Uploaded question] Error: {response.status_code}')
    elif response.json().get('error', True):
        print(f'[Uploaded question] Error: {response.json().get("detail", "")}')
    else:
        print(f'[Uploaded question] Success')

    response2 = requests.post('http://127.0.0.1:5000/api/v1/answer/',
        headers={
            'Content-Type': 'application/json',
            'Authorization': '5HanMEv0vIbnz9mSXpAnMlIxKlPnoGxYiAdr9UsAQNyc1yZFMpTt3QWsLGL8saX0nG--eRGxrBhnn5YLmJr9eY4Q526YjDx-RvMyqY1RMTnomRii-1y3WrJwruguNOYuBKAKAbVq1ZLaMq7F8LVx_FV-UYOSJwqnkIDhVpcYyjwYd9SGsLcctO_5wkew-Z_nqPbKqktB',
        }, json={
            'question_id': response.json().get('id', 0),
            'correct_answer': q.answer,
        }
    )
    if response2.status_code != 201:
        print(f'[Uploaded answer] Error uploading answer: { response2.status_code }')
    elif response2.json().get('error', True):
        print(f'[Uploaded answer] Error uploading answer: { response2.json().get("detail", "") }')
    else:
        print(f'[Uploaded answer] Success')

if __name__ == '__main__':
    for i in range(1, 101):
        try:
            page = get_links_page(i)
            question_links = parse_page(page)
            for link in question_links[:1]:
                quest_page = get_questions_page(link)
                questions = parse_questions_page(quest_page)
                for q in questions:
                    send_question_to_db(q)
        except Exception as e:
            print(f'[Error] { e }')