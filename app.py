from flask import Flask
from database import initialize_db

app = Flask(__name__)

# Setup Database
initialize_db(app)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Claude SDK Chatbot!"

if __name__ == '__main__':
    app.run(port=5005)