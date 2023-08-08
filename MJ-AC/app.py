import random
from flask import Flask, render_template
import os
import openai
from dotenv import load_dotenv
from chatgpt import initialize_openai
from dog import select_random_dog, get_random_dog_img
print("hello from in here")
# Importing functions from dog_api.py

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
initialize_openai()


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_message = request.form['user_input']

#     chat_log.append({"role": "user", "content": user_message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=chat_log
#     )

#     assistant_response = response["choices"][0]['message']['content']

#     chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

#     return render_template('response.html', assistant_response=assistant_response.strip("\n").strip())


@app.route('/dog', methods=['GET'])
def dog_api():
    random_dog = select_random_dog()
    dog_img = get_random_dog_img(random_dog)
    print(dog_img)
    chat_log = [{"role": "user", "content": f'Please provide a brief description about {random_dog}'}]

    create_gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )

    dog_gpt_query_response = create_gpt_response["choices"][0]['message']['content']

    app.logger.info("Accessed root route")
    
    random_dog = select_random_dog()
    app.logger.info(f"Random dog selected: {random_dog}")

    return render_template('dog.html', image_url=dog_img, dog_gpt_query_response=dog_gpt_query_response)

# app.route('test')

# def test():
#     return render_template('test.html')
print("hello from down here")
if __name__ == '__main__':
    app.run('localhost',port=9997)
