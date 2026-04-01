from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []




for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Question(q_text=question_text,q_answer=answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()