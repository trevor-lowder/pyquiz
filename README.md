# Trivia Quiz Program

This Python program is a simple trivia quiz game that fetches trivia questions from the Open Trivia Database API, presents them to the user, and evaluates their responses. The program is structured into several components:

## Usage

Here's how the game works:

### Initialize a list to store trivia questions:

    ```python
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question_text=question["text"],
                                      question_answer=question["answer"]))
    ```

### Create a `Quiz` object with the question bank:

    ```python
    quiz = Quiz(question_bank)
    ```

### Start the quiz loop:

    ```python
    while quiz.has_questions():
        quiz.next_question()
    ```

### Finish the game and display the final score:

    ```python
    quiz.finish_game()
    ```

## Fetching Trivia Data

The program fetches trivia questions from the Open Trivia Database using the `fetch_trivia_data` function. This function takes parameters for the number of questions, difficulty level, and question type. It returns a JSON object containing the trivia data.

```python
trivia_data = fetch_trivia_data(amount=10, difficulty='easy', question_type='boolean')
```

## Creating Question Objects

Trivia questions obtained from the API are converted into `Question` objects. These objects have a text attribute representing the question and an answer attribute representing the correct answer.

```python
class Question:

    def __init__(self, question_text, question_answer):
        # Initialization code...

    def __str__(self):
        # Prints question text and answer
```

## Running the Quiz

The `Quiz` class manages the quiz logic. It tracks the current question number, the question list, and the player's score. The `has_questions`, `next_question`, `check_answer`, and `finish_game` methods control the flow of the quiz.

```python
class Quiz:

    def __init__(self, q_list):
        # Initialization code...

    def has_questions(self):
        # Check if there are remaining questions...

    def next_question(self):
        # Present the next question...

    def check_answer(self, response, answer):
        # Check the user's answer...

    def finish_game(self):
        # Display the final score...
```

To play the game, run the 'main.py' file in a terminal. Feel free to customize the program or integrate it into other projects. Enjoy playing and learning with this trivia quiz program!
