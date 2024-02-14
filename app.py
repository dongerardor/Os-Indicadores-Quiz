from flask import Flask, render_template, request, redirect, url_for
from system import System
from user import User

app = Flask(__name__)

system = System()

@app.route("/", methods = ['GET', 'POST'])
@app.route("/start", methods = ['GET', 'POST'])
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

@app.route("/quiz", methods = ['GET', 'POST'])
def quiz():
    quiz = system.quiz

    cursor = quiz.getCursor()
    total_questions = quiz.getTotalQuestions()
    question = quiz.getQuestion()

    if request.method == 'POST':
        answer = request.form['answer']
        question.setAnswerSelected(answer)
        
        if cursor == total_questions - 1:
            quiz.setCursor(0)
            return redirect(url_for('results'))
        else:
            cursor = quiz.setCursorNext()
            return redirect(url_for('quiz'))
        
    return render_template(
        'quiz.html', 
        quiz=quiz, 
        question=question,
        cursor=cursor,
        total_questions=total_questions
    )


@app.route("/results")
def results():
    quiz = system.quiz
    score = quiz.getScore()
    return render_template('results.html', score=score)