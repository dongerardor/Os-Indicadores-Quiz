import random
from config import Config

class Question:
    def __init__(self, question):
        self.id = question['id']
        self.question = question['question'] 
        self.answers = question['answers']
        self.correct_answer = question['correctAnswer']
        self.answer_selected = None

    def getAnswers(self):
        return self.answers if not Config.SHUFFLE_ANSWERS \
            else random.sample(self.answers, len(self.answers))
        
    def getQuestion(self):
        return self.question
    
    def getCorrectAnswer(self):
        return self.correct_answer
    
    def getAnswerSelected(self):
        return self.answer_selected
    
    def setAnswerSelected(self, answer_selected):
        self.answer_selected = answer_selected
        return self.answer_selected
    
    def checkAnswer(self):
        return self.answer_selected == self.correct_answer
    
    def isAnswered(self):
        return self.answer_selected is not None