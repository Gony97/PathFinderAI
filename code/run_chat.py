from generate_questions import generate_questions
from generate_answer import  generate_answer
from llamaapi import LlamaAPI

import json


def print_questions(questions_dict):
    answer1 = input(f"{questions_dict[1]}")
    answer2 = input(f"{questions_dict[2]}")
    answer3 = input(f"{questions_dict[3]}")
    answer4 = input(f"{questions_dict[4]}")
    answer5 = input(f"{questions_dict[5]}")
    return [answer1, answer2, answer3, answer4, answer5]


def run_chat(llama_api):
    llama_api = LlamaAPI(llama_api)
    print("Hello! What an exciting time to embark on a new path. Let's start with answering a few questions")
    questions_dict = generate_questions(llama_api=llama_api)
    user_answers = print_questions(questions_dict)
    results = generate_answer(llama_api=llama_api, user_input=user_answers)
    print(results)
