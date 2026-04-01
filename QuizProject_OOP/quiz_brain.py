from time import sleep


class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_score = 0
        self.question_list = q_list


    def still_has_questions(self):
        if self.q_number < len(self.question_list):
            return True
        else: return False


    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number} : {current_question.text} (True/False) - ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self,user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.q_score += 1
            print("You got it right!")
            print("\n")

        else:
            print(f"You got it wrong!")
            print(f"The correct answer is : {correct_answer}.")
            print("\n")

        print(f"Your current score is {self.q_score}/{self.q_number}")
