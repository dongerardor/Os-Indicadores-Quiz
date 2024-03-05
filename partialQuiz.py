import random
from question import Question
from config import Config

class PartialQuiz():
    def __init__(self, quiz):
        self.id = quiz.id if quiz is not None else None
        self.title = quiz.title if quiz is not None else None
        self.questions_subset = random.sample(quiz.questions, Config.NUMBER_OF_QUESTIONS)
        self.selected_question = None
        self.questions = []

        for question in self.questions_subset:
            self.questions.append(Question(question))

        self.cursor = 0

    def getTotalQuestions(self):
        return len(self.questions)
    
    def getQuestion(self):
        return self.questions[self.cursor]
    
    def getCursor(self):
        return self.cursor
    
    def setCursor(self, cursor):
        self.cursor = cursor
        
    def setCursorNext(self):
        if self.cursor < len(self.questions):
            self.cursor += 1
            return self.cursor
        
    def getScore(self):
        score = 0
        for question in self.questions:
            if question.checkAnswer():
                score += 1
        return f'You scored {score} out of {len(self.questions)}'
    
    def quizCompleted(self):
        for question in self.questions:
            if not question.isAnswered():
                return False
        
        return True
    