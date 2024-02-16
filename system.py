from quizzes import Quizzes
from quiz import Quiz

# System is a Singleton class
class System:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.user = None
        self.quizzes = Quizzes()
        self.quiz = None

    def registerUser(self, user):
        self.user = user

    def getUser(self):
        return self.user
    
    def getQuizzes(self):
        if self.quizzes.getQuizzes():
            return self.quizzes.getQuizzes()
        else:
            return []

    def loadQuiz(self, quiz):
        self.quiz = Quiz(quiz)
        return self.quiz
    
    def getQuiz(self):
        return self.quiz
