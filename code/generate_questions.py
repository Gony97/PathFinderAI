from llama_query_request import llama_query_request


def extract_questions(text):
    questions = dict()
    questions[1] = text[text.index('1.'): text.index('2.')]
    questions[2] = text[text.index('2.'): text.index('3.')]
    questions[3] = text[text.index('3.'): text.index('4.')]
    questions[4] = text[text.index('4.'): text.index('5.')]
    questions[5] = text[text.index('5.'): text.index('END')]
    return questions


def generate_questions(llama_api):
    message = "I want you to help me find the best jobs for me based on my knowledge, skills, and Characteristics, in the world of tech companies. Please ask me EXACTLY FIVE simple short chat questions (must label questions 1. 2. 3. 4. 5.) and according to my answer recommend 3 choices. at the end of question 5 write END"
    questions = llama_query_request(llama_api=llama_api, query=message)
    questions_dict = extract_questions(questions)
    return questions_dict
