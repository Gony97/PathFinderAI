

def llama_query_request(llama_api, query):
    api_request_json = {
        "messages": [
            {"role": "user", "content": query},
        ],

        "stream": False,
    }
    response = llama_api.run(api_request_json)
    result = response.json()['choices'][0]['message']['content']
    return result
