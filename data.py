import requests


def fetch_trivia_data(amount=10, difficulty='easy', question_type='boolean'):
    url = f'https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={question_type}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'A problem occurred when trying to fetch the data. Status Code: {response.status_code}')
        return None


trivia_data = fetch_trivia_data()

question_data = []

if trivia_data:
    print(f"text: {trivia_data['results'][0]['question']}\nanswer: {trivia_data['results'][0]['correct_answer']}")
    for result in trivia_data['results']:
        question_data.append({"text": result['question'], "answer": result['correct_answer'].lower()})

print(question_data)

