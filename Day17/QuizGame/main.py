from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # print(question)
    # print(question.get("text"))
    question_obj = Question(question.get("text"), question.get("answer"))
    # question["text"] -  will raise a KeyError Exception if key is missing
    # question.get("text") - will not raise a error if key is missing and it will return None (or a default value you can specify)
    question_bank.append(question_obj)

# print(question_bank)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz !!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")