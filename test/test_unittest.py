import pytest
import random
from quiz import Quiz
from partialQuiz import PartialQuiz
from config import Config

def get_question_set():
    return [
    {
        "id": 27,
        "question": "Who is the CEO of Tesla?",
        "answers": [
            "Jeff Bezos",
            "Mark Zuckerberg",
            "Tim Cook",
            "Elon Musk"
        ],
        "correctAnswer": "Elon Musk"
    },
    {
        "id": 28,
        "question": "What type of animal is a penguin?",
        "answers": [
            "Mammal",
            "Reptile",
            "Insect",
            "Bird"
        ],
        "correctAnswer": "Bird"
    },
    {
        "id": 29,
        "question": "What is the capital city of Canada?",
        "answers": [
            "Vancouver",
            "Toronto",
            "Quebec City",
            "Ottawa"
        ],
        "correctAnswer": "Ottawa"
    },
    {
        "id": 30,
        "question": "What is the strongest muscle in the human body?",
        "answers": [
            "Biceps",
            "Quadriceps",
            "Heart",
            "Jaw Muscle (Masseter)"
        ],
        "correctAnswer": "Jaw Muscle (Masseter)"
    },
    {
        "id": 31,
        "question": "Who wrote the novel \"Pride and Prejudice\"?",
        "answers": [
            "Charlotte Bronte",
            "Mary Shelley",
            "Jane Austen",
            "Emily Dickinson"
        ],
        "correctAnswer": "Jane Austen"
    },
    {
        "id": 32,
        "question": "What is the fastest land animal?",
        "answers": [
            "Cheetah",
            "Ostrich",
            "Lion",
            "Elephant"
        ],
        "correctAnswer": "Cheetah"
    },
    {
        "id": 33,
        "question": "Who painted \"Starry Night\"?",
        "answers": [
            "Pablo Picasso",
            "Vincent van Gogh",
            "Claude Monet",
            "Edvard Munch"
        ],
        "correctAnswer": "Vincent van Gogh"
    }]


@pytest.fixture
def valid_quiz():
    # Preparación: crea un objeto Quiz válido
    id = random.randint(1, 100)
    title = "Quiz title"
    questions = get_question_set()
    quiz_params = {
        "id": id,
        "title": title,
        "quiz": questions
    }

    quiz = Quiz(quiz_params)
    return quiz


def test_initialization_with_valid_quiz(valid_quiz):
    partial_quiz = PartialQuiz(valid_quiz)
    assert partial_quiz is not None
    assert partial_quiz.id == valid_quiz.id
    assert partial_quiz.title == valid_quiz.title
    assert partial_quiz.questions is not None
    assert len(partial_quiz.questions) == Config.NUMBER_OF_QUESTIONS

