import openai


def generate_response(prompt):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()



# def generate_response(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response["choices"][0]["message"]["content"].strip()


# client = openai.OpenAI()
# response = client.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "system", "content": "Hello"}]
# )