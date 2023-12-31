class Question:

    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer

    def __str__(self):
        print(f"Q:{self.text} A:{self.answer}")
