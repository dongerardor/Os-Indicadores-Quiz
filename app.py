from flask import Flask, render_template, request, redirect, url_for
from system import System
from user import User

app = Flask(__name__)

system = System()

@app.route("/", methods = ['GET', 'POST'])
def start():
    user = system.getUser()
    if user == None:
        if request.method == 'POST':
            if request.form['username']:
                user = User(request.form['username'])
                system.registerUser(user)
    
    return render_template('start.html', user=user)

@app.route("/selectQuiz", methods = ['GET', 'POST'])
def selectQuiz():
    quizzes = system.getQuizzes()
    selected_quiz_id = None
    selected_quiz_title = None
    if request.method == 'POST':
        selected_quiz_id = request.form['quiz']
        for quiz in quizzes:
            if quiz['id'] == int(selected_quiz_id):
                selected_quiz_title = quiz['title']
                system.loadQuiz(quiz)
                break

    return render_template(
        'selectQuiz.html', 
        quizzes=quizzes, 
        selected_quiz_id=selected_quiz_id,
        selected_quiz_title=selected_quiz_title
    )

@app.route("/quiz/question", methods = ['GET', 'POST'])
def quiz():
    quiz = system.quiz

    cursor = quiz.getCursor()
    total_questions = quiz.getTotalQuestions()

    print(f'cursor: {cursor}, total_questions: {total_questions}')

    if request.method == 'GET':
        question = quiz.getNextQuestion()

    if request.method == 'POST':
        answer = request.form['answer']
        question = quiz.getQuestion()
        question.setAnswerSelected(answer)

        if(quiz.getCursor() == quiz.getTotalQuestions()):
            return redirect(url_for('results'))
              
    return render_template(
        'quiz.html', 
        quiz=quiz, 
        question=question,
        cursor=quiz.getCursor(),
        total_questions=quiz.getTotalQuestions()
    )


@app.route("/results")
def results():
    quiz = system.quiz
    score = quiz.getScore()
    return render_template('results.html', score=score)