from quizzes import Quizzes

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

    def getQuiz(self, quiz_id = None):
        return self.quizzes.getQuiz(quiz_id)
    
    def setQuiz(self, quiz_id):
        return self.quizzes.setQuiz(quiz_id)
    
    def getPartialQuiz(self):
        return self.quizzes.getPartialQuiz()
    
    def setPartialQuiz(self, quiz):
        return self.quizzes.setPartialQuiz(quiz)
        
    def getQuizzes(self):
        return self.quizzes.getQuizzes()
        
    def quizReady(self):
        return self.getPartialQuiz() is not None and self.user is not None
