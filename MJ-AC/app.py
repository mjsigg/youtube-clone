from flask import Flask, render_template
import os
import openai
from flask_gzip import Gzip
from dotenv import load_dotenv
from chatgpt import initialize_openai
from dog import select_random_dog, get_random_dog_img

# Importing functions from dog_api.py

app = Flask(__name__)
gzip = Gzip(app)

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
    chat_log = [{"role": "user", "content": f'Please provide a brief description about {random_dog} in 500 words or less.'}]

    create_gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )

    dog_gpt_query_response = create_gpt_response["choices"][0]['message']['content']
    
    random_dog = select_random_dog()

    return render_template('dog.html', image_url=dog_img, dog_gpt_query_response=dog_gpt_query_response)



if __name__ == '__main__':
    app.run('localhost',port=9997)
