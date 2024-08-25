import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all origins

# Load the configuration file
with open('config.json') as config_file:
    config = json.load(config_file)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"response": "Please provide a message."})
    
    if 'hello' in user_message.lower():
        response_message = config['chatbot']['responses']['greeting']
    elif 'bye' in user_message.lower():
        response_message = config['chatbot']['responses']['farewell']
    else:
        response_message = config['chatbot']['responses']['default']
    
    return jsonify({"response": response_message},status=200,mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5502)

