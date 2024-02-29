from flask import Flask, render_template, request, redirect, url_for
from system import System
from user import User

app = Flask(__name__)

system = System()

@app.route("/", methods = ['GET', 'POST'])
@app.route("/start", methods = ['GET', 'POST'])
def start():
    quizzes = system.getQuizzes()

    if request.method == 'POST':
        if 'form-type' in request.form:
            # load quiz
            if request.form['form-type'] == 'set-quiz':
                quiz_id = request.form['quiz']
                system.setQuiz(int(quiz_id))

            elif request.form['form-type'] == 'set-name':
                # set user name
                if request.form['username']:
                    user = User(request.form['username'])
                    system.registerUser(user)

    quiz = system.getQuiz()
    user = system.getUser()
    if quiz:
        system.setPartialQuiz(quiz)

    return render_template(
        'start.html',
        user=user,
        quizzes=quizzes,
        quiz=quiz,
    )


@app.route("/quiz", methods = ['GET', 'POST'])
def quiz():
    if(system.quizReady() == False):
        return redirect(url_for('start'))
    
    quiz = system.getQuiz()
    partialQuiz = system.getPartialQuiz()
    cursor = partialQuiz.getCursor()
    total_questions = partialQuiz.getTotalQuestions()
    question_obj = partialQuiz.getQuestion()
    question = question_obj.getQuestion()
    answers = question_obj.getAnswers()

    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            question_obj.setAnswerSelected(answer)
            
            if cursor == total_questions - 1:
                partialQuiz.setCursor(0)
                return redirect(url_for('results'))
            else:
                cursor = partialQuiz.setCursorNext()
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
    
    partialQuiz = system.getPartialQuiz()
    score = partialQuiz.getScore()
    return render_template('results.html', score=score)