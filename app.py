from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Simple chatbot logic
    if user_message.lower() == "hi":
        response = "Hello! How can I assist you today?"
    elif user_message.lower() == "bye":
        response = "Goodbye! Have a great day!"
    else:
        response = "Sorry, I don't understand that."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

