import itertools
import json

file_path = './read_raw_data/quiz_raw_data.txt'
prefixes = ["a)", "b)", "c)", "d)"]
quiz_data = []

class Question:
    instance_id = itertools.count()

    def __init__(self, _question):
        if _question:
            self.question = {
                "id": next(Question.instance_id),
                "question": _question,
                "answers": [],
                "correctAnswer": ""
            }

    def addAnswer(self, _answer):
        if _answer:
            self.question['answers'].append(_answer)

    def addCorrectAnswer(self, _correctAnswer):
        if _correctAnswer:
            self.question['correctAnswer'] = _correctAnswer

    def __str__(self):
        return f"id: {self.question['id']}, Q: {self.question['question']}, \
            A: {self.question['answers']}, R: {self.question['correctAnswer']}"
    
    def to_dict(self):
        return self.question
    
# Define una función personalizada para serializar objetos Question a JSON
def question_serializer(obj):
    if isinstance(obj, Question):
        return obj.to_dict()
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')


# if the line starts with a), b), c) or d), it is an answer
def is_answer(text):
    return any(text.startswith(prefix) for prefix in prefixes)


# Open the file in read mode
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process each line as needed
        line = line.strip()  # strip() removes leading and trailing whitespace

        if not is_answer(line):
            question = Question(line)
            quiz_data.append(question)
        else:
            question = quiz_data[-1]
            
            for prefix in prefixes:
                if line.startswith(prefix):
                    line = line.lstrip(prefix).strip()

            if '✅' in line:
               line = line.replace('✅', '').strip()
               question.addCorrectAnswer(line)

            question.addAnswer(line)


def write_file(list, filename):
    with open(filename, 'w') as file:
        for item in list:
            file.write(str(item) + '\n\n\n\n')

def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, default=question_serializer, indent=4)

# Ejemplo de uso
filename = 'quiz_data.json'

write_json(quiz_data, filename)
