from question_model import Question
from data import question_data
from quiz import Quiz

question_bank = []

for question in question_data:
    question_bank.append(Question(question_text=question["text"],
                                  question_answer=question["answer"]))

# for question in question_bank:
#     question.__str__()

quiz = Quiz(question_bank)

while quiz.has_questions():
    quiz.next_question()

quiz.finish_game()
