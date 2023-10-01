from flask import Flask, request, render_template, jsonify
from hugchat import hugchat
from hugchat.login import Login
import os

app = Flask(__name__)

# Inicia sesión en Hugging Face y obtén las cookies de autorización
email = os.environ.get("HUGGING_FACE_EMAIL")
password = os.environ.get("HUGGING_FACE_PASSWORD")

sign = Login(email, password)
cookies = sign.login()

# Crea una instancia del chatbot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chatbot', methods=['POST'])
def chatbot_endpoint():
    user_message = request.form['user_message']
    bot_response = chatbot.query(user_message)['text']
    return bot_response

@app.route('/discord_message', methods=['POST'])
def discord_message():
    # Aquí recibirás los mensajes enviados desde Discord
    data = request.json  # Supongo que los mensajes de Discord llegan como JSON
    user_message = data['content']  # Obtén el contenido del mensaje de usuario

    # Llama a tu chatbot de IA y obtén una respuesta
    bot_response = chatbot.query(user_message)['text']

    # Puedes devolver la respuesta del bot como JSON o como texto plano según tus necesidades
    response_data = {'bot_response': bot_response}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
