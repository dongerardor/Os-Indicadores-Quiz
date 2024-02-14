import random
from question import Question

class Quiz:
    def __init__(self, quiz):
        self.id = quiz['id']
        self.questions_subset = random.sample(quiz['quiz'], 10)
        self.questions = []
        self.title = quiz['title']
        self.selected_question = None

        for question in self.questions_subset:
            self.questions.append(Question(question))

        self.question_id_list = [question.id for question in self.questions]
        self.cursor = -1

    def getCursor(self):
        return self.cursor
    
    def getTotalQuestions(self):
        return len(self.questions)
    
    def getQuestion(self):
        return self.questions[self.cursor]
        
    def getNextQuestion(self):
        if self.cursor < len(self.questions):
            self.cursor += 1
            return self.getQuestion()
        else:
            return None
        
    def getScore(self):
        score = 0
        for question in self.questions:
            if question.checkAnswer():
                score += 1
        return f'You scored {score} out of {len(self.questions)}'