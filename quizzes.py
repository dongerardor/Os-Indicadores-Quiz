import os
from flask import json, current_app as app
from quiz import Quiz
from partialQuiz import PartialQuiz

# Quizzes is a Singleton class
class Quizzes:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.quizzes = None
        self.quiz = None
        self.partial_quiz = None

    def setQuizzes(self):
        quizzes = []
        with app.app_context():
            directory = os.path.join(app.static_folder, 'data')
            for index, filename in enumerate(os.listdir(directory)):
                if os.path.isfile(os.path.join(directory, filename)):
                    with open(os.path.join(directory, filename)) as data_file:
                        data = dict()
                        data['quiz'] = json.load(data_file)
                        data['id'] = index
                        data['title'] = filename.split('.')[0]
                        quizzes.append(data)

        self.quizzes = quizzes
        return quizzes
    
    def getQuizzes(self):
        if not self.quizzes:
            self.setQuizzes()
        return self.quizzes
    
    def getQuiz(self, quiz_id = None):
        if not quiz_id:
            if not self.quiz:
                return None
            return self.quiz
        return self.setQuiz(quiz_id)
    
    def setQuiz(self, quiz_id):
        quiz = self.quizzes[quiz_id]
        self.quiz = Quiz(quiz)
        return self.quiz

    def getPartialQuiz(self):
        return self.partial_quiz
    
    def setPartialQuiz(self, quiz):
        self.partial_quiz = None
        if quiz:
            self.partial_quiz = PartialQuiz(quiz)
        return self.partial_quiz
    
    def __iter__(self):
        return iter(self.quizzes)