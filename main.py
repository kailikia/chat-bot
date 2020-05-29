from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections
from pairs import pairs


app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    chat=Chat(pairs,reflections)
    response = chat.respond(userText)
    if response == None:
        return "Sorry,I don't understand that. Would you like a TV, Laptop or a Fridge?"
    else:
        return response


if __name__ == "__main__":
    app.run()
