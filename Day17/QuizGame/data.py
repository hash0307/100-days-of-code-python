# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

import requests

question_data = []

# Make a GET API call
response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
# Response content as json
# print(response.json())

if response.status_code == 200:
    for result in response.json()['results']:
        response_question = result['question']
        response_answer = result['correct_answer']

        question_item = {'text': response_question, 'answer': response_answer}
        question_data.append(question_item)
    print("Request successful. Your questions for the Quiz are ready.")
else:
    print(f"Request failed with status code: {response.status_code}")

# print(question_data)
