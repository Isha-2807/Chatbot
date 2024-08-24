from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple bot logic
def chatbot_response(message):
    if "hello" in message.lower():
        return "Hi there!"
    elif "how are you" in message.lower():
        return "I'm just a bot, but I'm doing well!"
    else:
        return "I don't understand that, but I'm learning!"


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot_response(user_message)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
