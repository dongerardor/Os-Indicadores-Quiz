from flask import Flask, render_template, request, redirect, url_for
from system import System
from user import User

app = Flask(__name__)

system = System()

@app.route("/", methods = ['GET', 'POST'])
@app.route("/start", methods = ['GET', 'POST'])
def start():
    quizzes = system.getQuizzes()
    selected_quiz = None

    if request.method == 'POST':
        if 'form-type' in request.form:
            # load quiz
            if request.form['form-type'] == 'set-quiz':
                selected_quiz_id = request.form['quiz']
                selected_quiz = quizzes[int(selected_quiz_id)]

            elif request.form['form-type'] == 'set-name':
                # set user name
                if request.form['username']:
                    user = User(request.form['username'])
                    system.registerUser(user)

    quiz = system.getQuiz(selected_quiz)
    user = system.getUser()

    return render_template(
        'start.html',
        user=user,
        quizzes=quizzes,
        quiz=quiz
    )


@app.route("/quiz", methods = ['GET', 'POST'])
def quiz():
    if(system.quizReady() == False):
        return redirect(url_for('start'))
    
    quiz = system.quiz
    cursor = quiz.getCursor()
    total_questions = quiz.getTotalQuestions()
    question_obj = quiz.getQuestion()
    question = question_obj.getQuestion()
    answers = question_obj.getAnswers()

    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            question_obj.setAnswerSelected(answer)
            
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
        answers=answers,
        cursor=cursor,
        total_questions=total_questions,
    )


@app.route("/results")
def results():
    if(system.quizReady() == False):
        return redirect(url_for('start'))
    
    quiz = system.quiz
    score = quiz.getScore()
    return render_template('results.html', score=score)