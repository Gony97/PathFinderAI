from llama_query_request import llama_query_request


def generate_answer(llama_api, user_input):
    message = f"answer to question:\
        1. {user_input[0]}\
        2. {user_input[1]}\
        3. {user_input[2]}\
        4. {user_input[3]}\
        5. {user_input[4]}\
        now suggest three jobs options"

    result = llama_query_request(llama_api=llama_api, query=message)
    return result