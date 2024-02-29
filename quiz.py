class Quiz:
    def __init__(self, quiz):
        self.questions = quiz['quiz'] if quiz is not None else None
        self.id = quiz['id'] if quiz is not None else None
        self.title = quiz['title'] if quiz is not None else None