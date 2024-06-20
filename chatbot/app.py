from flask import Flask,render_template, request, jsonify
import vertexai
from vertexai.language_models import CodeChatModel
from vertexai.preview.generative_models import GenerativeModel, Part

import os
from dotenv import load_dotenv
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-json-key-goes-here.json"
load_dotenv()
PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')
CODE_CHAT_MODEL = os.getenv('CODE_CHAT_MODEL')

app = Flask(__name__)

vertexai.init(project=PROJECT_ID, location=LOCATION)
config = {
    "max_output_tokens": 2048,
    "temperature": 0.9,
    "top_p": 1
}
model = GenerativeModel(CODE_CHAT_MODEL)
chat = model.start_chat()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    response = chat.send_message(userText, generation_config=config) # for the gemini AI model
    return response.text
if __name__ == "__main__":
    app.run()
    