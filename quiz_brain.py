import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.user_answer_is: bool = True
        self.text = []

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.text = html.unescape(self.current_question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {self.text} (True/False): "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.user_answer_is = True
        else:
            self.user_answer_is = False
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
