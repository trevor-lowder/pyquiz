class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = (input(f"Q.{self.question_number}: {current_question.text} Enter 'T' for True or 'F' for False:\n")
                    .lower())
        self.check_answer(response, current_question.answer)

    def check_answer(self, response, answer):
        if response == answer.lower():
            self.score += 1
            print(f"You got it! Current score: {self.score}/{self.question_number}")
        else:
            print(f"That's not right... Current score: {self.score}/{self.question_number}")

    def finish_game(self):
        print(f"Thanks for playing!\nFinal Score: {self.score}/{len(self.question_list)}")
