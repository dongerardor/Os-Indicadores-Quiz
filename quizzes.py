import os
from flask import json, current_app as app

# Quizzes is a Singleton class
class Quizzes:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):    
        self.quizzes = []
        self.selected_quiz = None



    def getQuizzes(self):
        self.quizzes = []
        with app.app_context():
            directory = os.path.join(app.static_folder, 'data')
            for index, filename in enumerate(os.listdir(directory)):
                if os.path.isfile(os.path.join(directory, filename)):
                    with open(os.path.join(directory, filename)) as data_file:
                        data = dict()
                        data['quiz'] = json.load(data_file)
                        data['id'] = index
                        data['title'] = filename.split('.')[0]
                        self.quizzes.append(data)

        for quiz in self.quizzes:
            print(quiz['id'])
            print(quiz['title'])
            print(' /////////// ')
        print(' ///////////////////////////////// ')

        return self.quizzes
    

    def select_quiz(self, quiz):
        self.quizzes.append(quiz)
    
    def __iter__(self):
        return iter(self.quizzes)