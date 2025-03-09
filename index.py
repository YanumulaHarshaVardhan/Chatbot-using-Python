from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer 
from flask import Flask, render_template,request
import json

app=Flask(__name__)

bot = ChatBot('chatbot', read_only=False, 
   logic_adapters=[ 

    {
        'import_path':'chatterbot.logic.BestMatch',
        "default_response":"sorry I don't have an answer",
        "maximum_similarity_threshold":0.9
        } 
    
    ])


trainer=ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english')








# Train with Custom Dataset
with open(r"F:\chatter\intents.json", "r", encoding="utf-8") as file:

    data = json.load(file)

list_trainer = ListTrainer(bot)

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        list_trainer.train([pattern] + intent["responses"])








@app.route('/')
def main():
    return render_template("index.html")

#while True:

 #   user_response =input('user: ')
 #   print('chatbot: ',str(bot.get_response(user_response)))

@app.route('/get')
def get_chatbot_response():
    userText=request.args.get('userMessage')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)